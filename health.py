import openai
import streamlit as st

openai.api_key = st.secrets['openai_key']

st.title('AI Health Coach')

# Get user input
age = st.number_input('What is your age?', min_value=1, max_value=120)
weight = st.number_input('What is your weight (in kg)?', min_value=1.0)
height = st.number_input('What is your height (in cm)?', min_value=1.0)

if st.button('Get advice'):
    # Generate AI response
    response = openai.Completion.create(
      engine="text-davinci-0",  
      prompt=f"I am an AI health coach. You told me that you are {age} years old, weigh {weight} kg and are {height} cm tall. Here's my advice for you: ",
      temperature=0.5,
      max_tokens=100
    )

    # Display AI response
    st.write(response.choices[0].text.strip())
