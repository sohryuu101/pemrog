# importing modules and files
import customtkinter as ctk
import csv
import string
from tkinter.messagebox import showinfo, showwarning
##################################################
# set tema dark
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class AppRegister(ctk.CTk):
    def __init__(self):
        super().__init__()
        # settingan awal 
        self.geometry("750x450")
        self.title("SQL Python GUI")
        self.bind('<Return>', self.onEnter)
        
        # frame register
        self.register_frame = ctk.CTkFrame(self)
        self.register_frame.pack(fill='both', expand=True)  
        
    # komponen-komponen
        # font
        self.font_header = ctk.CTkFont(family='Consolas', size=20)
        self.font_body = ctk.CTkFont(family='Consolas', size=10)
        
        #label untuk welcoming
        self.label_welcome = ctk.CTkLabel(master=self.register_frame, 
                                          text='Buat akun baru!', 
                                          font=self.font_header)
        self.label_welcome.pack(pady=10)
        
        # label untuk username
        self.label_input_username = ctk.CTkLabel(master=self.register_frame, 
                                        text='Masukkan username baru: ', 
                                        font=self.font_body)
        self.label_input_username.pack(pady=(0, 10))
        
        # input username
        self.username = ctk.StringVar()
        self.input_username = ctk.CTkEntry(master=self.register_frame, placeholder_text='Username',
                                  textvariable=self.username, 
                                  font=self.font_body, 
                                  corner_radius=30)
        self.input_username.pack(pady=(0, 10))
        
        # label untuk pass
        self.label_input_password = ctk.CTkLabel(master=self.register_frame, 
                                        text='Masukkan password baru: ', 
                                        font=self.font_body)
        self.label_input_password.pack(pady=(0, 10))
        
        # input password
        self.password = ctk.StringVar()
        self.input_password = ctk.CTkEntry(master=self.register_frame, placeholder_text='Password', 
                                  textvariable=self.password,
                                  show= '*', 
                                  font=self.font_body, 
                                  corner_radius=30)
        self.input_password.pack(pady=(0, 10))
        
    # tombol
        # tombol masukan
        self.tombol_input = ctk.CTkButton(master=self.register_frame, 
                                          text='Kirim', 
                                          command=self.onClick, 
                                          font=self.font_body, 
                                          corner_radius=30)
        self.tombol_input.pack(pady=10)
        
    # logika pada tombol
    def onClick(self):
        username = self.username.get()
        password = self.password.get()   
        
        if username or password == "":
            showwarning(title='Error', message='Username dan password tidak boleh kosong!')                   
        
        with open('user.csv', mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if username in lines[0]:
                    showwarning(title='Error', message='Username sudah digunakan!')
                
                else:
                    enkripsi = self.encrypt_decrypt(password, 3, characters=(string.ascii_lowercase + string.ascii_uppercase),
                                    decrypt=False, shift_type="left")
                    Akun_Baru = [username, enkripsi]
                    with open('user.csv', 'a') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerow(Akun_Baru)
                        showinfo(title='Info', message='Akun berhasil terdaftar!')
                        
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

        
    def onEnter(self, event):
        self.onClick()
    
if __name__ == '__main__':
    app = AppRegister()
    app.mainloop()