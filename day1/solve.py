
def solve(input): 
    ans = 0
    cur = 50
    for operation in input:
        operator = operation[0]
        distance = int(operation[1:])
        temp = cur
        if operator == 'R': # right turn
            temp += distance
        else: 
            temp -= distance
        
        cur = temp%100 # wrap over 
        if cur == 0:
            ans += 1
        
    return ans 






if __name__ == "__main__":
    input = open("input.txt", "r").read().splitlines()
    ans = solve(input)
    print(ans)
