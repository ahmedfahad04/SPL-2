import matplotlib.pyplot as plt

class PieChart:
    
    def __init__(self, labels, values, fileName, headline):
        self.labels = labels  # Limit labels to 10
        self.values = values # Limit values to 10
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
        # ax.pie(self.values, labels=self.labels, colors=colors, autopct='%1.1f%%', startangle=90)

        patches, texts, autotexts = ax.pie(self.values, labels=self.labels, autopct='%1.1f%%')
            
        # Set the value color to a different color (e.g., red)
        for text in texts:
            text.set_color('white')
            
        for autotext in autotexts:
            autotext.set_color('black')

        # Set the title with fontsize and color
        ax.set_title(self.headline, fontsize=14, fontweight='bold', color='white')

        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')

        # Save the figure as a PNG image
        plt.savefig(f'.temp/{self.fileName}', dpi=300, facecolor=ax.get_facecolor())

        
labels = ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5', 'Label 6']
values = [25, 35, 15, 25, 29, 30]
fileName = 'pie_chart.png'
headline = 'Pie Chart Example'

chart = PieChart(labels, values, fileName, headline)
chart.create_chart()

