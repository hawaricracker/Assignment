import tkinter as tk
import tkinter.messagebox as messagebox

class Credensial:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"Username: {self.username}, Password: {self.password}"
    
    def login(self, username, password):
        return self.username == username and self.password == password
        
login = Credensial("admin", "admin123")

def check_login():
    if login.login(username.get(), password.get()):
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Login Failed")

window = tk.Tk()
window.title("Login")
window.geometry("300x200")

tk.Label(window, text="Username").grid(row=1, padx=20)
tk.Label(window, text="Password").grid(row=2)
username = tk.Entry(window)
username.grid(row=1, column=1, pady=20, padx=20)
password = tk.Entry(window, show="*")
password.grid(row=2, column=1)
button = tk.Button(window, text="Login", command=check_login) 
button.grid(row=3, columnspan=2, pady=20)

window.mainloop()
