from PyQt5.QtWidgets import (
    QMainWindow, QApplication, 
    QWidget, QComboBox, 
    QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout
)
import sys
import pandas as pd
from abc import abstractmethod

# create a parent Widget that counts correct answer 
# and give feedback. Inherit from that to create different 
# exercises

class Exercise(QWidget):

    def __init__(
            self, 
            data: pd.DataFrame, 
            num_questions: int = 10, 
            *args, 
            **kwargs
        ) -> None:

        super().__init__(*args, **kwargs)
        self.correct_answers = 0
        self.num_questions = num_questions
        self.current_question = 0
        self.create_components()
        self.layout_components()

    def create_components(self) -> None:

        self.question = QWidget(self)
        self.validate = QPushButton(self)
        self.validate.setText('validate')
        self.validate.clicked.connect(self.validate_answer)

        self.question_number = QLabel(self)
        self.question_number.setText(f'{self.current_question}')
        self.right_answers = QLabel(self)
        self.right_answers.setText(f'{self.corr}') 
    
    def layout_components(self) -> None:
        
        main_layout = QHBoxLayout(self)
        main_layout.addStretch()
        main_layout.addWidget(self.question)
        main_layout.addWidget(self.validate)
        main_layout.addWidget(self.question_number)
        main_layout.addWidget(self.right_answers)
        main_layout.addStretch()

    def next_question(self) -> None:
        self.current_question += 1
        self.question_number.setText(f'{self.current_question}')
        if self.current_question <= self.num_questions:
            self.generate_question()

    def validate_answer(self) -> None:
        if self.check():
            self.correct_answers += 1
            self.right_answers.setText(f'{self.correct_answers}')
        self.next_question()

    @abstractmethod
    def generate_question(self) -> None:
        pass
        
    @abstractmethod
    def check(self, *args , **kwargs) -> bool:
        pass

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


    def create_components(self) -> None:

        self.revision = QComboBox(self)
        for item in DATA:
            self.revision.addItem(item[0])
        self.revision.currentIndexChanged.connect(self.load_data)


    def layout_components(self) -> None:

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
