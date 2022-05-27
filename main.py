import keyboard
import time
import os


def Clear():
    os.system('cls')


def Hello():
    print("Hotkey and macros manager by DOOMB")
    time.sleep(3)
    Clear()


def Help():
    print("newhk       Create new hotkey;\n"
          "clearhklist  Clear HotkeyList.txt;\n"
          "run          Run macros catcher.")


def HelpHk():
    print("Write key name or hotkey just like in this example:\n"
          "ctrl+p\n"
          "p\n\n"
          "Next you have to write a key name and delay between presses like this:\n"
          "a 3 b 3 j 1 ctrl 2")


def MainMenu():
    Help()
    while True:
        inp = input()
        if inp == "newhk":
            with open("MacrosList.txt", "a") as f:
                HelpHk()
                f.write(f"{input()}: {input()}\n")
                Clear()
                Help()
                f.close()
        elif inp == "clearhklist":
            with open("MacrosList.txt", "w") as f:
                f.truncate()
                Clear()
                Help()
                f.close()



if __name__ == "__main__":
    Hello()
    MainMenu()

