import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class PieChartWidget(QWidget):
    def __init__(self, content_ID, total_attempt):
        super().__init__()

        self.labels = content_ID
        self.values = total_attempt

        self.setWindowTitle('Pie Chart View')
        self.setGeometry(100, 100, 600, 400)

        self.initUI()

    def initUI(self):
        # create a QVBoxLayout to add the plot to the widget
        layout = QVBoxLayout(self)

        # create a Matplotlib figure and canvas
        fig, ax = plt.subplots()
        canvas = FigureCanvas(fig)

        # create a pie chart
        ax.pie(self.values, labels=self.labels, autopct='%1.1f%%')

        # add the canvas to the layout
        layout.addWidget(canvas)


if __name__ == '__main__':
    # create some data
    content_ID = [101, 102, 103, 104, 105]
    total_attempt = [10, 25, 5, 15, 20]

    app = QApplication(sys.argv)

    # create the widget and set its properties
    widget = PieChartWidget(content_ID, total_attempt)

    # show the widget
    widget.show()

    sys.exit(app.exec_())
