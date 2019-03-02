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
            print("Create Table: robot_ifsp")

        except MySQLdb.Error as e:
            print("Error %d: %s").format(e.args[0],e.args[1])



    def main(self):
        self.drop_database()
        self.create_database()
        self.db.close()


d = Database()
d.main()
