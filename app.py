import streamlit as st
import pickle

# Load model & vectorizer
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.title("📩 Spam Message Detector")
st.write("Enter a message and check if it's **Spam** or **Ham**.")

# Input box
user_input = st.text_area("Type your message here:")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message first.")
    else:
        # Transform input & predict
        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)[0]

        if prediction == "spam":
            st.error("🚨 This looks like **SPAM**!")
        else:
            st.success("✅ This looks like **HAM** (not spam).")
