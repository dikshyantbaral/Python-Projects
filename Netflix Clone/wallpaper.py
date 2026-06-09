from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'dikshyant@gmail.com' and password == '1234':
        messagebox.showinfo('Yayy','Login Successfull')
    else:
        messagebox.showerror('Error','Login Failed')


root = Tk()
root.title("Login Form")
root.iconbitmap('favicon.ico')

root.geometry('350x500')
root.configure(background='black')
img = Image.open('netflix.png')
resized_img = img.resize((100,80))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root,image=img,bg='black',highlightthickness=0)
img_label.pack(pady=(10,8))

text_label = Label(root,text='NETFLIX',fg='#E50914',bg='black')
text_label.pack()
text_label.config(font=('Roboto',26, 'bold'))

email_label = Label(root,text='Enter your email', fg='white', bg='black')
email_label.pack(pady=(20,5))
email_label.config(font=('Verdana',14,'bold'))

email_input = Entry(root, width=50)
email_input.pack(ipady=6)

password_label = Label(root,text='Enter Password', fg='white', bg='black')
password_label.pack(pady=(20,5))
password_label.config(font=('Verdana',14,'bold'))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root,text='Login Now',bg='black',fg='red' ,width=15,height=2,command=handle_login)
login_btn.config(font=('Arial',11,'bold'))
login_btn.pack(pady=(10,20))

root.mainloop()
