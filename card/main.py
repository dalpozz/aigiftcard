import streamlit as st

def main():
    st.title("AI Gift Card")
    st.write("Welcome to the AI Gift Card app!")
    st.write("Enter your gift card code below:")
    code = st.text_input("Gift card code")
    if st.button("Check balance"):
        # Here you can add code to check the balance of the gift card
        st.write(f"The balance of gift card {code} is $50")

if __name__ == "__main__":
    main()


