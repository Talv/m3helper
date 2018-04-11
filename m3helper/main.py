#!/usr/bin/python3

import sys
import signal
import logging
import os
import toml
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QPlainTextEdit, QFileDialog
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread, QObject
from .ui.main import Ui_MainWindow
from .ui.config import Ui_Config
from .ui.about import Ui_About
from .util import find_archives, find_files_in_archive, m3_textures_list, insert_texture_file
from .version import __appname__, __version__

logFormatter = logging.Formatter(
    fmt='[%(asctime)s] %(levelname)s [%(module)s/%(funcName)s]: %(message)s',
    datefmt='%H:%M:%S'
)
logging.getLogger().setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler(sys.stderr)
consoleHandler.setFormatter(logFormatter)
logging.getLogger().addHandler(consoleHandler)

logger = logging.getLogger()


class AppConfig(dict):
    defaults = {
        'source_dirs': [],
    }
    def __init__(self):
        for k, v in self.defaults.items():
            self.setdefault(k, v)
        self.filenames = ['config.toml', os.path.expanduser('~/.%s.toml' % __appname__)]
        self.fname = self.read()
        if not self.fname:
            logger.debug('config file not found')
            for x in self.filenames:
                with open(x, 'w') as fp:
                    self.fname = x
                    break
            self.write()

    def read(self):
        for x in self.filenames:
            if os.path.isfile(x):
                self.update(toml.load(x))
                return x
        return False

    def write(self):
        with open(self.fname, 'w') as fp:
            toml.dump(self, fp)


config = AppConfig()


def app_tpl(txt: str):
    txt = txt.replace('#name#', __appname__)
    txt = txt.replace('#version#', __version__)
    return txt


class QPlainTextLogHandler(logging.Handler):
    def __init__(self, ed_log: QPlainTextEdit):
        logging.Handler.__init__(self, level=logging.INFO)
        self.setFormatter(logging.Formatter(
            fmt='%(message)s'
        ))
        self.ed_log = ed_log

    def emit(self, record):
        msg = self.format(record)
        self.ed_log.appendPlainText(msg)


class AboutWindow(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_About()
        self.ui.setupUi(self)
        self.ui.aboutLbl.setText(app_tpl(self.ui.aboutLbl.text()))


class ConfigWindow(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Config()
        self.ui.setupUi(self)
        self.ui.btn_search_archives.clicked.connect(self.onSearchArchives)
        self.ui.ed_src_dirs.setText('\n'.join(config['source_dirs']))

    def onSearchArchives(self):
        src = QFileDialog.getExistingDirectory(self, 'Choose source directory')
        if not src:
            return
        logger.debug('find archives %s' % src)
        src_archives = list(find_archives(src))
        logger.debug('found %d' % len(src_archives))
        self.ui.ed_src_dirs.setText('\n'.join(src_archives))

    def accept(self):
        config['source_dirs'] = self.ui.ed_src_dirs.toPlainText().split('\n')
        config.write()
        QDialog.accept(self)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionSettings.triggered.connect(self.onConfigBtn)
        self.ui.actionAbout.triggered.connect(self.onAboutBtn)
        self.ui.actionClearLog.triggered.connect(self.onClearLog)

        self.ui.btn_select_dir.clicked.connect(self.onSelectDir)
        self.ui.btn_anim_dump.clicked.connect(self.onAnimDumpBtn)
        self.ui.btn_anim_dump.dragEnterEvent = self.dragEnterEvent
        self.ui.btn_anim_dump.dropEvent = self.dropEvent

    def onClearLog(self):
        self.ui.ed_log.clear()

    def onConfigBtn(self):
        cwnd = ConfigWindow(self)
        cwnd.exec_()

    def onAboutBtn(self):
        cwnd = AboutWindow(self)
        cwnd.exec_()

    def dragEnterEvent(self, e):
        if not e.mimeData().hasUrls():
            return
        e.accept()

    def dropEvent(self, e):
        e.accept()
        m = e.mimeData()
        for x in m.urls():
            print(x)
            if not x.isLocalFile():
                continue
            filename = x.toLocalFile()
            if not filename.endswith('m3'):
                continue
            self.processM3File(filename)

    def onSelectDir(self):
        s = QFileDialog.getExistingDirectory(self, 'Choose destination directory')
        if s:
            self.ui.ed_target_dir.setText(s)

    def onAnimDumpBtn(self):
        s = QFileDialog.getOpenFileName(self, 'Select m3 file', '', 'M3 (*.m3)')
        if s and len(s[0]):
            self.processM3File(s[0])

    def processM3File(self, mfname):
        logger.info('Processing "%s"' % os.path.basename(mfname))
        textl = m3_textures_list(mfname)
        logger.info('Model uses %d textures' % len(textl))

        target_dir = None
        if self.ui.cbx_auto_copy.isChecked() and len(self.ui.ed_target_dir.text()):
            target_dir = self.ui.ed_target_dir.text()

        i = 1
        for k, v in find_files_in_archive(textl, config['source_dirs']).items():
            logger.info('[%02d/%02d] %s' % (i, len(textl), k))
            if v:
                logger.info(v)
                if target_dir:
                    if insert_texture_file(target_dir, k, v):
                        logger.info('Have been copied successfully')
                    else:
                        logger.info('Already exists, skipping')
            else:
                logger.info('- not found -')
            i += 1
        logger.info('')


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    wnd = MainWindow()
    logging.getLogger().addHandler(QPlainTextLogHandler(wnd.ui.ed_log))
    wnd.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
