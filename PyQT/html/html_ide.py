import sys

from PyQt5.QtWidgets import QMainWindow, QTextEdit, QTextBrowser, QPushButton, QApplication

# Ширина и высота окна
WIDTH, HEIGHT = 1000, 500
# Ширина и высота внутренних элементов
B_WIDTH, B_HEIGHT = 450, 400
# Отступ
MARGIN = 25

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Меня держит в рабстве питон')
        self.setFixedSize(WIDTH, HEIGHT)

        text_edit = QTextEdit(self)
        text_edit.resize(B_WIDTH, B_HEIGHT)
        text_edit.move(MARGIN, MARGIN)

        text_browser = QTextBrowser(self)
        text_browser.resize(B_WIDTH, B_HEIGHT)
        text_browser.move(WIDTH - B_WIDTH - MARGIN, MARGIN)

        btn = QPushButton('ПЕРЕГНАТЬ ТЕКСТ ЛЮТО', self)
        btn.setFixedWidth(300)
        btn_size = btn.size()
        btn.move(WIDTH // 2 - btn_size.width() // 2, HEIGHT - btn_size.height() - MARGIN)
        btn.clicked.connect(self.on_click)

        self.text_edit, self.text_browser, self.btn = text_edit, text_browser, btn

    def on_click(self):
        html = self.text_edit.toPlainText()
        self.text_browser.setText(html)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ide = Window()
    ide.show()
    sys.exit(app.exec())