
"""
Author: Jennifer Perez
Date written: 2/22/20245
Assignment: Module 06 Project Status Report II
start of final project .Created the start screen and the game screen. Need to do more research to design the worm and cherries. 
"""


import tkinter as tk

def show_game_screen():
    start_frame.pack_forget()  # hide the start screen
    game_frame.pack(fill='both', expand=True)  # Show the game screen
    start_game()  # Initialize game elements

def show_start_screen():
    game_frame.pack_forget()  # Hide the game screen
    start_frame.pack(fill='both', expand=True)  # Show the start screen

def start_game():

    pass

# Initialize the main application window
root = tk.Tk()
root.title("The Cherry Muncher")

# Create the start screen frame
start_frame = tk.Frame(root, bg='black')
start_frame.pack(fill='both', expand=True)

# title label for the start screen
title_label = tk.Label(start_frame, text="The Cherry Muncher", font=('Times New Roman', 24), fg='white', bg='black')
title_label.pack(pady=20)

# start button for the start screen
start_button = tk.Button(start_frame, text="Start", font=('Times New Roman', 18), command=show_game_screen)
start_button.pack(pady=10)

# Create the game screen frame
game_frame = tk.Frame(root, bg='black')

# Add a black canvas to the game screen for the game graphics
game_canvas = tk.Canvas(game_frame, width=800, height=600, bg='black')
game_canvas.pack()

# Start the Tkinter main loop
root.mainloop()
