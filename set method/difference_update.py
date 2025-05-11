foods = {"injera", "shiro", "doro"}
to_remove = {"shiro", "doro"}
foods.difference_update(to_remove) 
print(foods)                                # {'injera'}