import sqlite3
import os
from abc import ABC, abstractmethod


class Database_Manager:
    
    def __init__(self) -> None:
        
        self.db_name = 'controller'

        # check if the database folder exists
        if not os.path.exists('Backend/Database'):
            os.mkdir('Backend/Database')
            print("Database folder created successfully!")

        # create database for student info
        self.controller_db, self.controller_db_cursor = self.__create_new_database(self.db_name)

        if os.path.exists('Backend/Database/{}'.format(self.db_name)):
            print("Student database found!")
        else:
            self.create_table()

    # ?Generic Method of CRUD

    def __create_new_database(self, db_name):
        db_object = sqlite3.connect('Backend\Database\{}.db'.format(db_name))
        db_object_cursor = db_object.cursor()

        return db_object, db_object_cursor

    @abstractmethod
    def create_table(self) -> bool:
        pass

    @abstractmethod
    def add_entry(self, data) -> bool:
        pass

    @abstractmethod
    def load_table(self) -> list:
        pass

    @abstractmethod
    def delete_table(self) -> bool:
        pass

    @abstractmethod
    def delete_entry(self) -> bool:
        pass

    @abstractmethod
    def update_entry(self, data) -> bool:
        pass
    