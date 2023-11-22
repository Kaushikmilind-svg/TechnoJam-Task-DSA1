def reverse_array(arr):
    return arr[::-1]

def reverse_string(st):
    return st[::-1]

#array
array = input("Enter an array: ").split(',')
reversed_array = reverse_array(array)
print("Your Array:", array)
print("Reversed Array:", reversed_array)

#string
string = str(input("Enter the string: "))
reversed_string = reverse_string(string)
print("Your String:", string)
print("Reversed String:", reversed_string)
