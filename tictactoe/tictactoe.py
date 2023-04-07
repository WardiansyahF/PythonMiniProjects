from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('TicTacToe - Wardiansyah F')
root.resizable(0,0)


#Fungsi menonatifkan semua button
def disable_all_buttons():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")
    b4.config(state="disabled")
    b5.config(state="disabled")
    b6.config(state="disabled")
    b7.config(state="disabled")
    b8.config(state="disabled")
    b9.config(state="disabled")

#Fungsi menentukan cek pemenang
def checkifwon():
    global winner
    winner = False
    #check untuk X
    if b1["text"]== "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT X, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b4["text"]== "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT X, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b7["text"]== "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT X, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b1["text"]== "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT X, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b2["text"]== "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT X, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b3["text"]== "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT X, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b1["text"]== "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT X, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b3["text"]== "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT X, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    
    #check untuk O
    if b1["text"]== "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT O, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b4["text"]== "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT O, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b7["text"]== "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT O, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b1["text"]== "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT O, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b2["text"]== "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT O, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b3["text"]== "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT O, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b1["text"]== "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT O, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    elif b3["text"]== "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe","SELAMAT O, ANDA MEMENANGKAN PERTANDINGAN!")
        disable_all_buttons()
    
    #Jika Kondisi Seri
    if count == 9 and winner == False:
        messagebox.showinfo("TIc Tac Toe","HASIL PERTANDINGAN SERI!")
        disable_all_buttons()  

#Fungsi memulai game kembali
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global Clicked,count
    Clicked =True
    count = 0       
    #Fungsi Button Clicked
    def b_click(b):
        global Clicked, count
        if b["text"] == " " and Clicked == True:
            b["text"] = "X"
            Clicked = False
            count += 1
            checkifwon()
        elif b["text"] == " " and Clicked == False:
            b["text"] = "O"
            Clicked = True
            count += 1
            checkifwon()
        else :
            messagebox.showerror("Tic Tac Toe","Box telah diisi\nPilih box lain")
    
    #Pengaturan button        
    b1 = Button(root, text=" ",font=("Helvatica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b1))
    b2 = Button(root, text=" ",font=("Helvatica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b2))
    b3 = Button(root, text=" ",font=("Helvatica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b3))

    b4 = Button(root, text=" ",font=("Helvatica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b4))
    b5 = Button(root, text=" ",font=("Helvatica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b5))
    b6 = Button(root, text=" ",font=("Helvatica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b6))

    b7 = Button(root, text=" ",font=("Helvatica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b7))
    b8 = Button(root, text=" ",font=("Helvatica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b8))
    b9 = Button(root, text=" ",font=("Helvatica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b9))

    #Letak Button
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

#Membuat Menu
my_menu = Menu(root)
root.config(menu = my_menu)

#Membuat option menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Restart Game", command=reset)


reset()
root.mainloop()