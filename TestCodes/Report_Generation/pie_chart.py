import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class PieChart:
    
    def __init__(self, labels, values, fileName, headline):
        self.labels = labels[:10]  # Limit labels to 10
        self.values = values[:10]  # Limit values to 10
        self.fileName = fileName
        self.headline = headline
        self.create_chart()
        
    def create_chart(self):
        # Create a figure and axes
        fig, ax = plt.subplots()

        # Set the facecolor of the axes background
        ax.set_facecolor('#002B5B')

        # Create a pie chart with custom colors
        colors = ['#8FE3CF', '#FFD700', '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#C70039', '#FF5733', '#FFD700']
        ax.pie(self.values, labels=self.labels, colors=colors, autopct='%1.1f%%', startangle=90)

        # Set the title with fontsize and color
        ax.set_title(self.headline, fontsize=14, fontweight='bold', color='white')

        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')

        # Save the figure as a PNG image
        plt.savefig(f'.temp/{self.fileName}', dpi=300, facecolor=ax.get_facecolor())


if __name__ == '__main__':
    # create some data
    content_ID = [101, 102, 103, 104, 105]
    total_attempt = [10, 25, 5, 15, 20]

    app = QApplication(sys.argv)

    # create the widget and set its properties
    widget = PieChart(content_ID, total_attempt)

    # show the widget
    widget.show()

    sys.exit(app.exec_())
