'''
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
    Input: [2,2,1]
    Output: 1

Example 2:
    Input: [4,1,2,1,2]
    Output: 4
'''


def singleNumber(nums: [int], oneElement: bool) -> int:
    list = []
    for i in nums:
        if i not in list:
            list.append(i)
        else:
            list.remove(i)
    if oneElement:
        return list.pop()
    return list

print(singleNumber(nums = [2, 1, 4, 3, 2], oneElement = False))
print(singleNumber(nums = [2, 1, 4, 4, 2], oneElement = True))