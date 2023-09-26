# importing modules and files
import tkinter as tk
import customtkinter as ctk
import csv
import string
from tkinter.messagebox import showerror, askyesno, showinfo, showwarning
from gui_sql_final import AppSQL
from gui_register_final import AppRegister
##################################################
# set tema dark
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class AppLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        # settingan awal 
        self.geometry("750x450")
        self.title("SQL Python GUI")
        self.bind('<Return>', self.onEnter)
        
        # variabel awal
        self.salah_login = 0
        
        # frame login
        self.login_frame = ctk.CTkFrame(self)
        self.login_frame.pack(fill='both', expand=True, anchor=tk.CENTER)  
        
    # komponen-komponen
        # font
        self.font_header = ctk.CTkFont(family='Consolas', size=20)
        self.font_body = ctk.CTkFont(family='Consolas', size=10)
        
        #label untuk welcoming
        self.label_welcome = ctk.CTkLabel(master=self.login_frame, 
                                          text='Selamat Datang di SQL Mockup!', 
                                          font=self.font_header)
        self.label_welcome.pack(pady=10)
        
        # label untuk username
        self.label_input_username = ctk.CTkLabel(master=self.login_frame, 
                                        text='Log in ke akun anda: ', 
                                        font=self.font_body)
        self.label_input_username.pack(pady=(0, 10))
        
        # input username
        self.username = ctk.StringVar()
        self.input_username = ctk.CTkEntry(master=self.login_frame, placeholder_text='Username',
                                  textvariable=self.username, 
                                  font=self.font_body, 
                                  corner_radius=30)
        self.input_username.pack(pady=(0, 10))
        
        # input password
        self.password = ctk.StringVar()
        self.input_password = ctk.CTkEntry(master=self.login_frame, placeholder_text='Password', 
                                  textvariable=self.password,
                                  show= '*', 
                                  font=self.font_body, 
                                  corner_radius=30)
        self.input_password.pack(pady=(0, 10))
        
    # tombol
        # tombol masukan
        self.tombol_input = ctk.CTkButton(master=self.login_frame, 
                                          text='Kirim', 
                                          command=self.onClick, 
                                          font=self.font_body, 
                                          corner_radius=30)
        self.tombol_input.pack(pady=10)
        
        # Label register 
        self.label_register = ctk.CTkLabel(master=self.login_frame, 
                                        text='Belum punya akun?: ', 
                                        font=self.font_body)
        self.label_register.pack(pady=(0, 10))
        
        # tombol register
        self.tombol_register = ctk.CTkButton(master=self.login_frame, 
                                          text='Daftar', 
                                          command=self.register, 
                                          font=self.font_body, 
                                          corner_radius=30)
        self.tombol_register.pack(pady=(0, 10))
        
    # logika pada tombol
    def onClick(self):
        username = self.username.get()
        password = self.password.get()
        
        if username == None or password == None:
            showwarning(title='Error', message='Username dan password tidak boleh kosong!')                    
        
        with open('user.csv', mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                dekripsi = self.encrypt_decrypt(lines[1], 3, characters=(string.ascii_lowercase + string.ascii_uppercase),
                                decrypt=True, shift_type="left")
                
                if username in lines[0] and dekripsi == password:
                    self.destroy()
                    app2 = AppSQL(uname=username, pwd=password)
                    app2.mainloop()
                    return
                elif username in lines[0] and dekripsi != password:
                    self.salah_login += 1
                    showerror(title='Error', message='username/password salah!')
                    
                    if self.salah_login == 3:
                        answer = askyesno(title='Error', message="Anda telah mencapai batas maksimum login! Atau anda ingin membuat akun baru?")
                        if answer == True:
                            self.register()
                        else:
                            showinfo(title='Info', message="Selamat Tinggal!")
                            self.destroy()
                elif username not in lines[0]:
                    showerror(title='Error', message='username tidak ditemukan!')

        
    def onEnter(self, event):
        self.onClick()
        
    def encrypt_decrypt(self, text, key, characters=string.ascii_lowercase, decrypt=False, shift_type="right"):
        if key < 0:
            print("K tidak valid (tidak boleh negatif)")
            return None
        n = len(characters)
        if decrypt == True:
            key = n - key
        if shift_type == "left":
            key = -key
        rumus_sulap = str.maketrans(characters, characters[key:] + characters[:key])
        tersulap = text.translate(rumus_sulap)
        return tersulap
    
    def register(self):
        self.destroy()
        app3 = AppRegister()
        app3.mainloop()

if __name__ == '__main__':
    app = AppLogin()
    app.mainloop()