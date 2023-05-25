# from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
# from PyQt5.QtCore import Qt, QPropertyAnimation, QRect

# class ShakyLabel(QLabel):
#     def __init__(self, text):
#         super().__init__(text)
#         self.animation = QPropertyAnimation(self, b"geometry")
#         self.animation.setDuration(500)
#         self.animation.setLoopCount(3)  # Number of times the animation should repeat

#     def start_shaky_animation(self):
#         start_rect = self.geometry()
#         animation_rect = QRect(start_rect.x() - 5, start_rect.y(), start_rect.width(), start_rect.height())
#         self.animation.setStartValue(start_rect)
#         self.animation.setEndValue(animation_rect)
#         self.animation.start()

# # Example usage
# if __name__ == "__main__":
#     app = QApplication([])
#     window = QWidget()

#     layout = QVBoxLayout()

#     shaky_label = ShakyLabel("Shaky Label")

#     layout.addWidget(shaky_label)

#     window.setLayout(layout)
#     window.setGeometry(500, 500, 200, 200)
#     window.show()

#     shaky_label.start_shaky_animation()

#     app.exec()

import time 
print(time.time())