
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