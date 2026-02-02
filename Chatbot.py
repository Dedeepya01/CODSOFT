def greet():
    print("Chatbot: Hey there! I'm your friendly assistant 😊")
    print("Chatbot: You can talk to me about anything. I'm always ready to chat!")
    print("Chatbot: Type 'bye' whenever you want to end the conversation.")

def chatbot():
    greet()
    while True:
        user = input("You: ").lower().strip()
        if user in ["bye", "exit"]:
            print("Chatbot: Bye! Catch you later 😄. I'm always here if you need a chat.")
            break
        elif user in ["hi", "hello", "hey"]:
            print("Chatbot: Hey! Great to see you. How can I help you today?")
        elif "how are you" in user:
            print("Chatbot: I'm feeling awesome today 😎! How about you?")
        elif "sad" in user:
            print("Chatbot: Aww, I'm sorry to hear that 💙. Want to talk about it or maybe hear a joke?")
        elif "happy" in user:
            print("Chatbot: Yay! Love that you're feeling good 😄 Keep that vibe going!")
        elif "help" in user:
            print("Chatbot: Sure! I can chat, tell jokes, share fun facts, or just hang out.")
            print("Try saying 'hi', 'tell me something', or 'joke'.")
        elif "what can you do" in user:
            print("Chatbot: I can chat, tell jokes, share fun facts, or just keep you company 🙂")
        elif "what should i do" in user:
            print("Chatbot: Hmm, can you tell me a bit more? Maybe I can suggest something fun!")
        elif "i don't understand" in user:
            print("Chatbot: No worries! I can explain it in a simpler way for you 😉")
        elif "tell me something" in user:
            print("Chatbot: Sure! Want a joke or a fun fact?")
        elif "bored" in user:
            print("Chatbot: Ah, feeling bored? Let's do something fun! Try 'joke' or 'fun fact'.")
        elif "joke" in user:
            print("Chatbot: Why was the cellphone wearing glasses? Because it lost its contacts 😆")
            step = input("Chatbot: Want another one? (yes/no) ").lower()
            if step == "yes":
                print("Chatbot: Why was the math book sad? It had too many problems 😂")
            else:
                print("Chatbot: No worries, maybe later!")
        elif "fun fact" in user:
            print("Chatbot: Did you know octopuses have three hearts? 🐙 Cool, right?")
        elif user in ["thanks", "thank you"]:
            print("Chatbot: Anytime! Happy to chat 😄")
        else:
            print("Chatbot: Hmm, I’m not sure about that 🤔. Can you try saying it differently?")
chatbot()
