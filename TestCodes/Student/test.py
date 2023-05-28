from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QMimeData, QPropertyAnimation, QRect
from PyQt5.QtGui import QDrag, QDragEnterEvent, QDragMoveEvent, QDropEvent, QPainter, QPixmap
from PyQt5.QtMultimedia import QSound

class DraggableLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setAcceptDrops(True)  # Enable drag events

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            drag = QDrag(self)
            mime_data = QMimeData()
            mime_data.setText(self.text())
            drag.setMimeData(mime_data)

            pixmap = QPixmap(self.size())
            painter = QPainter(pixmap)
            painter.drawPixmap(self.rect(), self.grab())
            painter.end()

            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.exec_(Qt.CopyAction | Qt.MoveAction)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

class DroppableLabel(QLabel):
    
    def __init__(self):
        super().__init__()
        
        # shaky animation
        
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(300)
        self.animation.setLoopCount(4)  # Number of times the animation should repeat
        self.animation.finished.connect(self.center_label)
        
        self.setAcceptDrops(True)  # Enable drop events

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasText():
            text = event.mimeData().text()
            
            if text == "Drag Me":
                self.setText(text)
            else: 
                self.start_shaky_animation()
                QSound.play("Frontend\Audio_Track\mistake_sound.wav")
                event.ignore()
                
    def center_label(self):
        parent_widget = self.parent()
        if parent_widget:
            center_x = (parent_widget.width() - self.width()) // 2
            center_y = (parent_widget.height() - self.height()) // 2
            self.move(center_x, self.height())                
                
    def start_shaky_animation(self):
        start_rect = self.geometry()
        animation_rect = QRect(start_rect.x() - 10, start_rect.y(), start_rect.width(), start_rect.height())
        self.animation.setStartValue(start_rect)
        self.animation.setEndValue(animation_rect)
        self.animation.start()

# Example usage
if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()

    layout = QVBoxLayout()

    draggable_label = DraggableLabel("Drag Me!!")
    
    droppable_label = DroppableLabel()
    droppable_label.setText("??")
    droppable_label.setStyleSheet("border: 5px solid blue; color: white;")

    layout.addWidget(draggable_label)
    layout.addWidget(droppable_label)

    window.setLayout(layout)
    window.setGeometry(500, 500, 200, 200)
    window.show()

    app.exec()
