# US States Guessing Game (Python Turtle)

An educational Python game built using the **Turtle graphics module** that helps users learn and memorize the 50 states of the United States.

The player guesses state names, and correct guesses are displayed on a US map at their corresponding positions.

---

## 🎮 How the Game Works

- A blank map of the United States is displayed.
- The player types the name of a US state.
- If the guess is correct:
  - The state name appears on the correct location on the map.
- The game continues until:
  - All 50 states are guessed, or
  - The player chooses to exit.

When the player exits:
- A CSV file is generated containing the states that were **not guessed**.

---

## 🛠️ Built With

- **Python**
- **Turtle module**
- **Pandas** (for CSV handling)

---

## 📁 Project Files

- `main.py` — main game logic
- `us_states.csv` — dataset containing US states and coordinates
- `blank_states_img.gif` — blank US map used in the game

---

## ▶️ How to Run the Project

1. Make sure Python is installed on your system.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run:
   ```bash
   python main.py
🎯 Learning Outcomes

This project demonstrates:

Python control flow and conditionals

File handling with CSV files

GUI programming with Turtle

Data tracking and validation

Basic game logic implementation

📌 Notes

The missed_states.csv file is generated only when the user exits the game.

This project was created as part of the 100 Days of Code – Python challenge.

👩‍💻 Author

Sonia Chima–Mpamah
