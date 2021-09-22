# Print the following pattern for the given N number of rows.
# Pattern for N = 4

# A
# BC
# CDE
# DEFG

# Input format :
# Integer N (Total no. of rows)

# Output format :
# Pattern in N lines

## Read input as specified in the question
## Print the required output in given format
n = int(input())
for i in range(1, n + 1):
    start_char = chr(ord("A") + i - 1)
    for j in range(1, i + 1):
        char = chr(ord(start_char) + j - 1)
        print(char, end='')
    print()
