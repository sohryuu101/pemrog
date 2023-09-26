# importing modules and files
import tkinter as tk
import customtkinter as ctk
import csv
import string
from tkinter.messagebox import showerror, askyesno, showinfo, showwarning
from gui_sql_final import AppSQL
from gui_register_final import AppRegister
from Dictionary import encrypt_decrypt
##################################################

# set tema dark dari customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class AppLogin(ctk.CTk): # membuat turunan kelas dari ctk.CTk
    def __init__(self):
        super().__init__()
        # settingan awal 
        self.geometry("750x450") # set ukuran window
        self.title("SQL Python GUI") # set judul window
        self.bind('<Return>', self.onEnter) # binding tombol enter dengan fungsi onEnter
        
        # variabel awal
        self.salah_login = 0 # untuk pengulangan login
        
        # frame login
        self.login_frame = ctk.CTkFrame(self) # inisiasi frame untuk login
        self.login_frame.pack(fill='both', expand=True, anchor=tk.CENTER) # menampilkan frame login 
        
    # komponen-komponen
        # font
        self.font_header = ctk.CTkFont(family='Consolas', size=20) # font untuk header
        self.font_body = ctk.CTkFont(family='Consolas', size=10) # font untuk body
        
        #label untuk welcoming
        self.label_welcome = ctk.CTkLabel(master=self.login_frame, 
                                          text='Selamat Datang di SQL Mockup!', 
                                          font=self.font_header) # membuat label untuk welcoming
        self.label_welcome.pack(pady=10) # menampilkan label
        
        # label untuk username
        self.label_input_username = ctk.CTkLabel(master=self.login_frame, 
                                        text='Log in ke akun anda: ', 
                                        font=self.font_body) # membuat label untuk login
        self.label_input_username.pack(pady=(0, 10)) # menampilkan label
        
        # input username
        self.username = ctk.StringVar() # inisiasi variabel untuk username
        self.input_username = ctk.CTkEntry(master=self.login_frame, placeholder_text='Username',
                                  textvariable=self.username, 
                                  font=self.font_body, 
                                  corner_radius=30) # membuat entry untuk username
        self.input_username.pack(pady=(0, 10)) # menampilkan entry
        
        # input password
        self.password = ctk.StringVar() # unisiasi variabel untuk password
        self.input_password = ctk.CTkEntry(master=self.login_frame, placeholder_text='Password', 
                                  textvariable=self.password,
                                  show= '*', 
                                  font=self.font_body, 
                                  corner_radius=30) # membuat entry untuk password
        self.input_password.pack(pady=(0, 10)) # menampilkan entry
        
    # tombol
        # tombol masukan
        self.tombol_input = ctk.CTkButton(master=self.login_frame, 
                                          text='Kirim', 
                                          command=self.onClick, 
                                          font=self.font_body, 
                                          corner_radius=30) # membuat tombol dan menjalankan fungsi onClick jika diklik
        self.tombol_input.pack(pady=10) # menampilkan tombol
        
        # Label register 
        self.label_register = ctk.CTkLabel(master=self.login_frame, 
                                        text='Belum punya akun?: ', 
                                        font=self.font_body) # label jika belum punya akun
        self.label_register.pack(pady=(0, 10)) # menampilkan label
        
        # tombol register
        self.tombol_register = ctk.CTkButton(master=self.login_frame, 
                                          text='Daftar', 
                                          command=self.register, 
                                          font=self.font_body, 
                                          corner_radius=30) # membuat tombol dan menjalankan fungsi register jika diklik
        self.tombol_register.pack(pady=(0, 10)) # menampilkan tombol
        
    # logika pada tombol
    def onClick(self):
        username = self.username.get() # mendapatkan username dari masukan
        password = self.password.get() # mendapatkan password dari masukan
        
        if username == None or password == None: # jika password kosong keluarkan pesan
            showwarning(title='Error', message='Username dan password tidak boleh kosong!')
            return # tidak menjalankan kode selanjutnya                  
        
        with open('user.csv', mode='r') as file: # membuka file csv
            csvFile = csv.reader(file) # membaca file csv
            for lines in csvFile: # untuk setiap baris di file csv
                dekripsi = encrypt_decrypt(lines[1], 3, characters=(string.ascii_lowercase + string.ascii_uppercase),
                                decrypt=True, shift_type="left")
                
                if username in lines[0] and dekripsi == password: # untuk setiap baris di file csv jika username dan pass matching dengan di csv
                    self.destroy() # hentikan aplikasi login
                    app2 = AppSQL(uname=username, pwd=password)
                    app2.mainloop() # menjalankan aplikasi SQL
                    return
                elif username in lines[0] and dekripsi != password: # jika username ada tapi password salah
                    self.salah_login += 1 # attempt login
                    showerror(title='Error', message='username/password salah!')
                    
                    if self.salah_login == 3: # jika salah login 3 kali tanya apakah mau keluar atau lanjut bikin baru
                        answer = askyesno(title='Error', message="Anda telah mencapai batas maksimum login! Atau anda ingin membuat akun baru?")
                        if answer == True:
                            self.register()
                        else:
                            showinfo(title='Info', message="Selamat Tinggal!")
                            self.destroy()
                elif username not in lines[0]: # jika username tidak ada
                    showerror(title='Error', message='username tidak ditemukan!')

        
    def onEnter(self, event): # jika tombol enter ditekan
        self.onClick()
    
    def register(self): # fungsi untuk ke window register
        self.destroy()
        app3 = AppRegister()
        app3.mainloop()

if __name__ == '__main__':
    app = AppLogin()
    app.mainloop()