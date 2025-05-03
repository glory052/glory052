
def palindrome(string):
    string=string.replace("","").lower()

    return string==string[::-1]

print(palindrome("madam"))

print(palindrome("hello"))

print(palindrome("A man a plan a canal panama"))


