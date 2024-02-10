from PyQt5.QtWidgets import (
    QMainWindow, QApplication, 
    QWidget, QVBoxLayout, 
    QHBoxLayout, QComboBox
)
import sys
import pandas as pd

DATA = [
    ('irregular verbs', 'irregular_verbs.csv'),
    ('declensions: definite', 'declensions_definite.csv'),
    ('declensions: indefinite', 'declensions_indefinite.csv'),
    ('declensions: nullartikel', 'declensions_nullartikel.csv'),
    ('declensions: reflected pronouns', 'declensions_reflected_pronouns.csv'),
    ('declensions: personal pronouns', 'declensions_personal_pronouns.csv')
]   

class DeutschRevisions(QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        
        super().__init__(*args, **kwargs)

        self.setWindowTitle('DeutschRevisions')
        self.data = None
        self.create_components()
        self.layout_components()
        self.show()


    def create_components(self):

        self.revision = QComboBox(self)
        for item in DATA:
            self.revision.addItem(item[0])
        self.revision.currentIndexChanged.connect(self.load_data)


    def layout_components(self):

        main_widget = QWidget()

        main_layout = QVBoxLayout(main_widget)
        main_layout.addWidget(self.revision)

        self.setCentralWidget(main_widget)


    def load_data(self, index: int) -> None:
        
        filename = DATA[index][1]
        self.data = pd.read_csv(filename)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = DeutschRevisions()
    sys.exit(app.exec())
