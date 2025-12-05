ans = 0

def check_num(num): # num is a string 
    n = len(num) #
    for i in range(1,n):
        chunk = num[:i]
        if n%i != 0:
            continue # skip if no chunk multiple 
        finished = True 
        for j in range(i,n,i): # can be chunked
            new_chunk=num[j:j+i]
            if new_chunk != chunk: # valid
                finished = False
                break
        if finished:
            return True
    return False 


            

def check_range(low, high):
    global ans 
    for i in range(low, high + 1): 
        str_i = str(i)
        is_invalid = check_num(str_i)
        if is_invalid:
            print(i)
            ans += i

        

def solve(input): 
    for r in input:
        ra = r.split('-')
        check_range(int(ra[0]), int(ra[1]))




if __name__ == "__main__":
    input = open("input.txt", "r").read().split(',')
    solve(input)
    print(ans)
    # is_invalid = check_num(str(82482482))
    # print('isinvalid',is_invalid)
    # print(ans)