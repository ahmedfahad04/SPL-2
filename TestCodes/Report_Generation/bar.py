import matplotlib.pyplot as plt


class BarChart:
    
    def __init__(self, labels, values, x_label, y_label) -> None:
        
        self.labels = labels
        self.values = values
        self.x_label = x_label
        self.y_label = y_label
        self.init()
        
    def init(self):
    
        # Create a figure and axes
        fig, ax = plt.subplots()

        # Set the facecolor of the axes background
        ax.set_facecolor('#002B5B')

        # Create a bar chart with custom bar color
        bars = ax.bar(range(len(self.labels)), self.values, color='#8FE3CF', edgecolor='black')

        # Set x-label and y-label with fontsize and color
        ax.set_xlabel(self.x_label, fontsize=12, color='white')
        ax.set_ylabel(self.y_label, fontsize=12, color='white')

        # Set the title with fontsize and color
        ax.set_title('Bar Chart', fontsize=14, fontweight='bold', color='white')

        # Customize the tick parameters
        ax.tick_params(axis='x', labelrotation=0, labelsize=10, colors='white')
        ax.tick_params(axis='y', labelrotation=0, labelsize=10, colors='white')

        # Adjust the y-axis limit to provide some padding at the top
        ax.set_ylim(top=max(self.values) * 1.5)

        # Add the values as text labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height + 1, str(height), ha='center', va='bottom', fontsize=8, color='white')

        # Save the figure as a PNG image
        plt.savefig('.temp/bar_chart.png', dpi=300, facecolor=ax.get_facecolor())
