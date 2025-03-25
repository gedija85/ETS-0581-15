data = "hellow this is lower"
is_lower = data.islower()

print(is_lower) 




# islower string methodThe islower() method in Python checks whether all the alphabetic characters in a string are lowercase. If the string contains at least one lowercase letter and no uppercase letters, it returns True; otherwise, it returns False. Non-alphabetic characters like numbers, spaces, and symbols do not affect the result. For example, "hello world".islower() returns True, while "Hello World".islower() returns False because of the uppercase letters. This method is useful for validating user input, text formatting, and ensuring consistency in string processing.
