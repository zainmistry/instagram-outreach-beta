import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Placeholder GUI App')
        label = QLabel('Hello, this is a placeholder for gui_app.py!', self)
        label.setGeometry(50, 50, 300, 50)
        self.setGeometry(100, 100, 400, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 