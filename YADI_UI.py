from tkinter import *
from tkinter.ttk import *
from Parser import *

def load_rules():    
    filename = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if filename: 
        try:
            #Label(definition_mode, text=filename).pack()
            print("dsf")
            DatalogParser(filename)
        except: 
            tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename) 

#create the window
master = Tk()

#styles for window
master.title("YADI")
master.geometry("400x400")

#set query mode
query_mode = Frame(master)
query_mode.pack(side=LEFT, fill=X)
#set definition mode
definition_mode = Frame(master)
rule_loader = Button(definition_mode, text="Select your file", command=load_rules)
rule_loader.pack(side=LEFT)
definition_mode.pack(side=LEFT, fill=X)
   

rules_text = Message(definition_mode)
query_text = Message(definition_mode)

execute_query = Button(definition_mode, text="Execute")
execute_query.pack(side=RIGHT)
definition_mode.pack(side=RIGHT, fill=X)

results_text = Message(definition_mode,)

master.mainloop()
