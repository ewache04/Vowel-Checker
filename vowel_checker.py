"""
Author: Jeremiah E. Ochepo
Code Description: Checking vowels in a plaintext file
Last Updated Date: 7/03/19
"""


def plain_text_opener(file_name):
    try:
        with open(file_name, "r") as file_opener:
            file_strings = file_opener.read()
        return file_strings
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
        return None


def extract_vowels(file_strings):
    if file_strings is not None:
        vowels = "aeiouy"
        file_strings_lower = file_strings.lower()  # Convert to lowercase for case-insensitive matching

        print("\nVowel Counts:")
        for vowel in vowels:
            count = file_strings_lower.count(vowel)
            print(f"  {vowel.upper()}: {count}")


def display_final_report(file_strings):
    print("\nFinal Report:")
    print("---------------")
    # print(f"PlainText: {file_strings}")
    print(f"Text Length: {len(file_strings)}")
    extract_vowels(file_strings)
    print("---------------")


if __name__ == "__main__":
    print("Welcome to the Vowel Checker!")
    file_name = input("Please enter the file name: ")
    file_strings = plain_text_opener(file_name)

    if file_strings:
        display_final_report(file_strings)
