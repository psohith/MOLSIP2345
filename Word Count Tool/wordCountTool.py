import tkinter as tk
from tkinter import filedialog

def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Count words, characters, and lines
            word_count = len(content.split())
            char_count = len(content)
            line_count = content.count('\n') + 1

            result_label.config(text=f"Words: {word_count}, Characters: {char_count}, Lines: {line_count}")

    except FileNotFoundError:
        result_label.config(text=f"Error: File not found at '{file_path}'")

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)
        count_words(file_path)

# Create the main window
window = tk.Tk()
window.title("Word Count Application")

# Create and configure widgets
file_path_entry = tk.Entry(window, width=40)
select_file_button = tk.Button(window, text="Select File", command=open_file_dialog)
result_label = tk.Label(window, text="")

# Grid layout
file_path_entry.grid(row=0, column=0, padx=10, pady=10)
select_file_button.grid(row=0, column=1, padx=10, pady=10)
result_label.grid(row=1, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
window.mainloop()
