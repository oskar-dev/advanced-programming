def is_requried_length(collection:list, length:int) -> bool:
    return len(collection) == length

print(is_requried_length([1,2], 2))
print(is_requried_length([1], 2))