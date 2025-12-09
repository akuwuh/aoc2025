package main

import (
	"fmt"
	"maps"
	"os"
	"strings"
)

func main() {
	data, _ := os.ReadFile("input.txt")

	lines := strings.Split(string(data), "\n")
	var grid [][]rune
	for _, line := range lines {
		if line != "" {
			grid = append(grid, []rune(line))
		}

	}

	solve(grid)

	// Build and write output
	out := ""
	for _, line := range grid {
		fmt.Println(string(line))
		out += string(line) + "\n"
	}
	os.WriteFile("output.txt", []byte(out), 0644)
}

func solve(grid [][]rune) { // pass by reference

	var startCol int
	for i, char := range grid[0] {
		if char == 'S' {
			startCol = i
			break
		}
	}

	// alright logic is we keep track of all the indices that has lines going down:
	// probably a set
	// if cur col is in the set and grid[r][c] is:
	// case 1: '.' then we just replace it with '|' if we want it to look pretty
	// case 2: '^' then we remove the index from the set and then add in a col + 1 and col - 1 (need to account for bounds)
	// 			   then we just increase count ? might have to check the condition that either splitting left or right is possible

	cols := len(grid[0])
	activeCols := make(map[int]bool, cols) // Pre-allocate map capacit
	activeCols[startCol] = true            // initialize startCol
	total := 0
	for r, row := range grid[1:] { // Start iterating from row 1
		newActiveCols := maps.Clone(activeCols)
		for c, char := range row {
			if activeCols[c] && char == '^' {
				// remove then add + 1 and - 1
				newActiveCols[c] = false
				if c-1 >= 0 {
					newActiveCols[c-1] = true
					grid[r+1][c-1] = '|'
				}
				if c+1 < cols {
					newActiveCols[c+1] = true
					grid[r+1][c+1] = '|'
				}
				// might need some more logic here but based on the test case, this checking is fine
				total += 1 // increment
			} else if activeCols[c] && char == '.' {
				grid[r+1][c] = '|'
			}

		}
		activeCols = newActiveCols
	}

	fmt.Printf("Total: %d\n", total)
}
