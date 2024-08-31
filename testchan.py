import requests

RPC_URL = 'https://api.mainnet-beta.solana.com'

def get_account_info(public_key):
    response = requests.post(RPC_URL, json={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getAccountInfo",
        "params": [public_key]
    })
    return response.json()

def get_recent_transactions(public_key):
    response = requests.post(RPC_URL, json={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getConfirmedSignaturesForAddress2",
        "params": [public_key]
    })
    return response.json()

def get_transaction_details(signature):
    response = requests.post(RPC_URL, json={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getConfirmedTransaction",
        "params": [signature]
    })
    return response.json()

def analyze_wallet(public_key):
    # Get account info
    account_info = get_account_info(public_key)
    print("Account Info:", account_info)
    
    # Get recent transactions
    transactions = get_recent_transactions(public_key)
    print("Recent Transactions:", transactions)
    
    # Get details for each transaction
    transaction_signatures = [tx['signature'] for tx in transactions['result']]
    for signature in transaction_signatures:
        transaction_details = get_transaction_details(signature)
        print("Transaction Details:", transaction_details)

if __name__ == "__main__":
    public_key = "3boWpKTf5keVKmdhbU7HnKmFjuCVyfa9sVAsEEb4WfJt"  # Replace with the actual wallet public key
    analyze_wallet(public_key)
