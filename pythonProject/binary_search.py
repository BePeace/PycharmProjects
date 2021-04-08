nums = [1,2,3,4,5]
lookFor = 1

low = 0;
high = len(nums)
found = False

while low < high and not found:
    #mid = int((low + high) / 2)
    mid = (low + high) // 2
    if nums[mid] < lookFor:
        low = mid + 1
    elif nums[mid] > lookFor:
        high = mid - 1
    elif nums[mid] == lookFor:
        print("Found", lookFor, "at index: ", mid)
        found = True

if not found:
    print("Value not found")