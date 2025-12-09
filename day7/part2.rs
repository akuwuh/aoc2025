#!/usr/bin/env rust-script

use std::fs::*; // importing all fs

fn main() {
    let input = read_to_string("test.txt").unwrap(); // right now its a String at

    let grid = input
        .lines()
        .map(
            |line| line.chars().collect(), // collect chars being split
        )
        .collect::<Vec<Vec<char>>>(); // holy shit this was hard to rmemeber

    println!("{:#?}", grid);

    let total = solve(grid);

    println!("Total: {}", total);
}

fn solve(grid: Vec<Vec<char>>) -> i64 {
    let start_col: i64;
    let cols = grid[0].len();
    let rows = grid.len();
    let mut active_cols: Vec<i64> = vec![0; cols]; // instead of map, we just use an array
    for c in 0..cols {
        if grid[0][c] == 'S' {
            start_col = c;
        }
    }

    active_cols[start_col] = 1; // init for start column

    for r in 1..rows {
        let mut new_active_cols = vec![0; cols];
        for c in 0..cols {
            if active_cols[c] > 0 && grid[r][c] == '^' {
                // need to split
                if c - 1 >= 0 {
                    new_active_cols[c - 1] += active_cols[c]; // will account for cascading anyway
                }
                if c + 1 < cols {
                    new_active_cols[c + 1] += active_cols[c];
                }
            } else if active_cols[c] > 0 && grid[r][c] == '.' {
                // we either cascade if empty or we add
                new_active_cols[c] += active_cols[c];
            }
        }

        active_cols = new_active_cols;
    }

    let total = active_cols.iter().sum();
    total
}
