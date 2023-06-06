from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QSizePolicy
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Janela Responsiva")
        self.setGeometry(100, 100, 300, 300)

        # Cria o botão
        button = QPushButton("Botão")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setSizePolicy(sizePolicy)

        # Cria o layout da janela
        layout = QGridLayout()
        layout.addWidget(button, 0, 0, 1, 1)
        layout.setAlignment(button, Qt.AlignCenter)

        # Cria um widget para a janela
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
