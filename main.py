import time
import tkinter as tk
from tkinter import font

# Sample text for the user to type
sample_text = "The quick brown fox jumps over the lazy dog."

def start_typing(event=None):
    """Show the entry field, focus on it, and hide the start button."""
    entry.pack(pady=10)
    entry.focus_set()
    start_button.pack_forget()
    global start_time
    start_time = time.time()  # Start the timer

def display_message(event=None):
    """Calculate typing performance and update the result label."""
    end_time = time.time()  # End the timer
    user_input = entry.get()  # Get the text from the entry field
    elapsed_time = end_time - start_time  # Time in seconds

    # Count words
    correct_words = user_input.split()
    sample_words = sample_text.split()

    num_correct = sum(
        1 for i in range(len(correct_words)) if i < len(sample_words) and correct_words[i] == sample_words[i]
    )

    # Calculate WPM
    minutes = elapsed_time / 60
    wpm = (num_correct / minutes) if minutes > 0 else 0

    # Update the message label with results
    result_text = (
        f"You typed {num_correct} correct words in {elapsed_time:.2f} seconds.\n"
        f"Your typing speed is {wpm:.2f} words per minute."
    )
    message_label.config(text=result_text)

# Create the main window
root = tk.Tk()
root.title("Typing Test App")
root.geometry("400x400")
root.config(bg="#e8f0f2")

# Use a custom font
custom_font = font.Font(family="Helvetica", size=12)

# Add labels and buttons
prompt_label = tk.Label(
    root, text="Type the following text:", bg="#e8f0f2", font=custom_font, fg="#333333"
)
prompt_label.pack(pady=10)

instruction_label = tk.Label(
    root, text=sample_text, bg="#e8f0f2", font=("Helvetica", 12, "italic"), fg="#555555"
)
instruction_label.pack(pady=10)

entry = tk.Entry(root, width=40, font=custom_font, borderwidth=2, relief="groove")
entry.pack_forget()  # Initially hidden
entry.bind("<Return>", display_message)

start_button = tk.Button(
    root, text="Start", command=start_typing, font=custom_font, bg="#4CAF50", fg="white",
    activebackground="#45a049", relief="raised"
)
start_button.pack(pady=10)

message_label = tk.Label(root, text="", bg="#e8f0f2", font=custom_font, fg="#333333",
                         relief="groove", padx=10, pady=10)
message_label.pack(pady=20, fill="x", padx=10)


root.mainloop()