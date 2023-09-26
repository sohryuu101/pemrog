from gui_login_final import AppLogin
from gui_sql_final import AppSQL
from gui_register_final import AppRegister

if __name__ == '__main__':
    app = AppLogin()
    app.mainloop()
    
    if app.onClick() == True:
        uname = app.onClick[1]
        pwd = app.onClick[2]
        print(uname, pwd)
        # app2 = AppSQL()
        # app2.mainloop()
    
    # app3 = AppRegister()
    # app3.mainloop()