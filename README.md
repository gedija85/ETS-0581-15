
           #isupper() string method

The 'isupper()' method checks if all characters in a string are uppercase.It returns True if all letters are uppercase and False otherwise.Numbers and symbols do not affect the result.If the string contains any lowercase letters, it returns False. This method is useful for text validation in Python programs.


           #islowwer()
islower string methodThe islower() method in Python checks whether all the alphabetic characters in a string are lowercase. If the string contains at least one lowercase letter and no uppercase letters, it returns True; otherwise, it returns False. Non-alphabetic characters like numbers, spaces, and symbols do not affect the result. For example, "hello world".islower() returns True, while "Hello World".islower() returns False because of the uppercase letters. This method is useful for validating user input, text formatting, and ensuring consistency in string processing.
          
          
           #title() String Method
The title() method in Python converts a string to title case, meaning the first letter of each word is capitalized while all other letters are converted to lowercase.Non-alphabetic characters (like numbers and symbols) are not affected. If a word starts with a non-letter, it remains unchanged.
          
          
           #capitalize() Method
The capitalize() method is used to convert the first letter of a string to uppercase, while converting all other letters to lowercase.

            
            #swapcase() methode
the swapcase() method is a built-in string function that returns a new string with all uppercase characters converted to lowercase and all lowercase characters converted to uppercase.


            #find() methode
The find() method in Python is used to search for a substring within a string and return the index of its first occurrence. If the substring is not found, it returns -1.

            
            #index() method
The index() method is used to find the first occurrence of a substring within a string. If the substring is not found, it raises a ValueError instead of returning -1 like find(). Use index() if you want an error when the substring is missing instead of find(), ensuring the substring must exist.