# importing modules and files
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from Dictionary import translation_dict_root, translation_dict_user
from tkinter.messagebox import showinfo, showerror
import mysql.connector
import datetime
##################################################
# set tema dark
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class AppSQL(ctk.CTk): # membuat class AppSQL
    def __init__(self, uname='', pwd=''): # menerima parameter username dan password
        super().__init__()
        # settingan awal 
        # membuat koneksi dengan mysql
        self.conn = mysql.connector.connect(host='127.0.0.1', password=pwd, user=uname,database='pemrog') # konek ke mysql
        self.geometry("750x450") # ukuran layar
        self.title("SQL Python GUI") # judul
        self.bind('<Return>', self.onEnter) # binding tombol enter dengan fungsi onEnter
        self.uname = uname # username
        
        # frame input
        self.input_frame = ctk.CTkFrame(self) # inisiasi frame untuk input
        self.input_frame.pack(fill='both', expand=True)  # menampilkan frame
        
        # frame tabel
        self.frame_table = ctk.CTkFrame(self) # inisiasi frame untuk tabel
        self.frame_table.pack(fill='both', expand=True) # menampilkan frame
        
    # komponen-komponen
        # font
        self.font_header = ctk.CTkFont(family='Consolas', size=20) # font untuk header
        self.font_body = ctk.CTkFont(family='Consolas', size=10) # font untuk body
        
        #label untuk welcoming
        waktu = self.waktu() # waktu
        self.label_welcome = ctk.CTkLabel(self.input_frame, 
                                          text=f'Hai, Selamat {waktu} {uname}!', 
                                          font=self.font_header) # label untuk welcome berdasarkan nama user dan waktu
        self.label_welcome.pack(pady=10) # menampilkan label
        
        # label untuk input
        self.label_input = ctk.CTkLabel(self.input_frame, 
                                        text='Masukkan Perintah: ', 
                                        font=self.font_body) # label untuk input
        self.label_input.pack(pady=10) # menampilkan label
        
        # input
        self.perintah = ctk.StringVar() # variabel untuk input
        self.input = ctk.CTkEntry(self.input_frame, 
                                  placeholder_text='Masukkan Perintah',
                                  width=200, 
                                  textvariable=self.perintah, 
                                  font=self.font_body, 
                                  corner_radius=30) # entry box perintah
        
        self.input.pack(pady=(0, 10)) # menampilkan
        
    # tombol
        # tombol masukan
        self.tombol_input = ctk.CTkButton(self.input_frame, 
                                          text='Kirim', 
                                          command=self.onClick, 
                                          font=self.font_body, 
                                          corner_radius=30) # tombol kirim
        self.tombol_input.pack(pady=(0, 10)) # menampilkan
        
        # tombol bantuan
        self.tombol_bantuan = ctk.CTkButton(self.input_frame,
                                            text='Butuh Bantuan?',
                                            command=self.help,
                                            font=self.font_body,
                                            corner_radius=30) # tombol bantuan
        self.tombol_bantuan.pack(pady=(0, 10)) # menampilkan
        
    # komponen tabel
        self.columns = ('character_name', 'rarity', 'region', 'vision', 'weapon_type', 'model', 'constellation', 'birthday', 'special_dish', 'affiliation') # inisiase kolom tabel
        self.tree = ttk.Treeview(self.frame_table,
                                columns=self.columns,
                                show='headings',
                                padding=(10, 10)) # inisiasi tabel
        
        # mendefinisikan heading
        self.tree.heading('character_name', text='Nama Karakter')
        self.tree.heading('rarity', text='Rarity')
        self.tree.heading('region', text='Wilayah Asal')
        self.tree.heading('vision', text='Vision')
        self.tree.heading('weapon_type', text='Jenis Senjata')
        self.tree.heading('model', text='Model') 
        self.tree.heading('constellation', text='Constellation')
        self.tree.heading('birthday', text='Tanggal Lahir')
        self.tree.heading('special_dish', text='Makanan Spesial')
        self.tree.heading('affiliation', text='Afiliasi')
        
        # menambahkan scrollbar
        self.hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tree.xview) # scrollbar horizontal
        self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview) # scrollbar vertical
        self.tree.configure(yscroll=self.vscrollbar.set)
        self.tree.configure(xscroll=self.hscrollbar.set)
        # self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        # self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # menambahkan style pada tabel
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#212121",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#212121",
                        bordercolor="#212121",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        style.map("Treeview.Heading",
                    background=[('active', '#3484F0')])
        
        self.tree.pack()
        
    def item_selected(self, event): # fungsi jika item pada tabel dipilih
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
        
        if self.uname != 'root':
            if translated not in translation_dict_user:
                showerror(title='Error', message='Perintah tidak ditemukan')
                return
        
        cursor = self.conn.cursor()
        cursor.execute(translated)
        results = cursor.fetchall()
        
        for item in results:
            self.tree.insert('', tk.END, values=item)
        # self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        
    def help(self):
        if self.uname == 'root':
            showinfo(title='Help', message='List perintah yang dapat digunakan: \n' + '\n'.join(translation_dict_root))
        else:
            showinfo(title='Help', message='List perintah yang dapat digunakan: \n' + '\n'.join(translation_dict_user))

    def onEnter(self, event):
        self.onClick()
        
    def translate(self, text):
        for key, value in translation_dict_root.items():
            text = text.replace(key, value)
        return text
    
    def waktu(self):
        now = datetime.datetime.now()
        hour = now.hour
        
        if hour < 12:
            return "Pagi"
        elif hour < 18:
            return "Siang"
        else:
            return "Malam"

if __name__ == '__main__':
    app = AppSQL()
    app.mainloop()