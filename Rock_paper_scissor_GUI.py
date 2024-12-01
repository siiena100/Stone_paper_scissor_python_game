import random
import tkinter as tk

# Original game variables
str = ["stone", "paper", "scissor"]
user_score = 0
com_score = 0

# Function to handle game logic
def play_game(user_input):
    global user_score, com_score

    winner_label["text"] = ""

    #Quit logic
    if user_input == "quit":
        result_label["text"] = "Game Over!"
        final_score_label["text"] = f"Final Scores:\nYou: {user_score}, Computer: {com_score}"
        if user_score > com_score:
            final_score_label["text"] += "\nCongratulations! You win the game!"
        elif user_score < com_score:
            final_score_label["text"] += "\nComputer wins the game.\nBetter luck next time!"
        else:
            final_score_label["text"] += "\nIt's a tie! Well played!"
        return
    #Computer choosing randoms
    com_input = random.choice(str)
    result_label["text"] = f"Computer chose: {com_input}"

    #Game Logic
    if user_input == "stone" and com_input == "paper":
        com_score += 1
        winner_label["text"] = "Computer wins"
    elif user_input == "stone" and com_input == "scissor":
        user_score += 1
        winner_label["text"] = "You win"
    elif user_input == "paper" and com_input == "scissor":
        com_score += 1
        winner_label["text"] = "Computer wins"
    elif user_input == "paper" and com_input == "stone":
        user_score += 1
        winner_label["text"] = "You win"
    elif user_input == "scissor" and com_input == "stone":
        com_score += 1
        winner_label["text"] = "Computer wins"
    elif user_input == "scissor" and com_input == "paper":
        user_score += 1
        winner_label["text"] = "You win"
    elif user_input == com_input:
        winner_label["text"] += "It's a tie!"

#reset game
def reset_game():
    global user_score, com_score
    user_score = 0
    com_score = 0
    winner_label["text"] = ""
    result_label["text"] = "Choose your move!"
    final_score_label["text"] = ""
    welcome_label.pack(pady=10)

# GUI Setup
root = tk.Tk()
root.title("Stone-Paper-Scissor Game")

# Labels
welcome_label = tk.Label(root, text="Welcome to Stone-Paper-Scissor Game!", font=("Arial", 10))
welcome_label.pack(pady=20)

versus_label = tk.Label(root, text="Player       vs       Computer", font=("Arial", 18, "bold"))
versus_label.pack(pady=5)

winner_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="white", width=20, relief="sunken")
winner_label.pack(pady=5)

result_label = tk.Label(root, text="Choose your move!", font=("Arial", 14))
result_label.pack(pady=10)

final_score_label = tk.Label(root, text="", font=("Arial", 14))
final_score_label.pack(pady=7)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

stone_button = tk.Button(button_frame, text="Stone", command=lambda: play_game("stone"), width=10)
stone_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("paper"), width=10)
paper_button.grid(row=0, column=1, padx=5)

scissor_button = tk.Button(button_frame, text="Scissor", command=lambda: play_game("scissor"), width=10)
scissor_button.grid(row=0, column=2, padx=5)

quit_button = tk.Button(root, text="Quit", command=lambda: play_game("quit"), bg="red", fg="white", width=10)
quit_button.pack(pady = 10)

reset_button = tk.Button(root, text="Reset", command=reset_game, bg="blue", fg="white", width=10)
reset_button.pack(pady = 10)



# Start the GUI loop
root.mainloop()


