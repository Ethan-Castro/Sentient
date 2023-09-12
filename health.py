import openai
import streamlit as st

openai.api_key = st.secrets['openai_key']

st.title('AI Health Coach')

# Get user input
sex = st.number_input('What is your sex? (if male put -5 or female put 161)', min_value = -5, max_value = 161)
age = st.number_input('What is your age?', min_value=1, max_value=100)
weight = st.number_input('What is your weight (in lbs)?', min_value=1.0)
height = st.number_input('What is your height (inches)?', min_value=1.0)
goal = st.text_input('What is your goal (can be anything health related)?')
activity = st.number_input('Rate your activity level from sedentary to very active (from 1.2 - 1.9)?', min_value= 1.2, max_value = 1.9)
bmi = weight / (height * height) * 703
bmr = 10 * weight + 6.25 * height - 5 * age - sex
tdee = bmr * sex


if st.button('Get advice'):
    # Generate AI response

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
                   " I am an AI health coach. You told me that you are {age} years old, weigh {weight} lbs, are {height} in tall, and your goal is {goal}. Here's your BMI {bmi} , TDEE or total daily energy expenditure {tdee}, and some advice. repeat the first part then put your own advice: "

    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)  # Debug print statement

if response.choices:
        print(response.choices[0])  # Debug print statement
        print("Your BMR is:", bmr)

if 'text' in response.choices[0]:
            # Display AI response
            st.write(response.choices[0].text.strip())
  
