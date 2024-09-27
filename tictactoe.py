import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.geometry("400x400")

score = 0
clicked = True

def won():
    global win
    win = False
    if button1["text"] == "x" and button2["text"] == "x" and button3["text"] == "x":
        win = True
        messagebox.showinfo(" ", "x wins")
    elif button4["text"] == "x" and button5["text"] == "x" and button6["text"] == "x":
        win = True
        messagebox.showinfo(" ", "x wins")
    elif button7["text"] == "x" and button8["text"] == "x" and button9["text"] == "x":
        win = True
        messagebox.showinfo(" ", "x wins")
    elif button1["text"] == "x" and button4["text"] == "x" and button7["text"] == "x":
        win = True
        messagebox.showinfo(" ", "x wins")
    elif button3["text"] == "x" and button5["text"] == "x" and button8["text"] == "x":
        win = True
        messagebox.showinfo(" ", "x wins")
    elif button3["text"] == "x" and button6["text"] == "x" and button9["text"] == "x":
        win = True
        messagebox.showinfo(" ", "x wins")
    elif button1["text"] == "x" and button5["text"] == "x" and button9["text"] == "x":
        win = True
        messagebox.showinfo(" ", "x wins")
    elif button3["text"] == "x" and button5["text"] == "x" and button7["text"] == "x":
        win = True
        messagebox.showinfo(" ", "x wins")
    elif button1["text"] == "o" and buttono["text"] == "o" and button3["text"] == "o":
        win = True
        messagebox.showinfo(" ", "o wins")
    elif button4["text"] == "o" and button5["text"] == "o" and button6["text"] == "o":
        win = True
        messagebox.showinfo(" ", "o wins")
    elif button7["text"] == "o" and button8["text"] == "o" and button9["text"] == "o":
        win = True
        messagebox.showinfo(" ", "o wins")
    elif button1["text"] == "o" and button4["text"] == "o" and button7["text"] == "o":
        win = True
        messagebox.showinfo(" ", "o wins")
    elif button3["text"] == "o" and button5["text"] == "o" and button8["text"] == "o":
        win = True
        messagebox.showinfo(" ", "o wins")
    elif button3["text"] == "o" and button6["text"] == "o" and button9["text"] == "o":
        win = True
        messagebox.showinfo(" ", "o wins")
    elif button1["text"] == "o" and button5["text"] == "o" and button9["text"] == "o":
        win = True
        messagebox.showinfo(" ", "o wins")
    elif button3["text"] == "o" and button5["text"] == "o" and button7["text"] == "o":
        win = True
        messagebox.showinfo(" ", "o wins")
    if win == False and score == 9:
        messagebox.showinfo(" ", "it's a tie")
        
def click(button):
    global score
    global clicked
    if button["text"] == " " and clicked == True:
        button["text"] = "x"
        clicked = False
        score += 1 
        won()
    elif button["text"] == " " and clicked == False:
        button["text"] = "o"
        clicked = True
        score += 1
        won()
    else:
        messagebox.showerror(" ", "this box is taken")

button1 = tkinter.Button(window, text = " ", command = lambda:click(button1))
button1.grid(row = 0, column = 0)
button2 = tkinter.Button(window, text = " ", command = lambda:click(button2))
button2.grid(row = 0, column = 1)
button3 = tkinter.Button(window, text = " ", command = lambda:click(button3))
button3.grid(row = 0, column = 2)
button4 = tkinter.Button(window, text = " ", command = lambda:click(button4))
button4.grid(row = 1, column = 0)
button5 = tkinter.Button(window, text = " ", command = lambda:click(button5))
button5.grid(row = 1, column = 1)
button6 = tkinter.Button(window, text = " ", command = lambda:click(button6))
button6.grid(row = 1, column = 2)
button7 = tkinter.Button(window, text = " ", command = lambda:click(button7))
button7.grid(row = 3, column = 0)
button8 = tkinter.Button(window, text = " ", command = lambda:click(button8))
button8.grid(row = 3, column = 1)
button9 = tkinter.Button(window, text = " ", command = lambda:click(button9))
button9.grid(row = 3, column = 2)



window.mainloop()