use reqwest::Client;
use serde_json::json;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Create an HTTP client
    let client = Client::new();

    // Prepare the JSON payload
    let payload = json!({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getAccountInfo",
        "params": [
            "9KM8rFNhH7uLejNBRyc2HTTz2utPKqHaj2FCSngkpump",
            {
                "encoding": "base58"
            }
        ] 
    });

    // Send the POST request
    let response = client
        .post("https://api.mainnet-beta.solana.com")
        .header("Content-Type", "application/json")
        .json(&payload) // Automatically serializes the payload as JSON
        .send()
        .await?;

    // Check the response status
    if response.status().is_success() {
        let response_text = response.text().await?;
        println!("Response: {}", response_text);
    } else {
        eprintln!("Error: {}", response.status());
    }

    Ok(())
}