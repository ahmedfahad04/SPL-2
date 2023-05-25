from abc import ABC
from Backend.Database.connectDB import Database_Manager


class evaluation_assessment_data(Database_Manager, ABC):
    def __init__(self):
        super().__init__()


    def create_table(self) -> bool:
        """This private method will create lesson table that will store all the student information"""

        try:
            self.controller_db_cursor.execute('''CREATE TABLE IF NOT EXISTS evaluation_assessment_data
            (
            Student_ID INT NOT NULL,
            Student_Name VARCHAR(255),
            Task_ID VARCHAR(255) NOT NULL,
            Attempt INT NOT NULL,
            Success_Rate Number NOT NULL,
            Completion_Time Number NOT NULL,
            UNIQUE (Student_ID, Task_ID)
            )''')

            self.controller_db.commit()
            print("[CREATE] Evaluation Assessment Data Table created successfully!")
            return True

        except:
            return False

    def add_entry(self, data) -> bool:
        '''Insert the data to DB using a parameterized query'''

        try:
            self.controller_db_cursor.execute(
                "INSERT INTO evaluation_assessment_data (Student_ID, Student_Name, Task_ID, Attempt, Success_Rate ,Completion_Time)"
                "VALUES (?, ?, ?, ?, ?, ?)", tuple(data))

            self.controller_db.commit()
            print("[INSERT] Data inserted into Evaluation Assessment Data Table successfully!")
            return True

        except:
            
            data.append(data[0])
            data.append(data[2])
            self.update_entry(data)
            return False

    def load_table(self, id) -> list:
        print ('ID: ', id)
        self.controller_db_cursor.execute("SELECT * from evaluation_assessment_data WHERE Student_ID=?", (id, ))
        return self.controller_db_cursor.fetchall()

    def delete_entry(self, Student_ID, Lesson_ID) -> bool:

        try:
            res = self.controller_db_cursor.execute(
                '''DELETE FROM evaluation_assessment_data WHERE Student_ID=? Task_ID=?''', (Student_ID, Lesson_ID))
            self.controller_db.commit()

            print("[DELETE] Data Deleted successfully!")
            return True

        except:
            print("Evaluation Assessment Data deletion failed!")
            return False

    def update_entry(self, data) -> bool:

        try:

            print("GOT the query...")

            query = "UPDATE evaluation_assessment_data SET Student_ID = ?, Student_Name = ?, Task_ID = ?, Attempt = ?, Success_Rate = ?, Completion_Time = ? WHERE Student_ID = ? AND Task_ID = ?;"

            self.controller_db_cursor.execute(query, tuple(data))
            self.controller_db.commit()

            print("[UPDATE] Data updated successfully!")

            return True
        
        except Exception as e:
            
            print(e)
            return False
