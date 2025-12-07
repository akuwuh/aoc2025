#!/usr/bin/env rust-script  // shebang so we can do './part2.rs' 

use std::fs::read_to_string; // imports just read_to_string
// use std::fs::*; // can use this to import everything and dont have to use fs::...

// fn main() -> std::io::Result<()>{   // so we can do read_to_string? instead of read_to_string.expect("error")
                                    // this means program fails + throws error to OS 
                                    // i guess this is good for offensive programming -> for critical systems


fn main() {  

    let input = read_to_string("./test.txt").unwrap(); // vars immutable? 

    println!(input);

    
}
