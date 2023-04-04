import window
import sys
from PySide6.QtWidgets import QApplication

# Run the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = window.MainWindow()
    sys.exit(app.exec())
