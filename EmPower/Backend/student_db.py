from abc import ABC
from Backend.connectDB import Database_Manager


class student_data(Database_Manager, ABC):
    def __init__(self):
        super().__init__()

    def create_table(self) -> bool:
        '''This private method will create Student table that will store all the student information'''

        try:
            self.controller_db_cursor.execute('''CREATE TABLE IF NOT EXISTS student_info
            (Std_ID INTEGER NOT NULL UNIQUE,
            Std_Name TEXT,
            Std_Age INTEGER,
            Guardian_Name TEXT,
            Contact_No TEXT)''')

            self.controller_db.commit()
            print("[CREATE] Table created successfully!")
            return True

        except:

            return False

    def add_entry(self, data) -> bool:
        '''Insert the data to DB using a parameterized query'''

        try:
            self.controller_db_cursor.execute(
                "INSERT INTO student_info VALUES (?, ?, ?, ?, ?)", tuple(data))

            self.controller_db.commit()
            print("[INSERT] Data inserted successfully!")
            return True

        except:

            return False

    def load_table(self) -> list:

        self.controller_db_cursor.execute("SELECT * FROM student_info")
        return self.controller_db_cursor.fetchall()

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

    def update_entry(self, data) -> bool:

        try:

            print("GOT the query...")

            query = "UPDATE student_info Set Std_ID=?, Std_Name=?, Std_Age=?, Guardian_Name=?, Contact_No=? Where Std_ID=?;"

            print("Data: ", data)

            self.controller_db_cursor.execute(query, tuple(data))
            self.controller_db.commit()

            print("[UPDATE] Data updated successfully!")

            return True
        except:

            return False