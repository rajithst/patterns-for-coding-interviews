arr = [2, 6, 4, 3, 1, 5]
# define current index to 0
current_index = 0

# iterate through indexes
while current_index < len(arr):
    # find correct index according to value
    # value = index - 1
    correct_index = arr[current_index] - 1
    # if current index value is not at the correct position
    if arr[current_index] != arr[correct_index]:
        # swap current index value with correct index
        arr[current_index], arr[correct_index] = arr[correct_index], arr[current_index]
    # if current index value is in correct position,move to next index
    else:
        current_index += 1

print(arr)
