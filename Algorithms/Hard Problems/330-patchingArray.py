def minPatches(nums: [int], n: int) -> int:
    patches = []
    for target in range(1, n+1):
        for num in nums:
            rem = target - num
            if(rem != 0):
                print("Adding {} because target is {} and number is {}".format(rem, target, num))
                patches.append(rem)
                break
    print(patches)
    return len(patches)

minPatches([1,3], 6)