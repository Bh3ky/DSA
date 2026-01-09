from next_permutation import Solution

def run_test(nums):
    sol = Solution()
    print(f"Input:  {nums}")
    sol.nextPermutation(nums)
    print(f"Output: {nums}")
    print("-" * 30)

if __name__ == "__main__":
    # Given examples
    run_test([1, 0, 3, 2])     # expected [1, 2, 0, 3]
    run_test([3, 2, 1, 0])     # expected []

    # Extra sanity tests
    run_test([1, 2, 3])        # [1, 3, 2]
    run_test([1, 3, 2])        # [2, 1, 3]
    run_test([2, 3, 1])        # [3, 1, 2]