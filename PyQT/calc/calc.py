import sys
from calc_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.expr = ''
        self.setWindowTitle('I HATE PYQT')
        self.setupUi(self)

        self.btn0.clicked.connect(lambda: self.add_symbol('0'))
        self.btn1.clicked.connect(lambda: self.add_symbol('1'))
        self.btn2.clicked.connect(lambda: self.add_symbol('2'))
        self.btn3.clicked.connect(lambda: self.add_symbol('3'))
        self.btn4.clicked.connect(lambda: self.add_symbol('4'))
        self.btn5.clicked.connect(lambda: self.add_symbol('5'))
        self.btn6.clicked.connect(lambda: self.add_symbol('6'))
        self.btn7.clicked.connect(lambda: self.add_symbol('7'))
        self.btn8.clicked.connect(lambda: self.add_symbol('8'))
        self.btn9.clicked.connect(lambda: self.add_symbol('9'))
        self.btn_rparen.clicked.connect(lambda: self.add_symbol('('))
        self.btn_lparen.clicked.connect(lambda: self.add_symbol(')'))
        self.btn_dot.clicked.connect(lambda: self.add_symbol('.'))
        self.btn_div.clicked.connect(lambda: self.add_symbol('/'))
        self.btn_mul.clicked.connect(lambda: self.add_symbol('*'))
        self.btn_neg.clicked.connect(lambda: self.add_symbol('-'))
        self.btn_sum.clicked.connect(lambda: self.add_symbol('+'))
        self.btn_eq.clicked.connect(lambda: self.get_eval())
        self.btn_clear.clicked.connect(lambda: self.clear_screen())
        self.btn_erase.clicked.connect(lambda: self.pop_back())
    
    def add_symbol(self, sym: str):
        self.expr += sym
        self.label.setText(self.expr)

    def pop_back(self):
        self.expr = self.expr[0:-1]
        self.label.setText(self.expr)

    def get_eval(self):
        try:
            self.label.setText(f'{eval(self.expr)}')
            self.expr = ''
        except:
            self.label.setText("Error")
            self.expr = ''

    def clear_screen(self):
        self.expr = ''
        self.label.setText(self.expr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Window()
    calc.show()
    sys.exit(app.exec())
