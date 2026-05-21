import tkinter as tk

#create main window
root=tk.Tk()
root.title("simple Calculator")
root.geometry("300x400")

#display Box
display=tk.Entry(
    root,
    font=("Arial",20),
    borderwidth=5,
    relief="ridge",
    justify="right"

)
display.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=10,
)
#Function to add values to display
def click(value):
    display.insert(tk.END,value)

#Function to clear display
def clear():
    display.delete(0,tk.END)

#Function to clear display
def calculate():
    try:
        result=eval(display.get())
        display.delete(0,tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0,tk.END)
        display.insert(tk.END,"Error")

#Button layout
button=[
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),

]
#create buttons
for(text,row,col)in button:

    if text=="=":
        btn = tk.Button(
        root,
        text=text,
        font=("Arial",18),
        bg="lightgreen",
        command=calculate
    )

    else:
        btn=tk.Button(
            root,
            text=text,
            font=("Arial",18),
            command=lambda t=text: click(t)

        )

    btn.grid(
        row=row,
        column=col,
        sticky="nsew",
        padx=5,
        pady=5

        )
        #clear button 
clear_btn=tk.Button(
    root,
    text="C",
    font=("Arial",18),
    bg="red",
    fg="white",
    command=clear

        )
clear_btn.grid(
    row=5,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=5,
    pady=5
         )

#Make rows and columns responsive
for i in range (6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i,weight=1) 

#Run application 
root.mainloop() 


