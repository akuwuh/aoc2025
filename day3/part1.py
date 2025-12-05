

def find_max_jolts(bank):
    n = len(bank)
    first, second= int(bank[n-2]), int(bank[n-1])
    for i in range(n-3, -1, -1 ): # iterate by length 
        temp_first = int(bank[i])
        if temp_first >= first:
            second = max(second,first)
            first = temp_first
        
    return first * 10 + second 


def solve(input): 
    ans = 0
    for bank in input:
        max_jolt = find_max_jolts(bank)
        print(max_jolt)
        ans += max_jolt
    return ans

if __name__ == "__main__":
    input = open("input.txt", "r").read().splitlines()
    ans = solve(input)
    print(ans)