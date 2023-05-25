import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar


class LineGraphWidget(QWidget):
    def __init__(self, content_ID, total_attempt):
        super().__init__()

        self.labels = content_ID
        self.values = total_attempt

        self.setWindowTitle('Line Graph View')
        self.setGeometry(100, 100, 600, 400)

        self.initUI()

    def initUI(self):
        # create a QVBoxLayout to add the plot to the widget
        layout = QVBoxLayout(self)

        # create a Matplotlib figure and canvas
        fig, ax = plt.subplots()
        canvas = FigureCanvas(fig)

        # create a line graph
        ax.plot(self.labels, self.values)

        # set x-label and y-label
        ax.set_ylabel('Total Attempt')
        ax.set_xlabel('Content ID')

        # add the navigation toolbar
        toolbar = NavigationToolbar(canvas, self)
        layout.addWidget(toolbar)

        # add the canvas to the layout
        layout.addWidget(canvas)
        
        # save the figure as a PNG image
        fig.savefig('line_graph.png', dpi=300)


if __name__ == '__main__':
    # create some data
    content_ID = [101, 102, 103, 104, 105]
    total_attempt = [10, 25, 5, 15, 20]

    app = QApplication(sys.argv)

    # create the widget and set its properties
    widget = LineGraphWidget(content_ID, total_attempt)

    # show the widget
    widget.show()

    sys.exit(app.exec_())
