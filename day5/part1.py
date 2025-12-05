


def solve(ranges,ids):
    ans = 0
    for i in ids:
        for low, high in ranges:
            if i in range(low,high):
                ans += 1
                break  # found one range, move to next id
 n   return ans

if __name__ == "__main__":
    input = open("input.txt", "r").read().splitlines()

    ranges=[]   
    ids=[]
    for line in input:
        if '-' in line:
            ra = line.split('-')
            ranges.apped([int(ra[0]), int(ra[1])])
        elif line.isdigit():
            ids.append(int(line))
    
    ans = solve(ranges,ids)

    print(ans)