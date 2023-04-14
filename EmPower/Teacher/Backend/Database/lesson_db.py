from abc import ABC
from Backend.Database.connectDB import Database_Manager


class lesson_data(Database_Manager, ABC):
    def __init__(self):
        super().__init__()

        self.create_table()

    def create_table(self) -> bool:
        """This private method will create lesson table that will store all the student information"""

        try:
            self.controller_db_cursor.execute('''CREATE TABLE IF NOT EXISTS lesson_data
            (
            Content_Type INT NOT NULL,
            Content_ID INT NOT NULL,
            Content_Topic VARCHAR(255) NOT NULL,
            Content_Path VARCHAR(255),
            PRIMARY KEY (Content_Type, Content_ID)
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
                "INSERT INTO lesson_data (Content_Type, Content_ID, Content_Topic, Content_Path)"
                "VALUES (?, ?, ?, ?)", tuple(data))

            self.controller_db.commit()
            print("[INSERT] Data inserted into LESSON successfully!")
            return True

        except:

            return False

    def load_table(self) -> list:

        self.controller_db_cursor.execute("SELECT * FROM lesson_data")
        return self.controller_db_cursor.fetchall()

    def delete_entry(self, Content_Type, Content_ID) -> bool:

        print("ID: ", Content_Type, Content_ID)

        try:
            res = self.controller_db_cursor.execute(
                '''DELETE FROM lesson_data WHERE Content_Type=?, Content_ID=?''', (Content_Type, Content_ID))
            self.controller_db.commit()

            print("[DELETE] Data Deleted successfully!")
            return True

        except:
            print("Lesson Table deletion failed!")
            return False

    def update_entry(self, data) -> bool:

        try:

            print("GOT the query...")

            query = "UPDATE lesson_data Set Content_Type=?, Content_ID=?, Content_Topic=?, Content_Path=? Where " \
                    "Content_Type=?, Content_ID=?;"

            print("Data: ", data)

            self.controller_db_cursor.execute(query, tuple(data))
            self.controller_db.commit()

            print("[UPDATE] Data updated successfully!")

            return True
        except:

            return False
