
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PeopleTable(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 380)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tbwKisiler = QtWidgets.QTableWidget(Form)
        self.tbwKisiler.setObjectName("tbwKisiler")
        self.tbwKisiler.setColumnCount(0)
        self.tbwKisiler.setRowCount(0)
        self.gridLayout.addWidget(self.tbwKisiler, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kisiler"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_PeopleTable()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
