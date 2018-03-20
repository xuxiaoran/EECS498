import sys, json, webbrowser

#Read command from front end
def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])

#do actual stuff here
def main():

    '''
    this is just to show that python can read from the front end
    CHANGE CODE BELOW
    '''
    webbrowser.open('https://www.google.com/')


if __name__ == '__main__':
    main()