from sys import maxint

lst = [1,3,5,10,45,-80,33]

def maxSubLstSum(lst,n):

    max = -maxint - 1
    newmax = 0

    for i in range(0,n):
        newmax += lst[i]
        if (max < newmax):
            max = newmax

        if newmax < 0:
            newmax = 0
    return max

print(maxSubLstSum(lst,len(lst)))

"""
I have solved this problem not using any sublist or tuple, because it will occupy more memory.

So instead of that i have used 2 pointer varibles max and newmax.
"""
