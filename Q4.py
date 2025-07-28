def get_bot_response(user_input):
    responses = {
        "hello": "Hi there!",
        "hi": "Hello!",
        "how are you": "I'm fine, thanks! How about you?",
        "bye": "Goodbye! Have a great day!",
        "help": "You can try saying hello, ask how I am, or say bye."
    }

    user_input = user_input.lower().strip()
    return responses.get(user_input, "Sorry, I don't understand that.")

def basic_chatbot():
    print("🤖 Basic Chatbot Initialized. Type 'bye' to exit.")
    while True:
        user_msg = input("You: ")
        reply = get_bot_response(user_msg)
        print("Bot:", reply)
        if user_msg.lower().strip() == "bye":
            break

basic_chatbot()