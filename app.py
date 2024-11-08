import streamlit as st
from prompt_generator import create_prompt
from generate_poem import generate_poem

# Streamlit UI
st.title("Poetry Generator")
st.write("Generate beautiful poetry based on a theme of your choice!")

# User input for theme and form
theme = st.text_input("Enter a theme for the poem:")
form = st.selectbox("Choose a form:", ["poem", "haiku"])

# Button to generate the poem
if st.button("Generate"):
    if theme:
        # Generate the prompt and poem
        prompt = create_prompt(theme, form)
        poem = generate_poem(prompt, max_length=20 if form == "haiku" else 50)
        st.subheader("Generated Poem:")
        st.write(poem)
    else:
        st.error("Please enter a theme for the poem.")

