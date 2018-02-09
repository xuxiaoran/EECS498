# Nick Shahin
# http://appjar.info

from appJar import gui
app = gui("Main Window", "600x350")

def main():

    # Define gui
    app.setTitle("Better Butler")
    app.setBg("white")
    app.setFont(48)

    # Input
    app.startLabelFrame("What can I do for you?")
    app.addEntry("command_input")
    app.setEntryDefault("command_input", "Type commands here")
    app.setEntrySubmitFunction("command_input", handleCommand)

    app.setFont(28)
    # Virtual keyboard
    app.addButtons([["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"], ["A", "S", "D", "F", "G", "H", "J", "K", "L"], ["Z", "X", "C", "V", "B", "N", "M"]], press)
    letters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
    app.setButtonWidths(letters, 40)
    # app.setButtonHeights(letters, 40)
    app.addButtons([["ENTER", "   SPACE   "]], press)
    app.stopLabelFrame()

    # Run
    app.go()

def press(button):
    if button == "ENTER":
        handleCommand("command_input")
    elif button == "   SPACE   ":
        app.setEntry("command_input", app.getEntry("command_input") + " ", callFunction=False)
    else:
        app.setEntry("command_input", app.getEntry("command_input") + button, callFunction=False)

def handleCommand(entry):
	print(app.getEntry(entry))
	app.clearEntry("command_input", callFunction=False)

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
