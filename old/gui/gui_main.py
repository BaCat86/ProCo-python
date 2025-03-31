from PyQt5.QtWidgets import QApplication, QWidget
import sys

main_app = QApplication(sys.argv)

window = QWidget()
window.show()

main_app.exec()