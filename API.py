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

def getTitle(link):
    prompt = "Tell me what the title of the article is. Just the title based on this AND ONLY THIS! link. I need just the title. Don't write 'The title of this article is THE_TITLE', just 'THE_TITLE'. Be honest."

    response = chat_session.send_message(prompt + link)
    return response.text