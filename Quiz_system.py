def start_quiz():
    score = 0

    print("What is the capital of Nigeria?")
    answer = input("Answer: ")
    if answer.lower() == "abuja":
        score += 1

    print("2 + 2 = ?")
    answer = input("Answer: ")
    if answer == "4":
        score += 1

    print("Your score:", score)

def main():
    while True:
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            start_quiz()
        elif choice == "2":
            break
        else:
            print("Invalid option")

main()
