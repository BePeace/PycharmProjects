

nums = [4,5,1,3,6,7]
print(nums)

len = len(nums)

for n in range(0, len - 1):
    for m in range(n+1,len):
        if nums[n] > nums[m]: #sort ascending
            tmp = nums[n]
            nums[n] = nums[m]
            nums[m] = tmp

print(nums)
