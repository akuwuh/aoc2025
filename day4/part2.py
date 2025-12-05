

def solve_once(matrix):
    dirv = [(0,1), (1,0), (-1,0), (0,-1), (-1,1), (1,1), (-1,-1), (1,-1)]
    rows, cols = len(matrix), len(matrix[0])
    ans = 0 
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '@':
                count = 0
                for x,y in dirv:
                    nr,nc = r+x, c+y

                    if 0 <= nr < rows and 0 <= nc < cols and matrix[r+x][c+y] == '@':
                        
                        count +=1 
                
                if count < 4:
                    matrix[r][c] = '.'
                    ans +=1

    return ans


def solve(matrix): 
    ans = 0
    while True:
        ans_temp = solve_once(matrix)
        if ans_temp == 0:
            break
        ans += ans_temp

    return ans



if __name__ == "__main__":
    input = open("input.txt", "r").read().splitlines()
    matrix = [list(i) for i in input]
    ans = solve(matrix)
    print(ans)
