# importing modules and files
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from Dictionary import translation_dict
from tkinter.messagebox import showinfo
# import mysql.connector
##################################################
# set tema dark
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# membuat koneksi dengan mysql
# conn = mysql.connector.connect(host='127.0.0.1', password='root', user='root',database='pemrog')

class App():
    def __init__(self, window):
        super().__init__()
        # settingan awal window
        self.window = window
        self.window.geometry("500x300")
        self.window.title("SQL Python GUI")
        self.window.bind('<Return>', self.onEnter)
        
        # frame input
        self.input_frame = ctk.CTkFrame(window)
        self.input_frame.pack(fill='both', expand=True)  
        
        # frame tabel
        self.frame_table = ctk.CTkFrame(window)
        self.frame_table.pack(fill='both', expand=True)
        
    # komponen-komponen
        # font
        self.font_header = ctk.CTkFont(family='Consolas', size=20)
        self.font_body = ctk.CTkFont(family='Consolas', size=10)
        
        #label untuk welcoming
        self.label_welcome = ctk.CTkLabel(self.input_frame, 
                                          text='Selamat Datang, User di SQL Mockup!', 
                                          font=self.font_header)
        self.label_welcome.pack(pady=10)
        
        # label untuk username
        self.label_input_username = ctk.CTkLabel(self.input_frame, 
                                        text='Masukkan username: ', 
                                        font=self.font_body)
        self.label_input_username.pack(pady=10)
        
        # input username
        self.username = ctk.StringVar()
        self.input_username = ctk.CTkEntry(self.input_frame, 
                                  placeholder_text='Username :', 
                                  textvariable=self.username, 
                                  font=self.font_body, 
                                  corner_radius=30)
        self.input_username.pack(pady=(0, 10))
        # label untuk password
        self.label_input_password = ctk.CTkLabel(self.input_frame, 
                                        text='Masukkan password: ', 
                                        font=self.font_body)
        self.label_input_password.pack(pady=10)
        # input password
        self.password = ctk.StringVar()
        self.label_input_username.pack(pady=10)
        self.input_password = ctk.CTkEntry(self.input_frame, 
                                  placeholder_text='Password', 
                                  textvariable=self.password, 
                                  font=self.font_body, 
                                  corner_radius=30)
        self.input_password.pack(pady=(0, 10))
        
    # tombol
        # tombol masukan
        self.tombol_input = ctk.CTkButton(self.input_frame, 
                                          text='Submit', 
                                          command=self.onClick, 
                                          font=self.font_body, 
                                          corner_radius=30)
        self.tombol_input.pack(pady=(0, 10))
        # tombol register 
        self.label_register = ctk.CTkLabel(self.input_frame, 
                                        text='Belum punya akun?: ', 
                                        font=self.font_body)
        self.label_register.pack(pady=10)
        self.tombol_register = ctk.CTkButton(self.input_frame, 
                                          text='Daftar', 
                                          command=self.onClick, 
                                          font=self.font_body, 
                                          corner_radius=30)
        self.tombol_register.pack(pady=(0, 10))
        
        
    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))
        
    # logika pada tombol
    def onClick(self):
        text = self.perintah.get()
        text = text.upper()+';'
        translated = self.translate(text)
        cursor = conn.cursor()
        cursor.execute(translated)
        results = cursor.fetchall()
        
        for item in results:
            self.tree.insert('', tk.END, values=item)
        # self.tree.bind('<<TreeviewSelect>>', self.item_selected)

    def onEnter(self, event):
        self.onClick()

if __name__ == '__main__':
    window = ctk.CTk()
    app = App(window)
    window.mainloop()