import streamlit as st
import random
import string

# --- Password Strength Function ---
def check_strength(pw):
    symbols = "!#$%&()*+"
    length = len(pw)
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_num = any(c.isdigit() for c in pw)
    has_sym = any(c in symbols for c in pw)
    score = sum([has_upper, has_lower, has_num, has_sym])

    if length < 8:
        return "Weak"
    elif score >= 3 and length >= 10:
        return "Strong"
    else:
        return "Medium"

# --- Streamlit UI ---
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

st.title(" Random Password Generator")
st.write("Generate a secure password and check its strength instantly!")

# User input: length & difficulty
length = st.slider("Select Password Length", min_value=6, max_value=20, value=10)
include_symbols = st.checkbox("Include Symbols (!, #, $, etc.)", value=True)
include_numbers = st.checkbox("Include Numbers (0–9)", value=True)

# Generate button
if st.button("Generate Password"):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += "!#$%&()*+"

    password = "".join(random.choice(characters) for _ in range(length))
    strength = check_strength(password)

    # Show results
    st.success(f"Your Password: `{password}`")
    if strength == "Strong":
        st.markdown(f"**Strength:** 🟢 {strength}")
    elif strength == "Medium":
        st.markdown(f"**Strength:** 🟡 {strength}")
    else:
        st.markdown(f"**Strength:** 🔴 {strength}")

# Footer
st.markdown("---")
st.caption("Made by Sabreen using Python & Streamlit")
