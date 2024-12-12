#Task 1 Reverse a string without using build-in methods.

def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):  
        reversed_str += s[i]
    return reversed_str


ogstr = input("Enter a string to reverse: ")
revstr = reverse_string(ogstr)
print(f"Reversed String: {revstr}")
