#!/usr/bin/env python

# This program creates a dialog box that allows the user to type in a Name, choose a type and date and add Notes
# The program will then print the selected values

from PyQt5 import QtWidgets
from PyQt5 import QtCore
import datetime

class BasicDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(BasicDialog, self).__init__(parent=parent)
        # Instantiate a layout and set it as the dialogs main layout
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        # Add ok and cancel buttons
        # And hook them up to dialogs accept/reject methods
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok|\
                                            QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        # Add a one line text editor and label it Name
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setPlaceholderText("Name")

        # Create a horizontal layout for the popup list and label
        type_layout = QtWidgets.QHBoxLayout()
        # Add popup list, add options and sort them alphabetically
        self.combo_box = QtWidgets.QComboBox()
        self.combo_box.addItems({"A", "B", "C"})
        self.combo_box.model().sort(0)
        # Add a label for the combo box, name it Type and center it
        type_label = QtWidgets.QLabel()
        type_label.setText("Type:")
        type_label.setAlignment(QtCore.Qt.AlignCenter)
        # Add popup list and label to horizontal layout
        type_layout.addWidget(type_label)
        type_layout.addWidget(self.combo_box)

        # Create a horizontal layout for the date editor and label
        need_by_layout = QtWidgets.QHBoxLayout()
        # Add a week to today's date
        now = datetime.datetime.today()
        week1 = datetime.timedelta(weeks=1)
        week_due_date = now + week1
        # Add a date editor, set the default date to a week from now and set the lowest possible date to today
        self.need_by = QtWidgets.QDateEdit()
        self.need_by.setDate(week_due_date)
        self.need_by.setMinimumDate(now)
        # Add label for date editor, name it Need By and center it
        need_by_label = QtWidgets.QLabel()
        need_by_label.setText("Need By:")
        need_by_label.setAlignment(QtCore.Qt.AlignCenter)
        # Add date editor and label to horizontal layout
        need_by_layout.addWidget(need_by_label)
        need_by_layout.addWidget(self.need_by)

        # Add a text editor and label it Notes
        self.notes = QtWidgets.QTextEdit()
        self.notes.setPlaceholderText("Notes")

        # Add created widgets and layouts to main layout
        main_layout.addWidget(button_box)
        main_layout.addWidget(self.line_edit)
        main_layout.addLayout(type_layout)
        main_layout.addLayout(need_by_layout)
        main_layout.addWidget(self.notes)

    # Get user's selected values if the user clicked Ok
    # Add them to a dictionary and return the dictionary
    def getValues(self):
        values = {"name": self.line_edit.text(), "Type": self.combo_box.currentText(),
                  "Need By": self.need_by.date().toString("M/dd/yyyy"), "Notes": self.notes.document().toPlainText()}
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
