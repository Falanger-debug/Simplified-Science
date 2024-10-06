"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyCM-tmQs9JfNew-DKu7XoieaKAXcLDjVto")

# Create the model configuration
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-002",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# Start a chat session
chat_session = model.start_chat(
    history=[
        # You can include previous messages here if needed
    ]
)

promptAddition = """
Do not use any special characters such as "*", "#", etc. Write in plain text and do not format the text in any way. 
Start your answer right away, without any "hey", "I see", or other initial inserts.
Do not suggest the user to look for information in other sources or provide links. 
Provide a full answer to the question, based only on the available material. 
Answers MUST BE ABSOLUTELY VALID, concise and clear and contain the most important information about the experiment.
After entering the page, compare the source address with the following one. 
If you are not on the correct page, then keep looking, but if you are on the correct page, then give me an answer.
To answer, search ONLY the page provided to you as a link"""

def getTitle(link):
    prompt = """
    I want to know the exact title of the article without any changes.
Be honest and provide the title without additional comments.
I want the chat to provide the title itself, without quotation marks, without ANY additional words, ONLY the title."""

    response = chat_session.send_message(prompt + promptAddition + link)
    return response.text

def getTestObject(link):
    prompt = """
    Provide a detailed description of the test object in the experiment, including its characteristics, purpose, and any relevant information related to the study.
    """

    response = chat_session.send_message(prompt + promptAddition + link)
    return response.text

def getExperimentGoal(link):
    prompt = """
    Please explain the main objective of this experiment, focusing on the scientific goals and the significance of the research
    """

    response = chat_session.send_message(prompt + promptAddition + link)
    return response.text

def getExperimentEnvironment(link):
    prompt = """
        Describe the environment in which the experiment takes place, including any specific conditions like temperature, humidity, gravity, and the use of specialized equipment. 
        Mention whether the experiment was conducted in space or on Earth, and specify any unique constraints or challenges related to the environment that could affect the experiment's outcome.
    """

    response = chat_session.send_message(prompt + promptAddition + link)
    return response.text

def askChat(message):
    prompt = "I have a question."

    response = chat_session.send_message(prompt + promptAddition + message)
    return response.text

#print(getTitle("https://osdr.nasa.gov/bio/repo/data/studies/OSD-665"))
#print(getTestObject("https://osdr.nasa.gov/bio/repo/data/studies/OSD-379"))
#print(getExperimentGoal("https://osdr.nasa.gov/bio/repo/data/studies/OSD-665"))
#print(getExperimentEnvironment("https://osdr.nasa.gov/bio/repo/data/studies/OSD-665"))

#askChat("tell me something about that")