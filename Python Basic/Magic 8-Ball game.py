import random


responses = [
    "Yes, definitely.",
    "No, not at all.",
    "Maybe.",
    "Ask again later.",
    "Very doubtful.",
    "It is certain."
]

def magic_8_ball():
    question = input("Ask the Magic 8 Ball a yes or no question: ")

    if not question.strip():
        print("Please ask a valid question.")
    elif not question.endswith("?"):
        print("Please ask a question that ends with a '?'.")
    elif not any(char.isalpha() for char in question):
        print("Please ask a question that contains letters.")
    else:
        answer = random.choice(responses)
        print("The Magic 8 Ball says: " + answer)



while True:
    magic_8_ball()
    play_again = input("Do you want to ask another question? (yes/no): ")
    if play_again.lower() != "yes" and play_again.lower() == "no":
        print("Goodbye!")
        break
    else:
        ans = input("Please enter 'yes' or 'no'-")
        while True:
            if ans.lower() == "yes":
                break
            elif ans.lower() == "no":
                print("Goodbye!")
                exit()
            else:
                ans = input("Please enter 'yes' or 'no'- ")