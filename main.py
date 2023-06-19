from tkinter import *
# from PIL import ImageTk, Image

from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import Crypto

window = Tk()
window.title("Sectert notes")
window.minsize(width=400, height=750)

# Input string to be encrypted (padding to adjust length)
input_string = "Hello World!".rjust(32)
# Secret key (pw)
key = b'1234567890123456'
# Encrypt the string
cipher = Crypto.Cipher.AES.new(key)
encrypted_string = cipher.encrypt(input_string.encode())
# Decrypt the encrypted string
decrypted_string = cipher.decrypt(encrypted_string)
# Print the original and decrypted strings
print("Original String:", input_string)
print("Decrypted String:", decrypted_string.decode())




title_text = Label(text="Enter your title", font=('Arial', 16, "normal"))
title_text.config(padx=20, pady=20)
title_text.pack()

title_enter = Entry(width=30)
title_enter.focus()
title_enter.pack()

secret_text = Label(text="Enter your secret", font=('Arial', 16, "normal"))
secret_text.config(padx=20, pady=20)
secret_text.pack()

secret_enter = Text(width=22, height=10)
secret_enter.pack()

key_text = Label(text="Enter your key", font=('Arial', 16, "normal"))
key_text.config(padx=20, pady=20)
key_text.pack()

key_enter = Entry(width=30)
key_enter.pack()


def save_encrypt():
    title = title_enter.get()
    textarea = secret_enter.get("1.0", END)
    key_info = key_enter.get()

    if (textarea.strip() == "" or title.strip() == "" or key_info.strip() == ""):
        showwarning(title="Error", message="Please enter all information")


    my_file = open("Secret note.txt", "a+")
    my_file.write(title)
    my_file.write('\n')
    my_file.write(textarea)
    my_file.write('\n')
    my_file.close()
    print('done')


def decrypt():
    textarea = secret_enter.get("1.0", END)



save_button = Button(text="Save & Encrypt", command=save_encrypt)
save_button.pack()

decrypt_button = Button(text="Decrypt", command=decrypt)
decrypt_button.pack()

window.mainloop()
