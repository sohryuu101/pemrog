# importing modules and files
import customtkinter as ctk
import csv
import string
from tkinter.messagebox import showinfo, showwarning
import mysql.connector
from Dictionary import encrypt_decrypt
##################################################
# set tema dark
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# mendapatkan pasword yang terenkripsi dari app login        
passuwodo = encrypt_decrypt('ollq', 3, characters=(string.ascii_lowercase + string.ascii_uppercase),
                                decrypt=True, shift_type="left")

# menghubungkan dengan database
conn = mysql.connector.connect(host='127.0.0.1', password=passuwodo, user='root',database='pemrog')

class AppRegister(ctk.CTk): # class untuk window register
    def __init__(self):
        super().__init__()
        # settingan awal 
        self.geometry("750x450") # set ukuran window
        self.title("SQL Python GUI") # set judul window
        self.bind('<Return>', self.onEnter) # binding tombol enter dengan fungsi onEnter
        
        # frame register
        self.register_frame = ctk.CTkFrame(self) # inisiasi frame untuk register
        self.register_frame.pack(fill='both', expand=True) # menampilkan frame register
        
    # komponen-komponen
        # font
        self.font_header = ctk.CTkFont(family='Consolas', size=20) # font untuk header
        self.font_body = ctk.CTkFont(family='Consolas', size=10) # font untuk body
        
        #label untuk welcoming
        self.label_register = ctk.CTkLabel(master=self.register_frame, 
                                          text='Buat akun baru!', 
                                          font=self.font_header) # label untuk register
        self.label_register.pack(pady=10)
        
        # label untuk username
        self.label_input_username = ctk.CTkLabel(master=self.register_frame, 
                                        text='Masukkan username baru: ', 
                                        font=self.font_body) # label untuk username
        self.label_input_username.pack(pady=(0, 10)) # menampilkan label
        
        # input username
        self.username = ctk.StringVar() # variabel untuk username
        self.input_username = ctk.CTkEntry(master=self.register_frame, placeholder_text='Username',
                                  textvariable=self.username, 
                                  font=self.font_body, 
                                  corner_radius=30) # entry box username 
        self.input_username.pack(pady=(0, 10)) # menampilkan entry box
        
        # label untuk pass
        self.label_input_password = ctk.CTkLabel(master=self.register_frame, 
                                        text='Masukkan password baru: ', 
                                        font=self.font_body) # label untuk password
        self.label_input_password.pack(pady=(0, 10)) # menampilkan label
        
        # input password
        self.password = ctk.StringVar() # variabel untuk password
        self.input_password = ctk.CTkEntry(master=self.register_frame, placeholder_text='Password', 
                                  textvariable=self.password,
                                  show= '*', 
                                  font=self.font_body, 
                                  corner_radius=30) # entry box password
        self.input_password.pack(pady=(0, 10)) # menampilkan entry box
        
    # tombol
        # tombol masukan
        self.tombol_input = ctk.CTkButton(master=self.register_frame, 
                                          text='Kirim', 
                                          command=self.onClick, 
                                          font=self.font_body, 
                                          corner_radius=30) # tombol kirim yang menjalankan onClick jika ditekan
        self.tombol_input.pack(pady=10) # menampilkan tombol
        
        # tombol kembali
        self.tombol_back = ctk.CTkButton(master=self.register_frame, 
                                          text='Kembali ke login', 
                                          command=self.back, 
                                          font=self.font_body, 
                                          corner_radius=30) # tombol kembali
        self.tombol_back.pack(pady=10) # menampilkan tombol
        
    # logika pada tombol
    def onClick(self): # jika tombol kirim ditekan
        username = self.username.get() # mendapatkan username dari entry
        password = self.password.get() # mendapatkan password dari entry
        double = False  # boolean cek apakah ada yang sama
        
        if username == "" or password == "": # jika username/password kosong keluarkan pesan
            showwarning(title='Error', message='Username dan password tidak boleh kosong!')
            return
        
        with open('user.csv', mode='r') as file: # membuka file csv
            csvFile = csv.reader(file) # membaca file csv
            for lines in csvFile: # untuk setiap baris di file csv
                if username == lines[0]: # jika username ada
                    showwarning(title='Error', message='Username sudah digunakan!')
                    double = True
                    return
                
        if double == False: # jika username belum ada
            comm1 = f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';"
            comm2 = f"GRANT ALL PRIVILEGES on pemrog.genshin TO '{username}'@'localhost';"
            comm3 = f"FLUSH PRIVILEGES;"
            comm = comm1 + "\n" + comm2 + "\n" + comm3
            cursor = conn.cursor()
            cursor.execute(comm) # eksekusi semua command yang diberikan kepada mysql yang berisi
                                # membuat user dan password, menambahkan privilege, akses perintah
            
            enkripsi = encrypt_decrypt(password, 3, characters=(string.ascii_lowercase + string.ascii_uppercase),
                            decrypt=False, shift_type="left") # enkripsi password
            Akun_Baru = [username, enkripsi] # pasangan username dan password
            with open('user.csv', mode='a', newline='') as csvfile: # membuka file csv 
                csvwriter = csv.writer(csvfile) # menulis file csv
                csvwriter.writerow(Akun_Baru) # menambahkan nilai
                showinfo(title='Info', message='Akun berhasil terdaftar!') # menampilkan pesan
        
    def onEnter(self, event): # jika tombol enter ditekan
        self.onClick()
        
    def back(self): # fungsi untuk ke window login (harusnya)
        self.destroy()
    
if __name__ == '__main__':
    app = AppRegister()
    app.mainloop()