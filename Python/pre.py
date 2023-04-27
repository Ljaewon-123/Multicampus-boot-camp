

lst = [1,2,3,4]
lst2 = lst
lst.pop()
print(lst)
print(lst2)
del lst[:0]
print(lst)

original = "EXAMPLE"
removed = original.replace("M", "")
print(removed)