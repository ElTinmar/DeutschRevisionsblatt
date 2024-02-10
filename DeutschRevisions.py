from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QTabWidget, QHBoxLayout
import sys

class DeutschRevisions(QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        
        super().__init__(*args, **kwargs)

        self.setWindowTitle('ZebraTrack')
        self.create_components()
        self.layout_components()
        self.show()

    def create_components(self):
        pass

    def layout_components(self):
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = DeutschRevisions()
    sys.exit(app.exec())
