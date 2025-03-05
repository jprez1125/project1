
"""
Author: Jennifer Perez
Date written: 03/04/2025
Assignment: Module 08 Final Project Submission.
1. Main Screen: Start button and game title.
2. Game Window: Displays the worm, cherries, and a score counter.
3. Controls: Keyboard arrow keys to move the worm and button or menu option to quit the
game.
4. Game Logic:
• Worm movement and collision detection
• Cherry consumption logic
• Increase speed after each cherry is eaten
• Timer interval reduction to gradually increase worm speed after each cherry is eaten
"""


import tkinter as tk
import random

# Constants
WIDTH = 600  # Width of the game window
HEIGHT = 400  # Height of the game window
SEGMENT_SIZE = 20  # size of each worm segment and cherry
SPEED = 300  # Initial speed of the worm (in milliseconds)
CHERRY_SCORE = 10  # Points earned for eating a cherry

class CherryMuncher:
    def __init__(self, root):
        # Set up the main window (start screen)
        self.root = root
        self.root.title("The Cherry Muncher")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")

        # Create a canvas for the start screen
        self.start_canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.start_canvas.pack()

        # Show the starting screen
        self.show_start_screen()

    def show_start_screen(self):
        """Display the start screen with the game title and start button."""
        self.start_canvas.delete("all")
        self.start_canvas.create_text(
            WIDTH // 2, HEIGHT // 6, text="The Cherry Muncher", fill="white", font=("Times New Roman", 24)
        )
        # create the Start button
        start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_canvas.create_window(WIDTH // 2, HEIGHT // 2, window=start_button)

    def start_game(self):
        """Initialize and start the game in a new window."""
        # Close the start screen
        self.root.withdraw()  # Hide the main window

        # Create a new window for the game screen
        self.game_window = tk.Toplevel()
        self.game_window.title("Cherry Muncher - Game Screen")
        self.game_window.geometry(f"{WIDTH}x{HEIGHT}")

        # Create a canvas for the game screen
        self.game_canvas = tk.Canvas(self.game_window, width=WIDTH, height=HEIGHT, bg="black")
        self.game_canvas.pack()

        # Initialize game variables
        self.is_game_running = True
        self.worm = [(100, 100), (80, 100), (60, 100)]  # Starting worm segments
        self.direction = "Right"  # Starting direction
        self.cherry = self.create_cherry()  # Create the first cherry
        self.score = 0  # Starting score
        self.speed = SPEED  # Starting speed

        # Draw the worm and cherry
        self.draw_worm()
        self.draw_cherry()

        # make use of arrow keys to control the worm
        self.game_window.bind("<Up>", lambda event: self.change_direction("Up"))
        self.game_window.bind("<Down>", lambda event: self.change_direction("Down"))
        self.game_window.bind("<Left>", lambda event: self.change_direction("Left"))
        self.game_window.bind("<Right>", lambda event: self.change_direction("Right"))

        # Add a quit button
        quit_button = tk.Button(self.game_window, text="Quit", command=self.quit_game)
        quit_button.pack()

        # Start the game loop
        self.update()

    def draw_worm(self):
        #Draw the worm on the canvas
        self.game_canvas.delete("worm")  # Clear previous worm segments
        for x, y in self.worm:
            self.game_canvas.create_rectangle(
                x, y, x + SEGMENT_SIZE, y + SEGMENT_SIZE, fill="pink", tags="worm"
            )

    def draw_cherry(self):
        """Draw the cherry on the canvas."""
        self.game_canvas.delete("cherry")  # Clear previous cherry
        x, y = self.cherry
        self.game_canvas.create_oval(
            x, y, x + SEGMENT_SIZE, y + SEGMENT_SIZE, fill="red", tags="cherry"
        )

    def create_cherry(self):
        #Generate a random position for the cherry
        x = random.randint(0, (WIDTH - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE
        y = random.randint(0, (HEIGHT - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE
        return (x, y)

    def change_direction(self, new_direction):
        """Change the worm's direction.
        Prevent the worm from reversing direction
        """
        if (new_direction == "Up" and self.direction != "Down") or \
           (new_direction == "Down" and self.direction != "Up") or \
           (new_direction == "Left" and self.direction != "Right") or \
           (new_direction == "Right" and self.direction != "Left"):
            self.direction = new_direction

    def move_worm(self):
        """Move the worm in the current direction."""
        head_x, head_y = self.worm[0]

        # Calculate the new head position based on the direction
        if self.direction == "Up":
            new_head = (head_x, head_y - SEGMENT_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + SEGMENT_SIZE)
        elif self.direction == "Left":
            new_head = (head_x - SEGMENT_SIZE, head_y)
        elif self.direction == "Right":
            new_head = (head_x + SEGMENT_SIZE, head_y)

        # Add the new head to the worm
        self.worm.insert(0, new_head)

        # Check if the worm eats the cherry
        if new_head == self.cherry:
            self.score += CHERRY_SCORE  # Increase the score
            self.cherry = self.create_cherry()  # Create a new cherry
            self.speed = max(50, self.speed - 5)  # Increase speed
        else:
            self.worm.pop()  # Remove the tail segment

    def update(self):
        """Update the game state."""
        if self.is_game_running:
            self.move_worm()  # Move the worm
            self.draw_worm()  # Redraw the worm
            self.draw_cherry()  # Redraw the cherry
            self.game_canvas.delete("score")  # Clear the previous score
            self.game_canvas.create_text(
                50, 20, text=f"Score: {self.score}", fill="white", font=("Times New Roman", 16), tags="score"
            )
            # Call the update function again after a delay
            self.game_window.after(self.speed, self.update)

    def quit_game(self):
        """Quit the game."""
        self.game_window.destroy()  # Close the game window
        self.root.deiconify()  # Show the start screen again


# Main program
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    game = CherryMuncher(root)  # Start the game
    root.mainloop()  # Run the game loop
