import tkinter as tk
import random

def create_window(username, no_rounds):  
    window = tk.Tk()
    window.title("Basic Tkinter Window")
    window.geometry("1680x800")
    window.config(bg="darkgreen")
    
    welcome = tk.Label(window, text=f"Welcome to the game, {username}!", bg="darkgreen", fg="white", font=("Arial", 20))
    welcome.pack(pady=50)
    
    rounds_total = tk.Label(window, text=f"Total number of rounds: {no_rounds}", bg="darkgreen", fg="white", font=("Arial", 15))
    rounds_total.pack(pady=20)

    play_button = tk.Button(window, text="Play", command=lambda: [window.destroy(), open_play_window(username, no_rounds)])
    play_button.pack(pady=20)

def open_play_window(username, no_rounds):
    play_window = tk.Tk()
    play_window.title("Play Window")
    play_window.geometry("1680x800")
    play_window.config(bg="darkblue")

    welcome = tk.Label(play_window, text=f"Let's play, {username}!", bg="darkblue", fg="white", font=("Arial", 20))
    welcome.pack(pady=50)

    rounds_total = tk.Label(play_window, text=f"Total number of rounds: {no_rounds}", bg="darkblue", fg="white", font=("Arial", 15))
    rounds_total.pack(pady=20)

    player1_score = 0
    player2_score = 0
    
    p1_score_label = tk.Label(play_window, text=f"Player 1 score: {player1_score}", bg="darkblue", fg="white", font=("Arial", 15))
    p1_score_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)
    
    p2_score_label = tk.Label(play_window, text=f"Player 1 score: {player2_score}", bg="darkblue", fg="white", font=("Arial", 15))
    p2_score_label.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

def store_input_and_create_window():
    username = user.get()
    no_rounds = no_rounds_entry.get()
    
    print("User input - Name:", username)
    print("User input - Rounds:", no_rounds)
    
    MainUser.destroy()
    create_window(username, no_rounds)

MainUser = tk.Tk()
MainUser.title("SET UP")

name_label = tk.Label(MainUser, text="Enter your name:")
name_label.pack(pady=5)

user = tk.Entry(MainUser, width=30)
user.pack(pady=5)

round_label = tk.Label(MainUser, text="Enter the number of rounds:")
round_label.pack(pady=5)

no_rounds_entry = tk.Entry(MainUser, width=30)
no_rounds_entry.pack(pady=5)

submit_button = tk.Button(MainUser, text="Submit", command=store_input_and_create_window)
submit_button.pack(pady=10)

MainUser.mainloop()


    
     


"""DO THIS LATER"""
class Deck:  # Class that defines the deck
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    def __init__(self):
        # Initialize a full deck of 52 cards
        self.cards = [f"{rank} of {suit}" for suit in self.suits for rank in self.ranks]
    
    def deal_random_card(self):#Deals random card
        if self.cards:
            card = random.choice(self.cards)
            self.cards.remove(card)
            return card
        else:
            return "No more cards in the deck"
    
   


# Create a deck instance
deck = Deck()

# Test 

#print("Random card dealt (removed from deck):", deck.deal_random_card())
#print("Remaining cards:", len(deck.cards))

