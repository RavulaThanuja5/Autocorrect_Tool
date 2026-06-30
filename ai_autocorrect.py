from textblob import TextBlob
import os
from datetime import datetime

HISTORY_FILE = "history.txt"


def save_history(original, corrected):
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 50 + "\n")
        file.write(f"Date: {datetime.now()}\n")
        file.write("Original Text:\n")
        file.write(original + "\n")
        file.write("Corrected Text:\n")
        file.write(corrected + "\n")


def autocorrect_text(text):
    blob = TextBlob(text)
    corrected = str(blob.correct())
    return corrected


def view_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            print("\n===== HISTORY =====")
            print(file.read())
    else:
        print("No history available.")


def text_statistics(text):
    words = text.split()
    chars = len(text)

    print("\n===== STATISTICS =====")
    print("Total Words :", len(words))
    print("Total Characters :", chars)


def search_word(text):
    word = input("Enter word to search: ")

    count = text.lower().count(word.lower())

    print(f"'{word}' found {count} times")


def save_corrected_file(corrected):
    filename = input("Enter file name: ")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(corrected)

    print("File saved successfully.")


def correct_file():
    filename = input("Enter text file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        corrected = autocorrect_text(content)

        print("\nCorrected Content:\n")
        print(corrected)

        save_history(content, corrected)

    except FileNotFoundError:
        print("File not found.")


def menu():

    current_original = ""
    current_corrected = ""

    while True:

        print("\n")
        print("=" * 40)
        print(" AI AUTOCORRECT SYSTEM ")
        print("=" * 40)
        print("1. Correct Text")
        print("2. View History")
        print("3. Statistics")
        print("4. Search Word")
        print("5. Save Corrected Text")
        print("6. Correct Text File")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            current_original = input("\nEnter text:\n")

            current_corrected = autocorrect_text(current_original)

            print("\nCorrected Text:")
            print(current_corrected)

            save_history(current_original, current_corrected)

        elif choice == "2":

            view_history()

        elif choice == "3":

            if current_corrected:
                text_statistics(current_corrected)
            else:
                print("No text available.")

        elif choice == "4":

            if current_corrected:
                search_word(current_corrected)
            else:
                print("No text available.")

        elif choice == "5":

            if current_corrected:
                save_corrected_file(current_corrected)
            else:
                print("No corrected text available.")

        elif choice == "6":

            correct_file()

        elif choice == "7":

            print("Thank you for using AI AutoCorrect.")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    menu()
    