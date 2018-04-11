# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm3helper/ui/about.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(315, 164)
        self.verticalLayout = QtWidgets.QVBoxLayout(About)
        self.verticalLayout.setObjectName("verticalLayout")
        self.aboutLbl = QtWidgets.QLabel(About)
        self.aboutLbl.setObjectName("aboutLbl")
        self.verticalLayout.addWidget(self.aboutLbl)
        self.buttonBox = QtWidgets.QDialogButtonBox(About)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(About)
        self.buttonBox.accepted.connect(About.accept)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.aboutLbl.setText(_translate("About", "<html><head/><body><p><span style=\" font-size:16pt;\">#name# #version#</span></p><p>Webpage: <a href=\"https://github.com/Talv/m3helper\"><span style=\" text-decoration: underline; color:#0000ff;\">github.com/Talv/m3helper</span></a></p><p>Author: Talv</p></body></html>"))

