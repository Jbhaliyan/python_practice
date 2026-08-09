arr = [20,12,18,12,30,40,1,9,30]

##############################################################################
# Question 1: largest number
##############################################################################
# Method 1: first sorting then print last elemnt using reverse indexing
arr.sort()   #O(n log n)
# print(arr[-1])    #O(1)

# O(1) * O( n log n) = O(n log n)

# Method 2 : set a max value and then loop over the 
# list one by one comparing each element with the 
# max value and if it is greater than the max value 
# then set the max value to that element
def largest():
    max = arr[0]    #O(1)
    for i in arr:    #O(n)
        if i > max:
            max = i
    # print("Largest Number is :", max)
    # O(1) * O(n) = O(n) time complexity

#######################################################################
# Question 2: Second largest
#######################################################################
arr = [20,12,18,12,30,40,1,40,10]

def second_largest(arr):
    max = arr[0]
    second_max = arr[1]

    for num in arr:

        if num > max:
            second_max = max
            max = num
        elif num > second_max and num != max:
            second_max = num

    # print("Second largest number is:", second_max)

##########################################################################
# Question 3: First non repeating element in array/list
###########################################################################
 
nums = [2,3,4,2,3,5]
# brute force nested loop approach for each element loop
# over all the remaiing elements.  O(n2)

# efficient

def first_non_repeating(nums):
    freq = {}

    for num in nums:       #O(n)
        # .get(num,0): return None if key not available, passing 0
        #  as second element we assign None as 0 
        freq[num] = freq.get(num,0) +1 
        # print(num, freq[num])

    for num in nums:       #O(n)
        if freq[num] == 1 :
            return num
    return 

ans  = first_non_repeating(nums)
print(ans)

#O(n) + O(n) : O(N)



