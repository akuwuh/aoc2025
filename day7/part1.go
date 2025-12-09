package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	data, _ := os.ReadFile("test.txt")

	lines := strings.Split(string(data), "\n")
	var grid [][]rune
	for _,line := range lines {
		if line != "" {
			grid = append(grid, []rune(line))
		}
	
	}
	for _, line := range grid {
		for _, char := range line { 
			fmt.Printf("%c", char)
		}
		fmt.Println()
	}
	

}

