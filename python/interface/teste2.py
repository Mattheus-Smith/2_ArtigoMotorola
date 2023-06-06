from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo TableView")
        self.setGeometry(100, 100, 400, 300)

        # Cria o modelo de dados
        self.model = QStandardItemModel()

        # Adiciona os cabeçalhos das colunas
        self.model.setHorizontalHeaderLabels(['Nome', 'Idade', 'Profissão'])

        # Adiciona alguns itens
        self.add_item("João", 25, "Engenheiro")
        self.add_item("Maria", 30, "Advogada")
        self.add_item("Pedro", 40, "Professor")

        # Cria o TableView e define o modelo de dados
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        # Cria o layout da janela
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)

        # Cria um widget para a janela
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def add_item(self, nome, idade, profissao):
        item_nome = QStandardItem(nome)
        item_idade = QStandardItem(str(idade))
        item_profissao = QStandardItem(profissao)

        self.model.appendRow([item_nome, item_idade, item_profissao])

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
