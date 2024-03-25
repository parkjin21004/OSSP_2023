from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    
    listlenght = len(nums)
    for i in range(0, listlenght):
        for j in range(i+1, listlenght):
            if nums[i]+nums[j] == target:
                return [i, j]

    return 0