import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#1.name, 2.height, 3.phone_number, 4.operator
def register():
    def validate_register():
        with open("Register_file.txt", "r", encoding="utf-8") as f:
            data = f.readlines()
            logins = data[0][0:-1]
            passwords = data[1]
        userid = username_entry.get()
        password = password_entry.get()
        password_check = password_check_entry.get()
        if userid in logins:
            messagebox.showerror("Register Failed!", "This username is already taken!")
        else:
            logins += "," + userid
            passwords += "," + password
            if len(password) < 3 and len(password_check) < 3:
                messagebox.showerror("Register Failed!", "Password need to be longer than 3 symbols!")

            elif password == password_check:
                messagebox.showinfo("Register Succesful!",f"Now login, {userid}")
                with open("Register_file.txt",'w',encoding="utf-8") as f:
                    f.write(logins + "\n" + passwords)
                register_window.destroy()



            else:
                messagebox.showerror("Register Failed!", "Passwords don't matches")





    register_window = Tk()
    register_window.title("Register window")
    username_label = ttk.Label(register_window, text="Userid:")
    username_label.pack()

    username_entry = ttk.Entry(register_window)
    username_entry.pack()

    password_label = ttk.Label(register_window, text="Password:")
    password_label.pack()

    password_entry = ttk.Entry(register_window, show="*")
    password_entry.pack()

    password_check_label = ttk.Label(register_window, text="Password check:")
    password_check_label.pack()

    password_check_entry = ttk.Entry(register_window, show ="*")
    password_check_entry.pack()

    register_button = ttk.Button(register_window,text="Register",command=validate_register)
    register_button.pack()

    register_window.mainloop()


def validate_login(admin_login = 'admin',admin_password = 'admin',user_login = 'user',user_password = 'user'):
    userid = username_entry.get()
    password = password_entry.get()
    with open("Register_file.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
        logins = data[0][0:-1].split(',')
        passwords = data[1].split(',')

    if userid == admin_login and password == admin_password:
        messagebox.showinfo("Login Successful", f"Welcome, {userid}!")
        parent.destroy()
        menu_super_admin()
    elif userid == user_login and password == user_password:
        messagebox.showinfo("Login Successful", f"Welcome, {userid}")
        parent.destroy()
        menu_user()
    elif userid in logins and password == passwords[logins.index(userid)]:
        messagebox.showinfo("Login Successful", f"Welcome, {userid}")
        parent.destroy()
        with open("admin.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        if userid in lines:
            menu_admin()
        else:
            menu_user()

    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
def menu_super_admin():
    def exit():
        root.destroy()
        sys.exit()
    root = Tk()
    root.title("Data Base Management System(superadmin-side)")
    root.geometry("400x300")
    btn_open = ttk.Button(text="Open", command=open_a_file)
    btn_write = ttk.Button(text="Write", command=writer)
    btn_remove = ttk.Button(text="Remove",command=remover)
    btn_find = ttk.Button(text="Find",command=finder)
    btn_twokeys_find = ttk.Button(text="Find(2keys)", command=two_keys_finder)
    btn_add_admin = ttk.Button(text="Add Admin", command=add_admin)
    btn_delete_admin = ttk.Button(text="Delete Admin", command=delete_admin)
    btn_exit = ttk.Button(text="Exit",command=exit)
    btn_names = (btn_open,btn_write,btn_remove,btn_find,btn_twokeys_find,btn_add_admin,btn_delete_admin,btn_exit)
    for i in btn_names:
        i.pack()
    root.mainloop()
def menu_admin():
    def exit():
        root.destroy()
        sys.exit()
    root = Tk()
    root.title("Data Base Management System(admin-side)")
    root.geometry("400x300")
    btn_open = ttk.Button(text="Open", command=open_a_file)
    btn_write = ttk.Button(text="Write", command=writer)
    btn_remove = ttk.Button(text="Remove",command=remover)
    btn_find = ttk.Button(text="Find",command=finder)
    btn_twokeys_find = ttk.Button(text="Find(2keys)", command=two_keys_finder)
    btn_exit = ttk.Button(text="Exit",command=exit)
    btn_names = (btn_open,btn_write,btn_remove,btn_find,btn_twokeys_find,btn_exit)
    for i in btn_names:
        i.pack()
    root.mainloop()
def menu_user():
    def exit():
        root.destroy()
        sys.exit()
    root = Tk()
    root.title("Data Base Management System(client-side)")
    root.geometry("400x300")
    btn_open = ttk.Button(text="Open", command=open_a_file)
    btn_exit = ttk.Button(text="Exit",command=exit)
    btn_names = (btn_open,btn_exit)
    for i in btn_names:
        i.pack()
    root.mainloop()

def open_a_file():
    os.system(r"DB.txt")
def finder():
    def exit():
        finding.destroy()
    def finding_func():
        result = ''
        with open('DB.txt', 'r', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if finding_entry.get().isalnum() == False:
                    messagebox.showerror("Error","Wrong input!")
                    break
                elif finding_entry.get() in line:
                    result += line
            if result == "":
                return None
            else:
                messagebox.showinfo("Success!", f"Result:\n{result}")
    finding = Tk()
    finding.title("Finding Field")

    finding_label = ttk.Label(finding, text="Your entry:\n"
                                            "Form: 1.name or 2.height or 3.phone_number or 4.operator", )
    finding_label.pack()

    finding_entry = ttk.Entry(finding)
    finding_entry.pack()

    finding_button = ttk.Button(finding, text ="Enter", command=finding_func)
    finding_button.pack()

    finding_exit_button = ttk.Button(finding, text ="Exit", command=exit)
    finding_exit_button.pack()

    finding.mainloop()

def two_keys_finder():
    def exit():
        finding.destroy()
    def finding_func():
        result = ''
        with open('DB.txt', 'r', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if finding_entry1.get().isalnum() == False or finding_entry2.get().isalnum() == False:
                    messagebox.showerror("Error","Wrong input!")
                    break
                elif finding_entry1.get() in line or finding_entry2.get() in line:
                    result += line
            if result == "":
                return None
            else:
                messagebox.showinfo("Success!", f"Result:\n{result}")

    finding = Tk()
    finding.title("Finding Field")

    finding_label = ttk.Label(finding, text="Your entry:\n"
                                            "Form: 1.name or 2.height or 3.phone_number or 4.operator", )
    finding_label.pack()

    finding_entry1 = ttk.Entry(finding)
    finding_entry1.pack()
    finding_entry2 = ttk.Entry(finding)
    finding_entry2.pack()

    finding_button = ttk.Button(finding, text ="Enter", command=finding_func)
    finding_button.pack()

    finding_exit_button = ttk.Button(finding, text ="Exit", command=exit)
    finding_exit_button.pack()

    finding.mainloop()

def remover():
    def exit():
        removing.destroy()
    def removing_func():

        with open('DB.txt', 'r', encoding="utf-8") as f:
            lines = f.readlines()
        with open('DB.txt', 'w', encoding="utf-8") as f:
            if removing_entry.get().isalnum() == False:
                messagebox.showerror("Error", "Wrong input!")
                for line in lines:
                    f.writelines(line)
            else:
                for line in lines:
                    if removing_entry.get() not in line:
                            f.writelines(line)

    removing = Tk()
    removing.title("Remover Field")

    removing_label = ttk.Label(removing, text="Your entry:\n"
                                            "Form: 1.name or 2.height or 3.phone_number or 4.operator", )
    removing_label.pack()

    removing_entry = ttk.Entry(removing)
    removing_entry.pack()

    removing_button = ttk.Button(removing, text ="Enter", command=removing_func)
    removing_button.pack()

    remover_exit_button = ttk.Button(removing, text ="Exit", command=exit)
    remover_exit_button.pack()

    removing.mainloop()
def writer():
    def exit():
        writing.destroy()
    def writing_func():
        with open('DB.txt', 'a', encoding="utf-8") as f:
            f.write("\n" + writing_entry.get())



    writing = Tk()
    writing.title("Writing Field")

    writing_label = ttk.Label(writing, text="Your entry:\n"
                                            "Form: 1.name, 2.height, 3.phone_number, 4.operator",)
    writing_label.pack()

    writing_entry = ttk.Entry(writing)
    writing_entry.pack()

    writing_button = ttk.Button(writing, text = "Enter",command=writing_func)
    writing_button.pack()

    writing_exit_button = ttk.Button(writing,text = "Exit",command=exit)
    writing_exit_button.pack()

    writing.mainloop()
def add_admin():
    def exit():
        add_admin.destroy()
    def add():
        with open("Register_file.txt", "r", encoding="utf-8") as f:
            data = f.readlines()
            logins = data[0][0:-1].split(',')
            passwords = data[1].split(',')
        with open("admin.txt", "r", encoding="utf-8") as f:
            admins = f.readlines()
        if add_admin_entry.get() in admins:
            messagebox.showerror("Fail!", f"{add_admin_entry.get()} is already an admin!")
        else:
            if add_admin_entry.get() in logins:
                with open("admin.txt", "a", encoding="utf-8") as f:
                    f.writelines("\n"+ add_admin_entry.get())
                    messagebox.showinfo("Success!",f"{add_admin_entry.get()} now admin!")
            else:
                messagebox.showerror("Fail!", "Invalid username!")


    add_admin = Tk()
    add_admin.title("Adding Admin")

    add_admin_label = ttk.Label(add_admin,text="Userid:")
    add_admin_label.pack()

    add_admin_entry = ttk.Entry(add_admin)
    add_admin_entry.pack()

    add_admin_button = ttk.Button(add_admin, text = "Enter",command=add)
    add_admin_button.pack()

    add_admin_exit_button = ttk.Button(add_admin, text="Exit", command=exit)
    add_admin_exit_button.pack()

    add_admin.mainloop()


def delete_admin():
    def exit():
        delete_admin.destroy()

    def delete():
        with open("admin.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open("Register_file.txt", "r", encoding="utf-8") as f:
            data = f.readlines()
            logins = data[0][0:-1].split(',')
            passwords = data[1].split(',')
        if delete_admin_entry.get() not in lines:
            messagebox.showerror("Fail!", f"{delete_admin_entry.get()} is not found!")
        else:
            if delete_admin_entry.get() in logins:
                with open("admin.txt", "w", encoding="utf-8") as f:
                    for line in lines:
                        if delete_admin_entry.get() not in line:
                                f.writelines(line)
                    messagebox.showinfo("Success!", f"{delete_admin_entry.get()} is not longer admin!")
            else:
                messagebox.showerror("Fail!", "Invalid username!")

    delete_admin = Tk()
    delete_admin.title("Adding Admin")

    delete_admin_label = ttk.Label(delete_admin, text="Userid:")
    delete_admin_label.pack()

    delete_admin_entry = ttk.Entry(delete_admin)
    delete_admin_entry.pack()

    delete_admin_button = ttk.Button(delete_admin, text="Enter", command=delete)
    delete_admin_button.pack()

    delete_admin_exit_button = ttk.Button(delete_admin, text="Exit", command=exit)
    delete_admin_exit_button.pack()

    delete_admin.mainloop()

parent = Tk()
parent.title("Login Form")

username_label = ttk.Label(parent, text="Userid:")
username_label.pack()

username_entry = ttk.Entry(parent)
username_entry.pack()

password_label = ttk.Label(parent, text="Password:")
password_label.pack()

password_entry = ttk.Entry(parent, show="*")
password_entry.pack()

login_button = ttk.Button(parent, text="Login", command=validate_login)
login_button.pack()

register_button = ttk.Button(parent, text="Register",command=register)
register_button.pack()

parent.mainloop()