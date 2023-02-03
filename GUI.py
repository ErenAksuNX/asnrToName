from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from Analyser import *


def help_window():
    showinfo(title="Hilfe", message="""Bei Problemen melden sie sich bei der folgende e-mail
e-mail: eren.aksu@nationalexpress.de""")


class GUI:
    def __init__(self, master):
        self.master = master

        self.master.title("National Express PDF Cutter")

        self.menubar = Menu(self.master)

        self.close_menu = Menu(self.menubar)
        self.close_menu.add_command(label="Programm schließen", command=self.programmSchliessen)

        self.help_menu = Menu(self.menubar)

        self.menubar.add_cascade(label="Programm", menu=self.close_menu)
        self.menubar.add_cascade(label="Hilfe", command=help_window)

        self.master.config(menu=self.menubar)

        self.master.geometry("500x500")
        self.master.minsize(500, 500)
        self.master.maxsize(500, 500)
        self.master.resizable(False, False)

        self.path = None
        self.speicherort = None

        self.bt_dateiWaehlen = Button(self.master, text="Datei Wählen", command=self.getPath)
        self.bt_speicheortWaehlen = Button(self.master, text="Speicheort Wählen", command=self.getSavePath)
        self.bt_start = Button(self.master, text="Programm Starten", command=self.start)

        self.bt_dateiWaehlen.pack(expand=True)
        self.bt_speicheortWaehlen.pack(expand=True)
        self.bt_start.pack(expand=True)

        self.master.mainloop()

    def getPath(self):
        path = askopenfilenames(title="Bitte wählen sie die PDF-Datei aus", filetypes=[("PDF-Datei", "*.pdf")])

        self.path = path

    def getSavePath(self):
        path = askdirectory(title="Wählen sie denn Speicherort aus")
        self.speicherort = path

    def programmSchliessen(self):
        self.master.destroy()

    def start(self):

            ah = AnalyseHandler(self.path, self.speicherort)
            ah.run()
