from customtkinter import CTkButton,CTk, CTkEntry
from tkinter import StringVar, PhotoImage
import customtkinter as ct

ct.set_appearance_mode("Dark")  

class CircularButton(CTkButton):
    def __init__(self, master=None, text='', command=None):
        super().__init__(master=master, text=text, command=command)
        self.configure(width=50, height=70, corner_radius=20,
            hover_color = ('#CCCCCC','#333333') ,
            fg_color = ('#7f5af0','#7f5af0'),
            text_font = ('Arial', 16)) # 
        self.grid(padx=5, pady=5, sticky='nsew')

def delete_last():
    global expression
    exp = expression.get()
    if exp:
        new_exp = exp[:-1]
        expression.set(new_exp)

def plus_minus():
    global expression
    exp = expression.get()
    if exp:
        if exp[0]!='-':
            exp = '-'+ exp    
        elif exp[0]=='-':
            exp = exp[1:]
    expression.set(exp)

def add_to_input(char):
    global expression
    ops = ['.', '+', '-', '*', '/']
    last_char = expression.get()[-1] if len(expression.get()) > 0 else ''
    if char in ops:
        if last_char in ops:
            return
    expression.set(expression.get() + char)

def calculate():
    global expression
    try:
        result = eval(expression.get())
        if isinstance(result, float):
            result = round(result, 3)
        expression.set(str(result))
    except Exception as e:
        expression.set("ERROR")

def toggle_mode():
    global mode
    if mode == "light":
        mode = "dark"
        button_mode.configure(image = img_light)         
        ct.set_appearance_mode("Dark")
        root.config(bg='black')
    else:
        mode = "light"
        button_mode.configure(image = img_dark )  
        ct.set_appearance_mode("Light")
        root.config(bg='white')

root = CTk()
root.geometry('375x500')
root.title('')
root.resizable(False, False)
root.call('wm', 'iconphoto', root._w, PhotoImage(file = 'images/logo.png'))
root.configure(bg="black")

mode = "dark" 
expression = StringVar() 
img_light = PhotoImage(file = 'images/sun.png')
img_dark = PhotoImage(file = 'images/moon.png')

button_mode = CTkButton(root, image = img_light , text='', 
    hover_color = ('white','black'),
    fg_color = ('white','black'),width=50, height=50,
    command= toggle_mode)
button_mode.grid(row=0, column=0)

entry = CTkEntry(root, textvariable = expression, 
    text_font=("Helvetica", 28), justify="right",
    text_color  =('black', 'white'),
    corner_radius=0,state="disabled" ,
    width=280, fg_color=('white', 'black'), border=0)
entry.grid(row=0, column=1, columnspan=3, pady=5,ipady=15)

CircularButton(root, text=" C ",  command=delete_last).grid(row=1, column=0)
CircularButton(root, text="+/-",  command=plus_minus).grid(row=1, column=1)
CircularButton(root,  text=" % ", command=lambda: add_to_input("/100")).grid(row=1, column=2)
CircularButton(root, text=" ÷ ",  command=lambda: add_to_input("/")).grid(row=1, column=3)

CircularButton(root, text="7",  command=lambda: add_to_input("7")).grid(row=2, column=0)
CircularButton(root, text="8",  command=lambda: add_to_input("8")).grid(row=2, column=1)
CircularButton(root, text="9",  command=lambda: add_to_input("9")).grid(row=2, column=2)
CircularButton(root, text="×",  command=lambda: add_to_input("*")).grid(row=2, column=3)

CircularButton(root, text="4",  command=lambda: add_to_input("4")).grid(row=3, column=0)
CircularButton(root, text="5",  command=lambda: add_to_input("5")).grid(row=3, column=1)
CircularButton(root, text="6",  command=lambda: add_to_input("6")).grid(row=3, column=2)
CircularButton(root, text="-",  command=lambda: add_to_input("-")).grid(row=3, column=3)

CircularButton(root, text="1",  command=lambda: add_to_input("1")).grid(row=4, column=0)
CircularButton(root, text="2",  command=lambda: add_to_input("2")).grid(row=4, column=1)
CircularButton(root, text="3",  command=lambda: add_to_input("3")).grid(row=4, column=2)
CircularButton(root, text="+",  command=lambda: add_to_input("+")).grid(row=4, column=3)

CircularButton(root, text="0",  command=lambda: add_to_input("0")).grid(row=5, column=0)
CircularButton(root, text=".",  command=lambda: add_to_input(".")).grid(row=5, column=1)
CircularButton(root, text="AC",  command = lambda:expression.set("")).grid(row=5, column=2)
CircularButton(root, text="=",  command=calculate).grid(row=5, column=3)

root.mainloop()

