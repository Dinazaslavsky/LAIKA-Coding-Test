#!/usr/bin/env python

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import datetime

class BasicDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(BasicDialog, self).__init__(parent=parent)
        #Instantiate a layout and set it as the dialogs main layout
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        #Add ok and cancel buttons
        #And hook them up to dialogs accept/reject methods
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok|\
                                            QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setPlaceholderText("Name")

        type_layout = QtWidgets.QHBoxLayout()
        self.combo_box = QtWidgets.QComboBox()
        self.combo_box.addItems({"A", "B", "C"})
        self.combo_box.model().sort(0)
        type_label = QtWidgets.QLabel()
        type_label.setText("Type:")
        type_label.setAlignment(QtCore.Qt.AlignCenter)
        type_layout.addWidget(type_label)
        type_layout.addWidget(self.combo_box)

        need_by_layout = QtWidgets.QHBoxLayout()
        now = datetime.datetime.today()
        week1 = datetime.timedelta(weeks = 1)
        week_due_date = now + week1
        self.need_by = QtWidgets.QDateEdit()
        self.need_by.setDate(week_due_date)
        self.need_by.setMinimumDate(now)
        need_by_label = QtWidgets.QLabel()
        need_by_label.setText("Need By:")
        need_by_label.setAlignment(QtCore.Qt.AlignCenter)
        need_by_layout.addWidget(need_by_label)
        need_by_layout.addWidget(self.need_by)


        self.notes = QtWidgets.QTextEdit()
        self.notes.setPlaceholderText("Notes")

        main_layout.addWidget(button_box)
        main_layout.addWidget(self.line_edit)
        main_layout.addLayout(type_layout)
        main_layout.addLayout(need_by_layout)
       # main_layout.addWidget(type_label)
       # main_layout.addWidget(self.combo_box)
       # main_layout.addWidget(need_by_label)
       # main_layout.addWidget(self.need_by)
        main_layout.addWidget(self.notes)

    def getValues(self):
        values = {"name": self.line_edit.text(), "Type": self.combo_box.currentText(), "Need By": self.need_by.date().toString("M/dd/yyyy"), "Notes": self.notes.document().toRawText()}
        return values

if __name__ == '__main__':
    #Instantiate a QApplication - requirement for Qt
    app = QtWidgets.QApplication([])
    #Instantiate, show, then raise our dialog to the front
    dlg = BasicDialog()
    dlg.show()
    dlg.raise_()

    dlg.getValues()
    #only getValues if 'Ok' is clicked
    if dlg.exec_():
        print(dlg.getValues())
