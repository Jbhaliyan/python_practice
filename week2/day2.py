###########################################################################
# Question 4: Two sum problem
# Indexes of two elements whose sum is target. 
# There is only one such pair.
###########################################################################
nums = [2,3,11,15,7]
target = 9

# brute force run two loops 
for num in nums:
    sum = num
    for j in range(0,len(nums)-1):
        sum += nums[j+1]
        # print(sum)
        if sum == target:
            ans = (nums.index(num),j+1)
        else:
            sum = num
        
# print(ans)  O(n2)

# better approach use dictionary
def get_two_sum(nums,target):

    sum = nums[0]
    nums[1:]
    for index,num in enumerate(nums):   #O(n)
        if sum + num == target:
            return nums.index(sum),index   #.index() is also O(n)

# print(get_two_sum(nums,target))


def get_two_sum(nums,target):

    indexes = {}
    # index: is the iterator num: element of the list
    for index,num in enumerate(nums):    #O(n)
        second_elmnt = target - num
        if second_elmnt in indexes:
            return (index,(indexes.get(second_elmnt)))
        # below condition if element not match when comparing each value
        indexes[num] = index
        print(num,indexes)

# print(get_two_sum(nums,target))

##########################################################################################
#  Question 5: Find elements that are duplicate in the list
##########################################################################################

nums = [4,2,3,2,4,5,1,4]

# Brute force using nested loop and another list
dup = []
itr = 0
itr2 = 0
for i,num in enumerate(nums):
    for j in range(i,len(nums)-1):
        if num == nums[j+1] and num not in dup:
            # print(num,nums[j+1])
            dup.append(num)
        # else :
            # print("˜not duplicate")          
# print(dup).     O(n2)

# using set as extra memory becuase it gives O(1) to do lookup

def find_duplicates(nums):
    seen = set()    #O(1) to do lookup
    dups = []     #if we use list here then if we have any element more than 2 
                    # times then it will add the element again
    dup_set = set()
    for num in nums:
        if num in seen:
            dups.append(num)
            dup_set.add(num)
        else:
            seen.add(num)
    return dups,dup_set

# nums = [4,2,3,2,4,5,1,4]
dup_list ,dup_set = find_duplicates(nums)
print('Duplicates using List:',dup_list)
print('Duplicates using set:',dup_set)

    












