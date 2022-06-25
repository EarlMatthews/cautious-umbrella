def five_sort(nums):
    head = 0 # start front at index 0
    tail = len(nums) - 1 # start tail at end of list
    while head < tail:
        if nums[head] == 5:
            if nums[tail] != 5:
                nums[head], nums[tail] = nums[tail], nums[head] # swap head and tail values
            else: 
                tail -= 1
        else: 
            head += 1
    return nums

#test_00
print(five_sort([12, 5, 1, 5, 12, 7]))
# -> [12, 7, 1, 12, 5, 5] 
#test_01
print(five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]))
# -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 
#test_02
print(five_sort([5, 5, 5, 1, 1, 1, 4]))
# -> [4, 1, 1, 1, 5, 5, 5] 
#test_03
print(five_sort([5, 5, 6, 5, 5, 5, 5]))
# -> [6, 5, 5, 5, 5, 5, 5] 
#test_04
print(five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]))
# -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 