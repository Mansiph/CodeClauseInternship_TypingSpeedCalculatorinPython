import tkinter as tk
from tkinter import messagebox
import time
import random

class SpeedTypingChallenge:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("Speed Typing Challenge")
        self.root_window.geometry("600x400")

        self.text_samples = [
            "The quick brown fox jumps over the lazy dog.",
            "A journey of a thousand miles begins with a single step.",
            "To be, or not to be, that is the question.",
            "All that glitters is not gold.",
            "The only limit to our realization of tomorrow is our doubts of today."
        ]

        self.start_time = None
        self.end_time = None
        self.select_new_sample()

        self.instructions_label = tk.Label(root_window, text="Type the following sentence:", font=("Arial", 14))
        self.instructions_label.pack(pady=10)

        self.text_to_type_label = tk.Label(root_window, text=self.text_sample, font=("Arial", 12), wraplength=550)
        self.text_to_type_label.pack(pady=10)

        self.text_input = tk.Text(root_window, height=5, width=70, font=("Arial", 12))
        self.text_input.pack(pady=10)
        self.text_input.bind("<KeyPress>", self.start_typing_timer)

        self.submit_button = tk.Button(root_window, text="Submit", command=self.calculate_results, font=("Arial", 12))
        self.submit_button.pack(pady=10)

    def select_new_sample(self):
        """Picks a random sentence from the pool."""
        self.text_sample = random.choice(self.text_samples)

    def start_typing_timer(self, event):
        """Starts the timer when the first key is pressed."""
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_results(self):
        """Calculates the typing speed and accuracy, then shows the result."""
        self.end_time = time.time()
        user_text = self.text_input.get("1.0", tk.END).strip()

        if not user_text:
            messagebox.showwarning("Warning", "Please type the sentence before submitting.")
            return

        # Calculate time taken in minutes
        time_taken = (self.end_time - self.start_time) / 60

        # Calculate Words Per Minute (WPM)
        words_count = len(user_text.split())
        wpm = words_count / time_taken

        # Calculate accuracy
        correct_words = sum(1 for expected, typed in zip(self.text_sample.split(), user_text.split()) if expected == typed)
        accuracy = (correct_words / len(self.text_sample.split())) * 100 if self.text_sample else 0

        # Show results
        messagebox.showinfo("Typing Results", f"Typing Speed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%")

        # Reset for a new test
        self.start_time = None
        self.text_input.delete("1.0", tk.END)
        self.select_new_sample()
        self.text_to_type_label.config(text=self.text_sample)

if __name__ == "__main__":
    window = tk.Tk()
    app = SpeedTypingChallenge(window)
    window.mainloop()
