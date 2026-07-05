import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as sql
from mysql.connector import Error
import os

try:
    connection = sql.connect(
        host='localhost',
        user='root',
        password='VlUhhrER9#S',
        database='stockmarket'
    )

    if connection.is_connected():
        print("Connected to MySQL database successfully!")
        cursor = connection.cursor()
    
except Error as e:
    print(f"Error while connecting to MySQL: {e}")

token = os.getenv("OPEN_ROUTER_API_KEY")
if not token:
    raise RuntimeError("Set OPEN_ROUTER_API_KEY in your environment")

def execute(query, params=None):
    cursor.execute(query, params or ())
    return cursor.fetchall()

def manipulate(sql, val):
    cursor.execute(sql, val)
    connection.commit()


print(token)


