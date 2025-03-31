
           1. isupper() string method

The 'isupper()' method checks if all characters in a string are uppercase.It returns True if all letters are uppercase and False otherwise.Numbers and symbols do not affect the result.If the string contains any lowercase letters, it returns False. This method is useful for text validation in Python programs.


           2. islowwer()
islower string methodThe islower() method in Python checks whether all the alphabetic characters in a string are lowercase. If the string contains at least one lowercase letter and no uppercase letters, it returns True; otherwise, it returns False. Non-alphabetic characters like numbers, spaces, and symbols do not affect the result. For example, "hello world".islower() returns True, while "Hello World".islower() returns False because of the uppercase letters. This method is useful for validating user input, text formatting, and ensuring consistency in string processing.
          

            3. title() String Method
The title() method in Python converts a string to title case, meaning the first letter of each word is capitalized while all other letters are converted to lowercase.Non-alphabetic characters (like numbers and symbols) are not affected. If a word starts with a non-letter, it remains unchanged.


            4. capitalize() Method
The capitalize() method is used to convert the first letter of a string to uppercase, while converting all other letters to lowercase.


            5. swapcase() methode
the swapcase() method is a built-in string function that returns a new string with all uppercase characters converted to lowercase and all lowercase characters converted to uppercase.


            6. find() methode
The find() method in Python is used to search for a substring within a string and return the index of its first occurrence. If the substring is not found, it returns -1.

            
            7. index() method
The index() method is used to find the first occurrence of a substring within a string. If the substring is not found, it raises a ValueError instead of returning -1 like find(). Use index() if you want an error when the substring is missing instead of find(), ensuring the substring must exist.

            8. starswith()
The startswith() method checks whether a string starts with a specified prefix. It returns True if the string starts with the given prefix and False otherwise.


            9. endswith()
Think of the endswith() method as a way to check how a string finishes—kind of like checking if a book title ends with a specific word or if a file has the right extension before opening it.


            10. count() string method 
The count() method counts occurrences of a specific substring in a given string and returns that number.


            11. replace() Method
The replace() method is used to replace all occurrences of a substring with another substring in the original string.


            12. strip() Method
The strip() method removes leading and trailing whitespace (spaces, tabs, newlines) from a string. Remove specific characters (like "#")


            13. lstrip() Method
The lstrip() method removes leading whitespace (spaces, tabs, newlines) from the left side of the string. It only removes characters from the beginning of the string.


            14. rstrip() method
The rstrip() method removes any trailing whitespace or specified characters from the right end of a string. The rstrip() method removes any trailing whitespace or specified characters from the right end of a string.


            15. split() method
The split() method splits a string into a list based on a separator.separator  → The delimiter to split the string. Default is whitespace.maxsplit Maximum number of splits.


            16. join() method
The join() method joins a list of strings into a single string, using a specified separator.


            17. isalpha() string method
The isalpha() method checks if all characters in a string are alphabetic (letters from A-Z or a-z). It returns True if the string consists only of letters and False otherwise. Numbers, spaces, and special characters cause this method to return False. This method is useful for validating input that should contain only letters.


            18. isdigit() string method
The isdigit() method checks if all characters in a string are digits (0-9). It returns True if the string consists only of numeric characters and False otherwise. If the string contains letters, spaces, or special symbols, it returns False. This method is useful for checking numerical input in Python programs.


            19. isalnum() string method
The isalnum() method checks if all characters in a string are alphanumeric (letters A-Z, a-z, or digits 0-9). It returns True if the string consists only of letters and/or numbers and False if it contains spaces, symbols, or special characters. This method is useful for validating usernames, passwords, and other text-based inputs where only letters and numbers are allowed.


            20. isspace() string method
The isspace() method checks if all characters in a string are whitespace characters (spaces, tabs, or newlines). It returns True if the string consists only of whitespace and False if it contains any non-whitespace characters. This method is useful for detecting empty or space-filled inputs.

            
            21. format() string method
The format() method is used to insert values into a string using placeholders {}. It allows flexible formatting by specifying positions, named arguments, or formatting options. This method is useful for dynamic string generation and compatibility with older Python versions.

            
            22. f-string string method
An f-string (formatted string literal) is a modern and efficient way to embed expressions inside strings using curly braces {}. It is prefixed with f or F before the quotation marks. This method is useful for improving readability, performance, and simplifying string formatting in Python 3.6 and later.