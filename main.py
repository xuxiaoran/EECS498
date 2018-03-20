import sys, json, webbrowser
from forwarding_file import send_command
import sched, time

'''s = sched.scheduler(time.time, time.sleep)
def newToken(sc): 
    print "************ Refreshing Token ************"
    refreshToken()
    s.enter(3500, 1, newToken, (sc,))

s.enter(3500, 1, newToken, (s,))
s.run()'''        

#Read command from front end
def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])

#do actual stuff here
def main():
    lines = read_in()
    line = ''
    for item in lines:
        line += item

    '''
    this is just to show that python can read from the front end
    CHANGE CODE BELOW
    '''
    send_command(line)

if __name__ == '__main__':
    main()