import tkinter as tk
from tkinter import messagebox, filedialog

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def process_message():
    text = text_entry.get("1.0", "end-1c")
    shift = shift_entry.get()
    mode = mode_var.get()

    if not text or not shift:
        messagebox.showwarning("Input Error", "Please enter both a message and a shift value.")
        return

    try:
        shift = int(shift)
    except ValueError:
        messagebox.showerror("Input Error", "Shift value must be an integer.")
        return

    result = caesar_cipher(text, shift, mode)
    result_label.config(text=f"Result: {result}", fg="#00cec9", font=("Arial", 14, "bold"))

def save_result():
    result_text = result_label.cget("text").replace("Result: ", "")
    if not result_text:
        messagebox.showwarning("No Result", "There is no result to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(result_text)
        messagebox.showinfo("Saved", "The result has been saved successfully.")

# Set up the main window
window = tk.Tk()
window.title("Caesar Cipher")
window.configure(bg="#2d3436")

def on_enter(e):
    e.widget.config(bg="#55efc4", fg="#2d3436")

def on_leave(e):
    e.widget.config(bg="#00b894", fg="#2d3436")

def on_save_enter(e):
    e.widget.config(bg="#74b9ff", fg="#2d3436")

def on_save_leave(e):
    e.widget.config(bg="#0984e3", fg="#2d3436")

# Create and place the components
header_label = tk.Label(window, text="Caesar Cipher Encryption & Decryption", font=("Arial", 16, "bold"), bg="#2d3436", fg="#dfe6e9")
header_label.grid(row=0, column=0, columnspan=3, pady=20)

tk.Label(window, text="Enter your message:", font=("Arial", 12), bg="#2d3436", fg="#dfe6e9").grid(row=1, column=0, padx=10, pady=10, sticky="e")
text_entry = tk.Text(window, height=5, width=40, font=("Arial", 12), bg="#636e72", fg="#dfe6e9", insertbackground="#dfe6e9")
text_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

tk.Label(window, text="Enter shift value:", font=("Arial", 12), bg="#2d3436", fg="#dfe6e9").grid(row=2, column=0, padx=10, pady=10, sticky="e")
shift_entry = tk.Entry(window, font=("Arial", 12), bg="#636e72", fg="#dfe6e9", insertbackground="#dfe6e9")
shift_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w", columnspan=2)

mode_var = tk.StringVar(value="encrypt")
encrypt_radio = tk.Radiobutton(window, text="Encrypt", variable=mode_var, value="encrypt", font=("Arial", 12), bg="#2d3436", fg="#dfe6e9", selectcolor="#00b894", activebackground="#2d3436")
encrypt_radio.grid(row=3, column=0, padx=10, pady=10, sticky="e")

decrypt_radio = tk.Radiobutton(window, text="Decrypt", variable=mode_var, value="decrypt", font=("Arial", 12), bg="#2d3436", fg="#dfe6e9", selectcolor="#d63031", activebackground="#2d3436")
decrypt_radio.grid(row=3, column=1, padx=10, pady=10, sticky="w", columnspan=2)

process_button = tk.Button(window, text="Process", command=process_message, font=("Arial", 14), bg="#00b894", fg="#2d3436", activebackground="#55efc4", activeforeground="#2d3436", relief="flat", padx=20, pady=10, bd=0)
process_button.grid(row=4, column=0, padx=10, pady=20)

save_button = tk.Button(window, text="Save Result", command=save_result, font=("Arial", 14), bg="#0984e3", fg="#2d3436", activebackground="#74b9ff", activeforeground="#2d3436", relief="flat", padx=20, pady=10, bd=0)
save_button.grid(row=4, column=1, padx=10, pady=20, columnspan=2)

# Add hover effects to buttons
process_button.bind("<Enter>", on_enter)
process_button.bind("<Leave>", on_leave)

save_button.bind("<Enter>", on_save_enter)
save_button.bind("<Leave>", on_save_leave)

result_label = tk.Label(window, text="Result:", font=("Arial", 14), bg="#2d3436", fg="#dfe6e9")
result_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Run the application
window.mainloop()
