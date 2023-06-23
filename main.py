from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
from cryptography.fernet import Fernet
import base64

window = Tk()
window.title("Sectert notes")
window.minsize(width=400, height=750)

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
    else:
        text_decrypt = str(encryptText(textarea))
        my_file = open("Secret note.txt", "a+")
        my_file.write(title)
        my_file.write('\n')
        my_file.write(text_decrypt)
        my_file.write('\n')
        my_file.close()


def decrypt():
    message = secret_enter.get("1.0", END)
    key = b'my_key_here'
    if len(key) < 32:
        key = key + b'=' * (32 - len(key))

    encoded_key = base64.urlsafe_b64encode(key)
    fernet = Fernet(encoded_key)
    decrypted_message = fernet.decrypt(message.encode()).decode()
    print(decrypted_message)

def encryptText(message):
    key = b'my_key_here'
    if len(key) < 32:
        key = key + b'=' * (32 - len(key))

    encoded_key = base64.urlsafe_b64encode(key)
    fernet = Fernet(encoded_key)
    return fernet.encrypt(message.encode())


save_button = Button(text="Save & Encrypt", command=save_encrypt)
save_button.pack()

decrypt_button = Button(text="Decrypt", command=decrypt)
decrypt_button.pack()

window.mainloop()
