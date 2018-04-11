# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm3helper/ui/config.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Config(object):
    def setupUi(self, Config):
        Config.setObjectName("Config")
        Config.resize(393, 183)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Config)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(Config)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.ed_src_dirs = QtWidgets.QTextEdit(Config)
        self.ed_src_dirs.setObjectName("ed_src_dirs")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ed_src_dirs)
        self.btn_search_archives = QtWidgets.QPushButton(Config)
        self.btn_search_archives.setObjectName("btn_search_archives")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btn_search_archives)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Config)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Config)
        self.buttonBox.rejected.connect(Config.reject)
        self.buttonBox.accepted.connect(Config.accept)
        QtCore.QMetaObject.connectSlotsByName(Config)

    def retranslateUi(self, Config):
        _translate = QtCore.QCoreApplication.translate
        Config.setWindowTitle(_translate("Config", "Preferences"))
        self.label.setToolTip(_translate("Config", "List of directories where to lookup for textures, separated by new line."))
        self.label.setText(_translate("Config", "Source"))
        self.btn_search_archives.setText(_translate("Config", "Add SC2/Storm archives from ..."))

