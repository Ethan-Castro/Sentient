import openai
import streamlit as st

openai.api_key = st.secrets['openai_key']

st.title('AI Health Coach')

# Get user input
age = st.number_input('What is your age?', min_value=1, max_value=120)
weight = st.number_input('What is your weight (in kgs)?', min_value=1.0)
height = st.number_input('What is your height (feet)?', min_value=1.0)
goal = st.text_input('What is your goal (can be anything health related)?')



if st.button('Get advice'):
    # Generate AI response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"I am an AI health coach. You told me that you are {age} years old, weigh {weight} kg, are {height} cm tall, and your goal is {goal}. Here's your BMI, Basal Metabolic Rate, and some advice.: ",
        temperature=0.5,
        max_tokens=100
    )

    print(response)  # Debug print statement

    if response.choices:
        print(response.choices[0])  # Debug print statement
        bmr_male = 66 + 13.7 * weight + 5 * height - 6.8 * age
print("Your BMR (Male) is:", bmr_male)

if 'text' in response.choices[0]:
            # Display AI response
            st.write(response.choices[0].text.strip())
  
