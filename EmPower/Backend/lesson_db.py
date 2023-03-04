from abc import ABC
from Backend.connectDB import Database_Manager


class lesson_data(Database_Manager, ABC):
    def __init__(self):
        super().__init__()
        
        self.create_table()

    def create_table(self) -> bool:
        '''This private method will create lesson table that will store all the student information'''

        try:
            self.controller_db_cursor.execute('''CREATE TABLE IF NOT EXISTS lesson_data
            (
            Category_ID INT NOT NULL,
            Lesson_ID INT NOT NULL,
            Lesson_Topic VARCHAR(255) NOT NULL,
            Lesson_Image VARCHAR(255),
            Lesson_Audio VARCHAR(255),
            PRIMARY KEY (Category_ID, Lesson_ID)
            )''')

            self.controller_db.commit()
            print("[CREATE] LESSON Table created successfully!")
            return True

        except:

            return False

    def add_entry(self, data) -> bool:
        '''Insert the data to DB using a parameterized query'''

        try:
            self.controller_db_cursor.execute(
                "INSERT INTO lesson_data (Category_ID, Lesson_ID, Lesson_Topic, Lesson_Image, Lesson_Audio)"
                "VALUES (?, ?, ?, ?, ?)", tuple(data))

            self.controller_db.commit()
            print("[INSERT] Data inserted into LESSON successfully!")
            return True

        except:

            return False

    def load_table(self) -> list:

        self.controller_db_cursor.execute("SELECT * FROM lesson_data")
        return self.controller_db_cursor.fetchall()

    # need to change...
    def delete_entry(self, student_id) -> bool:

        print("ID: ", student_id)

        try:
            res = self.controller_db_cursor.execute(
                '''DELETE FROM student_info WHERE Std_ID = ?''', (student_id,))
            self.controller_db.commit()

            print("[DELETE] Data Deleted successfully!")
            return True

        except:
            print("Student info deletion failed!")
            return False

    # need to change
    def update_entry(self, data) -> bool:

        try:

            print("GOT the query...")

            query = "UPDATE lesson_data Set Std_ID=?, Std_Name=?, Std_Age=?, Guardian_Name=?, Contact_No=? Where " \
                    "Std_ID=?;"

            print("Data: ", data)

            self.controller_db_cursor.execute(query, tuple(data))
            self.controller_db.commit()

            print("[UPDATE] Data updated successfully!")

            return True
        except:

            return False
