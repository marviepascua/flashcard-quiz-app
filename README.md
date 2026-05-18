# Flashcard Quiz App

A pastel-themed flashcard quiz application built with Python and Tkinter.

## Description

Flashcard Quiz App is a GUI-based study tool that allows users to create, manage, and review digital flashcards in an interactive way.

The application was created as a personal Boot.dev project to practice:
- Python programming
- GUI development using Tkinter
- JSON file handling
- Git and GitHub workflow
- User interaction and application design

Flashcards are automatically saved using a JSON file so users can continue studying even after closing the application.

---

## Features

### Flashcard Management
- Add flashcards
- Edit flashcards
- Delete flashcards
- View flashcards
- Hide flashcards
- Double-click a flashcard question to reveal the answer
- Save flashcards

### Quiz Mode
- Randomized flashcard questions
- Answer validation
- Score tracking
- Quiz-focused mode
- Flashcard controls disabled during quiz
- Flashcard list automatically hidden during quiz

### User Interface
- Built using Tkinter
- Purple and pink pastel theme
- Styled buttons and layouts
- Interactive flashcard list
- Custom application icon support

---

## Technologies Used

- Python
- Tkinter
- JSON
- Git
- GitHub

---

## Project Structure

```text
flashcard-quiz-app/
│
├── main.py
├── flashcards.json
├── icon.png
├── README.md
└── .gitignore
```

---

## .gitignore

The project uses a `.gitignore` file to prevent unnecessary files from being uploaded to GitHub, such as:

```text
__pycache__/
*.pyc
.DS_Store
```

This keeps the repository clean and focused only on important project files.

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/marviepascua/flashcard-quiz-app.git
```

### 2. Open the project folder

```bash
cd flashcard-quiz-app
```

### 3. Run the application

```bash
python3 main.py
```

---

## Future Improvements

Potential future features:
- Flashcard categories
- Multiple-choice quiz mode
- Quiz timer
- Flashcard search
- Import/export flashcards
- Dark mode theme
- Statistics and progress tracking
- Keyboard shortcuts
- Difficulty levels

---


Example:

```text
screenshots/
├── main-window.png
├── quiz-mode.png
└── flashcards.png
```

---

## Learning Outcomes

This project helped improve skills in:
- Structuring Python applications
- Working with Tkinter widgets and layouts
- Managing persistent data using JSON
- Handling user events and interactions
- Designing a clean and user-friendly interface
- Using Git and GitHub for version control

---

## Author

Created by Marvie Pascua as part of the Boot.dev learning journey.

---

## License

This project is open-source and available under the MIT License.