import datetime
import threading
import tkinter as tk
import customtkinter as ctk
import mysql.connector
from PIL import Image
from tabulate import tabulate

# global vars
sno_dict={}
column = ['Product', 'Barcode', 'Price', 'Discount%', 'Discount-Amt', 'Tax   ', 'Selling-price']
data_table = []
qty = 0
total = 0
discount = 0
coupon_disc=0
total_disc_amt=0
total_sale_amt = 0
tax = 0
sale_price = 0
bc = '#333547'
pm = 'CASH'
bill_no = '0'
mydb = mysql.connector.connect(host='localhost', password='SAGAR@pass1', user='root')
mycur = mydb.cursor()
mycur.execute('use Store')
w = ctk.CTk()
w.geometry('1920x1080')
w.config(background='#f3f6f9')
img_dict = {'shirt': 'hawaiian-shirt.png', 'pant': 'pants.png', 'tshirt': 't-shirt.png', 'cap': 'cap.png'}
stop_flag = False


def f10():
    mode.place(x=1300, y=700)


def applay_info(x):

    barcode = br_entry.get()
    brand_entry.delete(0, ctk.END)
    mrp_entry.delete(0, ctk.END)
    sale_entry.delete(0, ctk.END)
    mycur.execute(f"select * from sample_data where barcode='{barcode}'")
    data = list(mycur.fetchall()[0])

    global qty
    global total
    global discount
    global total_sale_amt
    global tax
    global sale_price
    global data_table
    global total_disc_amt
    global coupon_disc
    if qty>0 and del_check.get()==1:
        print('inside')
        qty = qty - 1
        total = total - data[3]
        discount = discount - (data[2] / 100) * data[3]
        total_sale_amt = total - discount
        tax = (5 / 100) * data[3]
        total_disc_amt = total_disc_amt - (data[2] / 100) * data[3] + coupon_disc
        data_table.pop(sno_dict[barcode]-1)
        brand_entry.insert(0, data[5])

    else:
        mrp_entry.delete(0,ctk.END)
        sale_entry.delete(0,ctk.END)
        brand_entry.insert(0, data[5])
        f7l1.configure(text=data[4])
        f7l3.configure(text=data[2])
        qty = qty + 1
        sno_dict[barcode] = qty
        total = total + data[3]
        discount = discount + (data[2] / 100) * data[3]
        total_sale_amt = total - discount
        tax = (5 / 100) * data[3]
        sale_price = data[3] - (data[2] / 100) * data[3]
        total_disc_amt =  discount + coupon_disc
        mrp_entry.insert(0,sale_price)
        sale_entry.insert(0,sale_price)
        show_data = [data[1], f'{barcode}', f'{data[3]}', f'{data[2]}', f'{(data[2] / 100) * data[3]}', f'{tax}',
                     f'{sale_price}']
        data_table.append(show_data)


    product_image = ctk.CTkImage(light_image=Image.open(img_dict[data[1]]), size=(80, 80))
    f7l2.configure(text="", image=product_image)
    tax1_l.configure(text=str(tax))
    tax2_l.configure(text=str(tax))
    total_tax_l.configure(text=str(2 * tax))
    f6l1.configure(text=str(qty))
    f6l4.configure(text=str(total))
    f6l6.configure(text=str(discount))
    f6l8.configure(text='00000')
    f6l10.configure(text='00000')
    f6l12.configure(text='00000')
    f6l14.configure(text=total_disc_amt)
    f6l15.configure(text=f"{total_sale_amt}/-")
    f6l19.configure(text='00000')
    a = tabulate(data_table, showindex=False, headers=column, tablefmt='plain')
    f5l1.configure(text=f"   {str(a)}")
    f5l1.grid(row=0, column=1)


def set_default():
    mode_label.configure(text='CASH')
    f6l1.configure(text='00')
    f6l4.configure(text='00000')
    f6l6.configure(text='00000')
    f6l8.configure(text='00000')
    f6l10.configure(text='00000')
    f6l12.configure(text='00000')
    f6l14.configure(text='00000')
    f6l15.configure(text='00000 /-')
    f6l19.configure(text='00000')
    # frame7
    f7l1.configure(text="-")
    f7l2.configure(text="--", image=None)
    f7l3.configure(text='10%')
    # frame8
    mode.set('CASH')
    mode1.set('CASH')
    mode1.place_forget()
    mode2.place_forget()
    f8e1.place_forget()
    f8e2.place_forget()
    global qty
    qty = 0
    global total
    total = 0
    mode.configure(state="disabled")


def get_amt():
    f8e2.configure(state='disabled')
    while not stop_flag:
        if re_amt1.get() == "":
            re_amt2.set(total_sale_amt)
        else:
            re_amt2.set(total_sale_amt - int(re_amt1.get()))



# -----------------------------Frames-------------------------
ctk.CTkFrame(w, width=1515, height=35, fg_color='#FFFFFF', bg_color='#F3F6F9', corner_radius=5).place(x=10, y=5)
ctk.CTkFrame(w, width=1515, height=30, fg_color='#FFFFFF', bg_color='#F3F6F9', corner_radius=5).place(x=10, y=50)
scrolls = ['vertical', 'horizontal']
ctk.CTkFrame(w, width=1515, height=30, fg_color='#FFFFFF', bg_color='#F3F6F9', corner_radius=5).place(x=10, y=195)
f5 = ctk.CTkScrollableFrame(w, width=1130, height=420, fg_color='#FFFFFF', bg_color='#F3F6F9', corner_radius=5,
                            border_width=5,
                            border_color='#EEEFFA')
f5.place(x=10, y=230)
# frame insidef5
#ctk.CTkFrame(w, width=45, height=420, fg_color='#fad1bd', bg_color='#ffffff').place(x=20, y=240)
# -
ctk.CTkFrame(w, width=348, height=450, fg_color='#FFFFFF', bg_color='#F3F6F9', corner_radius=5, border_width=5,
             border_color='#EEEFFA').place(x=1175, y=230)
ctk.CTkFrame(w, width=950, height=150, fg_color='#FFFFFF', bg_color='#F3F6F9', corner_radius=5, border_width=5,
             border_color='#EEEFFA').place(x=10, y=690)
ctk.CTkFrame(w, width=550, height=150, fg_color='#FFFFFF', bg_color='#F3F6F9', corner_radius=0, border_width=5,
             border_color='#EEEFFA').place(x=970, y=690)

# --------------------------Frame1---------------------------

date = datetime.date.today().strftime('%d-%m-%Y')
mycur.execute("select Store_name from Owner_logininfo where password='SAGAR@pass1'")
a = mycur.fetchall()
shop_name = a[0][0]
user_name = 'user_name'
ctk.CTkLabel(w, text=date, text_color='#333547', font=('Comic Sans MS', 20, 'bold'), bg_color='#FFFFFF').place(x=13,
                                                                                                               y=6)
ctk.CTkLabel(w, text=shop_name, text_color='#333547', font=('Comic Sans MS', 23, 'bold'), bg_color='#FFFFFF').place(
    relx=0.44, y=6)
ctk.CTkLabel(w, text=user_name, text_color='#333547', font=('Comic Sans MS', 20, 'bold'), bg_color='#FFFFFF').place(
    relx=0.90, y=6)

# --------------------------Frame3---------------------------
rf_img = ctk.CTkImage(light_image=Image.open('illustration-of-refresh-icon-vector.png'), size=(40, 40))
f31 = ctk.CTkFrame(w, width=150, height=95, corner_radius=15, fg_color='#ffffff', bg_color='#f2f2f2', border_width=0)
f31.place(x=15, y=90)
ctk.CTkLabel(f31, text='', image=rf_img).place(x=50, y=5)
ctk.CTkButton(f31, text='Refresh', text_color=bc, width=100, height=5, font=('Comic Sans MS', 30, 'bold'),
              fg_color='#ffffff', hover_color='#657176',corner_radius=5).place(x=10, y=45)

df_img = ctk.CTkImage(light_image=Image.open('shopping-bag.png'), size=(40, 40))
f32 = ctk.CTkFrame(w, width=150, height=95, corner_radius=15, fg_color='#ffffff', bg_color='#f2f2f2', border_width=0)
f32.place(x=180, y=90)
ctk.CTkLabel(f32, text='', image=df_img).place(x=50, y=5)
ctk.CTkButton(f32, text='Discount', text_color=bc, width=100, height=5, font=('Comic Sans MS', 30, 'bold'),
              fg_color='#ffffff', hover_color='#657176',corner_radius=5).place(x=10, y=45)

cf_img = ctk.CTkImage(light_image=Image.open('WhatsApp Image 2023-03-28 at 02.25.47.png'), size=(40, 40))
f33 = ctk.CTkFrame(w, width=130, height=95, corner_radius=15, fg_color='#ffffff', bg_color='#f2f2f2', border_width=0)
f33.place(x=340, y=90)
ctk.CTkLabel(f33, text='', image=cf_img).place(x=50, y=5)
ctk.CTkButton(f33, text='Coupon', text_color=bc, width=100, height=5, font=('Comic Sans MS', 30, 'bold'),
              fg_color='#ffffff', hover_color='#657176',corner_radius=5).place(x=10, y=45)

pf_img = ctk.CTkImage(light_image=Image.open('Screenshot 2023-03-28 031225.png'), size=(40, 40))
f34 = ctk.CTkFrame(w, width=160, height=95, corner_radius=15, fg_color='#ffffff', bg_color='#f2f2f2', border_width=0)
f34.place(x=480, y=90)
ctk.CTkLabel(f34, text='', image=pf_img).place(x=55, y=3)
ctk.CTkButton(f34, text='Payment', text_color=bc, width=100, height=35, font=('Comic Sans MS', 30, 'bold'),
              fg_color='#ffffff', hover_color='#657176',corner_radius=5).place(x=15, y=45)

bf_img = ctk.CTkImage(light_image=Image.open('3d-hand-with-safe-payment-confirmation-bill.png'), size=(80, 50))
f35 = ctk.CTkFrame(w, width=135, height=95, corner_radius=15, fg_color='#ffffff', bg_color='#f2f2f2', border_width=0)
f35.place(x=650, y=90)
ctk.CTkLabel(f35, text='', image=bf_img).place(x=20, y=3)
ctk.CTkButton(f35, text='Billing', text_color=bc, width=100, height=5, font=('Comic Sans MS', 30, 'bold'),
              fg_color='#ffffff', hover_color='#657176',corner_radius=5,command=f10).place(x=15, y=45)

hf_img = ctk.CTkImage(light_image=Image.open('hold.png'), size=(40, 40))
f36 = ctk.CTkFrame(w, width=130, height=95, corner_radius=15, fg_color='#ffffff', bg_color='#f2f2f2', border_width=0)
f36.place(x=795, y=90)
ctk.CTkLabel(f36, text='', image=hf_img).place(x=40, y=5)
ctk.CTkButton(f36, text='Hold', text_color=bc, width=100, height=5, font=('Comic Sans MS', 30, 'bold'),
              fg_color='#ffffff', hover_color='#657176',corner_radius=5).place(x=10, y=45)

uf_img = ctk.CTkImage(light_image=Image.open('minus.png'), size=(40, 40))
f37 = ctk.CTkFrame(w, width=150, height=95, corner_radius=15, fg_color='#ffffff', bg_color='#f2f2f2', border_width=0)
f37.place(x=935, y=90)
ctk.CTkLabel(f37, text='', image=uf_img).place(x=50, y=5)
ctk.CTkButton(f37, text='Un-Hold', text_color=bc, width=100, height=5, font=('Comic Sans MS', 30, 'bold'),
              fg_color='#ffffff', hover_color='#657176',corner_radius=5).place(x=10, y=45)


# frame4


def mode_changer(choise):
    mode_label.configure(text=mode.get())

    if mode.get() == 'COMBINED':

        if not th.is_alive():
             th.start()
        mode1.place(x=1300, y=750)
        mode2.place(x=1300, y=780)
        f8e1.place(x=1420, y=750)
        f8e2.place(x=1420, y=780)

        new_val = val.copy()
        new_val.remove(mode1.get())
        mode2.configure(values=new_val)

    else:

        mode1.place_forget()
        mode2.place_forget()
        f8e1.place_forget()
        f8e2.place_forget()


mode_label = ctk.CTkLabel(w, text='CASH', text_color='#333547', font=('Comic Sans MS', 20, 'bold'), bg_color='#ffffff')
mode_label.place(x=20, y=195)
ctk.CTkLabel(w, text='Bill number: ', text_color='#333547', font=('Comic Sans MS', 20, 'bold'),
             bg_color='#ffffff').place(x=150, y=195)
ctk.CTkLabel(w, text=bill_no, text_color='#333547', font=('Comic Sans MS', 20, 'bold'), bg_color='#ffffff').place(x=270,
                                                                                                                  y=195)

# frame 5

f5l1 = ctk.CTkLabel(f5, text="", font=('Comic Sans MS', 25, 'bold'), text_color=bc, width=400, height=30)


# frame6
f6l1 = ctk.CTkLabel(w, text='00', font=('Comic Sans MS', 45, 'bold'), fg_color='#ffffff', text_color=bc)
f6l1.place(x=1450, y=240)
f6l2 = ctk.CTkLabel(w, text='Bill View', text_color=bc, font=('Comic Sans MS', 35, 'bold'), width=100, height=50,
                    fg_color='#ffffff')
f6l2.place(x=1220, y=245)
f6l3 = ctk.CTkLabel(w, text='Total Amount :', text_color=bc, font=('Comic Sans MS', 20, 'bold'), width=100, height=40,
                    fg_color='#ffffff', bg_color='#ffffff')
f6l3.place(x=1200, y=300)
f6l4 = ctk.CTkLabel(w, text='00000', text_color=bc, font=('Comic Sans MS', 25, 'bold'), width=50, height=40,
                    fg_color='#ffffff', bg_color='#ffffff')
f6l4.place(x=1430, y=300)
f6l5 = ctk.CTkLabel(w, text='Discount Amt :', text_color=bc, font=('Comic Sans MS', 20, 'bold'), width=100, height=40,
                    fg_color='#ffffff', bg_color='#ffffff')
f6l5.place(x=1200, y=340)
f6l6 = ctk.CTkLabel(w, text='00000', text_color=bc, font=('Comic Sans MS', 25, 'bold'), width=50, height=40,
                    fg_color='#ffffff', bg_color='#ffffff')
f6l6.place(x=1430, y=340)
f6l7 = ctk.CTkLabel(w, text='Additional Disc%:', text_color=bc, font=('Comic Sans MS', 20, 'bold'), width=100,
                    height=40, fg_color='#ffffff', bg_color='#ffffff')
f6l7.place(x=1200, y=380)
f6l8 = ctk.CTkLabel(w, text='00000', text_color=bc, font=('Comic Sans MS', 25, 'bold'), width=50, height=40,
                    fg_color='#ffffff', bg_color='#ffffff')
f6l8.place(x=1430, y=380)
f6l9 = ctk.CTkLabel(w, text='Additional Disc Amt:', text_color=bc, font=('Comic Sans MS', 20, 'bold'), width=100,
                    height=40, fg_color='#ffffff', bg_color='#ffffff')
f6l9.place(x=1200, y=420)
f6l10 = ctk.CTkLabel(w, text='00000', text_color=bc, font=('Comic Sans MS', 25, 'bold'), width=50, height=40,
                     fg_color='#ffffff', bg_color='#ffffff')
f6l10.place(x=1430, y=420)
f6l11 = ctk.CTkLabel(w, text='Coupon Disc Amt:', text_color=bc, font=('Comic Sans MS', 20, 'bold'), width=100,
                     height=40, fg_color='#ffffff', bg_color='#ffffff')
f6l11.place(x=1200, y=460)
f6l12 = ctk.CTkLabel(w, text='00000', text_color=bc, font=('Comic Sans MS', 25, 'bold'), width=50, height=40,
                     fg_color='#ffffff', bg_color='#ffffff')
f6l12.place(x=1430, y=460)
f6l13 = ctk.CTkLabel(w, text='Total Disc Amt:', text_color=bc, font=('Comic Sans MS', 20, 'bold'), width=100, height=40,
                     fg_color='#ffffff', bg_color='#ffffff')
f6l13.place(x=1200, y=500)
f6l14 = ctk.CTkLabel(w, text='00000', text_color=bc, font=('Comic Sans MS', 25, 'bold'), width=50, height=40,
                     fg_color='#ffffff', bg_color='#ffffff')
f6l14.place(x=1430, y=500)
f61 = ctk.CTkFrame(w, width=305, height=60, fg_color='#626ed4', corner_radius=5, bg_color='#ffffff')
f61.place(x=1200, y=540)
f6l15 = ctk.CTkLabel(f61, text='00000 /-', text_color='#ffffff', font=('Comic Sans MS', 40, 'bold'))
f6l15.place(x=75, y=4)
f6l16 = ctk.CTkLabel(w, text='Amount Given:', text_color=bc, font=('Comic Sans MS', 20, 'bold'), width=100, height=40,
                     fg_color='#ffffff', bg_color='#ffffff')
f6l16.place(x=1200, y=600)
f6l17 = ctk.CTkEntry(w, width=160, height=30, fg_color='#ffffff', bg_color='#ffffff', text_color=bc,
                     font=('Comic Sans MS', 20, 'bold'))
f6l17.place(x=1350, y=605)
f6l18 = ctk.CTkLabel(w, text='Change :', text_color=bc, font=('Comic Sans MS', 20, 'bold'), width=100, height=40,
                     fg_color='#ffffff', bg_color='#ffffff')
f6l18.place(x=1200, y=630)
f6l19 = ctk.CTkLabel(w, text='00000', text_color='red', font=('Comic Sans MS', 20, 'bold'), width=50, height=30,
                     fg_color='#ffffff', bg_color='#ffffff')
f6l19.place(x=1440, y=640)

# frame7
br_entry = ctk.CTkEntry(w, text_color=bc, corner_radius=10, fg_color="#ffffff", bg_color='#ffffff', width=170,
                        height=40, font=('Comic Sans MS', 15, 'bold'))
br_entry.place(x=30, y=715)
br_entry.bind("<Return>", applay_info)
ctk.CTkLabel(w, text="Barcode", text_color=bc, font=('Comic Sans MS', 15, 'bold'), fg_color='#ffffff',
             bg_color="#ffffff").place(x=45, y=700)

ex_check=ctk.CTkCheckBox(w, text='Exchange', font=('Comic Sans MS', 15, 'bold'), text_color=bc, bg_color='#ffffff')
ex_check.place(x=230,y=705)
del_check=ctk.CTkCheckBox(w, text='Delete', font=('Comic Sans MS', 15, 'bold'), text_color=bc, bg_color='#ffffff')
del_check.place(x=230,y=740)
brand_entry = ctk.CTkEntry(w, text_color=bc, corner_radius=10, fg_color="#ffffff", bg_color='#ffffff', width=170,
                           height=40, font=('Comic Sans MS', 15, 'bold'))
brand_entry.place(x=30, y=785)
ctk.CTkLabel(w, text="Brand", text_color=bc, font=('Comic Sans MS', 15, 'bold'), fg_color='#ffffff',
             bg_color="#ffffff").place(x=45, y=770)
mrp_entry = ctk.CTkEntry(w, text_color=bc, corner_radius=10, fg_color="#ffffff", bg_color='#ffffff', width=75,
                         height=20, font=('Comic Sans MS', 13, 'bold'))
mrp_entry.place(x=250, y=770)
ctk.CTkLabel(w, text="MRP", text_color=bc, font=('Comic Sans MS', 15, 'bold'), fg_color='#ffffff',
             bg_color="#ffffff").place(x=210, y=770)
sale_entry = ctk.CTkEntry(w, text_color=bc, corner_radius=10, fg_color="#ffffff", bg_color='#ffffff', width=75,
                          height=20, font=('Comic Sans MS', 13, 'bold'))
sale_entry.place(x=250, y=800)
ctk.CTkLabel(w, text="Sale", text_color=bc, font=('Comic Sans MS', 15, 'bold'), fg_color='#ffffff',
             bg_color="#ffffff").place(x=210, y=800)
ctk.CTkLabel(w, text="Counter", text_color=bc, font=('Comic Sans MS', 20, 'bold'), fg_color='#ffffff',
             bg_color="#ffffff").place(x=360, y=705)
f7l1 = ctk.CTkLabel(w, text="-", text_color='#ffffff', font=('Comic Sans MS', 60, 'bold'), fg_color=bc,
                    bg_color="#ffffff", corner_radius=10, width=100, height=90)
f7l1.place(x=350, y=740)
ctk.CTkLabel(w, text="Product", text_color=bc, font=('Comic Sans MS', 20, 'bold'), fg_color='#ffffff',
             bg_color="#ffffff").place(x=480, y=705)

f7l2 = ctk.CTkLabel(w, text="--", font=('Comic Sans MS', 60, 'bold'), bg_color="#ffffff", corner_radius=10, width=100,
                    height=90)
f7l2.place(x=460, y=740)
ctk.CTkLabel(w, text="Discount", text_color=bc, font=('Comic Sans MS', 20, 'bold'), fg_color='#ffffff',
             bg_color="#ffffff").place(x=605, y=705)
f7l3 = ctk.CTkLabel(w, text="10%", text_color='#ffffff', font=('Comic Sans MS', 50, 'bold'), fg_color=bc,
                    bg_color="#ffffff", corner_radius=10, width=100, height=90)
f7l3.place(x=585, y=740)
tax1_l = ctk.CTkLabel(w, text='--', text_color=bc, corner_radius=10, fg_color="#ffffff", bg_color='#ffffff', width=75,
                      height=20, font=('Comic Sans MS', 13, 'bold'))
tax1_l.place(x=790, y=710)
ctk.CTkLabel(w, text="S-Gst", text_color=bc, font=('Comic Sans MS', 15, 'bold'), fg_color='#ffffff',
             bg_color="#ffffff").place(x=720, y=710)
tax2_l = ctk.CTkLabel(w, text='--', text_color=bc, corner_radius=10, fg_color="#ffffff", bg_color='#ffffff', width=75,
                      height=20, font=('Comic Sans MS', 13, 'bold'))
tax2_l.place(x=790, y=750)
ctk.CTkLabel(w, text="C-Gst", text_color=bc, font=('Comic Sans MS', 15, 'bold'), fg_color='#ffffff',
             bg_color="#ffffff").place(x=720, y=750)
total_tax_l = ctk.CTkLabel(w, text='--', text_color=bc, corner_radius=10, fg_color="#ffffff", bg_color='#ffffff',
                           width=75, height=20, font=('Comic Sans MS', 13, 'bold'))
total_tax_l.place(x=790, y=790)
ctk.CTkLabel(w, text="Tax-Amt", text_color=bc, font=('Comic Sans MS', 15, 'bold'), fg_color='#ffffff',
             bg_color="#ffffff").place(x=720, y=790)

# Frame8
def add_disc():
    print("inside--")
    add_disc_e1.place(x=1070,y=750)
    add_disc_e2.place(x=1070,y=800)
    add_disc_l1.place(x=980,y=750)
    add_disc_l2.place(x=980,y=800)


mode = ctk.CTkOptionMenu(w, width=200, height=40, values=['CASH', 'CARD', 'UPI', 'COMBINED'], command=mode_changer,
                         font=('Comic Sans MS', 15, 'bold'),
                         text_color=bc, fg_color='#eeeffa', bg_color='#ffffff', dropdown_fg_color='#eeeffa',
                         button_color='#eeeffa', button_hover_color='#fad1bd',
                         dropdown_text_color=bc, dropdown_hover_color='#fad1bd',
                         dropdown_font=('Comic Sans MS', 15, 'bold'))

mode.set('CASH')
mode1 = ctk.CTkOptionMenu(w, width=100, height=20, values=['CASH', 'CARD', 'UPI'], command=mode_changer,
                          font=('Comic Sans MS', 15, 'bold'),
                          text_color=bc, fg_color='#eeeffa', bg_color='#ffffff', dropdown_fg_color='#eeeffa',
                          button_color='#eeeffa', button_hover_color='#fad1bd',
                          dropdown_text_color=bc, dropdown_hover_color='#fad1bd',
                          dropdown_font=('Comic Sans MS', 15, 'bold'))
mode1.set('CASH')
re_amt1 = tk.StringVar()
re_amt1.set('0')
f8e1 = ctk.CTkEntry(w, width=80, height=14, font=('Comic Sans MS', 15, 'bold'), fg_color='#ffffff', text_color=bc,
                    corner_radius=10, bg_color='#ffffff', textvariable=re_amt1)

re_amt2 = tk.IntVar()
f8e2 = ctk.CTkEntry(w, width=80, height=14, font=('Comic Sans MS', 15, 'bold'), fg_color='#ffffff', text_color=bc,
                    corner_radius=10, bg_color='#ffffff', textvariable=re_amt2)

val = ['CASH', 'CARD', 'UPI']
mode2 = ctk.CTkOptionMenu(w, width=100, height=20, values=val, command=mode_changer,
                          font=('Comic Sans MS', 15, 'bold'),
                          text_color=bc, fg_color='#eeeffa', bg_color='#ffffff', dropdown_fg_color='#eeeffa',
                          button_color='#eeeffa', button_hover_color='#fad1bd',
                          dropdown_text_color=bc, dropdown_hover_color='#fad1bd',
                          dropdown_font=('Comic Sans MS', 15, 'bold'))
ctk.CTkButton(w,text="Additional-Disc",text_color="#ffffff",fg_color=bc,bg_color="#ffffff",width=150,height=40,font=('Comic Sans MS', 15, 'bold'),command=add_disc).place(x=980,y=700)
add_disc_e1=ctk.CTkEntry(w,width=80,height=30,font=('Comic Sans MS', 12, 'bold'),fg_color="#ffffff",text_color=bc,corner_radius=5,bg_color="#ffffff")
add_disc_e2=ctk.CTkEntry(w,width=80,height=30,font=('Comic Sans MS', 12, 'bold'),fg_color="#ffffff",text_color=bc,corner_radius=5,bg_color="#ffffff")
add_disc_l1=ctk.CTkLabel(w,text="Percent-%",font=('Comic Sans MS', 15, 'bold'),fg_color="#ffffff",text_color=bc,corner_radius=5,bg_color="#ffffff")
add_disc_l2=ctk.CTkLabel(w,text="Amount",font=('Comic Sans MS', 15, 'bold'),fg_color="#ffffff",text_color=bc,corner_radius=5,bg_color="#ffffff")

th = threading.Thread(target=get_amt)

w.mainloop()
