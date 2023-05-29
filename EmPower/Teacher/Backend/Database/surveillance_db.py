from abc import ABC
from Backend.Database.connectDB import Database_Manager


class surveillance_data(Database_Manager, ABC):
    def __init__(self):
        super().__init__()


    def create_table(self) -> bool:
        """This private method will create lesson table that will store all the student information"""

        try:
            self.controller_db_cursor.execute('''CREATE TABLE IF NOT EXISTS surveillance_data
            (
            Student_ID INT NOT NULL,
            Student_Name VARCHAR(255),
            Lesson_ID VARCHAR(255) NOT NULL,
            Module_ID VARCHAR(255) NOT NULL,
            Completion_Time VARCHAR(255) NOT NULL,
            UNIQUE (Student_ID, Lesson_ID, Module_ID)
            )''')

            self.controller_db.commit()
            print("[CREATE] Surveillance Table created successfully!")
            return True

        except:

            return False

    def add_entry(self, data) -> bool:
        '''Insert the data to DB using a parameterized query'''

        try:
            self.controller_db_cursor.execute(
                "INSERT INTO surveillance_data (Student_ID, Student_Name, Lesson_ID, Module_ID, Completion_Time)"
                "VALUES (?, ?, ?, ?, ?)", tuple(data))

            self.controller_db.commit()
            print("[INSERT] Data inserted into surveillance_data Table successfully!")
            return True

        except Exception as e:

            print("surveillance_data Table insertion failed!", e)
            return False

    def load_table(self, sid) -> list:

        self.controller_db_cursor.execute("SELECT * from surveillance_data WHERE Student_ID=?", (sid,))
        return self.controller_db_cursor.fetchall()

    def delete_entry(self, Student_ID, Lesson_ID) -> bool:

        try:
            res = self.controller_db_cursor.execute(
                '''DELETE FROM lesson_performance_data WHERE Student_ID=? Lesson_ID=?''', (Student_ID, Lesson_ID))
            self.controller_db.commit()

            print("[DELETE] Data Deleted successfully!")
            return True

        except:
            print("Lesson Table deletion failed!")
            return False

    def update_entry(self, data) -> bool:

        try:

            print("GOT the query...")

            query = "UPDATE surveillance_data Set Lesson_ID=?, Module_ID=?, Completion_Time=? Where " \
                    "Lesson_ID=?, Module_ID=?;"

            self.controller_db_cursor.execute(query, tuple(data))
            self.controller_db.commit()

            print("[UPDATE] Data updated successfully!")

            return True
        
        except Exception as e:
            
            print(e)
            return False
