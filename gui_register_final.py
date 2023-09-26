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
        
passuwodo = encrypt_decrypt('ollq', 3, characters=(string.ascii_lowercase + string.ascii_uppercase),
                                decrypt=True, shift_type="left")

conn = mysql.connector.connect(host='127.0.0.1', password=passuwodo, user='root',database='pemrog')

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
        
        # tombol kembali
        self.tombol_back = ctk.CTkButton(master=self.register_frame, 
                                          text='Kembali ke login', 
                                          command=self.back, 
                                          font=self.font_body, 
                                          corner_radius=30)
        self.tombol_back.pack(pady=10)
        
    # logika pada tombol
    def onClick(self):
        username = self.username.get()
        password = self.password.get()
        double = False    
        
        if username == "" or password == "":
            showwarning(title='Error', message='Username dan password tidak boleh kosong!')
            return
        
        with open('user.csv', mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if username in lines[0]:
                    showwarning(title='Error', message='Username sudah digunakan!')
                    double = True
                    break
                
        if double == False:
            comm1 = f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';"
            comm2 = f"GRANT PRIVILEGE ON pemrog.genshin TO '{username}'@'localhost';"
            comm3 = f"GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO '{username}'@'localhost' WITH GRANT OPTION;"
            comm4 = f"FLUSH PRIVILEGES;"
            comm5 = f"GRANT SELECT, INSERT, DELETE ON pemrog.* TO {username}@localhost;"
            comm = comm1 + "\n" + comm2 + "\n" + comm3 + "\n" + comm4 + "\n" + comm5
            cursor = conn.cursor()
            cursor.execute(comm)
            
            enkripsi = self.encrypt_decrypt(password, 3, characters=(string.ascii_lowercase + string.ascii_uppercase),
                            decrypt=False, shift_type="left")
            Akun_Baru = [username, enkripsi]
            with open('user.csv', mode='a', newline='') as csvfile:
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
        
    def back(self):
        self.destroy()
    
if __name__ == '__main__':
    app = AppRegister()
    app.mainloop()