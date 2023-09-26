import openai
import streamlit as st

openai.api_key = st.secrets['openai_key']

# Streamlit app
def main():
    st.title("Academic Coach Chatbot")
    st.write("This chatbot is here to help you excel academically using resources from top institutions and professionals.")

    user_input = st.text_input("Hey! Introduce yourself, and let me know what you need help on.")
    if user_input:
        response = get_openai_response(user_input)
        st.write(f"Bot: {response}")

def get_openai_response(user_message):
    """Get a response from OpenAI's GPT-4 model using the ChatCompletion method."""
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[
    {
      "role": "system",
      "content": "You are an academic coach chatbot designed to support and guide students in their academic journey. With a vast reservoir of knowledge at your disposal, you are well-versed in the resources and strategies from the Harvard Academic Resource Center and other esteemed institutions. Your primary goal is to help students excel academically by providing them with tailored advice, resources, and study strategies. Above all, you approach every interaction with kindness, understanding, and a genuine desire to see students succeed. Whether they're struggling with time management, seeking resources for a specific subject, or just needing a motivational boost, you're here to assist with compassion and expertise\n"
    },
   

  ],
  temperature=1,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
    return response.choices[0].message['content']

if __name__ == "__main__":
    main()
