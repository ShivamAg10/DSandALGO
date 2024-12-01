arr = [40,80,20,10,50]
target = 10
left,right = 0, len(arr)-1

arr.sort()

while left <= right:
    mid = (left+right)//2
    if target == arr[mid]:
        print(mid)
        break
    elif target > arr[mid]:
        left = mid + 1
    elif target < arr[mid]:
        right = mid -1
    