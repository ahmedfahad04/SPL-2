from abc import ABC
from Backend.Database.connectDB import Database_Manager


class lesson_assiging_data(Database_Manager, ABC):
    def __init__(self):
        super().__init__()


    def create_table(self) -> bool:
        """This private method will create lesson table that will store all the student information"""

        try:
            self.controller_db_cursor.execute('''CREATE TABLE IF NOT EXISTS lesson_assiging_data
            (
            Student_ID INT NOT NULL,
            Student_Name VARCHAR(255),
            Lesson_ID INT NOT NULL,
            MCQ_ID Varchar(255),
            Sequence_ID VarChar(255),
            Matching_ID VarChar(255),
            Puzzle_ID VarChar(255),
            Date DATETIME NOT NULL,
            UNIQUE (Student_ID, Student_Name, Lesson_ID, Date)
            )''')

            self.controller_db.commit()
            print("[CREATE] LESSON Assigning Table created successfully!")
            return True

        except:

            return False

    def add_entry(self, data) -> bool:
        '''Insert the data to DB using a parameterized query'''

        try:
            self.controller_db_cursor.execute(
                "INSERT INTO lesson_assiging_data (Student_ID, Student_Name, Lesson_ID, MCQ_ID, Sequence_ID, Matching_ID, Puzzle_ID, Date)"
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)", tuple(data))

            self.controller_db.commit()
            print("[INSERT] Data inserted into LESSON Assiging Table successfully!")
            return True

        except:

            return False

    def load_table(self) -> list:

        self.controller_db_cursor.execute("SELECT * FROM lesson_assiging_data")
        return self.controller_db_cursor.fetchall()

    def delete_entry(self, Student_ID) -> bool:

        try:
            res = self.controller_db_cursor.execute(
                '''DELETE FROM lesson_assiging_data WHERE Student_ID=?''', (Student_ID))
            self.controller_db.commit()

            print("[DELETE] Data Deleted successfully!")
            return True

        except:
            print("Lesson Table deletion failed!")
            return False

    def update_entry(self, data) -> bool:

        try:

            print("GOT the query...")

            query = "UPDATE lesson_data Set Student_ID=?, Student_Name=?, Lesson_ID=?, Date=? Where " \
                    "Student_ID=?;"

            self.controller_db_cursor.execute(query, tuple(data))
            self.controller_db.commit()

            print("[UPDATE] Data updated successfully!")

            return True
        
        except Exception as e:
            
            print(e)
            return False
