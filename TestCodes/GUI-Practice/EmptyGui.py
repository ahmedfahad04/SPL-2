import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)  # 2. Create QApplication object
window = QWidget()  # 3. Create window from QWidget object
window.show()  # 4. Call show to display GUI window
# 5. Start the event loop. Use sys.exit to close the program
sys.exit(app.exec())
