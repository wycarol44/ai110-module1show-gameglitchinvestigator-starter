# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened during your development process. Focus on your learning process rather than trying to make everything sound perfect.

## 1. What was broken when you started?

### What did the game look like the first time you ran it?

When I first launched the game, some components appeared immediately, while other components loaded several seconds later.

### List at least two concrete bugs you noticed at the start:

* The difficulty input produced an incorrect output range.
* The "Attempts Allowed" value displayed on the left sidebar showed 8, but the actual initial attempts value was 7.
* The hint system was not working correctly and provided incorrect hints.
* Clicking the "New Game" button did not clear the game history list.
* After winning the game, the alert message remained visible even after clicking the "New Game" button.
* Running `python -m pytest tests/` failed.

### Bug Reproduction Log

| Input                                     | Expected Behavior                                     | Actual Behavior                                                 | Console Output / Error |
| ----------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------- | ---------------------- |
| Start a new game with difficulty selected | The game should generate the correct difficulty range | The generated range did not match the selected difficulty       | N/A                    |
| Check the Attempts Allowed display        | Sidebar and internal attempt count should match       | Sidebar showed 8 attempts, but game initialized with 7 attempts | N/A                    |
| Click the Hint button                     | A valid hint should be displayed                      | The hint was incorrect or unrelated                             | N/A                    |
| Click New Game after winning              | The game should reset all states and clear messages   | Win alert and history remained visible                          | N/A                    |

---

## 2. How did you use AI as a teammate?

### Which AI tools did you use on this project?

I used ChatGPT, Codex, and GitHub Copilot to help analyze bugs, understand code behavior, and improve my debugging process.

### Give one example of an AI suggestion that was correct.

AI helped identify that some bugs were related to state management and component re-rendering. I verified the suggestions by manually reproducing the issues, applying the suggested fixes, and confirming that the game behavior matched the expected result.

### Give one example of an AI suggestion that was incorrect or misleading.

Some AI suggestions did not fully match the actual code behavior. I verified them by comparing the suggested fix with my own debugging results and testing the application after applying changes. This showed me that AI suggestions still need to be reviewed and validated.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed by manually testing the user flow and running automated tests. I checked whether the original issue could still be reproduced after each change.

One test I ran was `python -m pytest tests/`. This helped identify whether my changes affected existing functionality and whether the code behavior matched the expected test cases.

AI helped me understand some tests by explaining what each test was checking and suggesting possible causes when a test failed.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the script from top to bottom whenever the user interacts with the application. Because of this behavior, variables created during execution do not automatically preserve their values between interactions.

Session state allows Streamlit applications to store information across reruns. It acts like a memory for the app, keeping values such as game progress, attempts, history, and user selections between interactions.

---

## 5. Looking ahead: your developer habits

### What is one habit or strategy from this project that you want to reuse?

I want to continue taking notes, listing bugs clearly, fixing issues one at a time, and testing after each change. I also want to make smaller Git commits for each task instead of grouping too many changes together. My preferred workflow is to first get an overview of the problem, investigate details, make fixes, and then review the whole system again with integration testing.

### What is one thing you would do differently next time when working with AI on a coding task?

Next time, I would ask AI to first analyze the entire project and create a list of possible bugs before making changes. I would compare AI's diagnosis with my own findings and evaluate how accurate the suggestions are. I would also create a separate Git branch for AI-generated fixes and compare the results against my step-by-step debugging approach.

### How did this project change the way you think about AI-generated code?

This project showed me that AI is a useful debugging partner, but it is not a replacement for understanding the code. AI can quickly identify possible issues and suggest solutions, but developers still need to verify the logic, test the changes, and make final decisions.
