from datetime import datetime

print("=" * 50)
print("      AI LEARNING CHATBOT")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nHello {name}! Welcome to AI Learning Chatbot.")
print("Type 'bye' to exit.\n")

question_count = 0

while True:

    user = input("You: ").lower()
    question_count += 1

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Bot: I am doing great. Thanks for asking!")

    elif "your name" in user:
        print("Bot: I am AI Learning Chatbot.")

    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence.")

    elif "machine learning" in user:
        print("Bot: Machine Learning is a subset of AI.")

    elif "python" in user:
        print("Bot: Python is one of the most popular programming languages for AI.")

    elif "data science" in user:
        print("Bot: Data Science involves extracting insights from data.")

    elif "project" in user:
        print("Bot: Projects help you gain practical experience.")

    elif "time" in user:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current Time:", current_time)

    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's Date:", current_date)

    elif "help" in user:
        print("Bot: You can ask me about AI, Python, Machine Learning, Data Science, Date, Time and more.")

    elif "thanks" in user:
        print("Bot: You're welcome!")

    elif "questions" in user:
        print(f"Bot: You have asked {question_count} questions.")

    elif "bye" in user:
        print(f"Bot: Goodbye {name}!")
        print(f"Bot: Total Questions Asked = {question_count}")
        break

    else:
        print("Bot: Sorry, I didn't understand that. Please try another question.")