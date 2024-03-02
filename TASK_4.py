from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!",]
    ],
    [
        r"good morning",
        ["Good morning! How can I assist you today?",]
    ],
    [
        r"good afternoon",
        ["Good afternoon! How can I assist you today?",]
    ],
    [
        r"good evening",
        ["Good evening! How can I assist you today?",]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"what can you do for me\?",
        ["I can answer your queries, provide information, or just have a friendly chat. Feel free to ask anything!",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!",
         "I told my wife she was drawing her eyebrows too high. She looked surprised!",
         "Why was the math book sad? Because it had too many problems.",
         "Why did the scarecrow win an award? Because he was outstanding in his field!",
         "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"who created you?",
        ["I was created by Ashish Ransing. He is a Artificial Intelligence and Data Science Student",]
    ],
    [
        r"bye|quit",
        ["Bye! Take care. See you soon :) ","It was nice talking to you. Goodbye!"]
    ],
]

# Create a chatbot with the pairs
def chatbot():
    print("Hi! I'm ChatBot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
