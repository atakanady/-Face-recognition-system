
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DoorCheck(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 542)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 10, 391, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lbDurum = QtWidgets.QLabel(Form)
        self.lbDurum.setGeometry(QtCore.QRect(30, 450, 541, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.lbDurum.setFont(font)
        self.lbDurum.setObjectName("lbDurum")
        self.lbKamera = QtWidgets.QLabel(Form)
        self.lbKamera.setGeometry(QtCore.QRect(20, 90, 531, 361))
        self.lbKamera.setText("")
        self.lbKamera.setObjectName("lbKamera")
        self.btnTekrarDene = QtWidgets.QPushButton(Form)
        self.btnTekrarDene.setGeometry(QtCore.QRect(450, 14, 111, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnTekrarDene.setFont(font)
        self.btnTekrarDene.setObjectName("btnTekrarDene")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kişi Kontrol Kamera Taraması"))
        self.label.setText(_translate("Form", "Kapı Kontrol"))
        self.lbDurum.setText(_translate("Form", "Onay Durumu: Bekleniyor"))
        self.btnTekrarDene.setText(_translate("Form", "Başlat"))


