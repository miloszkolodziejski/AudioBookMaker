import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLabel, QHBoxLayout
import buttonController
import appUI


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = appUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.buttonController = buttonController.buttonController(self.ui)

        self.ui.browsePushButton.clicked.connect(lambda: self.buttonController.browseClick())
        self.ui.convertPushButton.clicked.connect(lambda: self.buttonController.convertClick())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Text to Audio Converter")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    window.setWindowIcon(icon)
    window.show()
    sys.exit(app.exec_())
