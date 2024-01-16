#Registration Form Using GUI System
#Programmer: Rishi Patel
#Version: 1.0

#Important Functions Imported
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import string
import sys

#Standard GUI System Components
window=Tk()
window.title("Registration Form")
window.geometry("420x450")
window.resizable(False, False)

#All of the Different Frames, Labels, Entry Boxes, Comboboxes, Radio Buttons, and Check Buttons
lbl=Label(window)
lbl.grid(row=0,column=0,ipady=50)

lbl1=Label(window,text="Registration Form",font=("arial black",20))
lbl1.place(x=76,y=50)

lbl2=Label(window,text="Full Name",font=("arial black",10))
lbl2.grid(row=1,column=0,sticky="W",ipadx=70,ipady=10)

e=StringVar()
txt1=Entry(window,width=20,textvariable=e)
txt1.grid(row=1,column=1,sticky="W")

lbl3=Label(window,text="Email",font=("arial black",10))
lbl3.grid(row=2,column=0,sticky="W",ipadx=70,ipady=10)

e1=StringVar()
txt2=Entry(window,width=20,textvariable=e1)
txt2.grid(row=2,column=1,sticky="W")

lbl4=Label(window,text="Gender",font=("arial black",10))
lbl4.grid(row=3,column=0,sticky="W",ipadx=70,ipady=10)

frame1=Frame(window)
frame1.grid(row=3,column=1)

a=IntVar()
radiobutton1=Radiobutton(frame1,text="Male",value=1,variable=a)
radiobutton1.grid(row=0,column=0,sticky="W")

radiobutton2=Radiobutton(frame1,text="Female",value=2,variable=a)
radiobutton2.grid(row=0,column=1,sticky="W")
a.set(0)

lbl5=Label(window,text="Country",font=("arial black",10))
lbl5.grid(row=4,column=0,sticky="W",ipadx=70,ipady=10)

combo1=ttk.Combobox(window,state="readonly",width=15)
combo1.grid(row=4,column=1,sticky="W")
combo1["values"]=("Select One","Canada","India","USA")
combo1.current(0)

lbl6=Label(window,text="Language",font=("arial black",10))
lbl6.grid(row=5,column=0,sticky="W",ipadx=70,ipady=10)

frame2=Frame(window)
frame2.grid(row=5,column=1)
    
c=BooleanVar()
check1=Checkbutton(frame2,text="English",var=c)
check1.grid(row=0,column=0,sticky="W")
c.set(False)
    
c1=BooleanVar()
check2=Checkbutton(frame2,text="German",var=c1)
check2.grid(row=0,column=1,sticky="W")
c1.set(False)

#Submit function, will work when button is pressed and if any errors there will be an error message
def submit():
    #Checks If Full Name is Blank or Not
    if e.get()=="":
        messagebox.showerror("Error","Invalid Full Name Entry\nTry Again!")
        txt1.focus()
        return
    
    #Checks For All The Errors Which Can Be Located In The Email Entry By User
    email=e1.get().strip()
    lower=string.ascii_lowercase
    #Checks if email is blank or not
    if email=="":
        messagebox.showerror("Error","Invalid Email Entry\nTry Again!")
        txt2.focus()
        return
    else:
        #Checks if "_" and "^" are in email or not
        if ("_" not in email) or("^" not in email):
            messagebox.showerror("Error","Invalid Email Entry\nTry Again!")
            txt2.focus()
            return
        else:
            under=email.index("_")
            hat=email.index("^")
            #Checks if the "_" is before or after the "^"
            if under>hat:
                messagebox.showerror("Error","Invalid Email Entry\nTry Again!")
                txt2.focus()
                return
            #Checks if all letters are lowercase or not and checks if there are any empty areas of string in the email entered

            #Checks if its blank before "_" and if it is it shows error
            if email[:under:]=="":
                messagebox.showerror("Error","Invalid Email Entry\nTry Again!")
                txt2.focus()
                return
            else:
                for i in range(under):
                    if email[i] not in lower:
                        messagebox.showerror("Error","Invalid Email Entry\nTry Again!")
                        txt2.focus()
                        return
            #Checks if its blank between "^" and "_" and if it is it shows error
            if email[under+1:hat:]=="":
                messagebox.showerror("Error","Invalid Email Entry\nTry Again!")
                txt2.focus()
                return
            else:
                for i in range(under+1,hat):
                    if email[i] not in lower:
                        messagebox.showerror("Error","Invalid Email Entry\nTry Again!")
                        txt2.focus()
                        return
            #Checks if its blank after "^" and if it is it shows error
            if email[hat+1::]=="":
                messagebox.showerror("Error","Invalid Email Entry\nTry Again!")
                txt2.focus()
                return
            else:
                for i in range(hat+1,len(email)):
                    if email[i] not in lower:
                        messagebox.showerror("Error","Invalid Email Entry\nTry Again!")
                        txt2.focus()
                        return
                    
    #Checks if User Picked a Gender or not
    if (a.get()!=1) and (a.get()!=2):
        messagebox.showerror("Error","Pick a Gender\nTry Again!")
        radiobutton1.focus()
        return

    #Checks if User Picked a Country or not
    if (combo1.current()==0):
        messagebox.showerror("Error","Pick a Country\nTry Again!")
        combo1.focus()
        return
    
    #Checks if User Picked One Language or not
    if (c.get()==False) and (c1.get()==False):
        messagebox.showerror("Error","Pick One Language\nTry Again!")
        check1.focus()
        return
    elif (c.get()==True) and (c1.get()==True):
        messagebox.showerror("Error","Pick One Language\nTry Again!")
        check1.focus()
        return

    #If everything went well, will show appropriate message and will terminate the window
    messagebox.showinfo("Success","Registration Has Been Accepted")
    window.destroy()
    sys.exit()

#The button that is placed at the bottom of the form
btn1=Button(window,text="Submit",width=20,bg="#010101",fg="white",command=submit)
btn1.place(x=120,y=350)

#Puts cursor on first text box 
txt1.focus()
#Puts the window in the center of your screen
window.eval("tk::PlaceWindow . center")
#Loop that keeps the window on your screen at all times until terminated
window.mainloop()
