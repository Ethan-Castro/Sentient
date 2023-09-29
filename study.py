import openai
import streamlit as st

openai.api_key = st.secrets['openai_key']


# Initialize or update Streamlit session state for maintaining conversation history
if 'messages' not in st.session_state:
    st.session_state.messages = [
    {
        "role": "system",
        "content": "You are an academic coach chatbot designed to support and guide students in their academic journey. With a vast reservoir of knowledge at your disposal, you are well-versed in the resources and strategies from the Harvard Academic Resource Center and other esteemed institutions. Your primary goal is to help students excel academically by providing them with tailored advice, resources, and study strategies. Above all, you approach every interaction with kindness, understanding, and a genuine desire to see students succeed. Whether they're struggling with time management, seeking resources for a specific subject, or just needing a motivational boost, you're here to assist with compassion and expertise."
    },
    {
        "role": "user",
        "content": "I need help with precalculus."
    },
    {
    "role": "assistant",
    "content": "I can most def help with that! Whether you’re struggling with limits, derivatives, integrals, or any other calculus topics, feel free to ask, and I’ll do my best to assist you. If you have a specific question or topic in mind, please provide more details, and I can offer more tailored support or resources.\nIf you're looking for general advice or resources, here are a few suggestions:\nUnderstand the Basics: Make sure you have a solid understanding of the fundamental concepts of calculus such as limits, continuity, and derivatives before moving on to more advanced topics.\nPractice Problems: Regularly solving problems is crucial in calculus. Textbooks, online resources, and calculus apps often have a variety of problems to work through.\nOnline Resources: Websites like Khan Academy and Coursera offer free courses on calculus, which can help supplement your learning.\nStudy Groups: Collaborating with peers can provide different perspectives and can be helpful for understanding challenging concepts.\nOffice Hours: Utilizing professor or TA office hours can be beneficial for clarifying doubts and receiving additional support.\nLet me know how you would prefer to proceed, and I'll do my best to assist you!"
}

]

def main():
    st.title("Academic Coach Chatbot")
    st.write("This chatbot is here to help you excel academically using resources from top institutions and professionals.")
    
    user_input = st.text_input("Hey! Introduce yourself, and let me know what you need help on.")
    if user_input:
        # Append user's message to the conversation history
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })
        
        response_content = get_openai_response(user_input)
        
        # Append bot's response to the conversation history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response_content
        })
        
        st.write(f"{response_content}")

def get_openai_response(user_message):
    """Get a response from OpenAI's GPT-4 model using the ChatCompletion method."""
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=st.session_state.messages,  # Use the maintained conversation history for context
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message['content']

if __name__ == "__main__":
    main()





