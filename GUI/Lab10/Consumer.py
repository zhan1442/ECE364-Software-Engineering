import sys, re
from PySide.QtGui import *
from BasicUI import *

states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
          "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
          "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.line_edits = [self.firstNameLineEdit, self.lastNameLineEdit, self.addressLineEdit, self.cityLineEdit,
                           self.stateLineEdit, self.zipLineEdit, self.emailLineEdit]

        for edit in self.line_edits:
            edit.textChanged.connect(self.Ena)

        self.clearButton.clicked.connect(self.Clear)
        self.saveToTargetButton.clicked.connect(self.Save)
        self.loadButton.clicked.connect(self.loadData)

    def Ena(self):
        self.saveToTargetButton.setEnabled(True)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """
        with open(filePath, 'r') as myfile:
            content = myfile.readlines()
        for line in content[2:]:
            line = line.strip()
            if '<FirstName>' in line:
                self.firstNameLineEdit.setText(line[11:-12])
            elif '<LastName>' in line:
                self.lastNameLineEdit.setText(line[10:-11])
            elif '<Address>' in line:
                self.addressLineEdit.setText(line[9:-10])
            elif '<City>' in line:
                self.cityLineEdit.setText(line[6:-7])
            elif '<State>' in line:
                self.stateLineEdit.setText(line[7:-8])
            elif '<ZIP>' in line:
                self.zipLineEdit.setText(line[5:-6])
            elif '<Email>' in line:
                self.emailLineEdit.setText(line[7:-8])
        self.errorInfoLabel.text() == ""
        self.saveToTargetButton.setEnabled(True)
        self.loadButton.setEnabled(False)

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def Clear(self):
        for edit in self.line_edits:
            edit.clear()
        self.errorInfoLabel.text() == ""
        self.saveToTargetButton.setEnabled(False)
        self.loadButton.setEnabled(True)

    def Save(self):
        global states
        self.errorInfoLabel.setText("")
        for edit in self.line_edits:
            if edit.text() == "":
                self.errorInfoLabel.setText("Error: all entries must be populated.")
                return
        if self.stateLineEdit.text() not in states:
            self.errorInfoLabel.setText("Error: The state must be one of the valid US states.")
            return
        if len(self.zipLineEdit.text()) != 5 or not self.zipLineEdit.text().isalnum():
            self.errorInfoLabel.setText("Error: The zip code must be a 5-digit number.")
            return
        r_email = re.search(r'(\w+@\w+\.\w+)', self.emailLineEdit.text())
        if r_email is None:
            self.errorInfoLabel.setText("Error: The Email must have a valid email format.")
            return
        s = '<?xml version="1.0" encoding="UTF-8"?>\n'
        s += '<user>\n'
        s += '\t<FirstName>' + self.firstNameLineEdit.text() + '</FirstName>\n'
        s += '\t<LastName>' + self.lastNameLineEdit.text() + '</LastName>\n'
        s += '\t<Address>' + self.addressLineEdit.text() + '</Address>\n'
        s += '\t<City>' + self.cityLineEdit.text() + '</City>\n'
        s += '\t<State>' + self.stateLineEdit.text() + '</State>\n'
        s += '\t<ZIP>' + self.zipLineEdit.text() + '</ZIP>\n'
        s += '\t<Email>' + self.emailLineEdit.text() + '</Email>\n'
        s += '</user>\n'
        with open("target.xml", 'w') as myfile:
            myfile.write(s)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
