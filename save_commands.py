# Nick Shahin
# Xiaoran Xu
import os, os.path
import sys
import shutil
import sqlite3
import webbrowser

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
    #webbrowser.open('https://www.google.com/'+str(command_id)+ '+' + input_string)
    conn = sqlite3.connect('saved_commands.db')
    db = conn.cursor()
    edit_command = "UPDATE commands SET command = \"" + input_string + "\" WHERE cid = " + str(command_id)
    db.execute(edit_command)
    conn.commit()
    conn.close()



# Saves compound commands
# commands_list is a list of textual commands
def save_compound_command(commands_list):
    num_file = open("num_file", "r")
    pos = num_file.read()
    num_file.close()
    pos = int(pos)
    pos+=1
    num_file = open("num_file", "w")
    num_file.write(str(pos))
    num_file.close()

    filename = "compound_command_" + str(pos)
    command_file = open("filename", "w")
    command_file.writelines(commands_list)
    command_file.close()

# Returns a list of lists of commands. The first thing in each list of commands is the id for that compound command
def retrieve_compound_commands(compound_command_name):
    commands_list = []
    for possible_file in os.listdir("/"):
        if possible_file.find("compound_command_") != -1:
            pos = possible_file.replace("compound_command_", "")
            command_file = open(possible_file, "r")
            commands = command_file.readlines()
            command_file.close()
            commands.insert(0, pos)
            commands_list.append(commands)

    return commands_list

def delete_compound_command(compound_command_id):
    filename = "compound_command_" + str(compound_command_id)
    os.remove(filename)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        retrieve_commands()

    elif sys.argv[1] == 'add':
        save_command(sys.argv[2])

    elif sys.argv[1] == 'delete':
        delete_command(sys.argv[2])

    elif sys.argv[1] == 'edit':
        edit_command(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == 'rcompound':
        retrieve_compound_commands()

    elif sys.argv[1] == 'ncompound':
        save_compound_command(sys.argv[2])

    elif sys.argv[1] == 'dcompound':
        delete_compound_command(sys.argv[2])
