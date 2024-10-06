from flask import Flask, render_template, request
import nltk
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import requests


def analyze_text_frequency(text):
    # Preprocessing: lowercase and remove punctuation
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize the text
    words = word_tokenize(text)

    # Initialize stemmer (to handle words like "rats" -> "rat")
    stemmer = PorterStemmer()

    # Stem words to their base form
    stemmed_words = [stemmer.stem(word) for word in words]

    # Count word frequencies
    word_counts = Counter(stemmed_words)

    # Return the most common words (top 10 or more, depending on the use case)
    return word_counts.most_common(10)



def analyze():
    # Get the URL from the form input
    url = request.form['link']

    # Extract text from the webpage
    webpage_text = extract_text_from_url(url)

    if not webpage_text:
        return "Error fetching text from the provided link.", 400

    # Analyze word frequency
    word_count_result = analyze_text_frequency(webpage_text)

    # Pass the link and the word count results to streszczenie.html
    return render_template('streszczenie.html', link=url, word_count=word_count_result)
