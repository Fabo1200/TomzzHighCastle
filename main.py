import tkinter
from plant import Plant
from window import gGUI
from settings import settings
#Main
def main():
    print("Welcome to", settings.NAME)
    Plant.print_data(Plant)
    gGUI.gui(gGUI)

if __name__ == '__main__':
    main()
#EndMain