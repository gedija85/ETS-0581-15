            1. add() Method
The add() method inserts a single element into a set. If the element already exists, the set remains unchanged. It modifies the original set.


            2. clear() Method
The clear() method removes all elements from a set, leaving it empty. This changes the original set and cannot be undone.


            3. copy() Method
The copy() method creates a shallow copy of a set. Changes to the copied set do not affect the original.


            4. difference() Method
The difference() method returns a new set with elements that are in the first set but not in the other(s). It doesn’t change the original set.


            5. difference_update() Method
The difference_update() method removes all elements found in another set from the original set. It modifies the original set.


            6. discard() Method
The discard() method removes a specific element from the set if it exists. If the element is not found, it does nothing and does not raise an error.


            7. intersection() Method
The intersection() method returns a new set with elements that are common to both sets. It doesn’t modify the original sets


            8. intersection_update() Method
The intersection_update() method keeps only the elements that are present in both sets. It modifies the original set.


            9. isdisjoint() Method
The isdisjoint() method returns True if two sets have no elements in common. Otherwise, it returns False.


            10. issubset() Method
The issubset() method returns True if all elements of the set are present in another set. Otherwise, it returns False.


            11. issuperset() Method
The issuperset() method returns True if the set contains all elements of another set. Otherwise, it returns False.


            12. pop() Method
The pop() method removes and returns a random element from the set. If the set is empty, it raises a KeyError.


            13. remove() Method
The remove() method deletes a specific element from the set. If the element is not found, it raises a KeyError.


            14. symmetric_difference() Method
The symmetric_difference() method returns a new set with elements that are in either set, but not in both. It does not modify the original sets.


            15. symmetric_difference_update() Method
The symmetric_difference_update() method removes common elements and adds unique elements from another set. It updates the original set.


            16. union() Method
The union() method returns a new set that contains all elements from both sets, removing duplicates. It does not change the original sets.