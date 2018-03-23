
from tkinter import *
from tkinter import filedialog

import drill65of68_func
import drill65of68_gui

class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master 
        self.master.title("CopyCat") 
        arg = self.master

        drill65of68_gui.load_gui(self)

if __name__ == "__main__":
    root = Tk() 
    App = ParentWindow(root) 
    root.mainloop() 

