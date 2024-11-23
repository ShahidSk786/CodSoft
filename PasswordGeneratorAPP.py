import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4!")
            return
        
        # Define character pools
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation
        
        # Combine all characters
        all_characters = lower + upper + digits + special
        
        # Ensure the password includes at least one character from each pool
        password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(special)
        
        # Fill the rest of the password with random choices
        password += ''.join(random.choices(all_characters, k=length - 4))
        
        # Shuffle the password to avoid predictable patterns
        password = ''.join(random.sample(password, len(password)))
        
        # Display the password
        password_display.config(state='normal')
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
        password_display.config(state='readonly')
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Create the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("800x600")
app.config(bg="#34495e")

# Title Label
title_label = tk.Label(app, text="Password Generator", font=("Arial", 36, "bold"), bg="#34495e", fg="#ecf0f1")
title_label.pack(pady=10)

# Length Input
length_label = tk.Label(app, text="Enter Password Length:", font=("Arial", 28), bg="#34495e", fg="#ecf0f1")
length_label.pack(pady=5)

length_entry = tk.Entry(app, font=("Arial", 28),justify="center")
length_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(app, text="Generate Password", font=("Arial", 28, "bold"), bg="#2ecc71", fg="white", command=generate_password)
generate_button.pack(pady=10)

# Password Display
password_display = tk.Entry(app, font=("Arial", 28), state="readonly", justify="center")
password_display.pack(pady=10)

# Footer
footer_label = tk.Label(app, text="Developed by Shahid", font=("Arial", 10), bg="#34495e", fg="#bdc3c7")
footer_label.pack(side="bottom", pady=10)

# Run the application
app.mainloop()
