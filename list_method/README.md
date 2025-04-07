            1. append() 
method adds an element to the end of a list while keeping the existing elements unchanged. It modifies the original list and is often used for dynamically growing lists.


            2. extend() 
method adds multiple elements from an iterable (e.g., list, tuple) to the end of a list while maintaining the order of elements. It modifies the original list and is useful for merging collections.


            3. insert() 
method inserts an element at a specified index in a list while shifting the subsequent elements to the right. It modifies the original list and is commonly used for precise element placement.


            4. remove() Method
The remove() method deletes the first occurrence of a specified element from a list while keeping the rest of the elements unchanged. It modifies the original list and raises a ValueError if the element is not found.


            5. pop() Method
The pop() method removes and returns an element at a specified index in a list while shifting subsequent elements left. If no index is given, it removes and returns the last element. It modifies the original list and raises an IndexError if the list is empty.


            6. clear() Method
The clear() method removes all elements from a list while keeping the list itself intact. It modifies the original list and results in an empty list.


            7. copy() Method
The copy() method returns a shallow copy of the list. Modifications to the new list do not affect the original list, unless the list contains nested objects (in which case references are shared). It does not take any arguments and does not modify the original list.


            8. index() Method
The index() method returns the first index at which a specified value is found. It raises a ValueError if the value is not found. It can also take optional start and end parameters to limit the search range. The original list is not modified.


            9. count() Method
The count() method returns the number of times a specified value appears in the list. It takes one required argument — the element to be counted. It does not modify the original list and always returns an integer. If the element is not found, it returns 0 instead of raising an error.


            10. reverse()
Reverses the elements of the list in place. Does not return a new list. This method modifies the original list and does not take any arguments. No exception is raised unless the object is not a list.


            11. sort()
Sorts the elements of the list in ascending order by default. Optional arguments: key (function to customize sort logic) and reverse (boolean to sort in descending order). It modifies the original list. Raises TypeError if elements are not comparable.