#!/usr/bin/env rust-script

// learning rust lel


use std::fs::read_to_string; // imports just read_to_string
                             // use std::fs::*; // can use this to import everything and dont have to use fs::...

// fn main() -> std::io::Result<()>{   // so we can do read_to_string? instead of read_to_string.expect("error")
// this means program fails + throws error to OS
// i guess this is good for offensive programming -> for critical systems

fn main() {
    let input = read_to_string("test.txt").unwrap(); // of type String -> data structure that poitns to the text buffer in the heap (it contains the content of the file read i think)

    // let lines: Vec<&str> = input.lines().collect(); // gotta collect it + we use &str to create a vector of str pointers to the text buffer  
    
    // using turbo fish format

    //let lines = input.lines().collect::<Vec<&str>>(); // defined that the collect functoin needs to return a Vec<&str> format
    
    // println!("{:#?}", lines); // ':?' = debug formatter to print vecs. the # means pretty print

    // now lines is vector of strings. we should first count the lengths of all the spacing between the operators then push each of the strings above to a new datastructure

    // we want a vector of vectors of chars to travser
    
    let grid = input.lines().map(|line| line.chars().collect()).collect::<Vec<Vec<char>>>();


    // now we need to traverse the bottom row to determine the operator + the indentation length
    let rows = grid.len(); let cols = grid[0].len();
    let mut transformed = Vec::new(); // create new vector of unknown type? 
    let mut cur_line = Vec::<String>::new();
    for c in 0..cols { // traverse horizontally first then vertically upwards.
        // each vertical should be a new string 
        let mut new_num = String::new();
        for r in (0..rows).rev() { // traverse backwards
            // last row is operator row
            // if next column is an operator we skip and make new string 
            // if current one is an operator we create new string

            // STIL HAVE TO HANDLE FIRST OPERATOR COORERCLTY
            let is_operator = grid[r][c] == '+' || grid[r][c] == '*';
            if is_operator && !cur_line.is_empty() {
                transformed.push(cur_line);
                cur_line = Vec::<String>::new(); 
                cur_line.push(grid[r][c].to_string());
            } else if r == rows - 1 {
                continue; // skip this row
            }
            
            // valid number construction 
            new_num.push(grid[r][c]);
        }

        if !new_num.trim().is_empty() {
            cur_line.push(new_num); // 
        }
    } 

    // add last one 



    println!("{:#?}", transformed);       
}
