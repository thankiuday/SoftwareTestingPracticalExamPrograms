# Step 1: Define the function to be tested
def is_even(num):
    return num % 2 == 0

# Step 2: Create a list of test cases as (input, expected_output)
test_cases = [
    (0, True),
    (1, False),
    (2, True),
    (3, False),
    (-4, True),
    (-5, False),
    (100, True),
    (101, False)
]

# Step 3: Simulate automated testing
def run_tests(function, test_cases):
    print("Running Automated Tests...\n")
    passed = 0

    for i, (input_val, expected) in enumerate(test_cases, 1):
        actual = function(input_val)
        result = " PASSED" if actual == expected else " FAILED"
        print(f"Test {i}: {function.__name__}({input_val}) → Expected: {expected}, Actual: {actual} → {result}")
        if actual == expected:
            passed += 1

    # Step 4: Summary
    total = len(test_cases)
    print(f"\nSummary: {passed}/{total} tests passed.")

# Run the tests on the is_even function
run_tests(is_even, test_cases)
