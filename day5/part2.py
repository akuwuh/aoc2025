


def solve(ranges):
    ans = 0 
    ranges.sort(key=lambda x:x[0])
    intervals = [ranges[0]]
    for r in range(1,len(ranges)):
        start,end = ranges[r][0], ranges[r][1]
        last_merged = intervals[-1]
        if start > last_merged[1]: # new interval
            intervals.append(ranges[r])
        elif end > last_merged[1]:
            intervals[-1][1] = end

    
    for low,high in intervals:
        ans += high-low + 1

    return ans

        

if __name__ == "__main__":
    input = open("input.txt", "r").read().splitlines()

    ranges = []
    for line in input:
        if '-' in line:
            ra = line.split('-')
            ranges.append([int(ra[0]), int(ra[1])])

    
    ans = solve(ranges)

    print(ans)