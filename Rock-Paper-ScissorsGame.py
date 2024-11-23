import tkinter as tk
from tkinter import messagebox
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Global variables for score
user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score

    # Computer's choice
    computer_choice = random.choice(choices)

    # Determine the result
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    # Update the result and score display
    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\nResult: {result}")
    score_label.config(text=f"User: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your choice to start the game!")
    score_label.config(text="User: 0 | Computer: 0")

# Create the main application window
app = tk.Tk()
app.title("Rock-Paper-Scissors Game")
app.geometry("880x600")
app.config(bg="#1a1a2e")  # Background color

# Title
title_label = tk.Label(app, text="Rock-Paper-Scissors", font=("Arial", 36, "bold"), bg="#1a1a2e", fg="#e94560")
title_label.pack(pady=10)

# Result display
result_label = tk.Label(app, text="Make your choice to start the game!", font=("Arial", 28), bg="#1a1a2e", fg="#ffffff", wraplength=350, justify="center")
result_label.pack(pady=20)

# Buttons for choices
button_frame = tk.Frame(app, bg="#1a1a2e")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 28), bg="#0f3460", fg="#ffffff", command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 28), bg="#16213e", fg="#ffffff", command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 28), bg="#53354a", fg="#ffffff", command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Score display
score_label = tk.Label(app, text = "User: 0 | Computer: 0", font=("Arial", 28), bg="#1a1a2e", fg="#f4f4f4")
score_label.pack(pady=10)

# Reset Button
reset_button = tk.Button(app, text="Reset Game", font=("Arial", 28), bg="#e94560", fg="#ffffff", command=reset_game)
reset_button.pack(pady=10)

# Footer
footer_label = tk.Label(app, text="Developed by Shahid", font=("Arial", 28), bg="#1a1a2e", fg="#e94560")
footer_label.pack(side="bottom", pady=10)

# Run the application
app.mainloop()
