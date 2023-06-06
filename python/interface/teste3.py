from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QLabel, QFrame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QHBoxLayout com Borda")
        self.setGeometry(100, 100, 300, 200)

        # Cria o QHBoxLayout
        layout = QHBoxLayout()

        # Cria os QLabel que serão adicionados ao layout
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")

        # Cria um QFrame para conter os QLabel e aplicar as bordas
        frame = QFrame()
        frame.setFrameStyle(QFrame.Box | QFrame.Plain)  # Define o estilo da borda
        frame.setLineWidth(1)  # Define a largura da borda

        # Cria um QHBoxLayout para o QFrame
        frame_layout = QHBoxLayout(frame)
        frame_layout.addWidget(label1)
        frame_layout.addWidget(label2)

        # Adiciona o QFrame ao layout principal
        layout.addWidget(frame)

        # Cria um QWidget para conter o layout principal
        widget = QWidget()
        widget.setLayout(layout)

        # Define o QWidget contendo o layout como widget central
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
