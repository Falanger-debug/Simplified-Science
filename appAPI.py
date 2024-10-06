"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyBR4_Ii_2ACCGN2QsSDTaKJCAd8khYRYgI")

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

promptAddition = ' Musisz być tego pewny, postaraj się. Bez znaków specjalnych'

def getTitle(link):
    prompt = "Powiedz mi tytuł tego czegoś. Sam tytuł."

    response = chat_session.send_message(prompt + promptAddition + link)
    return response.text

def getTestObject(link):
    prompt = "Tell me what the test object is"

    response = chat_session.send_message(prompt + promptAddition + link)
    return response.text

def getExperimentGoal(link):
    prompt = "Tell me what the goal of the experiment is"

    response = chat_session.send_message(prompt + promptAddition + link)
    return response.text

def askChat(message):
    prompt = "mam pytanie."

    response = chat_session.send_message(prompt + promptAddition + message)
    return response.text

