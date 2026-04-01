import streamlit as st
import random

# Title
st.title("✊✋✌️ Rock Paper Scissors Game")

st.write("Choose Rock, Paper, or Scissors and play against the computer!")

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Initialize score in session state
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "draw_score" not in st.session_state:
    st.session_state.draw_score = 0

# User choice
user_choice = st.selectbox("Select your choice:", choices)

# Play button
if st.button("Play"):
    computer_choice = random.choice(choices)

    st.subheader(f"🖥️ Computer chose: {computer_choice}")
    st.subheader(f"🙋 You chose: {user_choice}")

    # Game logic
    if user_choice == computer_choice:
        st.info("🤝 It's a Draw!")
        st.session_state.draw_score += 1

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.success("🎉 You Win!")
        st.session_state.user_score += 1

    else:
        st.error("😢 Computer Wins!")
        st.session_state.computer_score += 1

# Scoreboard
st.markdown("## 🏆 Scoreboard")
st.write(f"🙋 Your Score: {st.session_state.user_score}")
st.write(f"🖥️ Computer Score: {st.session_state.computer_score}")
st.write(f"🤝 Draws: {st.session_state.draw_score}")

# Reset button
if st.button("Reset Score"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.draw_score = 0
    st.success("🔄 Scores reset successfully!")