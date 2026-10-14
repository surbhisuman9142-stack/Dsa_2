arr = [2,3,1,2,4,3]
target = 7
left = 0
window_sum = 0
min_length = len(arr) + 1
for right in range(len(arr)):
    window_sum += arr[right]
    while window_sum >= target:
        length = right - left + 1
        if length < min_length:
            min_length = length
        window_sum -= arr[left]
        left += 1
if min_length == len(arr) + 1:
    print(0)
else:
    print(min_length)
