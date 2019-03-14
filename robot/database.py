#!/usr/bin/env python3

# import MySQLdb
import mysql.connector
from mysql.connector import Error


"""Connector mysql"""
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123"
)
db = db
cursor = db.cursor()


class Database:
    def __init__(self):
        self.db = db 
        self.cursor = cursor
        print(db.is_connected())


    def drop_database(self):
        cursor.execute("DROP DATABASE IF EXISTS robot_ifsp")
        print("Drop database: robot_ifsp")


    def create_database(self):
        cursor.execute("CREATE DATABASE robot_ifsp")
        print("Create Database: robot_ifsp")


    def create_table(self):
        self.create_table_courses()


    def create_table_courses(self):
        table = """
            CREATE TABLE robot_ifsp.courses (
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                url VARCHAR(255),
                introdution TEXT 
            );
            """
        cursor.execute(table)
        cursor.execute("Use robot_ifsp")
        print("Create Table courses")


    
    def insert_table_courses(self, name, url, introdution):
        insert = """
                INSERT INTO robot_ifsp.courses (name, url, introdution) VALUES(
                    '{0}',
                    '{1}',
                    '{2}'
                );
        """.format(name, url, introdution)

        cursor.execute(insert)
        db.commit()
        print(insert)


    def run(self):
        self.drop_database()
        self.create_database()
        self.create_table()


d = Database()
d.run()
