# Import the required libraries
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# New filw function
def newFile():
    global file
    root.title('Untitled - Notepad')
    file = None
    TextArea.delete(1.0,END)

# Open a new file function
def openFile():
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    if file == '':
        file = None
    else:
        root.title(os.path.basename(file) + ' - Notepad')
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()

# Save a file
def saveFile():
    global file
    if file == None:
        file=asksaveasfilename(initialfile = 'Untitled.txt',defaultextension ='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])

        if file == '':
            file = None

        else:
            # save as a new file
            f = open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + ' - NotePad')
            print('File Saved!')
    else:
        # Save the file
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()

# Quit the application
def quitApp():
    root.destroy()

# Cut the selected text
def cut():
    TextArea.event_generate(("<<Cut>>"))

# Copy the selected text
def copy():
    TextArea.event_generate(("<<Copy>>"))

# Paste the selected text
def paste():
    TextArea.event_generate(("<<Paste>>"))

# Notification about the notepad
def about():
    showinfo('Notepad','Notepad By Sumedha Zaware')


if __name__ == '__main__':
    # Basic tkinter Setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.iconbitmap('notepad.ico')
    root.geometry('644x788')

    # Add TextArea
    TextArea = Text(root, font = 'Calibre')
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # ****MENU BAR STARTS****
    MenuBar = Menu(root) 
    FileMenu = Menu(MenuBar,tearoff=0)

    # FILE MENU
    MenuBar.add_cascade(label = 'File',menu = FileMenu)     # Creating file menu
    FileMenu.add_command(label = 'New',command=newFile)     # pen new file
    FileMenu.add_command(label = 'Open',command=openFile)   # Open saved file
    FileMenu.add_command(label = 'Save',command =saveFile)  # Save a file
    FileMenu.add_separator()                                # add a separator in the file menu
    FileMenu.add_command(label='Exit',command = quitApp)    # exit the application

    # EDIT MENU
    EditMenu = Menu(MenuBar,tearoff=0)
    MenuBar.add_cascade(label='Edit', menu = EditMenu)
    EditMenu.add_command(label='Cut', command=cut)         # Cut the content
    EditMenu.add_command(label='Copy', command=copy)        # Copy the content
    EditMenu.add_command(label='Paste', command=paste)     # Paste the content

    # HELP MENU
    HelpMenu = Menu(MenuBar,tearoff=0)
    MenuBar.add_cascade(label='Help',menu=HelpMenu)
    HelpMenu.add_command(label='About Notepad',command=about)
    root.config(menu = MenuBar)
    # ****MENU BAR ENDS****

    # SCROLL BARS
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = Scroll.set)

    # Pack all the functions and elements together
    root.mainloop()