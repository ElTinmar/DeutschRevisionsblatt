from PyQt5.QtWidgets import (
    QMainWindow, QApplication, 
    QWidget, QVBoxLayout, 
    QHBoxLayout, QComboBox
)
import sys
import pandas as pd

class IrregularVerbTranslation(QWidget):

    def __init__(self, *args, **kwargs) -> None:    
        super().__init__(*args, **kwargs)


class IrregularVerb(QWidget):
    
    def __init__(self, *args, **kwargs) -> None:    
        super().__init__(*args, **kwargs)


class DeclensionDefinite(QWidget):
    
    def __init__(self, *args, **kwargs) -> None:    
        super().__init__(*args, **kwargs)


class DeclensionIndefinite(QWidget):
    
    def __init__(self, *args, **kwargs) -> None:    
        super().__init__(*args, **kwargs)


class DeclensionNull(QWidget):
    
    def __init__(self, *args, **kwargs) -> None:    
        super().__init__(*args, **kwargs)


class DeclensionReflected(QWidget):
    
    def __init__(self, *args, **kwargs) -> None:    
        super().__init__(*args, **kwargs)


class DeclensionPersonal(QWidget):
    
    def __init__(self, *args, **kwargs) -> None:    
        super().__init__(*args, **kwargs)


DATA = [
    ('irregular verbs', 'irregular_verbs.csv', IrregularVerb),
    ('irregular verbs: translation', 'irregular_verbs.csv', IrregularVerbTranslation),
    ('declensions: definite', 'declensions_definite.csv', DeclensionDefinite),
    ('declensions: indefinite', 'declensions_indefinite.csv', DeclensionIndefinite),
    ('declensions: nullartikel', 'declensions_nullartikel.csv', DeclensionNull),
    ('declensions: reflected pronouns', 'declensions_reflected_pronouns.csv', DeclensionReflected),
    ('declensions: personal pronouns', 'declensions_personal_pronouns.csv', DeclensionPersonal)
]   

class DeutschRevisions(QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        
        super().__init__(*args, **kwargs)

        self.setWindowTitle('DeutschRevisions')
        self.data = None
        self.exercise_widget = QWidget()
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
        main_layout.addWidget(self.exercise_widget)

        self.setCentralWidget(main_widget)


    def load_data(self, index: int) -> None:
        
        filename = DATA[index][1]
        self.data = pd.read_csv(filename)
        self.exercise_widget = DATA[index][2]()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = DeutschRevisions()
    sys.exit(app.exec())
