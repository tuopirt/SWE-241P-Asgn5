from Recursion import PermutationChecker, EightQueensSolver

checker = PermutationChecker()
queens_solver = EightQueensSolver()

# Task 1: String Permutation (checkPermutation)
# Task 1 Simple Test
assert checker.checkPermutation("ab", "eidbaooo") == True
assert checker.checkPermutation("ab", "eidboaoo") == False
print("Task 1 Simple Test Passed")

# Task 1 Medium Test
assert checker.checkPermutation("hello", "ooolleoooleh") == False
assert checker.checkPermutation("adc", "dcda") == True
print("Task 1 Medium Test Passed")

# Task 1 Hard Test (Edge cases & missing/empty checks)
assert checker.checkPermutation("a", "a") == True
assert checker.checkPermutation("a", "b") == False
assert checker.checkPermutation("abc", "a") == False  # s1 longer than s2
assert checker.checkPermutation("ab", "ba") == True    # exact length match
print("Task 1 Hard Test Passed")


# Task 2: Eight Queens Minimum Moves (minMovesToValidQueens)
# Task 2 Simple Test
assert queens_solver.minMovesToValidQueens("1 2 3 4 5 6 7 8") == 7
assert queens_solver.minMovesToValidQueens("1 1 1 1 1 1 1 1") == 7
print("Task 2 Simple Test Passed")

# Task 2 Medium Test
assert queens_solver.minMovesToValidQueens("2 4 6 8 3 1 7 5") == 0
print("Task 2 Medium Test Passed")

# Task 2 Hard Test (Edge cases: symmetric and heavily clustered configurations)
assert queens_solver.minMovesToValidQueens("4 1 5 8 2 7 3 6") == 0
assert queens_solver.minMovesToValidQueens("5 5 5 5 5 5 5 5") == 7
print("Task 2 Hard Test Passed")