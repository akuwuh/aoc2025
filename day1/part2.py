
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
        
        if (temp > 100):
            ans += (temp - 1) // 100 # - 1 needed to account for more than 1 rotations that doesn't land on 0 
        elif (temp < 0):
            diff = (abs(temp) - 1) // # this is for + 1 rotations
            if (cur > 0): # for not full rotations that still passed
                diff += 1
            ans += diff

        cur = temp%100 # wrap over 
        if cur == 0:
            ans += 1
        
    return ans 






if __name__ == "__main__":
    input = open("test.txt", "r").read().splitlines()
    ans = solve(input)
    print(ans)
    assert(ans==6)

    input = open("test2.txt", "r").read().splitlines()
    ans = solve(input)
    print(ans)
    assert(ans==10)

    input = open("test3.txt", "r").read().splitlines()
    ans = solve(input)
    print(ans)
    assert(ans==24)
    input = open("test4.txt", "r").read().splitlines()
    ans = solve(input)
    print(ans)
    assert(ans==5847)

    input = open("input.txt", "r").read().splitlines()
    ans = solve(input)
    print(ans)
