rom tkinter import *
import tkinter as tk
import random
from PIL import Image, ImageTk


upload = Image.open("upload.png")
upload = upload.resize((100, 100))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="lightblue")
label.pack(x= 180, y=20)

player_score = 0
computer_score = 0
round_number = 0

def play_game(player_choice):
    global player_score, computer_score, round_number

    choices = ["Rock","Paper","Scissors"]
    score = {"Player": 0, "Computer": 0, "Ties" : 0}

    computer_choice = random.choice(choices)
    round_number +=1

    
    player_choice_label.config(text = "Your choice" + player_choice)
    computer_choice_label.config(text = "Computer choice: " + computer_choice)
    
    if player_choice == computer_choice:
        return "Tie"

    elif player_choice == "Rock" and computer_choice == "scissors":
        reuslts = "You win!"
        player_score += 1

    elif player_choice == "Paper" and computer_choice == "Rocks":
            reuslts = "You win!"
            player_score += 1 

    elif player_choice == "Scissors" and computer_choice == "Paper":
            reuslts = "You win!"
            player_score += 1

    else:
        reuslts = "Computer win!"
        computer_score += 1


    score_label.config(text = f"score You:{player_score}    Computer {computer_score}")
    round_label.config(text = f"Round: {round_number}" )
   
def reset_game():
    global player_score, computer_score, round_number


    player_score = 0
    computer_score = 0
    round_number = 0


    player_score_label.config(text  = "Your choice")
    computer_choice_label.config(text = "Computer Choice")
    result_label.config(text  = "Choose Rock, Paper or scissors")
    score_label.config(text = "Score    You: 0   Compter : 0")
    round_label.config(text = "Round: 0")


    def show_rules():
        rules = (" Rock Paper Scissors Rules: \n ", "Rock beats scissors"
                  " ")

        rules_labl.config(text=rules)


    window = tk.TK()
    window.title("Rock Paper Scissors")
    window.geometry("800x800")
    window.configure(bg = "light blue")


    rock_image = tk.PhotoImage(file = "rock.png")
    paper_image =  tk.PhotoImage(file = "paper.png")
    scissors_image = tk.PhotoImage(file= "scissors.png")

    title_label = Label(text = "ROCK PAPER SCISSORS" , bg = "light grey", font  = ("Arial",28,"bold"))
    title_label.pack(pady = 20)

    instruction_label = Label(text = "Choose your move!" , bg = "light blue", font  = ("Arial",15))
    instruction_label.pack()

    round_label = Label(text = "ROCK PAPER SCISSORS" , bg = "orange", font  = ("Arial", 10))
    round_label.pack(pady=10)

    player_choice_label = Label(text = "ROCK PAPER SCISSORS" , bg = "yellow")
    player_choice_label.pack(pady = 5)

    computer_choice_label = Label(text = "ROCK PAPER SCISSORS" , bg = "black")
    computer_choice_label(pady=10)
 
    result_label = Label(text = "ROCK PAPER SCISSORS" , bg = "red")
    result_label.pack(pady = 10)


window.mainloop()

     
    

    
