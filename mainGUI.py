import PySimpleGUI as sg
import os

from ctypes import alignment
from tkinter import *
from tkinter import tkk



root = Tk()
mainMenu = Menu(root)
root.configure(menu = mainMenu)
root.title("CSGOForecaster")
root.geometry("640x480")


def showCredits(event):
    creditsWindow = Toplevel(root)
    creditsWindow.geometry("640x480")
    creditsWindow.title("CSGOForecaster > Credits")

    main_frame = Frame(creditsWindow)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    hScrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    
    wScrollbar = Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
    hScrollbar.pack(side=RIGHT, fill=Y)
    wScrollbar.pack(side=TOP, fill=X)

    my_canvas.configure(yscrollcommand=hScrollbar.set, xscrollcommand=wScrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    f = open('Documents/_java/CSGOForecaster/credits.txt', 'r', encoding='utf-8')
    file_contents = f.read()
    creditsLabel = Label(second_frame, text=file_contents, justify=LEFT)
    f.close()
    creditsLabel.pack()
    
    
def createNewWindow():
    newWindow = Toplevel(root)


def simulate(self):
    for root, dirs, files in os.walk("Documents\_java\CSGOForecaster\data", topdown=False):
        for filename in files:
            if filename.endswith('.xlsx'):
                print (os.path.join(root, filename))


theLabel = Label(root, text="CSGOForecaster\n by Petre Leonid-Dalin\n\n\n")
theLabel.pack()

mmSim1Button = Button(None, text="Head-to-Head Simulation", fg="blue")
mmSim1Button.bind("<Button-1>", simulate)
mmSim1Button.pack(side="top", fill="x")

mmSim2Button = Button(None, text="Tournament Simulation", fg="blue")
mmSim2Button.pack(side="top", fill="x")

mmCreditButton = Button(None, text="Credits", fg="blue" )
mmCreditButton.bind("<Button-1>", showCredits)
mmCreditButton.pack(side="top", fill="x")

mmExitButton = Button(None, text="Exit", fg="blue", command=exit )
mmExitButton.pack(side="top", fill="x")

root.mainloop()


#filename = sg.popup_get_file('Enter the file you wish to process')
#sg.popup('You entered', filename)