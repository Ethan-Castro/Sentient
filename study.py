import openai
import streamlit as st

openai.api_key = st.secrets['openai_key']

st.title('Personal Study Coach by Ethan Castro')

# Get user input
goal = st.text_input('What topic or subject do you want to study (literally anything!)?')
time = st.number_input('How long do you want your study plan to be? (days)', min_value=1, max_value=365)
rigor = st.number_input('How rigorous do you want this to be easy (1) to very rigorous (10)?', min_value=1, max_value=10)
knowledge = st.number_input('How much do you already know nothing (1) to practically an expert (10)?', min_value=1, max_value=10)
goal = st.text_input('What is your goal (can be career, mastery, money or related to something else)?')
name = st.text_input('What is your name so I know who I am talking to?')

if st.button('Get advice'):
    # Generate AI response

    prompt_template = (
    "This is the script you repeat first 'Hey {name}! /n I am your personal AI study coach, this is not professional advice, but it is helpful ;). Okay, so you want to learn about {goal} and you want to spend around {time} days learning it. Here's the study plan I have for you, Repeat everything before and input the proper values' Then provide advice for the goal, an easy-to-follow detailed study plan in a list format, a philosophical motivational quote for fulfilling cognitive potential, and a piece of advice on mind & body connection. Then end off with an encouraging message. "
     )
    
    user_data = {
        'name':name,
        'goal': goal,
        'time': time, 
        'rigor': rigor,  
        'knowledge': knowledge,
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
    
    
### if response.choices:
#            print(response.choices[0])  # Debug print statement
#            print("Your BMR is:", bmr)
    
    if 'text' in response.choices[0]:
                # Display AI response
                st.write(response.choices[0].text.strip())
    

  
