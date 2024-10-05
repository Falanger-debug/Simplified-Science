"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyArNS7cIvztvHVwPjGgpXJVpbwj_8dJ6MY")

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

def getTitle(link):
    prompt = "Tell me what the title of the article is. Be honest"

    response = chat_session.send_message(prompt + link)
    return response.text

def getTestObject(link):
    prompt = "Tell me what the test object is"

    response = chat_session.send_message(prompt + link)
    return response.text

def getExperimentGoal(link):
    prompt = "Tell me what the experiment goal is"

    response = chat_session.send_message(prompt + link)
    return response.text

def getExperimentGroupKind(link):
    prompt = "Tell me what the experiment group kind is"

    response = chat_session.send_message(prompt + link)
    return response.text

def getExperimentGroupKind(link):
    prompt = "Tell me what the experiment group kind is"

    response = chat_session.send_message(prompt + link)
    return response.text

def getExperimentGoal(link):
    prompt = "Tell me what the goal of experiment is"

    response = chat_session.send_message(prompt + link)
    return response.text

def getExperimentEnvironment(link):
    prompt = "Tell me what the goal of experiment is"

    response = chat_session.send_message(prompt + link)
    return response.text
