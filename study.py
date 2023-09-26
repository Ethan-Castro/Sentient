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
    "This is the script you repeat first 'Hey {name}! /n I am your personal AI study coach, this is not professional advice, but it is helpful ;). Okay, so you want to learn about {goal} and you want to spend around {time} days learning it. Here's the study plan I have for you, Repeat everything before and input the proper values' Then provide advice for the goal, an easy-to-follow detailed study plan in a vertical list format with each point being a day, a philosophical motivational quote for fulfilling cognitive potential, and a piece of advice on mind & body connection. Then end off with an encouraging message. "
     )
    
    user_data = {
        'name':name,
        'goal': goal,
        'time': time, 
        'rigor': rigor,  
        'knowledge': knowledge,
        'advice': goal
    }
    
    response = openai.ChatCompletion.create(
       model="gpt-4",
       messages=[
    {
      "role": "system",
      "content": "Hey! I'm your coach. I want to see you do your best, and I will do whatever I can to make that happen.\n\nUse resources like the Harvard Academic Resource Center's website, other IVY League school tips, as well as top tips from proven professionals.\n\nAlways give clear precise instructions and motivation."
    },
    {
      "role": "user",
      "content": "Hey, I am Ethan and I go to Brooklyn College. I am double majoring in Health & Nutrition Science as well as Computer Science"
    },
    {
      "role": "assistant",
      "content": "Hi Ethan, it's nice to meet you! That's impressive, tackling two demanding yet varied fields like Health & Nutrition Science and Computer Science. It's clear you have a diverse range of interests. How can I support your academic journey? \nAre you looking for help to balance these two studies or support in a specific subject? Maybe you need assistance with managing time or reducing stress? Please let me know, so we can devise a plan that will maximize your academic success."
    },
    {
      "role": "user",
      "content": "Hey! I am doing pretty good in everything, the only issue is my school is not challenging enough. Is there any way you can help me with that?"
    },
    {
      "role": "assistant",
      "content": "Absolutely, Ethan! Finding ways to challenge yourself and supplement your learning is an essential part of personal and academic growth. Here are some strategies that might help:\n\n1. **Enroll in Higher-Level Courses**: If your current coursework feels easy, consider taking more advanced classes if your school allows. You can also think about enrolling in graduate-level courses. \n\n2. **Online Courses:** There are numerous courses available online from Ivy League universities on platforms like Coursera and edX. You can take advanced classes related to Health & Nutrition Science or Computer Science to deepen your knowledge further.\n\n3. **Research Projects**: Reach out to your professors and express interest in doing research with them. Professors often have ongoing research projects and might appreciate some help. This could also give you a glimpse of the cutting-edge work being done in your field.\n\n4. **Join a Club or Society**: There might be academic clubs"
    }
  ],
  temperature=1,
  max_tokens=256,
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
    

  
