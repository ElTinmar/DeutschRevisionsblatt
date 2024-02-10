from PyQt5.QtWidgets import (
    QMainWindow, QApplication, 
    QWidget, QVBoxLayout, 
    QHBoxLayout, QComboBox
)
import sys
import pandas as pd

# maybe create a parent Widget that counts correct answer 
# and give feedback. Inherit from that to create different 
# exercises

class Exercise(QWidget):

    def __init__(self, data: pd.DataFrame, *args, **kwargs) -> None:    
        super().__init__(*args, **kwargs)

class IrregularVerbTranslation(Exercise):
    pass

class IrregularVerb(Exercise):
    pass

class DeclensionDefinite(Exercise):
    pass

class DeclensionIndefinite(Exercise):
    pass

class DeclensionNull(Exercise):
    pass

class DeclensionReflected(Exercise):
    pass

class DeclensionPersonal(Exercise):
    pass

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
        data = pd.read_csv(filename)
        self.exercise_widget = DATA[index][2](data)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = DeutschRevisions()
    sys.exit(app.exec())
