# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened during your development process. Focus on your learning process rather than trying to make everything sound perfect.

## 1. What was broken when you started?

### What did the game look like the first time you ran it?

When I first launched the game, the main issue was not just visual timing but inconsistent game rules: the chosen difficulty did not always produce the expected range, the displayed attempts-left value could disagree with the real state, and the score/hint logic did not reflect the current rules. Ying Wang’s commits on the project helped clarify these behaviors by updating the app flow and logic utilities in a way that matched the intended difficulty system.

### List at least two concrete bugs you noticed at the start:

* Difficulty selection did not consistently update the game range and attempt limit.
* The sidebar and main page showed mismatched attempt counts, which made the game feel broken.
* Hint text and score feedback were based on older logic and needed to be aligned with the current rules.
* The new-game flow did not fully reset history and score in every case.
* Input handling and scoring needed extra validation and tests to cover edge cases.

### Bug Reproduction Log

| Input                                     | Expected Behavior                                                   | Actual Behavior                                                        | Console Output / Error |
| ----------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------- |
| Change difficulty from Normal to Hard     | The game should update the allowed range and attempt limit immediately | The range and attempt limit did not always reflect the selected difficulty | N/A                    |
| Check the main page attempts counter      | The displayed “Attempts left” should match the real game state       | The sidebar and main page could show different values                 | N/A                    |
| Submit a guess and view the hint/score   | Hint text and score feedback should follow the current game rules    | Hint and score behavior were inconsistent with the updated logic      | N/A                    |
| Click New Game after a few guesses        | History, score, and status should reset for a fresh game             | Previous history or score could remain visible after reset           | N/A                    |

---

## 2. How did you use AI as a teammate?

### Which AI tools did you use on this project?

I used ChatGPT, Codex, and GitHub Copilot to analyze the existing logic, compare the behavior of the app and utility functions, and verify the fixes.

### Give one example of an AI suggestion that was correct.

AI helped identify that some bugs were related to state management and component re-rendering. I verified the suggestions by manually reproducing the issues, applying the suggested fixes, and confirming that the game behavior matched the expected result.

### Give one example of an AI suggestion that was incorrect or misleading.

Some AI suggestions did not fully match the actual code behavior. I verified them by comparing the suggested fix with my own debugging results and testing the application after applying changes. This showed me that AI suggestions still need to be reviewed and validated.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed by manually testing the user flow and then running the automated tests that cover the updated logic. The recent work on `parse_guess`, `update_score`, and difficulty-related behavior was especially important because it added tests for edge cases and scoring outcomes.

One test I ran was `python -m pytest tests/`, and the result confirmed that the updated logic still behaved as expected after the fixes. The added tests for parsing and scoring helped verify the rules that Carol Wang’s commits were improving.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the script from top to bottom whenever the user interacts with the application. Because of this behavior, variables created during execution do not automatically preserve their values between interactions.

Session state allows Streamlit applications to store information across reruns. It acts like a memory for the app, keeping values such as game progress, attempts, history, and user selections between interactions.

---

## 5. Looking ahead: your developer habits

### What is one habit or strategy from this project that you want to reuse?

I want to continue taking notes, listing bugs clearly, fixing issues one at a time, and testing after each change. I also want to use commit history more actively as a debugging reference, since Carol Wang’s updates showed how the app logic evolved across difficulty, hint, score, and input-handling changes. My preferred workflow is to review the current behavior, compare it to recent commits, make focused fixes, and then verify the result with tests.

### What is one thing you would do differently next time when working with AI on a coding task?

Next time, I would ask AI to first analyze the entire project and create a list of possible bugs before making changes. I would compare AI's diagnosis with my own findings and evaluate how accurate the suggestions are. I would also create a separate Git branch for AI-generated fixes and compare the results against my step-by-step debugging approach.

### How did this project change the way you think about AI-generated code?

This project showed me that AI is a useful debugging partner, but it is not a replacement for understanding the code. AI can quickly identify possible issues and suggest solutions, but developers still need to verify the logic, test the changes, and make final decisions.
