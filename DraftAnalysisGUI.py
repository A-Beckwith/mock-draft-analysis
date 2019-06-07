from tkinter import *

gui = Tk()
gui.title("Draft Analysis")

analysisChoice = StringVar(gui)
analysisChoice.set("Total Mocks")

choices = {
    "Total Mocks",
    "Sources",
    "Most Frequently Drated Players",
    "Most Frequently Drafted Players (By Position)",
    "Most Frequently Drafted Players (By Depth)",
    "Average Round Drafted (By Player)",
    "Average Round Drafted (By Depth)"
}

menu = OptionMenu(gui, analysisChoice, *choices)

gui.mainloop()