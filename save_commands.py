# Nick Shahin
# Xiaoran Xu
import os, os.path
import sys
import shutil
import sqlite3

def output(msg):
    print(msg.encode('unicode-escape'))
    sys.stdout.flush()

# Retrieves all saved commands, and sends data back in a dictionary of the form {id: command}
def retrieve_commands():
    conn = sqlite3.connect('saved_commands.db')
    db = conn.cursor()
    db.execute("SELECT * FROM commands")
    data = db.fetchall()
    dic = {}
    for pair in data:
        dic[str(pair[0])] = str(pair[1])
    conn.commit()
    conn.close()
    for key, value in dic.items():
        output(str(key+'%'+value))

# Saves the given command to the database
def save_command(command):
    conn = sqlite3.connect('saved_commands.db')
    db = conn.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS commands (cid integer primary key autoincrement, command)")
    insert_command = "INSERT INTO commands (command) VALUES (\"" + command + "\")"
    db.execute(insert_command)

    db.execute("SELECT MAX(cid) FROM commands")
    new_id = db.fetchone()
    conn.commit()
    conn.close()
    output(str(new_id[0]))


# Deletes the command with the given command_id
def delete_command(command_id):
    conn = sqlite3.connect('saved_commands.db')
    db = conn.cursor()
    delete_command = "DELETE FROM commands WHERE cid = " + str(command_id)
    db.execute(delete_command)
    conn.commit()
    conn.close()


# Edits the command with command_id to be input_string
def edit_command(command_id, input_string):
    conn = sqlite3.connect('saved_commands.db')
    db = conn.cursor()
    edit_command = "UPDATE commands SET command = " + str(input_string) + " WHERE cid = " + int(command_id)
    db.execute(edit_command)
    conn.commit()
    conn.close()


# Saves compound commands
# command_list is a string of comma-separated command ids, such as 1,2,3,4,5
def save_compound_command(command_ids):
    conn = sqlite3.connect('saved_commands.db')
    db = conn.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS compound_commands (ccid integer primary key autoincrement, command_list)")
    compound_command = ""
    for cid in command_ids:
        compound_command = compound_command + str(cid) + ","
    insert_command = "INSERT INTO compound_commands (command_list) VALUES (\"" + compound_command + "\")"
    db.execute(insert_command)
    conn.commit()
    conn.close()


# Returns a list of lists of command_ids [[list of command ids][list of command ids][list of command ids][etc]]
# On the front end, we'll need to match up this list of IDs with the data from retrieve_commands to 
# put together what the actual compound commands looks like
def retrieve_compound_commands():
    conn = sqlite3.connect('saved_commands.db')
    db = conn.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS compound_commands (ccid integer primary key autoincrement, command_list)")
    db.execute("SELECT * FROM compound_commands")
    data = db.fetchall()
    dic = {}
    for pair in data:
        dic[str(pair[0])] = str(pair[1].split(","))
    conn.commit()
    conn.close()
    for key, value in dic.items():
        output(str(key+'%'+value))



if __name__ == '__main__':
    if len(sys.argv) == 1:
        retrieve_commands()
    elif sys.argv[1] == 'add':
        save_command(sys.argv[2])
    elif sys.argv[1] == 'delete':
        delete_command(sys.argv[2])
