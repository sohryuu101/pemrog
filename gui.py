import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
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
        
        # frame input
        self.input_frame = ctk.CTkFrame(window)
        # self.input_frame.pack(padx=10, pady=40, fill='both', expand=True, side='top')  
        self.input_frame.pack()  
        
    # komponen-komponen
        # font
        self.font_header = ctk.CTkFont(family='Consolas', size=20)
        self.font_body = ctk.CTkFont(family='Consolas', size=10)
        
        #label untuk welcoming
        self.label_welcome = ctk.CTkLabel(self.input_frame, 
                                          text='Selamat Datang di SQL Mockup!', 
                                          font=self.font_header)
        # self.label_welcome.pack(padx=10, pady=0, expand=True)
        self.label_welcome.pack()
        
        # label untuk input
        self.label_input = ctk.CTkLabel(self.input_frame, 
                                        text='Masukkan Perintah: ', 
                                        font=self.font_body)
        # self.label_input.pack(padx=(200, 0), side='left')
        self.label_input.pack()
        
        # input
        self.perintah = ctk.StringVar()
        self.input = ctk.CTkEntry(self.input_frame, 
                                  placeholder_text='Masukkan Perintah', 
                                  textvariable=self.perintah, 
                                  font=self.font_body, 
                                  corner_radius=30)
        
        # self.input.pack(padx=(10, 0), pady=0, side='left')
        self.input.pack()
        
        # tombol
        self.tombol_input = ctk.CTkButton(self.input_frame, 
                                          text='Submit', 
                                          command=self.onClick, 
                                          font=self.font_body, corner_radius=30)
        self.tombol_input.pack(expand=True)
        self.window.bind('<Return>', self.onEnter)
        
    # komponen tabel
        self.columns = ('first_name', 'last_name', 'email')
        self.tree = ttk.Treeview(self.input_frame, columns=self.columns, show='headings')
        
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
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
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
        print(self.perintah.get())
        
    def onEnter(self, event):
        self.onClick()

if __name__ == '__main__':
    window = ctk.CTk()
    app = App(window)
    window.mainloop()