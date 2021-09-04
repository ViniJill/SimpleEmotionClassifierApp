# Load Database Packages
import sqlite3
conn sqlite3.connect('data.db')
c = conn.cursor()

# Database Functions
def create_page_visited_table():
    c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT, timeOfVisit TIMESTAMP)')

def add_page_visited_details(pagename, timeOfVisit):
    c.execute('INSERT INTO pageTrackTable(pagename, timeOfVisit) VALUES(?,?)', (pagename,timeOfVisit))
    conn.commit()

def view_all_page_visited_details():
    c.execute('SELECT * FROM pageTrackTable')
    data = c.fetchall()
    return data

# Function to Track Input and Prediction
def create_emotionclf_table():
    c.execute('CREATE TABLE IF NOT EXISTS emotionClfTable(rawtext TEXT, prediction TEXT, probability NUMBER, timeOfVisit TIMESTAMP)')

def add_prediction_details(rawtext, prediction, probability, timeOfVisit):
    c.execute('INSERT INTO emotionClfTable(rawtext, prediction, probability, timeOfVisit) VALUES(?,?,?,?)',(rawtext, prediction, probability, timeOfVisit))
    conn.commit()

def view_all_prediction_details():
    c.execute('SELECT * FROM emotionClfTable')
    data = c.fetchall()
    return data
