# TASK 4: Basic Chatbot - Improved Version

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi!"

    elif "how are you" in user_input:
        return "I'm fine, thanks!"

    elif "bye" in user_input:
        return "Goodbye!"

    else:
        return "I'm not sure how to respond to that."


def chatbot():
    print("🤖 Chatbot: Hello! I'm a simple bot. Type 'bye' to quit.\n")

    while True:
        message = input("You: ")
        reply = get_response(message)
        print("🤖 Chatbot:", reply, "\n")

        if "bye" in message.lower():
            break

chatbot()