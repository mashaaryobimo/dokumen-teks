import os
import hashlib
import tkinter as tk
from tkinter import messagebox

class Document:
    def __init__(self, filename):
        self.filename = filename
        self.content = None
        self.root = tk.Tk()
        self.root.title(f"Dokumen: {self.filename}")

        # Menambahkan opsi pilihan hash function
        self.hash_function = tk.StringVar(self.root)
        self.hash_function.set("SHA-256") # opsi default
        self.hash_options = tk.OptionMenu(self.root, self.hash_function, "SHA-256", "MD5", "SHA-1")
        self.hash_options.pack()

        self.text = tk.Text(self.root)
        self.text.pack()
        
         # Membuat tombol Hash
        self.hash_button = tk.Button(self.root, text="Hash", command=self.calculate_hash)
        self.hash_button.pack()

    def read(self):
        with open(self.filename, 'r') as file:
            self.content = file.read()
            self.text.insert('1.0', self.content)

    def write(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)

    def size(self):
        return os.path.getsize(self.filename)
    
    def calculate_hash(self):
        content = self.text.get('1.0', 'end')
        hash_function = self.hash_function.get()
        if hash_function == "SHA-256":
            hash = hashlib.sha256(content.encode()).hexdigest()
        elif hash_function == "MD5":
            hash = hashlib.md5(content.encode()).hexdigest()
        elif hash_function == "SHA-1":
            hash = hashlib.sha1(content.encode()).hexdigest()
        messagebox.showinfo(title="Hash", message=f"Hash dari dokumen: {hash}")

# Contoh penggunaan kelas
doc = Document('Tiriz.txt')
doc.read()
doc.root.mainloop()