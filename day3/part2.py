
def find_max_jolts(bank):
    n = len(bank)
    jolt = { # 0 = left most most index of the jolt
        # key = jolt index in string. 
        # val = the index in bank it occupies
        0: n-12,
        1: n-11,
        2: n-10,
        3: n-9,
        4: n-8,
        5: n-7,
        6: n-6,
        7: n-5,
        8: n-4,
        9: n-3,
        10: n-2,
        11: n-1
    }

    for i in range(n-13, -1, -1): # iterate by length 
        temp_first = int(bank[i])
        if temp_first >= int(bank[jolt[0]]): #compare potential jolt with first (index 0 )
            # if valid, we start shifting the other indices,
            for key,val in jolt.items(): 
                if key == 0: # skip first
                    jolt[0] = i
                    continue
                start = jolt[key] # starting index 
                end = jolt[key - 1] # the next highest jolt. we shouldn't check it
                temp = start # just a copy of jolt
                for j in range(start-1,end,-1): #gotta iterate backwards on bank
                    if int(bank[temp]) <= int(bank[j]):
                        temp = j

                jolt[key] = temp       

    max_jolt = int("".join(bank[jolt[k]] for k in range(12)))
                 
             
    return max_jolt


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