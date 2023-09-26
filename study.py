import openai
import streamlit as st

openai.api_key = st.secrets['openai_key']

# Streamlit app
def main():
    st.title("Academic Coach Chatbot")
    st.write("This chatbot is here to help you excel academically using resources from top institutions and professionals.")

    user_input = st.text_input("Ask your academic-related question:")
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
                "content": "Hey! I'm your coach. I want to see you do your best, and I will do whatever I can to make that happen.\n\nUse resources like the Harvard Academic Resource Center's website, other IVY League school tips, as well as top tips from proven professionals.\n\nAlways give clear precise instructions and motivation."
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message['content']

if __name__ == "__main__":
    main()
