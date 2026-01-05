def can_jump(A):
    max_reach = 0
    n = len(A)

    # main loop
    for i in range(n):
        if i > max_reach: # stuck, can't move further
            return False
        max_reach = max(max_reach, i + A[i])
        if max_reach >= n - 1: # can reach the last index
            return True
        
    return False 


print(can_jump([2, 3, 1, 1, 4]))  # True
print(can_jump([3, 2, 1, 0, 4]))  # False
print(can_jump([0]))              # True