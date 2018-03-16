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


if __name__ == '__main__':
    if len(sys.argv) == 1:
        retrieve_commands()
    elif sys.argv[1] == 'add':
        save_command(sys.argv[2])
    elif sys.argv[1] == 'delete':
        delete_command(sys.argv[2])
