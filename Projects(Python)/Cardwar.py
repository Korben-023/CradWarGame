import tkinter as tk 
import random

card_value = {#Dictionary that assign each card rank a value 
    "Ace": 14, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "Jack": 11, "Queen": 12, "King": 13
}

round_counter=1

class Deck:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    def __init__(self):
        self.cards = [f"{rank} of {suit}" for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)
        half_size = len(self.cards) // 2
        self.p1_cards = self.cards[:half_size]
        self.p2_cards = self.cards[half_size:]
        self.p1_discard = []  # Player 1's discard pile
        self.p2_discard = []  # Player 2's discard pile

deck = None

def comparison(card1, card2, deck):
    value_p1 = card_value[card1.split()[0]]
    value_p2 = card_value[card2.split()[0]]
    
    # Compare values and add cards to discard piles
    if value_p1 > value_p2:
        deck.p1_discard.extend([card1, card2])  # Player 1 wins, add both cards to p1_discard
        return "Player 1 wins the round!"
    elif value_p1 < value_p2:
        deck.p2_discard.extend([card1, card2])  # Player 2 wins, add both cards to p2_discard
        return "Player 2 wins the round!"
    else:
        deck.p1_discard.append(card1)  #NEED TO CHNAGE LATER FOR CARDWAR MECHNAICS
        deck.p2_discard.append(card2)
        return "It's a tie!"

def create_window(username, no_rounds):  
    window = tk.Tk()
    window.title("Basic Tkinter Window")
    window.geometry("1680x800")
    window.config(bg="darkblue")
    
    welcome = tk.Label(window, text=f"Welcome to the game, {username}!", bg="darkblue", fg="white", font=("Arial", 20))
    welcome.pack(pady=50)
    
    rounds_total = tk.Label(window, text=f"Total number of rounds: {no_rounds}", bg="darkblue", fg="white", font=("Arial", 15))
    rounds_total.pack(pady=20)

    play_button = tk.Button(window, text="Play", command=lambda: [window.destroy(), open_play_window(username, no_rounds)])
    play_button.pack(pady=20)

def open_play_window(username, no_rounds):
    global deck
    deck = Deck()

    play_window = tk.Tk()
    play_window.title("Play Window")
    play_window.geometry("1680x800")
    play_window.config(bg="darkblue")

    welcome = tk.Label(play_window, text=f"Let's play, {username}!", bg="darkblue", fg="white", font=("Arial", 20))
    welcome.pack(pady=50)

    player1_score = 0
    player2_score = 0

    p1_score_label = tk.Label(play_window, text=f"Player 1 score: {player1_score}", bg="darkblue", fg="white", font=("Arial", 15))
    p1_score_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

    p2_score_label = tk.Label(play_window, text=f"Player 2 score: {player2_score}", bg="darkblue", fg="white", font=("Arial", 15))
    p2_score_label.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

    # Setup for Player 1 cards
    p1_frame = tk.Frame(play_window, bg="darkblue")
    p1_frame.pack(side=tk.LEFT, padx=20, pady=20)

    p1_label = tk.Label(p1_frame, text="Player 1 Cards:", bg="darkblue", fg="white", font=("Arial", 12))
    p1_label.pack()

    p1_scrollbar = tk.Scrollbar(p1_frame)
    p1_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    p1_listbox = tk.Listbox(p1_frame, bg="white", fg="black", font=("Arial", 10), height=20, width=20, yscrollcommand=p1_scrollbar.set)
    p1_listbox.pack()
    p1_scrollbar.config(command=p1_listbox.yview)

    for card in deck.p1_cards:
        p1_listbox.insert(tk.END, card)
    
    # Randomly select and display cards (MAKE INTO FUNCTION)
    player1_hand = random.choice(deck.p1_cards)
    deck.p1_cards.remove(player1_hand)

    p1_hand_label = tk.Label(play_window, text=f"Player 1's Hand: {player1_hand}", bg="darkblue", fg="white", font=("Arial", 15))
    p1_hand_label.pack(side=tk.LEFT, pady=10)

    player2_hand = random.choice(deck.p2_cards)
    deck.p2_cards.remove(player2_hand)

    p2_frame = tk.Frame(play_window, bg="darkblue")
    p2_frame.pack(side=tk.RIGHT, padx=20, pady=20)

    p2_label = tk.Label(p2_frame, text="Player 2 Cards:", bg="darkblue", fg="white", font=("Arial", 12))
    p2_label.pack()

    p2_hand_label = tk.Label(p2_frame, text=f"Player 2's Hand: {player2_hand}", bg="darkblue", fg="white", font=("Arial", 15))
    p2_hand_label.pack(side=tk.LEFT, padx=5)

    p2_scrollbar = tk.Scrollbar(p2_frame)
    p2_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    p2_listbox = tk.Listbox(p2_frame, bg="white", fg="black", font=("Arial", 10), height=20, width=20, yscrollcommand=p2_scrollbar.set)
    p2_listbox.pack(side=tk.LEFT)
    p2_scrollbar.config(command=p2_listbox.yview)

    for card in deck.p2_cards:
        p2_listbox.insert(tk.END, card)
    
    # Run comparison and show result
    result = comparison(player1_hand, player2_hand, deck)
    result_label = tk.Label(play_window, text=result, bg="darkblue", fg="white", font=("Arial", 15))
    result_label.pack(pady=10)
    
    submit_button = tk.Button(MainUser, text="Submit", command=store_input_and_create_window)
    submit_button.pack(pady=10)

def store_input_and_create_window():
    username = user.get()
    no_rounds = no_rounds_entry.get()
    MainUser.destroy()
    create_window(username, no_rounds)

# Set up form for the game
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






