use std::process::Command;
use std::time::Instant;

fn main() {
    // Specify the path to the program you want to time
    let program_path = "../rpc/target/debug/rpc"; // Change this to the actual program path

    // Measure the start time
    let start_time = Instant::now();

    // Execute the command
    let output = Command::new(program_path)
        .output() // Capture the output
        .expect("Failed to execute the program");

    // Measure the elapsed time
    let elapsed_time = start_time.elapsed();

    // Convert the output to a String
    let stdout = String::from_utf8_lossy(&output.stdout);
    let stderr = String::from_utf8_lossy(&output.stderr);

    // Print the results
    println!("Output:\n{}", stdout);
    println!("Errors:\n{}", stderr);
    println!("Elapsed time: {:?}", elapsed_time);
}

