from fpdf import FPDF
import datetime

class Report_Card_Generator(FPDF):
    
    def __init__(self, student_details=None, report_card_name=None):
        super().__init__()
        
        print("student_details: ", student_details)
        self.student_data = student_details
        self.report_card_name = report_card_name
    
    def header(self):
        print("Entering Header!")
        self.image(r"Backend\PDF_ReportGeneration\footer.PNG", 0, 0, self.w + 2)

    def footer(self):
        print("Entering Footer!")
        self.image(r"Backend\PDF_ReportGeneration\footer.PNG", 0, self.h - 5, self.w + 2)

        temp_y = -50
        while temp_y != -350:
            self.set_y(temp_y)
            self.image(r'Backend\PDF_ReportGeneration\leftBorder.PNG', x=0, y=self.get_y(), w=8)
            self.image(r'Backend\PDF_ReportGeneration\rightBorder.PNG', x=self.w - 8, y=self.get_y(), w=8)
            temp_y = temp_y - 50

        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f"Created on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 0, 'R')

    def student_details(self, name, student_id, guardian_name, phone, address):
        
        print("Processissng Student Details!")
        self.ln(100)
        self.set_font('Arial', 'B', 16)

        self.set_fill_color(1, 42, 89)  # Set background color to blue
        self.set_text_color(255, 255, 255)  # Set text color to white

        # Set cell width and height
        cell_width = self.w - (2 * self.l_margin)
        cell_height = 15
        self.cell(cell_width, cell_height, "Student Details", ln=True, align='C', fill=True)

        # Set table properties
        self.set_fill_color(1, 42, 89)  # Set background color to blue
        self.set_text_color(255, 255, 255)  # Set text color to white
        self.set_font('Arial', 'B', 12)

        # Set column widths
        col_width = (self.w - (2 * self.l_margin)) / 2 - 0.1
        col_height = 8

        # Reset table properties for cell content
        self.set_fill_color(255)  # Reset background color
        self.set_text_color(0)  # Reset text color
        self.set_font('Arial', 'B', 12)

        # Display table rows
        self.cell(col_width, col_height, 'Student Name', 1, 0, 'L', fill=True)
        self.cell(col_width, col_height, name, 1, 1, 'L')

        self.cell(col_width, col_height, 'Student ID', 1, 0, 'L', fill=True)
        self.cell(col_width, col_height, student_id, 1, 1, 'L')

        self.cell(col_width, col_height, 'Guardian Name', 1, 0, 'L', fill=True)
        self.cell(col_width, col_height, guardian_name, 1, 1, 'L')

        self.cell(col_width, col_height, 'Phone', 1, 0, 'L', fill=True)
        self.cell(col_width, col_height, phone, 1, 1, 'L')

        self.cell(col_width, col_height, 'Address', 1, 0, 'L', fill=True)
        self.cell(col_width, col_height, address, 1, 1, 'L')

        self.ln(10)

    def report_details(self):
        
        print("Processing Report Details!")
        self.ln(20)
        self.set_font('Arial', 'B', 16)

        self.set_fill_color(1, 42, 89)  # Set background color to blue
        self.set_text_color(255, 255, 255)  # Set text color to white

        # Set cell width and height
        cell_width = self.w - (2 * self.l_margin)
        cell_height = 15
        self.cell(cell_width, cell_height, "Report Details", ln=True, align='C', fill=True)

        # Set table properties
        self.set_fill_color(1, 42, 89)  # Set background color to blue
        self.set_text_color(255, 255, 255)  # Set text color to white
        self.set_font('Arial', 'B', 12)

        # Set column widths
        col_width = (self.w - (2 * self.l_margin)) / 2 - 0.1
        col_height = 8

        # Reset table properties for cell content
        self.set_fill_color(255)  # Reset background color
        self.set_text_color(0)  # Reset text color
        self.set_font('Arial', 'B', 12)

        # Display table rows
        self.cell(col_width, col_height, 'Month', 1, 0, 'L', fill=True)
        self.cell(col_width, col_height, datetime.datetime.now().strftime('%B'), 1, 1, 'L')

        self.cell(col_width, col_height, 'Date', 1, 0, 'L', fill=True)
        self.cell(col_width, col_height, str(datetime.date.today()), 1, 1, 'L')

        self.ln(10)

    def signature_section(self):
        
        print("Processing Signature Section!")
        self.ln(20)
        # Signature Section
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(255)  # Reset background color
        self.set_text_color(0)  # Reset text color

        # Add signature text
        self.cell(0, 10, "Signature:", ln=True, align='L', fill=False)
        self.ln(5)

        # Add a line for signature
        self.line(self.l_margin,  self.get_y(),  self.w - 100,  self.get_y())

    def create_report(self, filename="student_report_card.self"):
        
        print("Creating Report Card!")
        
        ''' First Page '''
        self.add_page()
        self.image(r"Backend\PDF_ReportGeneration\banner.PNG", 0, 0, self.w)
        
        std_id = str(self.student_data[0])
        name = self.student_data[1]
        address = self.student_data[3]
        guardian_name = self.student_data[4]
        phone = self.student_data[5]
       
        self.student_details(
            name,
            std_id, 
            address,
            guardian_name,
            phone
        )
        
        self.report_details()
        self.signature_section()

        ''' Second Page '''
        self.add_page()

        self.image(".temp\matching_success_rate_bar_chart.png", 5, 20, self.w / 2 - 10)
        self.image(".temp\matching_time_bar_chart.png", self.w / 2, 20, self.w / 2 - 10)

        self.image(".temp\puzzle_success_rate_bar_chart.png", 5, 110, self.w / 2 - 10)
        self.image(".temp\puzzle_time_bar_chart.png", self.w / 2, 110, self.w / 2 - 10)

        self.image(".temp\sequence_success_rate_bar_chart.png", 5, 200, self.w / 2 - 10)
        self.image(".temp\sequence_time_bar_chart.png", self.w / 2, 200, self.w / 2 - 10)
        
        self.add_page()
        
        self.image(".temp\mcq_success_rate_bar_chart.png", 5, 200, self.w / 2 - 10)
        self.image(".temp\mcq_time_bar_chart.png", self.w / 2, 200, self.w / 2 - 10)
        
        self.image(".temp\lesson_attempt_bar_chart.png", 5, 20, self.w / 2 - 10)
        self.image(".temp\lesson_time_bar_chart.png", self.w / 2, 20, self.w / 2 - 10)

        self.output('Reports/'+self.report_card_name)
        print("Report Card Created Successfully")

# if __name__ == '__main__':
#     create_report()
