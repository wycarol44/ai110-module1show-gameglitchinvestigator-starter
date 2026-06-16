import random
import streamlit as st
from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score
from score_tracker import load_high_scores, save_score, is_high_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
    key="difficulty_select",
)

# Display high scores for current difficulty
st.sidebar.header("🏆 Top Scores")
top_scores = load_high_scores(difficulty=difficulty, limit=5)
if top_scores:
    for rank, (score, diff, timestamp) in enumerate(top_scores, 1):
        st.sidebar.metric(f"#{rank}", f"{score} pts", f"{diff} • {timestamp}")
else:
    st.sidebar.caption("No scores yet for this difficulty!")

attempt_limit_map = {
    "Easy": 8,
    "Normal": 6,
    "Hard": 5,
}

low, high = get_range_for_difficulty(difficulty)
attempt_limit = attempt_limit_map[difficulty]

if "last_difficulty" in st.session_state and st.session_state.last_difficulty != difficulty:
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.secret = random.randint(low, high)
    st.session_state.last_difficulty = difficulty
    st.rerun()

if "last_difficulty" not in st.session_state:
    st.session_state.last_difficulty = difficulty

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "show_hint" not in st.session_state:
    st.session_state.show_hint = True

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

guess_key = f"guess_input_{difficulty}"
raw_guess = st.text_input("Enter your guess:", key=guess_key)
current_guess = st.session_state.get(guess_key, raw_guess)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    st.checkbox("Show hint", key="show_hint", value=st.session_state.show_hint)

if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.score = 0
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    submitted_guess = st.session_state.get(guess_key, raw_guess)
    st.session_state.history = list(st.session_state.history) + [submitted_guess]
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(submitted_guess)

    if not ok:
        st.error(err)
    else:

        if st.session_state.attempts % 2 == 0:
            secret = str(st.session_state.secret)
        else:
            secret = st.session_state.secret

        outcome, message = check_guess(guess_int, secret)

        if st.session_state.show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            
            # Save score and check if it's a high score
            save_score(st.session_state.score, difficulty)
            if is_high_score(st.session_state.score, difficulty):
                st.success(
                    f"🎉 You won! The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score} ⭐ NEW HIGH SCORE!"
                )
            else:
                st.success(
                    f"You won! The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score}"
                )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

st.caption("Guess history")
if st.session_state.history:
    st.write(st.session_state.history)
else:
    st.write("No guesses yet.")

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
