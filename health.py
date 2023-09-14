import openai
import streamlit as st

openai.api_key = st.secrets['openai_key']

st.title('Personal AI Health Coach')

# Get user input
sex = st.number_input('What is your sex? (if male put -5 or female put 161)', min_value = -5, max_value = 161)
age = st.number_input('What is your age?', min_value=1, max_value=100)
weight = st.number_input('What is your weight (in lbs)?', min_value=1)
height = st.number_input('What is your height (inches)?', min_value=1)
goal = st.text_input('What is your goal (can be anything health related)?')
activity = st.number_input('Rate your activity level from sedentary to very active (from 1.2 - 1.9)?', min_value= 1.2, max_value = 1.9)
bmi = weight / (height * height) * 703
bmr = 10 * weight + 6.25 * height - 5 * age - sex
tdee = bmr * activity



if st.button('Get advice'):
    # Generate AI response

     prompt_template = (
    "REPEAT THIS SCRIPT before everytime with the sex, age, weight, height, goal, activity, that the USER puts. if it's in brackets put the value they put not the actual word. I am an AI health coach, this is not medical advice. Ok so, you are {age} years old, weigh {weight} lbs, "
    "are {height} inches tall, and your goal is {goal}. Here's your BMI {bmi}, TDEE or total daily energy expenditure {tdee} calories, Repeat everything before and input the proper values"
    "after doing above: provide a brief easy-to-follow detailed exercise routine, a philosophical motivational quote, a piece of nutrition psychology advice, healthy snacks, and words for consistency. "
    "{advice}."
     )

    user_data = {
    'age': age,  # Example age
    'weight': weight,  # Example weight in lbs
    'height': height,  # Example height in inches
    'goal': goal,  # Example goal
    'bmi': bmi,  # Example BMI value
    'tdee': tdee,  # Example TDEE value
    'advice': goal
}

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt = prompt_template.format(**user_data),
      temperature=.5,
      max_tokens=500,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    
# You can then format this prompt with the specific details:

prompt = prompt_template.format(**user_data)
print(response)  # Debug print statement


if response.choices:
        print(response.choices[0])  # Debug print statement
        print("Your BMR is:", bmr)

if 'text' in response.choices[0]:
            # Display AI response
            st.write(response.choices[0].text.strip())


  

