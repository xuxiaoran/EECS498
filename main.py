import sys, json, webbrowser
from forwarding_file import send_command
import sched, time

def main(cmd):
    '''
    this is just to show that python can read from the front end
    CHANGE CODE BELOW
    '''
    send_command(cmd)

if __name__ == '__main__':
    main(sys.argv[1])