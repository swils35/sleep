#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:34:12 2020

@author: StephanieWilson
"""

import sqlite3 as sqlite
from sqlite3 import Error

# create a database connection
# param db_file: database file name
def connection(db_file):
    conn = None
    
    try:
        conn = sqlite.connect(db_file)
        return conn
    
    except Error as e:
        print(e)
        
    return conn


# create table from the create sql statements 
# param conn: connection
# param create_table_sql: a create table statement (housed in a variable)
def create_table(conn, create_table_sql):   
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        
    except Error as e:
        print(e)
    
def main():
    sql_create_exercise_table = '''CREATE TABLE IF NOT EXISTS exercise (
                                        exerciseid INTEGER PRIMARY KEY,
                                        activity INTEGER NOT NULL); '''
    
    sql_create_nights_table = '''CREATE TABLE IF NOT EXISTS nights (
                                    nightid INTEGER PRIMARY KEY,
                                    night TEXT NOT NULL);'''
    
    sql_create_report_table = '''CREATE TABLE IF NOT EXISTS report(
                                    id INTEGER PRIMARY KEY,
                                    night INTEGER NOT NULL,
                                    date TEXT NOT NULL,
                                    activity INTEGER,
                                    exercise_time INTEGER NOT NULL,
                                    exercise_hr INTEGER NOT NULL,
                                    time_til_sleep INTEGER NOT NULL,
                                    total_hours_sleep INTEGER NOT NULL,
                                    deep_sleep INTEGER NOT NULL,
                                    sleep_hr INTEGER NOT NULL,
                                    quality_score INTEGER,
                                    
                                    FOREIGN KEY(night) REFERENCES nights(nightid),
                                    FOREIGN KEY(activity) REFERENCES exercise(exerciseid)
                                    );'''
        
    create_connection = connection("sleepStudy.db")
    
    if create_connection is not None:
        create_table(create_connection, sql_create_exercise_table)
        
        create_table(create_connection, sql_create_nights_table)
        
        create_table(create_connection, sql_create_report_table)
        
    else:
        print("Error! Cannot create the db connection.")
        

if __name__ == '__main__':
    main()
        
    