import nltk
import random
import string
from nltk.stem import WordNetLemmatizer
from datetime import datetime

lemmatizer = WordNetLemmatizer()

intents = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "hii", "hiii"],
        "responses": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you today?"]
    },
    "goodbye": {
        "patterns": ["bye", "quit", "exit", "see you", "goodbye"],
        "responses": ["Goodbye!", "See you later!", "Have a nice day!", "Bye! Come back soon."]
    },
    "thanks": {
        "patterns": ["thank you", "thanks", "thx", "thank you very much"],
        "responses": ["You're welcome!", "No problem!", "My pleasure!"]
    },
    "name_query": {
        "patterns": ["what is your name", "who are you", "your name", "what should I call you"],
        "responses": ["I am an AI Chatbot created with Python and NLTK.", "You can call me ChatBot!"]
    },
    "help": {
        "patterns": ["help", "can you help me", "i need assistance", "support", "what can you do"],
        "responses": [
            "I can chat with you and answer simple questions.",
            "Try saying hello or asking me basic questions!"
        ]
    },
    "how_are_you": {
        "patterns": ["how are you", "how are you doing", "how is it going"],
        "responses": [
            "I'm a bot, so I don't have feelings, but thanks for asking!",
            "I'm here to help you anytime!",
            "Doing great! How about you?"
        ]
    },
    "weather": {
        "patterns": ["weather", "how is the weather", "weather today", "what's the weather"],
        "responses": [
            "I can't check real-time weather yet, but I hope it's nice where you are!",
            "Weather seems fine from my side, but you might want to check a weather website for updates."
        ]
    },
    "time": {
        "patterns": ["time", "what time is it", "current time", "tell me the time"],
        "responses": []  # will generate dynamically
    },
    "date": {
        "patterns": ["date", "what's the date", "today's date", "tell me the date"],
        "responses": []  # will generate dynamically
    },
    "favorite_language": {
        "patterns": ["favorite programming language", "what language do you like", "which programming language do you prefer"],
        "responses": [
            "I like Python because it's versatile and great for AI and machine learning!",
            "Python is my favorite language, of course!",
            "I love Python for its simplicity and power."
        ]
    },
    "default": {
        "responses": [
            "Sorry, I didn't quite get that. Can you rephrase?",
            "I'm not sure I understand. Could you say that differently?",
            "I can help with simple questions and greetings."
        ]
    }
}

def lemmatize_sentence(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens if token not in string.punctuation]
    return lemmatized

def pattern_in_input(pattern_words, input_words):
    # Return True if all words in pattern_words are in input_words
    return all(word in input_words for word in pattern_words)

def find_intent(user_input):
    lemmatized_input = lemmatize_sentence(user_input)
    for intent_name, intent_data in intents.items():
        for pattern in intent_data.get("patterns", []):
            pattern_lem = lemmatize_sentence(pattern)
            if pattern_in_input(pattern_lem, lemmatized_input):
                return intent_name
    return "default"

def chatbot_response(user_input):
    intent = find_intent(user_input)
    
    if intent == "time":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif intent == "date":
        today = datetime.now()
        current_date = today.strftime("%B %d, %Y")
        return f"Today's date is {current_date}."
    else:
        return random.choice(intents[intent]["responses"])

def main():
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("ChatBot: Goodbye! Have a great day.")
            break
        response = chatbot_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()