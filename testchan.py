import requests
import json

# Define the Solana JSON RPC endpoint
SOLANA_RPC_URL = 'https://api.mainnet-beta.solana.com'

def send_request(method, params=None):
    headers = {'Content-Type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params or []
    }
    response = requests.post(SOLANA_RPC_URL, headers=headers, data=json.dumps(payload))
    return response.json()

def get_account_transactions(pubkey, limit=10):
    result = send_request("getConfirmedSignaturesForAddress2", [pubkey, {"limit": limit}])
    return result

def get_transaction_details(signature):
    # Updated method: use getTransaction to check for new parameters or methods
    result = send_request("getTransaction", [signature, {"encoding": "jsonParsed"}])
    return result

def main():
    print("Solana Transaction History")
    pubkey = input("Enter account public key: ")
    limit = int(input("Enter the number of recent transactions to retrieve: "))

    # Get recent transaction signatures
    transaction_signatures = get_account_transactions(pubkey, limit)
    
    if 'error' in transaction_signatures:
        print(f"Error fetching transaction signatures: {transaction_signatures['error']['message']}")
        return

    print(f"\nRecent Transactions for {pubkey}:\n")
    
    for tx in transaction_signatures['result']:
        signature = tx['signature']
        print(f"Signature: {signature}")
        details = get_transaction_details(signature)
        if 'error' in details:
            print(f"Error fetching transaction details: {details['error']['message']}")
        else:
            print(json.dumps(details, indent=4))
        print("-" * 80)
        alskdfj
if __name__ == "__main__":
    main()
