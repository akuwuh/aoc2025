ans = 0

def check_range(low, high):
    global ans
    for i in range(low, high + 1): 
        str_i = str(i)
        n = len(str_i) # gets length of num
        if n%2 != 0: #odd lengths dont check
            continue

        half_way = n//2
        if str_i[:half_way] == str_i[half_way:]: 
            ans += i

        

def solve(input): 
    for r in input:
        ra = r.split('-')
        check_range(int(ra[0]), int(ra[1]))





if __name__ == "__main__":
    input = open("input.txt", "r").read().split(',')
    solve(input)
    print(ans)
