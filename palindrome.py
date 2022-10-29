import string
def is_palindrome(text):
    """Check if the text string is a palindrome or not. Example  - level = level in reverse"""
    flag = False
    original_string = text
    reverse_string = original_string[::-1]
    if original_string == reverse_string:
        flag = True
        print("\nPalindrome status: ", flag, "\n")
        print(text, "is a palindrome.")
    else:
        print("\nPalindrome status: ", flag, "\n")
        print(text, "is not a palindrome.")

def main():
    text = "text"
    is_palindrome(text)
    text_dictionary = ["level", "ratstar", "racecar", "eve", "eye", "evil"]
    for texts in text_dictionary:
        is_palindrome(texts)
    
if __name__ == "__main__":
    main()
