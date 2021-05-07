#import the 'tkinter module
import string
from tkinter import*
root = Tk() # Blank window
root.geometry("1000x800")
#adding a background colour
root.config(bg='yellow')
#Can't change the size and shape of the window
root.resizable(width=False, height=False) #The set size cannot be changed
#Title for the window
root.title("Celsius to Fahrenheit Convertor!")
#The label frames
label_celfah = LabelFrame(root, text = "Celsius to Fahrenheit", fg="purple", font = ("Helvetica", 15)) # The labels must be purple when enabled
label_fahcel = LabelFrame (root, text = "Fahrenheit to Celsius", fg="purple", font = ("Helvetica", 15))
label_celfah.place(x=150, y=50, width=300, height=200)
label_fahcel.place(x=550, y=50, width=300, height=200)

#Creating the textbox widgets
fah_cel = Entry (label_fahcel, state = "disabled")
fah_cel.place (x=50, y=50, width=180, height = 30)
cel_fah = Entry (label_celfah, state = "disabled")
cel_fah.place(x=50, y=50, width=180)

#The output displaying widget
display_output = Entry (root, width=20, font = ("Helvetica", 20))
display_output.configure(bg='lime', state='readonly') #The display box must not permit the input of text at any point in the program


#functions: Showing the work that the buttons do
def button_clear ():
#clearing the textboxes and the label field
    display_output.config(state='normal')
    cel_fah.delete(0, END)
    fah_cel.delete(0, END)
    display_output.delete(0, END)
#If the clear button is pressed without an answer on the entry field, all the fields must be disabled
    cel_fah.configure(state = 'disable')
    fah_cel.configure(state = 'disable')
    display_output.configure(state ='disable')

def button_celfah ():
    cel_fah.configure(state = 'normal')
    fah_cel.configure(state = 'disabled')


def button_fahcel ():
    fah_cel.configure(state = 'normal')
    cel_fah.configure(state = 'disabled')


def button_conv_celfah ():
    display_output.config(state="normal") #From disabled/readonly to normal for display when pressed
    display_output.config(font = ("Helvetica", 20))
    temp = float(cel_fah.get()) #Getting the value from the entry box
    fahrenheit = (temp*9/5)+32 #Converting celcius to Fahrenheit button
    display_output.insert(0, fahrenheit)
    display_output.config( state="readonly",fg='red') #From normal to readonly, so that no user edits are permitted
    button_conv_celfah.config(state="disabled") #The button can only be pressed once per entry to avoid the increment of the output by the user

def button_conv_fahcel ():
    display_output.config(state="normal")  # From disabled/readonly to normal for display when pressed
    display_output.config( font=("Helvetica", 20),fg='red')
    temp = float(fah_cel.get()); #Getting the values from the entry box
    celcius = (temp-32)*5/9 #Converting Fahrenheit to celcius
    display_output.insert(0, celcius)
    display_output.config(state="readonly", fg='red')  # From normal to readonly, so that no user edits are permitted
    button_conv_fahcel.config(state="disabled") #The button can only be pressed once per entry to avoid the increment of the output by the user

def take(option):
    if option == "YES": #If the user chooses 'yes' to exit, the whole window/program  will shutdown
        root.destroy()
    elif (option == "NO"): #If the user chooses 'no', not to exit, ONLY THE POPUP box will disappear.
            pop.destroy()

def button_exit (): #When the user presses 'exit', a popup box to ask the user whether they really want to exit will show up
    global pop
    pop = Toplevel(root)
    pop.title("EXIT POPUP BOX")
    pop.geometry("350x250")
    pop.resizable(width=False, height=False)  # The set size cannot be changed
    pop.config(bg="green")

    #global Hloni

    #Hloni = PhotoImage(file="image/Profile-pic.png")
    #self.tk.call(('image', 'create', imgtype, name,) + options)

    pop_label = Label(pop, text ="Do you really want to exit?", bg="yellow", font = ("Helvetica", 15))
    pop_label.pack(pady= 10)

    my_frame = Frame(pop, bg="yellow")
    my_frame.pack(pady=5)
    #myself = Label(my_frame, image=Hloni, borderwidth = 0)
    #myself.grid(row=0, column=0, padx=10)

    button_yes = Button(my_frame,text="YES", borderwidth=10, font=("Consolas 10 bold"),fg='black', command=lambda: take("YES"), width=10)
    button_yes.grid(row=0, column=1)

    no = Button(my_frame, text="NO", borderwidth=10, font=("Consolas 10 bold"),fg='black', command=lambda: take("NO"), width=10)
    no.grid(row=0, column=2)

# Creating, positioning and commanding the buttons
button_celfah = Button(root,  borderwidth=10, font=("Consolas 10 bold"),text="Activate-Celcius to Fahrenheit", bg="green", fg="white", width=35, command=button_celfah)
button_fahcel = Button(root, text="Activate-Fahrenheit to Celcius", borderwidth=15, font=("Consolas 10 bold"), bg="green", fg="white", width=35, command=button_fahcel)
button_exit = Button(root, text="Exit", borderwidth=10, font=("Consolas 10 bold"), bg="green", fg="white", width=10, command=button_exit)
button_clear = Button (root, borderwidth=10, font=("Consolas 10 bold"),text="Clear", bg="green", fg="white", width=10, command=button_clear)
button_conv_celfah = Button (root, borderwidth=10, font=("Consolas 10 bold"),text="Conversion", bg="green", fg="white", width=10, command = button_conv_celfah)
button_conv_fahcel = Button (root, borderwidth=10, font=("Consolas 10 bold"),text="Conversion", bg="green", fg="white", width=10, command = button_conv_fahcel)


button_celfah.place (x=170, y=300)
button_fahcel.place( x=570, y=300)
button_clear.place (x=170, y = 500)
button_conv_celfah.place(x=170, y= 400)
button_conv_fahcel.place(x=570, y=400)
button_exit.place(x=170, y=600)
display_output.place(x=550, y=550)

root.mainloop()
