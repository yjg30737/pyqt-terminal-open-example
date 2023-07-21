import subprocess

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Thread(QThread):
    def __init__(self):
        super(Thread, self).__init__()

    def run(self):
        try:
            if sys.platform.startswith('win'):
                # For Windows (cmd)
                result = subprocess.run(['start', 'cmd', '/k', 'gen.bat'], capture_output=True, text=True, shell=True)
            elif sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
                # For Unix-based systems (shell)
                result = subprocess.run(["sh", "gen.sh"], capture_output=True, text=True, shell=True)

            # Check the return code to see if the command ran successfully
            if result.returncode == 0:
                print("Command executed successfully.")
            else:
                print("Command failed.")

        except Exception as e:
            raise Exception(e)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__initUi()

    def __initUi(self):
        btn = QPushButton('Run')
        btn.clicked.connect(self.__run)
        self.setCentralWidget(btn)

    def __run(self):
        self.__t = Thread()
        self.__t.start()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
