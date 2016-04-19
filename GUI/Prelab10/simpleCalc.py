# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

operator = ""
op1 = 0.0
new_op_flag = True
eq_op2 = 0.0
eq_operator = ""
de_flag = False

class CalculatorConsumer(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):
        super(CalculatorConsumer, self).__init__(parent)
        self.setupUi(self)

        nums = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        ops = [self.btnMultiply, self.btnMinus, self.btnPlus, self.btnDivide]

        for i in nums:
            i.clicked.connect(self.Nums)
        for i in ops:
            i.clicked.connect(self.Operator)

        self.btnClear.clicked.connect(self.Clear)
        self.btnEqual.clicked.connect(self.Equal)
        self.btnDot.clicked.connect(self.Dot)

    def Nums(self):
        global operator
        global new_op_flag
        global de_flag
        de_flag = False
        if new_op_flag is True:
            self.txtDisplay.setText(self.sender().text())
            new_op_flag = False
        else:
            raw_s = self.txtDisplay.text().replace(",", "")
            if len(raw_s) < 12:
                s = self.Sep(raw_s+self.sender().text())
                self.txtDisplay.setText(s)
            else:
                self.txtDisplay.setText("Restrict the maximum number of digits to display to be 12 digits")

    def Operator(self):
        global operator
        global new_op_flag
        global op1
        global de_flag
        de_flag = False
        if new_op_flag is True:
            pass
        elif operator != "":
            self.Equal()
        else:
            new_op_flag = True
        if self.txtDisplay.text() != "":
            s = self.txtDisplay.text()
            x = s.replace(",", "")
            try:
                op1 = float(x)
            except ValueError:
                pass
        operator = self.sender().text()

    def Clear(self):
        global operator
        global op1
        global new_op_flag
        global de_flag
        de_flag = False
        operator = ""
        op1 = 0.0
        new_op_flag = True
        self.txtDisplay.setText("0.")

    def Dot(self):
        global new_op_flag
        if new_op_flag is True:
            self.txtDisplay.setText("0.")
            new_op_flag = False
        elif '.' not in self.txtDisplay.text():
            self.txtDisplay.setText(self.txtDisplay.text()+'.')

    def Equal(self):
        global operator
        global op1
        global new_op_flag
        global de_flag
        global eq_op2
        global eq_operator
        if de_flag is True:
            try:
                op1 = float(self.txtDisplay.text().replace(",", ""))
            except ValueError:
                pass
            op2 = eq_op2
            operator = eq_operator
        else:
            op2 = self.txtDisplay.text().replace(",", "")
        if operator == "+":
            result = op1 + float(op2)
        elif operator == "-":
            result = op1 - float(op2)
        elif operator == "x":
            result = op1 * float(op2)
        elif operator == "/":
            try:
                result = op1 / float(op2)
            except ZeroDivisionError:
                self.txtDisplay.setText("Division Error")
        if operator != "":
            de_flag = True
            eq_op2 = op2
            eq_operator = operator
            s = ('{0:.'+str(self.cboDecimal.currentText())+'f}').format(result)
            if self.chkSeparator.isChecked():
                s = self.Sep(s)
            x = s.replace(",", "")
            x = x.replace(".", "")
            x = x.replace("-", "")
            if len(x) < 13:
                self.txtDisplay.setText(s)
            else:
                self.txtDisplay.setText("Restrict the maximum number of digits to display to be 12 digits")
        operator = ""
        new_op_flag = True

    def Sep(self, s):
        if '.' in s:
            i, d = s.split('.')
        else:
            i = s
        news = ""
        count = 0
        for ind in reversed(range(0, len(i))):
            if count == 3:
                if s[ind] != "-":
                    news = ',' + news
                news = s[ind] + news
                count = 1
            else:
                count += 1
                news = s[ind] + news
        if '.' in s:
            news = news + "." + d
        return news

	self.line_edits = [self.firstNameLineEdit, self.lastNameLineEdit, self.addressLineEdit, self.cityLineEdit,
                           self.stateLineEdit, self.zipLineEdit, self.emailLineEdit]

        self.clearButton.clicked.connect(self.Clear)
        self.saveToTargetButton.clicked.connect(self.Save)
        self.loadButton.clicked.connect(self.loadData)

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
                self.errorInfoLabel.setText("Error: all entries should be filled.")
                return
        if self.stateLineEdit.text() not in states:
            self.errorInfoLabel.setText("Error: state need to be valid.")
            return
        if len(self.zipLineEdit.text()) != 5:
            self.errorInfoLabel.setText("Error: zip code need to be 5 digits.")
            return
        r_email = re.search(r'(\w+@\w+\.\w+)', self.emailLineEdit.text())
        if r_email is None:
            self.errorInfoLabel.setText("Error: email need to be valid.")
            return	

currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()

currentForm.show()
currentApp.exec_()
