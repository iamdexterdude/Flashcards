BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd
import random
from tkinter import *


# Check if unlearned_words.csv exists and is not empty; if not, create it from the full dataset
try:
    data = pd.read_csv("./data/unlearned_words.csv")
    if data.empty:  # If the file exists but is empty, load from the original file
        raise pd.errors.EmptyDataError
    data = data.to_dict(orient="records")
    print("Loaded unlearned words from file.")
except (FileNotFoundError, pd.errors.EmptyDataError):
    # Load the original data and save it to unlearned_words.csv
    data = pd.read_csv("./data/german-uzbek.csv").to_dict(orient="records")
    pd.DataFrame(data).to_csv("./data/unlearned_words.csv", index=False)
    print("Loaded original dataset and initialized unlearned_words.csv.")

current_word = {}

# Function to show the next card with a new German word
def next_card():
    global current_word
    if data:
        current_word = random.choice(data)
        german_word = current_word["German"]
        canvas.itemconfig(card_title, text="German")
        canvas.itemconfig(card_word, text=german_word)
        canvas.itemconfig(card_background, image=card_front_img)
    else:
        congrats()

# Function to flip the card and display the Uzbek translation and save unlearned word
def flip_card():
    uzbek_word = current_word["Uzbek"]
    canvas.itemconfig(card_title, text="Uzbek")
    canvas.itemconfig(card_word, text=uzbek_word)
    canvas.itemconfig(card_background, image=card_back_img)

# Function to mark the word as learned and update unlearned_words.csv
def mark_as_learned():
    global current_word
    data.remove(current_word)  # Remove from data list
    # Save the updated list of unlearned words to the file
    updated_data_df = pd.DataFrame(data)
    updated_data_df.to_csv("./data/unlearned_words.csv", index=False)
    next_card()

# Function to display a congratulations message when all words are learned
def congrats():
    canvas.itemconfig(card_title, text="Congratulations")
    canvas.itemconfig(card_word, text="You have learned all the words!")
    canvas.itemconfig(card_background, image=card_back_img)

# Tkinter setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas setup for displaying the flashcard
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons for known and unknown words
right_button_img = PhotoImage(file="./images/right.png")
wrong_button_img = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=mark_as_learned)
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=flip_card)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

# Start by displaying the first card
next_card()

# Run the Tkinter main loop
window.mainloop()
