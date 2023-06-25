import tkinter as tk
import random

flashcards = {
    "Sulfuric acid": "H2SO4",
    "Nitric acid": "HNO3",
    "Hydrochloric acid": "HCl",
    "Potassium hydroxide": "KOH",
    "Calcium hydroxide": "Ca(OH)2",
    "Sodium hydroxide": "NaOH"
}

def show_random_flashcard():
    random_card = random.choice(list(flashcards.items()))
    flashcard_label.config(text=random_card[0])
    formula_button.config(state=tk.NORMAL)
    formula_label.config(text="")

def show_formula():
    flashcard = flashcard_label.cget("text")
    formula_label.config(text=flashcards[flashcard])

root = tk.Tk()
root.title("Acid Flashcards")

# Create a label to display the flashcard
flashcard_label = tk.Label(root, text="Click 'Show Flashcard'")
flashcard_label.pack(pady=20)

# Create a button to show a random flashcard
show_flashcard_button = tk.Button(root, text="Show Flashcard", command=show_random_flashcard)
show_flashcard_button.pack(pady=10)

# Create a button to show the formula
formula_button = tk.Button(root, text="Show Formula", command=show_formula, state=tk.DISABLED)
formula_button.pack(pady=10)

# Create a label to display the formula
formula_label = tk.Label(root, text="")
formula_label.pack(pady=10)

root.mainloop()
