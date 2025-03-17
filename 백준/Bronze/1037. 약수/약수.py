N = int(input())
nums = list(map(int, input().split()))
nums.sort()
length = len(nums)

print(nums[0]*nums[length-1])