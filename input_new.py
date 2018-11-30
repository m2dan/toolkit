
from tkinter import *
#Automated Date input
from datetime import date
from datetime import datetime
import os

def window_three():
    #time showing date and time
    today = datetime.now().strftime("%d-%m-%Y um %H %M %S Uhr") 

    def mhello():
        mtext = mEntry.get()
        mlabel2 = Label(mGui, text=str(today)+": " + mtext)
        mlabel2.pack()
        #Creates the note folder, no error message, if directory already exists
        os.makedirs("./note/", exist_ok=True)
        # Definition of filename and write path
        fileinput = open("./note/"+ str(today) +".txt", 'w')#
        fileinput.write(mtext)
        # Closes file
        fileinput.close()
        
    
    mGui = Tk()

    mGui.geometry('450x500')
    mGui.title('Notizen')
    #note label
    mlabel = Label(mGui, text='Geben Sie Ihre Notizen ein:')
    mlabel.pack()
    mbutton = Button(mGui, text ='OK',command=mhello,fg="black",bg="light grey")
    mbutton.pack()

    mEntry = Entry(mGui)
    mEntry.pack()

    mGui.mainloop()



