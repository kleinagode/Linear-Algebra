
string_input = input()

if string_input.replace(" ","") == string_input[::-1].replace(" ",""):
    print(f"palindrome: {string_input}")
else:
    print(f"not a palindrome: {string_input}") 