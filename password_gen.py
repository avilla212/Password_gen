import secrets 

import tkinter as tk
from tkinter import filedialog

# creating our password gen function 
def password_gen(num_passwords):
    
    length = int(length_entry.get())
    num_passwords = int(num_pass_entry.get())
    
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    passwords = []

    if num_passwords > 15 or length > 60:
        password_label.config(text="Number of passwords can be no greater than 15 \n and the length can't be greater than 60   \U0001F60E")
        return
    
    elif num_passwords <= 0 or length <= 0:
        password_label.config(text="Did you forget to enter an amount for the length or the amount of passwords? \U0001F60E")
        return

    # creating our password for the amount of passwords we want
    for _ in range(num_passwords):
        password = ""
        # creating our password for the length we want
        for _ in range(length):
            # adding a random character to our password
            password += secrets.choice(chars)
        # adding our password to our list of passwords
        passwords.append(password)
    password_label.config(text=" \n".join(passwords))

# function to copy our generated password to our clipboard 
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_label.cget("text"))

def write_to_file():
    # user selects the file they want to write to
    file = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if file:
        file.write(password_label.cget("text"))
        file.close()
    else:
        return

        
# function to create our window
def create_window():
    global length_entry, password_label, root, num_pass_entry, file

    # creating our tk instance 
    root = tk.Tk() 
    root.title("Super cool password generator")
    root.geometry("600x500")

    # creating our label to enter the length of the password 
    length_label = tk.Label(root,text="Enter the length of the passwords (click beneath)", anchor="center")
    length_label.pack()

    length_entry = tk.Entry(root)
    length_entry.pack()
    length_entry.focus_set()
    
    # asking for number of passwords 
    num_pass_label = tk.Label(root,text="How many passwords would you like? \U0001F914",anchor="center")
    num_pass_label.pack(pady=10)

    num_pass_entry = tk.Entry(root)
    num_pass_entry.pack(pady=10)

    """
        - binding the return key so we dont have to hit generate password everytime 
            - we can simply hit return and it will call the password gen function
    """
    num_pass_entry.bind('<Return>', lambda event: password_gen(int(num_pass_entry.get())))
    length_entry.bind('<Return>', lambda event: password_gen(int(length_entry.get())))
    
    # button to copy the password into our clipboard
    copy_button = tk.Button(root,text="Copy passwords \U0001F60E",command=copy_password,anchor="center")
    copy_button.pack(pady=10)

    # creating our button to allow user to save their passwords to a file
    save_button = tk.Button(root,text="Save passwords to file",command=write_to_file,anchor="center")
    save_button.pack(pady=10)

    # where our password is showing up
    password_label = tk.Label(root,text="",anchor="center")
    password_label.pack(pady=10)

    # button to exit the program 
    exit_button = tk.Button(root,text="Exit",command=root.quit,anchor="center")
    exit_button.pack(pady=10)

    root.mainloop()

create_window()
