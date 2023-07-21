import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import mysql.connector

mydb = mysql.connector.connect(host='localhost', password='SAGAR@pass1', user='root')
mycur = mydb.cursor()
mycur.execute('use Store')


def login():
    try:
        mycur.execute(f"select Password from Acc_info where Username='{e1.get()}'")
        a = mycur.fetchall()
        if a[0][0] == e2.get():
            pass  # main application
    except:
        messagebox.showerror(title='Error', message='Invalid Username or Password')


def forget_password():
    def update():
        if fpe2.get() == fpe3.get():
            try:
                mycur.execute(f"update Acc_info set Password = '{fpe2.get()}' where Username='{fpe1.get()}'")
                messagebox.showinfo(title='password-changed', message='please login again with new password')
                mydb.commit()
                fpw.destroy()

            except:
                messagebox.showerror(title='Error', message="Invalid Username")

    fpw = ctk.CTk()
    fpw.geometry('400x400')
    fpw.resizable(width=False, height=False)
    ctk.CTkLabel(fpw, text="Create New-Password", text_color='#57a1f8',
                 font=('Microsoft Yahei UI light', 30, 'bold',)).place(x=50, y=10)
    ctk.CTkLabel(fpw, text="Username", text_color='#57a1f8', font=('Microsoft Yahei UI light', 15, 'bold',)).place(
        x=100, y=93)
    fpe1 = tk.Entry(fpw, width=17, font=('Microsoft Yahei UI light', 17, 'bold'), border=0, fg='black')
    fpe1.place(x=120, y=150)
    ctk.CTkLabel(fpw, text="New-Password", text_color='#57a1f8', font=('Microsoft Yahei UI light', 15, 'bold',)).place(
        x=100, y=170)
    fpe2 = tk.Entry(fpw, width=20, font=('Microsoft Yahei UI light', 17, 'bold'), border=0, fg='black')
    fpe2.place(x=120, y=250)
    ctk.CTkLabel(fpw, text="Conform Password", text_color='#57a1f8',
                 font=('Microsoft Yahei UI light', 15, 'bold',)).place(x=100, y=250)
    fpe3 = tk.Entry(fpw, width=20, font=('Microsoft Yahei UI light', 17, 'bold'), border=0, fg='black')
    fpe3.place(x=120, y=350)
    ctk.CTkButton(fpw, text="Submit", font=('Microsoft Yahei UI light', 15, 'bold',), width=80, height=30,
                  corner_radius=0, command=update).place(x=150, y=320)
    fpw.mainloop()


def create_acc():
    def create():
        try:
            mycur.execute('select Password from Owner_logininfo')
            a = mycur.fetchall()
            if cawe4.get() == a[0][0]:
                mycur.execute(f"insert into Acc_info values('{cawe1.get()}','{cawe2.get()}','{cawe3.get()}')")
                mydb.commit()
                messagebox.showinfo(title='Acc_info', message='Account_created successfully')
                caw.destroy()
        except:
            messagebox.showerror(title='Error', message="Invalid Owner password")

    caw = ctk.CTk()
    caw.geometry('400x550')
    caw.resizable(width=False, height=False)
    ctk.CTkLabel(caw, text="Create New-Account", text_color='#57a1f8',
                 font=('Microsoft Yahei UI light', 30, 'bold',)).place(x=50, y=10)
    ctk.CTkLabel(caw, text="Name", text_color='#57a1f8', font=('Microsoft Yahei UI light', 15, 'bold',)).place(
        x=100, y=93)
    cawe1 = tk.Entry(caw, width=17, font=('Microsoft Yahei UI light', 17, 'bold'), border=0, fg='black')
    cawe1.place(x=120, y=150)
    ctk.CTkLabel(caw, text="Username", text_color='#57a1f8', font=('Microsoft Yahei UI light', 15, 'bold',)).place(
        x=100, y=170)
    cawe2 = tk.Entry(caw, width=20, font=('Microsoft Yahei UI light', 17, 'bold'), border=0, fg='black')
    cawe2.place(x=120, y=250)
    ctk.CTkLabel(caw, text="Password", text_color='#57a1f8',
                 font=('Microsoft Yahei UI light', 15, 'bold',)).place(x=100, y=250)
    cawe3 = tk.Entry(caw, width=20, font=('Microsoft Yahei UI light', 17, 'bold'), border=0, fg='black')
    cawe3.place(x=120, y=350)
    ctk.CTkLabel(caw, text="Conform Password", text_color='#57a1f8',
                 font=('Microsoft Yahei UI light', 15, 'bold',)).place(x=100, y=330)
    cawe4 = tk.Entry(caw, width=20, font=('Microsoft Yahei UI light', 17, 'bold'), border=0, fg='black')
    cawe4.place(x=120, y=450)
    ctk.CTkLabel(caw, text="Owner Password", text_color='#57a1f8',
                 font=('Microsoft Yahei UI light', 15, 'bold',)).place(x=100, y=410)
    cawe5 = tk.Entry(caw, width=20, font=('Microsoft Yahei UI light', 17, 'bold'), border=0, fg='black')
    cawe5.place(x=120, y=550)
    ctk.CTkButton(caw, text="Create", font=('Microsoft Yahei UI light', 15, 'bold',), width=80, height=30,
                  corner_radius=0, command=create).place(x=150, y=490)
    caw.mainloop()


ctk.set_appearance_mode('light')
w = ctk.CTk()
w.geometry('700x500')
w.resizable(width=False, height=False)
bgimg = ctk.CTkImage(light_image=Image.open('login_img2.png'), size=(400, 500))
ctk.CTkLabel(w, image=bgimg, text='').place(x=0, y=0)
ctk.CTkLabel(w, text='WELCOME', text_color='#57a1f8', font=('Microsoft Yahei UI light', 50, 'bold'), width=20,
             height=10).place(x=400, y=80)
ctk.CTkLabel(w, text='Username', text_color='#57a1f8', font=('Microsoft Yahei UI light', 15, 'bold'), width=20,
             height=10).place(x=400, y=190)
ctk.CTkLabel(w, text='Password', text_color='#57a1f8', font=('Microsoft Yahei UI light', 15, 'bold'), width=20,
             height=10).place(x=400, y=270)
e1 = tk.Entry(w, border=0, fg='black', width=17, bg='white', font=('Microsoft Yahei UI light', 17))
e1.place(x=500, y=270)
e2 = tk.Entry(w, border=0, fg='black', width=17, bg='white', font=('Microsoft Yahei UI light', 17))
e2.place(x=500, y=370)
ctk.CTkButton(w, text='forget-password?', width=100, height=15, font=('Microsoft Yahei UI light', 15, 'bold'),
              corner_radius=0, text_color='#57a1f8', fg_color='transparent', hover_color='#d9d9d9',
              command=forget_password).place(x=500, y=333)
ctk.CTkButton(w, text='Create-Account?', width=100, height=15, font=('Microsoft Yahei UI light', 15, 'bold'),
              corner_radius=0, text_color='#57a1f8', fg_color='transparent', hover_color='#d9d9d9',
              command=create_acc).place(x=500, y=357)
ctk.CTkButton(w, text='Sign-in', width=100, height=40, font=('Microsoft Yahei UI light', 20, 'bold'), corner_radius=0,
              text_color='white', command=login).place(x=470, y=400)
w.mainloop()
