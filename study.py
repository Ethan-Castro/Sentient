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
      "content": "Absolutely, Ethan! Finding ways to challenge yourself and supplement your learning is an essential part of personal and academic growth. Here are some strategies that might help:\n\n1. **Enroll in Higher-Level Courses**: If your current coursework feels easy, consider taking more advanced classes if your school allows. You can also think about enrolling in graduate-level courses. \n\n2. **Online Courses:** There are numerous courses available online from Ivy League universities on platforms like Coursera and edX. You can take advanced classes related to Health & Nutrition Science or Computer Science to deepen your knowledge further.\n\n3. **Research Projects**: Reach out to your professors and express interest in doing research with them. Professors often have ongoing research projects and might appreciate some help. This could also give you a glimpse of the cutting-edge work being done in your field.\n\n4. **Join a Club or Society**: There might be academic clubs at your college related to your fields of study. If not, you can also look outside your school for professional societies.\n\n5. **Compete**: Intellectual competitions like Hackathons or Nutrition Science debates can be highly stimulating. They challenge you to apply what you've learned in novel ways.\n\n6. **Teach or Tutor**: Explaining concepts to others is one"
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
