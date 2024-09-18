use tokio_tungstenite::connect_async;
use tokio_tungstenite::tungstenite::protocol::Message;
use serde_json::{json, Value};
use futures_util::{stream::StreamExt, sink::SinkExt}; // Import necessary traits

#[tokio::main]
async fn main() {
    // Set the WebSocket URL and token mint address
    let ws_url = "wss://api.mainnet-beta.solana.com/";
    let token_mint_address = "HyzFqBd6WUqYq2eX8vU8sX4CVNp15druJScRvW4apump";

    // Create the JSON payload to get token supply
    let payload = json!({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenSupply",
        "params": [token_mint_address],
    });

    // Connect to the WebSocket
    let (mut ws_stream, _) = connect_async(ws_url)
        .await
        .expect("Failed to connect");

    println!("Connected to WebSocket");

    // Send the request
    ws_stream
        .send(Message::Text(payload.to_string()))
        .await
        .expect("Failed to send message");

    // Wait for the response
    if let Some(response) = ws_stream.next().await {
        match response {
            Ok(Message::Text(text)) => {
                let json_response: Value = serde_json::from_str(&text).expect("Failed to parse JSON");
                println!("Response: {}", json_response);
            }
            Ok(_) => println!("Received non-text message"),
            Err(e) => eprintln!("Error receiving message: {}", e),
        }
    }
}
