# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

0. `python3 -m venv venv` and `source venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Purpose

This is a simple Number Guessing Game built with Streamlit. Players choose a difficulty (sets the number range and attempt limit), submit numeric guesses, receive higher/lower hints, and earn points based on accuracy and remaining attempts.

### Bugs Found

- Difficulty selection did not always update the allowed range or attempt limit.
- Sidebar and main page could display mismatched "Attempts left" values.
- Hints (Higher/Lower) were sometimes generated from outdated logic and could be incorrect.
- New-game flow did not always clear history and score.
- Input parsing and scoring needed more validation and edge-case tests.

### Fixes Applied

- Persisted game state using `st.session_state` for the secret number, attempts, history, and score.
- Consolidated hint/score logic into `logic_utils.py` and corrected hint calculation so it always reflects the current secret number.
- Ensured New Game resets history, attempts, and score consistently.
- Added input validation and updated/added unit tests for parsing and scoring behavior.

## 📸 Demo Walkthrough

1. Start the app:

```bash
python -m streamlit run app.py
```

2. Open the "Developer Debug Info" tab to reveal the current secret number for debugging.
3. Select a difficulty (Easy / Normal / Hard). The displayed range and attempt limit update to match the selection.
4. Enter a numeric guess and click "Submit". The app shows a correct hint ("Higher" or "Lower"), decrements attempts, updates history, and adjusts score based on remaining attempts.
5. Click "New Game" to reset the secret number, attempts, history, and score for a fresh round.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/ 
# python -m pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
