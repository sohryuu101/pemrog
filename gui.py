import customtkinter as ctk

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
        self.input_frame.pack(padx=10, pady=40, fill='both', expand=True, side='top')  

    # komponen-komponen
        # font
        self.font_header = ctk.CTkFont(family='Consolas', size=20)
        self.font_body = ctk.CTkFont(family='Consolas', size=10)
        
        #label untuk welcoming
        self.label_welcome = ctk.CTkLabel(self.input_frame, 
                                          text='Selamat Datang di SQL Mockup!', 
                                          font=self.font_header)
        self.label_welcome.pack(padx=10, pady=0, expand=True)
        # self.label_welcome.pack()
        
        # label untuk input
        self.label_input = ctk.CTkLabel(self.input_frame, 
                                        text='Masukkan Perintah: ', 
                                        font=self.font_body)
        self.label_input.pack(padx=(200, 0), side='left')
        
        # input
        self.perintah = ctk.StringVar()
        self.input = ctk.CTkEntry(self.input_frame, 
                                  placeholder_text='Masukkan Perintah', 
                                  textvariable=self.perintah, 
                                  font=self.font_body, 
                                  corner_radius=30)
        
        self.input.pack(padx=(10, 0), pady=0, side='left')

        # tombol
        self.tombol_input = ctk.CTkButton(self.input_frame, 
                                          text='Submit', 
                                          command=self.onClick, 
                                          font=self.font_body, corner_radius=30)
        self.tombol_input.pack(expand=True)
        self.window.bind('<Return>', self.onEnter)
        
    # logika pada tombol
    def onClick(self):
        print(self.perintah.get())
        
    def onEnter(self, event):
        self.onClick()

if __name__ == '__main__':
    window = ctk.CTk()
    app = App(window)
    window.mainloop()