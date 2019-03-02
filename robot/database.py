#!/usr/bin/env python3

import MySQLdb
import sys


class Database:
    def __init__(self):
        self.db = None
        self.cursor = None

    def connector(self):
        """Connector mysql"""
        try:
            db = MySQLdb.connect(
                host="localhost",
                user="root",
                password="123"
            )
            self.db = db
            self.cursor = db.cursor()

        except MySQLdb.Error as e:
            print("Error %d: %s").format(e.args[0],e.args[1])


    def drop_database(self):
        self.connector()
        self.cursor.execute("DROP DATABASE IF EXISTS robot_ifsp")


    def create_database(self):
        try:
            self.connector()
            self.cursor.execute("CREATE DATABASE robot_ifsp")
            print("Create Database: robot_ifsp")

        except MySQLdb.Error as e:
            print("Error %d: %s").format(e.args[0],e.args[1])


    def create_table_courses(self):
        table = """
            CREATE TABLE courses (
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                url VARCHAR(255)
            );
            """
        self.cursor.execute(table)
        print("CREATE TABLE courses")


    def create_table(self):
        self.connector()
        self.cursor.execute("USE robot_ifsp")
        self.create_table_courses()


    def run(self):
        self.drop_database()
        self.create_database()
        self.create_table()
        self.db.close()


d = Database()
d.run()
