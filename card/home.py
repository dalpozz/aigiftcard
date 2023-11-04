import streamlit as st
import streamlit.components.v1 as components

stripe_js = """<script async
  src="https://js.stripe.com/v3/buy-button.js">
</script>

<stripe-buy-button
  buy-button-id="buy_btn_1O8mmzHAXdK6842ASqRSyEH5"
  publishable-key="{}"
>
</stripe-buy-button>
""".format(st.secrets["stripe_publishable_key"])


def main():
    st.title("AI Gift Card")
    st.subheader("Welcome to the AI Gift Card app!")
    
    st.write("Enter your gift card code below to check your balance or generate a new gift card:")
    code = st.text_input("Gift card code")
    if st.button("Check balance"):
        # Here you can add code to check the balance of the gift card
        st.write(f"The balance of gift card {code} is $50")

    components.html(html=stripe_js, height=300)


if __name__ == "__main__":
    main()


