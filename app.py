import pickle
import streamlit as st

# Load the phishing model
loaded_model = pickle.load(open('phishing.pk1', 'rb'))

# Function to predict whether a URL is malicious or not
def predict(url):
    # Make prediction
    prediction = loaded_model.predict([url])
    st.write("Prediction:", prediction)
    # Return the prediction result
    return prediction[0]

def main():
    # Set page title and favicon
    st.set_page_config(page_title="Phishing URL Detection App", page_icon="🔒")

    # Add title and description
    st.title("Phishing URL Detection App")
    st.write("This app predicts whether a URL is malicious or not.")

    # Add image
    image = st.image("img.png", caption="Phising Website Detection", use_column_width=True)

    # Textbox input for URL
    url = st.text_input("Enter a URL:", "")

    # Add prediction button
    if st.button("Predict"):
        if url:
            # Call the predict function
            prediction = predict(url)
            # Display prediction result
            if prediction == "bad":
                st.error(f"The URL '{url}' is malicious (phishing).")
            else:
                st.success(f"The URL '{url}' is safe (legitimate).")

    # Add bullet points
    st.subheader("How to Protect Your Computer")
    st.markdown("""
    - **Keep Your Firewall Turned On:** A firewall helps protect your computer from hackers who might try to gain access to crash it, delete information, or even steal passwords or other sensitive information. Software firewalls are widely recommended for single computers. The software is prepackaged on some operating systems or can be purchased for individual computers. For multiple networked computers, hardware routers typically provide firewall protection.

    - **Install or Update Your Antivirus Software:** Antivirus software is designed to prevent malicious software programs from embedding on your computer. If it detects malicious code, like a virus or a worm, it works to disarm or remove it. Viruses can infect computers without users’ knowledge. Most types of antivirus software can be set up to update automatically.

    - **Install or Update Your Antispyware Technology:** Spyware is just what it sounds like—software that is surreptitiously installed on your computer to let others peer into your activities on the computer. Some spyware collects information about you without your consent or produces unwanted pop-up ads on your web browser. Some operating systems offer free spyware protection, and inexpensive software is readily available for download on the Internet or at your local computer store. Be wary of ads on the Internet offering downloadable antispyware—in some cases, these products may be fake and may actually contain spyware or other malicious code. It’s like buying groceries—shop where you trust.

    - **Keep Your Operating System Up to Date:** Computer operating systems are periodically updated to stay in tune with technology requirements and to fix security holes. Be sure to install the updates to ensure your computer has the latest protection.

    - **Be Careful What You Download:** Carelessly downloading e-mail attachments can circumvent even the most vigilant anti-virus software. Never open an e-mail attachment from someone you don’t know, and be wary of forwarded attachments from people you do know. They may have unwittingly advanced malicious code.

    - **Turn Off Your Computer:** With the growth of high-speed Internet connections, many opt to leave their computers on and ready for action. The downside is that being “always on” renders computers more susceptible. Beyond firewall protection, which is designed to fend off unwanted attacks, turning the computer off effectively severs an attacker’s connection—be it spyware or a botnet that employs your computer’s resources to reach out to other unwitting users.
    """)

if __name__ == "__main__":
    main()
