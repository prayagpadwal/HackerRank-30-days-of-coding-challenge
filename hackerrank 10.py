user_input =int(input())

converted_int = (bin(user_input)[2:])
#print(converted_int)

count = 0 
result = 0

for i in range(0, len(converted_int)):
    if converted_int[i] == 0:
        count = 0
    else:
        count += 1
        result = max(result, count)

print(result)
