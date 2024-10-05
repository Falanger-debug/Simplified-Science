"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyArNS7cIvztvHVwPjGgpXJVpbwj_8dJ6MY")

# Create the model
generation_config = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-002",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("https://osdr.nasa.gov/bio/repo/data/studies/OSD-379 Hello, here I have results of an experiment performed on mice aboard ISS. Could You explain me in detail what are the results of this experiment and how did the 'test bench' look like")
print(response.text)
print("----------------------------1-------------------------------")

response = chat_session.send_message("Are you sure?")
print(response.text)
print("----------------------------2-------------------------------")


response = chat_session.send_message("Ok. Can You also tell me more about the genes that were subjected to the analysis?")
print(response.text)
print("----------------------------3-------------------------------")

print(chat_session)
print("----------------------------4-------------------------------")