# AI Study Buddy - For Kenyan Students
print("Welcome to AI Study Buddy Kenya!")

def study_helper():
    subject = input("What subject are you studying? ")
    topic = input(f"What topic in {subject}? ")
    print(f"\nLet's study {topic}!")
    print("Tips: Break it down, practice questions, explain to a friend")
    question = input("\nAsk your question (or 'quit'): ")
    if question.lower() != 'quit':
        print(f"\nFor '{question}': Define it, give 2 examples, why it matters.")

study_helper()