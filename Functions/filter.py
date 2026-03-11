# Filter function with a lambda function amd multiple condition.

numbers = [1,2,3,4,5,6,7,8,9,10]

even_and_greater_than_four = list(filter(lambda x:x>4 and x%2==0, numbers ))

print(even_and_greater_than_four)