def compare(cat,dog,goat)
if cat>dog and cat>goat:
    print("The greatest number is", cat)
elif dog>cat and dog>goat:
    print("The greatest number is", dog)
else:
    print("The greatest number is", goat)

compare(1,2,3)