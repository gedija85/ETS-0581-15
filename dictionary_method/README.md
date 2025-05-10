            1. get() Method
The get() method returns the value for the specified key if it exists in the dictionary. If the key is not found, it returns None or a user-defined default value. It does not raise an error like direct key access does.


            2. keys() Method
The keys() method returns a dynamic view of all the keys in the dictionary. The view updates automatically if the dictionary changes.


            3. values() Method
The values() method returns a view of all the values in the dictionary. Like keys(), it reflects any changes made to the dictionary.


            4. items() Method
The items() method returns a view object containing the dictionary’s key-value pairs as tuples. It is commonly used in loops to access both keys and values.


            5. update() Method
The update() method modifies the dictionary by adding key-value pairs from another dictionary or from keyword arguments. Existing keys will be updated, and new ones will be added.


            6. clear() Method
The clear() method removes all items (key-value pairs) from the dictionary, leaving it empty. This is an irreversible operation and the dictionary will be reset to an empty state.


            7. copy() Method
The copy() method creates a shallow copy of the dictionary. It returns a new dictionary with the same key-value pairs, but changes to the original dictionary will not affect the copy.


            8. fromkeys() Method
The fromkeys() method creates a new dictionary from a sequence of keys and assigns them a default value. The default value is None, but you can specify a value if needed.


            9. pop() Method
The pop() method removes and returns the value associated with a specified key. If the key doesn’t exist, it raises a KeyError unless a default value is provided.


            10. popitem() Method
The popitem() method removes and returns a random (key, value) pair as a tuple. If the dictionary is empty, it raises a KeyError. It is commonly used for pop operations in loops.