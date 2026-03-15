from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('My bot')
trainer = ListTrainer(chatbot)

trainer.train([
    "Hi, there!",
    "Hello!",
    "How are you?",
    "I am doing well, thank you!",
    "What is your name?",
    "My name is MyBot.",
     "What is a fever?",
    "A fever is a temporary increase in body temperature, often caused by an infection.",

    "What is normal body temperature?",
    "Normal body temperature is around 36.5 to 37.5 degrees Celsius.",

    "What causes headaches?",
    "Headaches can be caused by stress, dehydration, lack of sleep, or illness.",

    "What should I do if I have a high fever?",
    "You should rest, drink fluids, and see a doctor if the fever is high or persistent.",

    "Can you diagnose diseases?",
    "No. I cannot diagnose diseases. You should consult a qualified medical professional."
])

while True:
    try:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print(f"Bot response: {response}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break