import tkinter as tk  # GUI
import random  # generating random numbers

# Function to open the main game window
def create_window(username, no_rounds):  
    window = tk.Tk()  # Initialize the main window
    window.title("Basic Tkinter Window")  # Set the title of the window
    window.geometry("1680x800")  # Set the size of the window
    window.config(bg="darkgreen")#Changes background colour to green
    
    # Welcome message
    welcome = tk.Label(window, text=f"Welcome to the game, {username}!", bg="darkgreen", fg="white", font=("Arial", 20))
    welcome.pack(pady=50)
    
    # Rounds display
    rounds_total = tk.Label(window, text=f"Total number of rounds: {no_rounds}", bg="darkgreen", fg="white", font=("Arial", 15))
    rounds_total.pack(pady=20)

    # Play button to open the play window
    play_button = tk.Button(window, text="Play", command=lambda: open_play_window(username, no_rounds))
    play_button.pack(pady=20)

#Main game window
def open_play_window(username, no_rounds):
    play_window = tk.Tk()  
    play_window.title("Play Window")  
    play_window.geometry("1680x800")  
    play_window.config(bg="darkgreen")


    

# Function to store input and create the game window
def store_input_and_create_window():
    # Get inputs from entry widgets
    username = user.get()
    no_rounds = no_rounds_entry.get()
    
    # Debug print
    print("User input - Name:", username)
    print("User input - Rounds:", no_rounds)
    
    # Close the input window and create the main game window
    MainUser.destroy()
    create_window(username, no_rounds)
    

# Create the setup form
MainUser = tk.Tk()
MainUser.title("SET UP")

# Name input
name_label = tk.Label(MainUser, text="Enter your name:")
name_label.pack(pady=5)

user = tk.Entry(MainUser, width=30)
user.pack(pady=5)

# Rounds input
round_label = tk.Label(MainUser, text="Enter the number of rounds:")
round_label.pack(pady=5)

no_rounds_entry = tk.Entry(MainUser, width=30)
no_rounds_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(MainUser, text="Submit", command=store_input_and_create_window)
submit_button.pack(pady=10)

# Run the main loop
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

