# importing modules and files
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from Dictionary import translation_dict
from tkinter.messagebox import showinfo

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App():
    def __init__(self, window):
        super().__init__()
        # settingan awal window
        self.window = window
        self.window.geometry("750x450")
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
        
        # label untuk input
        self.label_input = ctk.CTkLabel(self.input_frame, 
                                        text='Masukkan Perintah: ', 
                                        font=self.font_body)
        self.label_input.pack(pady=10)
        
        # input
        self.perintah = ctk.StringVar()
        self.input = ctk.CTkEntry(self.input_frame, 
                                  placeholder_text='Masukkan Perintah', 
                                  textvariable=self.perintah, 
                                  font=self.font_body, 
                                  corner_radius=30)
        
        self.input.pack(pady=(0, 10))
        
    # tombol
        # tombol masukan
        self.tombol_input = ctk.CTkButton(self.input_frame, 
                                          text='Submit', 
                                          command=self.onClick, 
                                          font=self.font_body, 
                                          corner_radius=30)
        self.tombol_input.pack(pady=(0, 10), expand=True)
        
        # tombol bantuan
        self.tombol_bantuan = ctk.CTkButton(self.input_frame,
                                            text='Butuh Bantuan?',
                                            font=self.font_body,
                                            corner_radius=30)
        self.tombol_bantuan.pack(pady=(0, 10), expand=True)
        
    # komponen tabel
        self.columns = ('first_name', 'last_name', 'email')
        self.tree = ttk.Treeview(self.frame_table,
                                columns=self.columns,
                                show='headings',
                                padding=(10, 10))
        
        # mendefinisikan heading
        self.tree.heading('first_name', text='First Name')
        self.tree.heading('last_name', text='Last Name')
        self.tree.heading('email', text='Email')
        
        # data dummy
        self.contacts = []
        for n in range(1, 100):
            self.contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
        
        # menambahkan data ke treeview
        for contact in self.contacts:
            self.tree.insert('', tk.END, values=contact)
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        
        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self.window, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        
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
        
    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))
        
    # logika pada tombol
    def onClick(self):
        text = self.perintah.get()
        text = text.upper()
        translated = self.translate(text)
        print(translated)
        
    def onEnter(self, event):
        self.onClick()
        
    def translate(self, text):
        for key, value in translation_dict.items():
            text = text.replace(key, value)
        return text

if __name__ == '__main__':
    window = ctk.CTk()
    app = App(window)
    window.mainloop()