import sqlite3
import os


class Database_Manager:

    def __init__(self) -> None:

        # check if the database folder exists
        if not os.path.exists('Database'):
            os.mkdir('Database')
            print("Database folder created successfully!")

        # create database for student info
        self.student_db, self.student_db_cursor = self.__create_new_database(
            'student')

        self.lesson_db, self.lesson_db_cursor = self.__create_new_database(
            'lesson')

        self.assessment_db, self.assessment_db_cursor = self.__create_new_database(
            'assessment')

        print(self.__student_info_table())
        print('DB connected!')

    def __create_new_database(self, db_name):
        db_object = sqlite3.connect('Database\{}.db'.format(db_name))
        db_object_cursor = db_object.cursor()

        return db_object, db_object_cursor

    def __student_info_table(self) -> bool:

        '''This private method will create Student table that will store all the student information'''

        try:
            self.student_db_cursor.execute('''CREATE TABLE IF NOT EXISTS student_info
            (Std_ID INTEGER NOT NULL UNIQUE,
            Std_Name TEXT,
            Std_Age INTEGER,
            Guardian_Name TEXT,
            Contact_No TEXT)''')

            self.student_db.commit()
            return True

        except:

            return False

    def add_student_entry(self, data) -> bool:

        '''Insert the data to DB using a parameterized query'''
        
        try:
            self.student_db_cursor.execute("INSERT INTO student_info VALUES (?, ?, ?, ?, ?)", tuple(data))

            self.student_db.commit()
            print("Data inserted successfully!")
            return True 
        
        except:
            
            return False

    def load_student_entry(self) -> list:
    
        self.student_db_cursor.execute("SELECT * FROM student_info")
        return self.student_db_cursor.fetchall()
    
    def delete_student_entry(self, student_id) -> bool:
        
        print("ID: ",student_id)

        try:
            res = self.student_db_cursor.execute('''DELETE FROM student_info WHERE Std_ID = ?''', (student_id,))
            self.student_db.commit()  
        
            print("Student info deleted successfully!")
            return True
        
        except:
            print("Student info deletion failed!")
            return False
    
if __name__ == '__main__':
    db = Database_Manager()
