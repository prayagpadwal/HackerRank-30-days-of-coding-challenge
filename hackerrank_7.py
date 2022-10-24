input_for_size_of_array = int(input())

array_to_store_the_numbers = []

# input_from_user = list(map(int, input().split()))

for i in range(0, input_for_size_of_array):
    elements_in_array = list(map(int, input().split()))

    array_to_store_the_numbers.append(elements_in_array)

print(array_to_store_the_numbers)

    
