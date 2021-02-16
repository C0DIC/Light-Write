from tkinter import (
    Text,
    Entry,
    Tk,
    RIGHT,
    LEFT,
    BOTH,
    END,
    scrolledtext,
    filedialog
)

class LW:

    def __init__(self, master):
        self.config = {
            "materialGray" : "#211f1f",
            "materialLightGray" : "#292727",
            "whiteColor" : "white",
            "blackColor" : "black",
            "blinkTime" : 700,
            "defaultFont" : ("Sans", 11)
        }

        self.version = "v3.0"
        self.projectName = "Light Write"
        self.appName = f"{self.projectName} {self.version}"
        
        self.master = master

        self.master.title(self.appName)
        self.master.config(bg = self.config["materialGray"])
        self.master.minsize(width = '660', height = '500')
        self.master.maxsize(height = '800')

        self.createWriteSpace()

        # Command line will be in next 'Beta' update
        # self.createCommandLine()

        self.master.bind('<Escape>', self.closeApplication)

        self.master.bind('<Control-n>', self.newFile)
        self.master.bind('<Control-s>', self.saveFile)
        self.master.bind('<Control-o>', self.openFile)

        self.master.mainloop()

    def changeTitle(self, newTitle: str):
        self.master.title(newTitle)

    def closeApplication(self, event):
	    self.master.destroy()

    def createWriteSpace(self):
        self.write = Text(
            self.master,
            bg = self.config["materialGray"],
            fg = self.config["whiteColor"],
            bd = 0,
            highlightcolor = self.config["blackColor"],
            insertbackground = self.config["whiteColor"],
            insertwidth = 0.5,
            insertontime = 700,
            font = self.config["defaultFont"]
        )
        self.write.pack(expand = True, fill = BOTH)
        self.write.focus()

    def createCommandLine(self):
        self.commandLine = Entry(
            self.master,
            bg = self.config["materialLightGray"],
            fg = self.config["whiteColor"],
            bd = 0,
            highlightcolor = self.config["blackColor"],
            insertbackground = self.config["whiteColor"],
            insertwidth = 6,
            insertontime = 700,
            font = self.config["defaultFont"]
        )
        self.commandLine.pack(side = RIGHT, fill = BOTH, expand = True)

    def newFile(self, event):
        self.changeTitle(f"{self.appName} - [UNSAVED]")
        self.write.delete('1.0', END)

    def saveFile(self, event):
        # More file extensions will be in next update

        try:
            files = filedialog.asksaveasfile(mode = 'w', 
                filetypes = (
                    ('Text', '*.txt'),
                    ('Python', '*.py'),
                    ('C-file', '*.c')
                )
            )

            self.changeTitle(f"{self.appName} {str(files.name)}")            
            data = self.write.get('1.0', END)
            files.write(data)
        except AttributeError:
            pass

    def openFile(self, event):
        try:
            files = filedialog.askopenfile(mode = 'r')
            self.changeTitle(f"{self.appName} - {str(files.name)}")
            
            data = files.read()

            self.write.delete('1.0', END)
            self.write.insert('1.0', data)
        except (UnicodeDecodeError, AttributeError):
            self.write.insert(1, "It's not a text file")            
		    #comm_line.insert(2, "It's not a text file")

if __name__ == "__main__":
    master = Tk()
    app = LW(master)