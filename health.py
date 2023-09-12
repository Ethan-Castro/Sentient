import openai
import streamlit as st

openai.api_key = st.secrets['openai_key']

st.title('AI Health Coach')

# Get user input
male = -5
female = 161
sex = st.text_input('What is your sex? (male or female)')
age = st.number_input('What is your age?', min_value=1, max_value=100)
weight = st.number_input('What is your weight (in lbs)?', min_value=1.0)
height = st.number_input('What is your height (inches)?', min_value=1.0)
goal = st.text_input('What is your goal (can be anything health related)?')
activity = st.number_input('Rate your activity level from sedentary to very active (from 1.2 - 1.9)?', min_value=1.2)
bmi = weight / (height * height) * 703
bmr = 10 * weight + 6.25 * height - 5 * age - sex
tdee = bmr * sex


if st.button('Get advice'):
    # Generate AI response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"I am an AI health coach. You told me that you are {age} years old, weigh {weight} lbs, are {height} in tall, and your goal is {goal}. Here's your BMI {bmi} , TDEE or total daily energy expenditure {tdee}, and some advice.: ",
        temperature=0.5,
        max_tokens=100
    )

    print(response)  # Debug print statement

    if response.choices:
        print(response.choices[0])  # Debug print statement
        print("Your BMR is:", bmr)

if 'text' in response.choices[0]:
            # Display AI response
            st.write(response.choices[0].text.strip())
  
