'''
Created by: Sumedha Zaware
'''

# Import the required libraries
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def new_file():
    ''' New file function
    '''
    global file
    root.title('Untitled - Notepad')
    file = None
    TextArea.delete(1.0,END)

def open_file():
    '''Open a new file function
    '''
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

def save_file():
    '''Save a file
    '''
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

def quit_app():
    '''Quit the application
    '''
    root.destroy()

def cut():
    '''Cut the selected text
    '''
    TextArea.event_generate(("<<Cut>>"))

def copy():
    '''Copy the selected text
    '''
    TextArea.event_generate(("<<Copy>>"))

def paste():
    '''Paste the selected text
    '''
    TextArea.event_generate(("<<Paste>>"))

def about():
    '''Notification about the notepad
    '''
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
    FileMenu.add_command(label = 'New',command=new_file)     # pen new file
    FileMenu.add_command(label = 'Open',command=open_file)   # Open saved file
    FileMenu.add_command(label = 'Save',command =save_file)  # Save a file
    FileMenu.add_separator()                                # add a separator in the file menu
    FileMenu.add_command(label='Exit',command = quit_app)    # exit the application

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
