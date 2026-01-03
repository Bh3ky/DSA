from plus_one import plus_one
import random

def run_leetcode_style_tests():
    # Predefined test cases
    test_cases = [
        ([1, 2, 3], [1, 2, 4]),
        ([1, 2, 9], [1, 3, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([0], [1]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
    ]

    # Add a random large test case (simulate 1000-digit number)
    large_number = [9]*1000
    test_cases.append((large_number.copy(), [1] + [0]*1000))

    all_passed = True

    for i, (digits, expected) in enumerate(test_cases):
        result = plus_one(digits.copy())  # copy to avoid modifying original
        if result != expected:
            print(f"Test case {i+1} FAILED:")
            print(f"Input:      {digits[:20]}{'...' if len(digits)>20 else ''}")
            print(f"Output:     {result[:20]}{'...' if len(result)>20 else ''}")
            print(f"Expected:   {expected[:20]}{'...' if len(expected)>20 else ''}\n")
            all_passed = False
        else:
            print(f"Test case {i+1} passed ✅")

    if all_passed:
        print("\nAll test cases passed! 🎉")
    else:
        print("\nSome test cases failed. ❌")

if __name__ == "__main__":
    run_leetcode_style_tests()