import streamlit as st
from targeting_plan import targeting_plan_form
from utils import chat_with_user, get_faq_response, get_all_faqs
from audio_utils import speech_to_text, text_to_speech

def main():
    st.sidebar.title("Brandify.io Chatbot")

    # User API key input
    api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
    if not api_key:
        st.sidebar.warning("Please enter your API key to use the chatbot.")
        return

    # Navigation options
    choice = st.sidebar.radio("Navigate", ["Chat", "FAQs", "Targeting Plan"])

    if choice == "Chat":
        st.title("Chat with Brandify.io")
        st.write("You can either type your query or upload an audio file.")

        # Text input
        user_query = st.text_input("Type your query:")

        # Audio input
        # audio_file = st.file_uploader("Or upload an audio file (MP3/WAV format)", type=["mp3", "wav"])

        # if audio_file:
            # st.write("Processing your audio...")
            # with st.spinner("Transcribing audio to text..."):
                # user_query = speech_to_text(audio_file, api_key)
               # st.write("**Transcribed Text:**", user_query)

        if user_query:
            with st.spinner("Generating response..."):
                response = chat_with_user(user_query, api_key)
                st.write("**Bot Response:**", response)

                # Option to convert bot response to audio
                if st.checkbox("Convert response to audio"):
                    with st.spinner("Converting text to speech..."):
                        audio_response = text_to_speech(response, api_key)
                        st.audio(audio_response, format="audio/mp3")

    elif choice == "FAQs":
        st.title("Frequently Asked Questions")
        query = st.text_input("Search for a topic:")

        if query:
            response = get_faq_response(query)
            st.write("**Answer:**", response)
        else:
            st.subheader("All FAQs")
            faqs = get_all_faqs()
            for category, faq_list in faqs.items():
                st.markdown(f"### {category}")
                for faq in faq_list:
                    st.markdown(f"**Q:** {faq['question']}")
                    st.markdown(f"**A:** {faq['answer']}")
                    st.markdown("---")
                st.markdown("Do Check https://brandify.io/faq/ for more faqs")

    elif choice == "Targeting Plan":
        st.title("Targeting Plan")
        targeting_plan_form()

if __name__ == "__main__":
    main()
