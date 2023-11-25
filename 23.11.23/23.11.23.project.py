
#python -m PyQt5.uic.pyuic -x untitled.ui -o ui.py


from random import choice
import random
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from ui import Ui_MainWindow 

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.generate)
   
    def generate(self):
        self.password_len = 8
        alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        numbers = '1234567890'
        symbols = "!@#$%^&*()_+-=\\'\"|?.,<>/:;"
        passlenth = self.number()
        password = ""
        
        for i in range(self.password_len):
            if self.ui.cb_numbers.isChecked():
                digit = choice(numbers)
                password += digit
            if self.ui.cb_alphabet.isChecked():
                letter = choice(alphabet)
                password += letter
            symbol = choice(symbols)
            password += symbol
        result = ''.join(random.choice(password) for _ in range(passlenth))
        self.ui.result.setText(result)
                
    def number(self):
        number = self.ui.spinBox.value()
        return number
        
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()

