import tkinter as tk
import os
import shutil
from tkinter import filedialog


def move_files():
    source_path = source_entry.get()
    destination_path = destination_entry.get()
    extensions = [ext.strip() for ext in extensions_entry.get().split(',')]
    
    for root, _, files in os.walk(source_path, topdown=False):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                shutil.move(os.path.join(root, file), os.path.join(destination_path, file))

    for root, dirs, _ in os.walk(source_path, topdown=False):
        for dir in dirs:
            folder_path = os.path.join(root, dir)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)

    result_label.config(text="Files have been moved successfully!", fg="green")

def browse_source():
    folder_selected = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, folder_selected)

def browse_destination():
    folder_selected = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, folder_selected)

root = tk.Tk()
root.title("File Mover")
root.geometry("600x525")
root.config(bg="#f7f7f7")
root.resizable(False, False)

header_label = tk.Label(root, text="File Mover", font=("Helvetica", 18, "bold"), bg="#f7f7f7", fg="#333")
header_label.pack(pady=20)

source_label = tk.Label(root, text="Source Directory", font=("Helvetica", 12, "bold"), bg="#f7f7f7", fg="#333")
source_label.pack(pady=5)
source_entry = tk.Entry(root, width=40, font=("Helvetica", 12, "bold"), borderwidth=2, relief="solid", bd=2)
source_entry.pack(pady=10)
source_button = tk.Button(root, text="Browse", command=browse_source, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=2)
source_button.pack(pady=10)

destination_label = tk.Label(root, text="Destination Directory", font=("Helvetica", 12, "bold"), bg="#f7f7f7", fg="#333")
destination_label.pack(pady=5)
destination_entry = tk.Entry(root, width=40, font=("Helvetica", 12, "bold"), borderwidth=2, relief="solid", bd=2)
destination_entry.pack(pady=10)
destination_button = tk.Button(root, text="Browse", command=browse_destination, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=2)
destination_button.pack(pady=10)

extensions_label = tk.Label(root, text="Enter Extensions (comma separated)", font=("Helvetica", 12, "bold"), bg="#f7f7f7", fg="#333")
extensions_label.pack(pady=5)
extensions_entry = tk.Entry(root, width=40, font=("Helvetica", 12, "bold"), borderwidth=2, relief="solid", bd=2)
extensions_entry.pack(pady=10)
extensions_entry.insert(0, ".package, .ts4script") # Default extensions

start_button = tk.Button(root, text="Move Files", command=move_files, bg="#2196F3", fg="white", font=("Helvetica", 14, "bold"), relief="raised", bd=2)
start_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"), bg="#f7f7f7", fg="red")
result_label.pack(pady=5)

root.mainloop()
