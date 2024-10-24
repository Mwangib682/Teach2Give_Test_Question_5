"""
QUESTION 5: Write a program that accepts a string as input, capitalizes the first letter of each 
word in the string, and then returns the result string.
Examples:
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"
"""


#defining a new function named capitalize_words
def capitalize_words(input_string):
    # Capitalizing the first letter of each word
    capitalized_string = input_string.title()
    return capitalized_string

# Testing the function with examples
print(capitalize_words("hi"))                  # Output: "Hi"
print(capitalize_words("teach2give is a nice, great and educational organization"))  # Output: Teach2give Is A Nice, Great And Educational Organization

# Accepting input from the user
user_input = input("Enter the string to be capitalized: ")
result = capitalize_words(user_input)
print("Capitalized String:", result)




"""
My Pycharm results for the above written code are as follows:
C:\Users\hp\PycharmProjects\pythonProject2\.venv\Scripts\python.exe "C:\Users\hp\PycharmProjects\pythonProject2\QUESTION 5.py" 
Hi
Teach2Give Is A Nice, Great And Educational Organization
Enter the string to be capitalized: datascience is my number one passion
Capitalized String: Datascience Is My Number One Passion

Process finished with exit code 0
"""