from multiply_two_arbitrary import multiply
import random

def run_tests():

    test_cases = [
        # (A, B, expected)
        ([1, 2, 3], [4, 5], [5, 5, 3, 5]),          # 123 × 45
        ([0], [9, 9, 9], [0]),                      # 0 × 999
        ([9], [9], [8, 1]),                         # 9 × 9
        ([1, 0, 0], [2, 0], [2, 0, 0, 0]),           # 100 × 20
        ([-1, 2, 3], [4, 5], [-5, 5, 3, 5]),         # -123 × 45
        ([-1, 2, 3], [-4, 5], [5, 5, 3, 5]),         # -123 × -45
        ([9, 9, 9], [9, 9, 9], [9, 9, 8, 0, 0, 1]),  # 999 × 999
    ]

    large_a = [9] * 500
    large_b = [9] * 500


    all_passed = True

    for i, (A, B, expected) in enumerate(test_cases):
        result = multiply(A.copy(), B.copy())  # copy to avoid mutation

        if expected is not None:
            if result != expected:
                print(f"Test case {i+1} FAILED:")
                print(f"Input A:    {A[:10]}{'...' if len(A) > 10 else ''}")
                print(f"Input B:    {B[:10]}{'...' if len(B) > 10 else ''}")
                print(f"Output:     {result[:10]}{'...' if len(result) > 10 else ''}")
                print(f"Expected:   {expected[:10]}{'...' if len(expected) > 10 else ''}\n")
                all_passed = False
            else:
                print(f"Test case {i+1} passed ✅")
        else:
            # Large test: basic sanity checks (LeetCode-style stress)
            if result[0] != 9 or len(result) < 900:
                print(f"Test case {i+1} FAILED (large input sanity check)")
                all_passed = False
            else:
                print(f"Test case {i+1} passed ✅ (large input)")

    if all_passed:
        print("\nAll test cases passed! 🎉")
    else:
        print("\nSome test cases failed. ❌")

if __name__ == "__main__":
    run_tests()