# importing modules and files
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter.messagebox import showinfo
import csv
import string
##################################################
# set tema dark
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class AppLogin():
    def __init__(self, window):
        super().__init__()
        # settingan awal window
        self.window = window
        self.window.geometry("750x450")
        self.window.title("SQL Python GUI")
        self.window.bind('<Return>', self.onEnter)
        
        # frame login
        self.login_frame = ctk.CTkFrame(window)
        self.login_frame.pack(fill='both', expand=True)  
        
    # komponen-komponen
        # font
        self.font_header = ctk.CTkFont(family='Consolas', size=20)
        self.font_body = ctk.CTkFont(family='Consolas', size=10)
        
        #label untuk welcoming
        self.label_welcome = ctk.CTkLabel(self.login_frame, 
                                          text='Selamat Datang di SQL Mockup!', 
                                          font=self.font_header)
        self.label_welcome.pack(pady=10)
        
        # label untuk username
        self.label_input_username = ctk.CTkLabel(self.login_frame, 
                                        text='Masukkan username: ', 
                                        font=self.font_body)
        self.label_input_username.pack(pady=(0, 10))
        
        # input username
        self.username = ctk.StringVar()
        self.input_username = ctk.CTkEntry(self.login_frame,
                                  textvariable=self.username, 
                                  font=self.font_body, 
                                  corner_radius=30)
        self.input_username.pack(pady=(0, 10))
        
        # label untuk password
        self.label_input_password = ctk.CTkLabel(self.login_frame, 
                                        text='Masukkan password: ', 
                                        font=self.font_body)
        self.label_input_password.pack(pady=(0, 10))
        
        # input password
        self.password = ctk.StringVar()
        self.input_password = ctk.CTkEntry(self.login_frame, 
                                  textvariable=self.password,
                                  show= '*', 
                                  font=self.font_body, 
                                  corner_radius=30)
        self.input_password.pack(pady=(0, 10))
        
    # tombol
        # tombol masukan
        self.tombol_input = ctk.CTkButton(self.login_frame, 
                                          text='Kirim', 
                                          command=self.onClick, 
                                          font=self.font_body, 
                                          corner_radius=30)
        self.tombol_input.pack(pady=10)
        
        # Label register 
        self.label_register = ctk.CTkLabel(self.login_frame, 
                                        text='Belum punya akun?: ', 
                                        font=self.font_body)
        self.label_register.pack(pady=(0, 10))
        
        # tombol register
        self.tombol_register = ctk.CTkButton(self.login_frame, 
                                          text='Daftar', 
                                          command=self.onClick, 
                                          font=self.font_body, 
                                          corner_radius=30)
        self.tombol_register.pack(pady=(0, 10))
        
    # logika pada tombol
    def onClick(self):
        username = self.username.get()
        password = self.password.get()                    
        salah_login = 0
        
        with open('user.csv', mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                dekripsi = self.encrypt_decrypt(lines[1], 3, characters=(string.ascii_lowercase + string.ascii_uppercase),
                                decrypt=True, shift_type="left")
                if username in lines[0] and dekripsi == password:
                    return True
        

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

if __name__ == '__main__':
    window = ctk.CTk()
    app = AppLogin(window)
    window.mainloop()