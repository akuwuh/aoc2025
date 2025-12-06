
def solve(problems):
    total_sum = 0
    for problem in problems:
        op = problem[-1]
        ans = int(problem[0])
        for i in range(1, len(problem) - 1): # skips first index, and last index
            if op == '*':
                ans *= int(problem[i])
            elif op == '+':
                ans += int(problem[i])
        total_sum += ans
    return total_sum



if __name__ == "__main__":
    input = open("input.txt", "r").read().splitlines()

    unpacked = [line.split() for line in input]
        
    problems = [list(i) for i in zip(*unpacked)]
    
    ans = solve(problems)

    print(ans)