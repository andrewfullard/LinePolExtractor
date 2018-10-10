from lines_pol_gui import MainWindow
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication([])

    mainWindow: MainWindow = MainWindow()
    mainWindow.getWindow().show()

    app.exec_()

if __name__ == "__main__":
    main()