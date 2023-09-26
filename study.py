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
      "content": "I am your academic coach. I want to see you succeed. How can I help?\n\n"
    },
    {
      "role": "user",
      "content": "Hey, I currently go to --- College and I need help with ---"
    }
    
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
