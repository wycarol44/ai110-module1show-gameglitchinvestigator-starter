# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

### Prior Refactoring Work

**What task did you give the agent?**

I asked AI tools to help analyze and refactor the game's logic: move core game logic out of `app.py` into `logic_utils.py`, improve `parse_guess` and `update_score`, correct hint generation, ensure difficulty selection updates the allowed range/attempts, and suggest unit tests for edge cases.

**What did the agent do?**

- Suggested refactors and code snippets for parsing input and scoring.
- Recommended using Streamlit session state (`st.session_state`) to persist the secret number and game state across reruns.
- Provided example unit test ideas for `parse_guess` and `update_score`.
- Assisted with small wording and README updates that were incorporated.

**Relevant commits (high level):**

- `e714352` — moved `check_guess` logic from `app.py` to `logic_utils.py`.
- `4e1cc18` / `78840f2` / `326ff04` — refactored `update_score`, enhanced `parse_guess`, and moved difficulty range logic to utilities.
- `7dc5fde` / `ec23c44` — updated hint messages and fixed attempts display discrepancies.
- `ce5e603` / `2a98780` / `b9d7255` — added an architecture diagram and project documentation updates.

(Full recent commit list was consulted when writing this log.)

**What did you have to verify or fix manually?**

- Ensured `st.session_state` usage was correct and did not introduce duplicate state updates.
- Reviewed and adjusted AI-proposed code to fit the project's existing conventions and tests.
- Validated hint logic against the secret number flow and fixed edge-case scoring behaviors.
- Ran and reviewed unit tests to confirm changes did not break expected behavior.

---

### High Score Tracker Feature (New)

**What task did you give the agent?**

Build a "High Score" tracker feature that:
- Persists scores to a CSV file (one score per game win)
- Displays top 5 scores for each difficulty in the sidebar
- Checks if a newly won game score qualifies as a high score
- Shows special congratulations when a high score is achieved
- Includes comprehensive unit tests for all score-tracking functions

**Files created/modified:**

- **Created:** `score_tracker.py` — Core module with functions: `load_high_scores()`, `save_score()`, `is_high_score()`
- **Created:** `tests/test_score_tracker.py` — 10 comprehensive unit tests covering file I/O, sorting, filtering, and edge cases
- **Modified:** `app.py` — Added score_tracker imports, sidebar display of top scores per difficulty, and logic to save scores on win and show "⭐ NEW HIGH SCORE!" message if applicable

**What did the agent do?**

- Proposed a CSV-based persistence approach with timestamp logging.
- Designed the module API: `load_high_scores(difficulty, limit)`, `save_score(score, difficulty)`, `is_high_score(score, difficulty, limit)`.
- Suggested test cases covering: file creation, score sorting, difficulty filtering, limits, and edge cases (empty file, below limit, at limit).
- Proposed the sidebar display logic and the win-screen high score check.

**Test results:**

All 10 new score_tracker tests pass; all 30 total project tests pass (20 existing + 10 new).

```
============================== 30 passed in 0.05s ==============================
```

**What did you have to verify or fix manually?**

- Verified the CSV module import and file-handling logic.
- Tested that the sidebar score display renders correctly (initially coded to use `st.metric()` which required tweaking for readability).
- Confirmed that `save_score()` is called only on win (not on lose or reset).
- Ensured the "NEW HIGH SCORE!" message displays conditionally based on `is_high_score()` logic.
- Manually ran all tests locally to ensure backward compatibility with existing logic and no import conflicts.
- Adjusted the sidebar layout so top scores don't crowd the difficulty selector.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Non-numeric input | "Generate pytest for parse_guess to handle non-numeric input" | Assert parse_guess returns None or proper error for non-numeric inputs | Yes | Tests ensure input validation handles strings gracefully |
| Out-of-range guess | "Test guessing values outside difficulty range" | Assert guesses outside range are handled and attempts decrement appropriately | Yes | Confirms range enforcement and that scoring/attempts behave correctly |
| Boundary guesses (min/max) | "Add tests for boundary values" | Assert correct hint/score for guessing the exact min or max | Yes | Verifies inclusive range behavior and scoring on edge guesses |
| CSV file creation | "How should I test file I/O for a score persistence module?" | Assert save_score creates the CSV file if it doesn't exist, and properly formats headers | Yes | Ensures robust file handling and data structure |
| High score sorting | "Generate tests for sorting scores in descending order" | Assert load_high_scores returns scores sorted by highest first | Yes | Confirms users see the best scores at the top of the leaderboard |
| Score filtering by difficulty | "Test filtering scores by game difficulty" | Assert load_high_scores(difficulty='Easy') returns only Easy scores | Yes | Verifies difficulty isolation so leaderboards are fair |
| High score qualification | "Test whether a new score qualifies as a high score" | Assert is_high_score returns True/False based on top-N ranking | Yes | Validates the eligibility check before showing the "NEW HIGH SCORE!" message |

Test summary: 20 existing tests + 10 new score_tracker tests = 30 total, all passing.

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
Help me make this Python function clearer and more idiomatic. Please suggest formatting and small refactors.
```

**Linting output before:**

```
Minor readability issues and a few unused imports in `logic_utils.py` and `app.py` (warnings fixed during refactor).
```

**Changes applied:**

- Simplified some helper functions and removed duplicated logic after consolidating code into `logic_utils.py`.
- Standardized error/edge-case handling for `parse_guess`.
- Minor README wording improvements suggested by AI were applied.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

Ask each model to propose a refactor that extracts guess-parsing and scoring logic from `app.py` into `logic_utils.py`, and to provide unit test ideas for edge cases.

| | Model A | Model B |
|-|---------|---------|
| **Model name** | GitHub Copilot | ChatGPT (GPT-family) |
| **Response summary** | Quick inline code suggestions and small edits tied to local context | Higher-level design suggestions, explanations, and test-generation prompts |
| **More Pythonic?** | Often yes for small snippets | Yes for design and explicit safety checks |
| **Clearer explanation?** | Moderate (code-first) | High (rationale + examples) |

**Which did you prefer and why?**

I used both: Copilot for quick inline suggestions while editing files in the editor, and ChatGPT for broader design recommendations, test prompts, and explanation. Both were helpful; I reviewed and adapted each suggestion rather than accepting them blindly.
