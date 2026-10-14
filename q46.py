arr = [0,1,0,3,12]
position = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[position] = arr[i]
        position += 1
while position < len(arr):
    arr[position] = 0
    position += 1
print(arr)

        