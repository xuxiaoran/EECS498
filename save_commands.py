# Nick Shahin
import os, os.path
import sys
import shutil
import sqlite3

# Saves the given command to the database
def save_command(command):
    conn = sqlite3.connect('saved_commands.db')
    db = conn.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS commands (cid integer primary key autoincrement, command)")
    insert_command = "INSERT INTO commands (command) VALUES (\"" + command + "\")"
    db.execute(insert_command)
    conn.commit()
    conn.close()

# Retrieves all saved commands, and sends data back in a dictionary of the form {id: command}
def retrieve_commands():
    conn = sqlite3.connect('saved_commands.db')
    db = conn.cursor()
    db.execute("SELECT * FROM commands")
    data = db.fetchall()
    dic = {}
    for pair in data:
        dic[pair[0]] = pair[1]
    conn.commit()
    conn.close()
    return dic

# Deletes the command with the given command_id
def delete_command(command_id):
    conn = sqlite3.connect('saved_commands.db')
    db = conn.cursor()
    delete_command = "DELETE FROM commands WHERE cid = " + str(command_id)
    db.execute(delete_command)
    conn.commit()
    conn.close()