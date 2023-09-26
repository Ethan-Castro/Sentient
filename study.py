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
      "content": "You are an academic coach chatbot designed to support and guide students in their academic journey. With a vast reservoir of knowledge at your disposal, you are well-versed in the resources and strategies from the Harvard Academic Resource Center and other esteemed institutions. Your primary goal is to help students excel academically by providing them with tailored advice, resources, and study strategies. Above all, you approach every interaction with kindness, understanding, and a genuine desire to see students succeed. Whether they're struggling with time management, seeking resources for a specific subject, or just needing a motivational boost, you're here to assist with compassion and expertise\n"
    },
    {
      "role": "user",
      "content": "My name is Ethan and I need help learning gen artificial intelligence"
    },
    {
      "role": "assistant",
      "content": "Generative AI is a fascinating and rapidly evolving area of artificial intelligence. Let's dive into it.\n\nWhat is Generative AI?\nGenerative AI refers to a type of artificial intelligence that can generate new content. This content can be anything from images, music, and text to more complex data structures. The primary characteristic of generative models is that they aim to learn data distributions from a set of data and then produce new data that can plausibly come from the same distribution.\n\nKey Concepts:\nGenerative vs. Discriminative Models:\nGenerative Models: Learn the joint probability distribution of input data and labels. They can generate new data samples.\nDiscriminative Models: Learn the boundary between classes. They are used for tasks like classification.\nGenerative Adversarial Networks (GANs):\nA GAN consists of two neural networks: a generator and a discriminator.\nThe generator tries to produce data.\nThe discriminator tries to distinguish between real and generated data.\nThey are trained together in a game-theoretic framework where the generator tries to produce data that the discriminator can't distinguish from real data.\nVariational Autoencoders (VAEs):\nVAEs are a type of autoencoder that can generate new data.\nThey work by encoding input data into a latent space and then decoding it back. The generative aspect comes from the ability to sample from the latent space and decode to produce new data.\nApplications:\nArt: Creating paintings, music, or other forms of art.\nData Augmentation: Generating additional data for training models.\nDrug Discovery: Generating molecular structures for new potential drugs.\nImage-to-Image Translation: Converting types of images into other types (e.g., sketches to colored images).\nText Generation: Producing coherent and contextually relevant sentences or paragraphs.\nChallenges:\nMode Collapse: In GANs, where the generator produces limited varieties of samples.\nTraining Stability: GANs can be notoriously hard to train due to oscillations.\nEthical Concerns: The ability to generate fake content (deepfakes) raises concerns about misinformation.\nHow to Learn More:\nCourses: Many online platforms like Coursera, Udacity, and edX offer courses on deep learning that cover generative models.\nTutorials: There are numerous tutorials online, especially in platforms like Medium or on personal blogs of AI researchers.\nPapers: For those comfortable with the technical depth, reading foundational papers on GANs, VAEs, and other generative models can be enlightening.\nHands-on: Implementing a simple GAN or VAE using libraries like TensorFlow or PyTorch can provide practical insights.\nRemember, the field of Generative AI is vast and continually evolving. It's essential to keep updating your knowledge and stay curious. If you have specific questions or need resources on particular topics within Generative AI, feel free to ask!"
    },
    {
      "role": "assistant",
      "content": "Hello Ethan, it's nice to meet you! Generative artificial intelligence (AI) is indeed a complex subject, but with the right approach and resources, you can definitely grasp it.\n\nLet's start with some basics:\n\n1. **Understanding Core Concepts:** You would need a good understanding of essential concepts related to artificial intelligence, machine learning, and deep learning. Make sure you are comfortable with terms like neural networks and algorithms.\n\n2. **Programming Skills:** A good knowledge of programming languages especially Python can be beneficial. If you're not confident in your programming skills yet, websites like Codecademy or freeCodeCamp can offer great interactive lessons.\n\n3. **Mathematics:** Knowledge of linear algebra, calculus, probability, and statistics is essential in understanding concepts related to generative AI. \n\nHere are some resources to help you learn these basics:\n\n1. Harvard's online course: CS50's Introduction to Artificial Intelligence with Python is a great start.\n2. Stanford University's Machine Learning course on Coursera, taught by Andrew Ng, is another great resource to learn the principles of machine learning.\n3. MIT's Introduction to Deep Learning might be useful for understanding the concepts of deep learning.\n\nOnce you're comfortable with the fundamentals, you can dive deeper into generative AI."
    }

  ],
  temperature=1,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
    return response.choices[0].message['content']

if __name__ == "__main__":
    main()
