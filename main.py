import json
import random
import tkinter as tk
from tkinter import messagebox

FLASHCARD_FILE = "flashcards.json"
BG_COLOR = "#fdf2ff"
CARD_COLOR = "#ffffff"
PRIMARY_COLOR = "#c77dff"
PRIMARY_HOVER = "#b05cff"
TEXT_COLOR = "#5a189a"
LISTBOX_COLOR = "#fff0fb"
BORDER_COLOR = "#e9c8ff"
BUTTON_TEXT = "#ffffff"


def load_flashcards():
    try:
        with open(FLASHCARD_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_flashcards():
    with open(FLASHCARD_FILE, "w") as file:
        json.dump(flashcards, file, indent=4)


def add_flashcard():
    global editing_index
    
    question = question_entry.get().strip()
    answer = answer_entry.get().strip()

    if question == "" or answer == "":
        messagebox.showwarning("Missing Input", "Please enter both question and answer.")
        return
    
    if editing_index is not None:
        flashcards[editing_index] = {
            "question": question,
            "answer": answer
        }
        
        editing_index = None
        add_button.config(text="Add flashcard")
        messagebox.showinfo("Success", "Flascard updated successfully!")
    
    else:
        flashcards.append({
            "question": question,
            "answer": answer
        })
        messagebox.showinfo("Success", "Flashcard addedd successfully!")

    save_flashcards()

    question_entry.delete(0, tk.END)
    answer_entry.delete(0, tk.END)


def edit_selected_flashcard():
    global editing_index
    
    selected_index = flashcard_list.curselection()
    
    if not selected_index:
        messagebox.showwarning("No selection", "Please select a flashcard to edit.")
        return
    
    editing_index = selected_index[0]
    selected_card = flashcards[editing_index]
    
    question_entry.delete(0, tk.END)
    answer_entry.delete(0, tk.END)
    
    question_entry.insert(0, selected_card["question"])
    answer_entry.insert(0, selected_card["answer"])
    
    add_button.config(text="Save Chagnes")

def view_flashcards():
    flashcard_list.delete(0, tk.END)

    if not flashcards:
        flashcard_list.insert(tk.END, "No flashcards available.")
        return

    for index, card in enumerate(flashcards, start=1):
        flashcard_list.insert(tk.END, f"{index}. {card['question']}")

def show_selected_answer(event):
    selected_index = flashcard_list.curselection()
    
    if not selected_index:
        return
    
    index = selected_index[0]
    
    if index >= len(flashcards):
        return
    
    question = flashcards[index]["question"]
    answer = flashcards[index]["answer"]
    messagebox.showinfo("Flashcard Answer", f"Question: {question}\n\nAnswer: {answer}")
        
def hide_flashcards():
    flashcard_list.delete(0, tk.END)


def start_quiz():
    global quiz_cards, current_card, score

    if not flashcards:
        messagebox.showwarning("No Flashcards", "Please add flashcards first.")
        return
    
    add_button.config(state=tk.DISABLED)
    view_button.config(state=tk.DISABLED)
    hide_button.config(state=tk.DISABLED)
    edit_button.config(state=tk.DISABLED)
    
    flashcard_list.delete(0,tk.END)

    quiz_cards = flashcards.copy()
    random.shuffle(quiz_cards)
    current_card = 0
    score = 0

    show_question()


def show_question():
    if current_card < len(quiz_cards):
        question_label.config(text=quiz_cards[current_card]["question"])
        quiz_answer_entry.delete(0, tk.END)
        feedback_label.config(text="")
    else:
        question_label.config(text="Quiz Complete!")
        feedback_label.config(text=f"Your score: {score}/{len(quiz_cards)}") 
        add_button.config(state=tk.NORMAL)
        view_button.config(state=tk.NORMAL)
        hide_button.config(state=tk.NORMAL)
        edit_button.config(state=tk.NORMAL)   


def check_answer():
    global current_card, score

    if current_card >= len(quiz_cards):
        return

    user_answer = quiz_answer_entry.get().strip().lower()
    correct_answer = quiz_cards[current_card]["answer"].strip().lower()

    if user_answer == correct_answer:
        score += 1
        feedback_label.config(text="Correct!")
    else:
        feedback_label.config(
            text=f"Incorrect. Correct answer: {quiz_cards[current_card]['answer']}"
        )

    current_card += 1
    root.after(1200, show_question)


flashcards = load_flashcards()
quiz_cards = []
current_card = 0
score = 0
editing_index = None

root = tk.Tk()
root.title("Flashcard Quiz App")
root.geometry("700x700")
root.config(bg=BG_COLOR)

title_label = tk.Label(root, text="Flashcard Quiz App", font=("Arial", 24, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
title_label.pack(pady=20)

input_frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20, highlightbackground=BORDER_COLOR, highlightthickness=2)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Question:", bg=CARD_COLOR, fg=TEXT_COLOR, font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
question_entry = tk.Entry(input_frame, width=50, font=("Arial", 10), relief="flat", highlightthickness=2, highlightbackground=BORDER_COLOR)
question_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Answer:", bg=CARD_COLOR, fg=TEXT_COLOR,font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)
answer_entry = tk.Entry(input_frame, width=50, font=("Arial", 10), relief="flat", highlightthickness=2, highlightbackground=BORDER_COLOR)
answer_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Flashcard", command=add_flashcard, bg=PRIMARY_COLOR, fg=BUTTON_TEXT, activebackground=PRIMARY_HOVER, activeforeground=BUTTON_TEXT, relief="flat", width=18, font=("Arial", 10, "bold"), padx=10, pady=5)
add_button.pack(pady=5)

view_hide_frame = tk.Frame(root, bg=BG_COLOR)
view_hide_frame.pack(pady=5)

view_button = tk.Button(view_hide_frame, text="View Flashcards", command=view_flashcards, bg=PRIMARY_COLOR, fg=BUTTON_TEXT, activebackground=PRIMARY_HOVER, activeforeground=BUTTON_TEXT, relief="flat", width=18, font=("Arial", 10, "bold"), padx=10, pady=5)
view_button.pack(side=tk.LEFT, padx=5)

hide_button = tk.Button(view_hide_frame, text="Hide Flashcards", command=hide_flashcards, bg=PRIMARY_COLOR, fg=BUTTON_TEXT, activebackground=PRIMARY_HOVER, activeforeground=BUTTON_TEXT, relief="flat", width=18, font=("Arial", 10, "bold"), padx=10, pady=5)
hide_button.pack(side=tk.LEFT, padx=5)

edit_button = tk.Button(view_hide_frame, text="Edit Selected", command=edit_selected_flashcard, bg=PRIMARY_COLOR, fg=BUTTON_TEXT, activebackground=PRIMARY_HOVER, activeforeground=BUTTON_TEXT, relief="flat", width=18, font=("Arial", 10, "bold"), padx=10, pady=5)
edit_button.pack(side=tk.LEFT, padx=5)

flashcard_list = tk.Listbox(root, width=70, height=8, bg=LISTBOX_COLOR, fg=TEXT_COLOR, font=("Arial", 10), relief="flat", highlightthickness=2, highlightbackground=BORDER_COLOR, selectbackground=PRIMARY_COLOR, selectforeground="white")
flashcard_list.pack(pady=10)

flashcard_list.bind("<Double-Button-1>", show_selected_answer)

quiz_frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20, highlightbackground=BORDER_COLOR, highlightthickness=2)
quiz_frame.pack(pady=10)

start_quiz_button = tk.Button(quiz_frame, text="Start Quiz", command=start_quiz, bg=PRIMARY_COLOR, fg=BUTTON_TEXT, activebackground=PRIMARY_HOVER, activeforeground=BUTTON_TEXT, relief="flat", width=18, font=("Arial", 10, "bold"), padx=10, pady=5)
start_quiz_button.pack(pady=5)

question_label = tk.Label(quiz_frame, text="Click Start Quiz to begin", font=("Arial", 12))
question_label.pack(pady=5)

quiz_answer_entry = tk.Entry(quiz_frame, width=50, font=("Arial", 10), relief="flat", highlightthickness=2, highlightbackground=BORDER_COLOR)
quiz_answer_entry.pack(pady=5)

check_button = tk.Button(quiz_frame, text="Check Answer", command=check_answer, bg=PRIMARY_COLOR, fg=BUTTON_TEXT, activebackground=PRIMARY_HOVER, activeforeground=BUTTON_TEXT, relief="flat", width=18, font=("Arial", 10, "bold"), padx=10, pady=5)
check_button.pack(pady=5)

feedback_label = tk.Label(quiz_frame, text="", font=("Arial", 11))
feedback_label.pack(pady=5)

root.mainloop()