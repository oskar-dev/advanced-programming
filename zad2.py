
# 2.a
def print_names(names) -> None:
    for name in names:
        print(name)

print("2.a")
print_names(["Alice","Bob","Charlie","Doug","Emily"])

# 2.b
def multiply_for(numbers) -> list:
    output = []
    for number in numbers:
        output.append(number * 2)
    return output

def multiply_lis(numbers) -> list:
    return [number * 2 for number in numbers]

nums = [1,2,3,4,5]
print("2.b")
print(multiply_for(nums))
print(multiply_lis(nums))

# 2.c
def print_even(numbers) -> list:
    output = []
    for index in range(0, len(numbers)):
        if index % 2 == 1:
            output.append(numbers[index])
    return output
print("2.c")
print(print_even(nums))
# 3.d
nums2 = [1,2,3,4,5,6,7,81,9,10,211,120,13,14,15]
def print_sparse(numbers, stride: int) -> list:
    output = []
    i = 0    
    for index in range(0, len(numbers)):
        i += 1
        if i == stride:
            output.append(numbers[index])
            i = 0
    return output;
print("3.d")
print(print_sparse(nums2, 2))