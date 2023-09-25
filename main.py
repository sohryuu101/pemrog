from gui_login import AppLogin
from gui_sql import AppSQL
import customtkinter as ctk

if __name__ == '__main__':
    window = ctk.CTk()
    app_login = AppLogin(window)
    window.mainloop()
    
    if app_login.onClick() == True:
        app_sql = AppSQL(window)
