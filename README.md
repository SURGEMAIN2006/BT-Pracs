# Blockchain Implementation Using Python, Flask API and Postman

## 1. Project Overview

This practical implements a blockchain using Python and Flask. It demonstrates:

- Creating blocks
- Adding transactions
- Mining blocks using Proof of Work
- Validating the blockchain
- Connecting two blockchain nodes
- Replacing the chain with a longer valid chain
- Testing REST APIs using Postman

## 2. Required Libraries

Install the required libraries using:

```bash
pip install Flask requests
```

## 3. Run the Python Files

I have created two Python files:

- `prac1.py` – Node 1
- `prac2.py` – Node 2

Open two separate terminals in VS Code.

**Terminal 1:**

```bash
python prac1.py
```

Node 1 runs at:

`http://127.0.0.1:5001`

**Terminal 2:**

```bash
python prac2.py
```

Node 2 runs at:

`http://127.0.0.1:5002`

Keep both terminals running while testing in Postman.

## 4. Postman API Testing (Follow This Order)

### Step 1: Connect Nodes

First, connect Node 1 with Node 2.

- Method: POST
- URL: `http://127.0.0.1:5001/connect_nodes`

Go to Body → raw → JSON and enter:

```json
{
  "nodes": [
    "http://127.0.0.1:5002"
  ]
}
```

Click **Send**.

Expected response:

```json
{
  "message": "all nodes are now connected",
  "Total nodes": [
    "127.0.0.1:5002"
  ]
}
```

**Purpose:** Connects Node 1 to Node 2 so that they can communicate with each other.

### Step 2: Add a Transaction

- Method: POST
- URL: `http://127.0.0.1:5001/add_transaction`

Go to Body → raw → JSON:

```json
{
  "sender": "Pritam",
  "receiver": "Rahul",
  "amount": 100
}
```

Click **Send**.

Expected response:

```json
{
  "Message": "The transaction is added to block 2"
}
```

**Purpose:** Adds transaction details to the list of pending transactions.

### Step 3: Mine a Block

- Method: GET
- URL: `http://127.0.0.1:5001/mine_block`

Click **Send**.

Expected response contains:

```json
{
  "message": "block is mined",
  "index": 2
}
```

Other fields include timestamp, proof and previous hash.

**Purpose:** Mines a new block using the Proof of Work algorithm. The pending transaction is included in the newly created block.

### Step 4: Get the Blockchain

- Method: GET
- URL: `http://127.0.0.1:5001/get_chain`

Click **Send**.

Expected response contains:

```json
{
  "chain": [],
  "length": 2
}
```

The actual `chain` field contains the complete block details, not an empty list.

**Purpose:** Displays all blocks stored in the blockchain, including their transactions, hashes, proof and timestamps.

### Step 5: Validate the Blockchain

- Method: GET
- URL: `http://127.0.0.1:5001/is_valid`

Click **Send**.

Expected response:

```json
{
  "message": "Your chain is validated"
}
```

**Purpose:** Checks whether the blockchain is valid by verifying previous hashes and Proof of Work.

### Step 6: Replace the Chain

- Method: GET
- URL: `http://127.0.0.1:5001/replace_chain`

Click **Send**.

Possible response:

```json
{
  "message": "chain not replaced"
}
```

**Purpose:** Checks whether another connected node has a longer valid blockchain. If a longer valid chain is found, Node 1 replaces its chain with that chain.

**Important:** If Node 2 does not have a longer chain than Node 1, the response will be `chain not replaced`. This is normal.

## 5. Important API Endpoints

| API Endpoint | Method | Purpose |
|---|---|---|
| `/mine_block` | GET | Mines a new block |
| `/get_chain` | GET | Displays the blockchain |
| `/is_valid` | GET | Validates the blockchain |
| `/add_transaction` | POST | Adds a transaction |
| `/connect_nodes` | POST | Connects blockchain nodes |
| `/replace_chain` | GET | Replaces the chain if a longer valid chain exists |

## 6. Important Concepts

**Blockchain:** A chain of blocks containing transaction information.

**Block:** Stores data such as index, timestamp, proof, previous hash and transactions.

**Genesis Block:** The first block in the blockchain.

**Proof of Work:** A process of finding a valid proof by repeatedly calculating hashes.

**SHA-256:** A cryptographic hashing algorithm used to generate hashes.

**Flask:** A Python framework used to create REST APIs.

**Postman:** A tool used to send HTTP requests and test APIs.

**Node:** An individual computer or server participating in the blockchain network.

**Chain Validation:** Checks whether the blockchain has valid hashes and Proof of Work.

**Chain Replacement:** Replaces the current blockchain with a longer valid blockchain from another connected node.

## 7. Final Result

Successfully implemented a blockchain using Python and Flask. Tested blockchain operations such as adding transactions, mining blocks, retrieving the blockchain, validating the chain and connecting nodes using Postman.




# Practical 8 – Single Node Blockchain Using Python and Flask

## Aim
To implement a single-node blockchain in Python using Flask API and demonstrate blockchain operations such as creating blocks, adding transactions, mining blocks using Proof of Work, validating the blockchain, and accessing the blockchain through REST APIs.

## Requirements
- Python
- VS Code
- Flask
- Requests
- Postman

## Step 1: Install Required Libraries

Open the VS Code terminal and run:

```bash
pip install flask requests
```

## Step 2: Create Python File

Create a file named:

`prac8.py`

Paste the Practical 8 Python blockchain code into this file and save it.

## Step 3: Run the Python Program

Open the terminal and execute:

```bash
python prac8.py
```

The Flask server will start at:

`http://127.0.0.1:5001`

Keep the terminal running while testing with Postman.

## Step 4: Open Postman

Open Postman and create a new HTTP request.

### 1. View Initial Blockchain

- Method: GET
- URL: `http://127.0.0.1:5001/get_chain`
- Click Send.

Expected output: Initial blockchain containing the Genesis Block and length 1.

### 2. Add Transaction

- Method: POST
- URL: `http://127.0.0.1:5001/add_transaction`
- Select Body → raw → JSON.

Enter:

```json
{
  "sender": "Pritam",
  "receiver": "Rahul",
  "amount": 100
}
```

Click Send.

Expected output:

```json
{
  "Message": "The transaction is added to block 2"
}
```

### 3. Mine Block

- Method: GET
- URL: `http://127.0.0.1:5001/mine_block`
- Click Send.

Expected output: Block is mined successfully.

### 4. View Updated Blockchain

- Method: GET
- URL: `http://127.0.0.1:5001/get_chain`
- Click Send.

Expected output: Updated blockchain with length 2 and the transaction stored in block 2.

### 5. Validate Blockchain

- Method: GET
- URL: `http://127.0.0.1:5001/is_valid`
- Click Send.

Expected output:

```json
{
  "message": "Your chain is validated"
}
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /get_chain | View blockchain |
| POST | /add_transaction | Add transaction |
| GET | /mine_block | Mine a new block |
| GET | /is_valid | Validate blockchain |
| POST | /connect_nodes | Connect nodes |
| GET | /replace_chain | Replace with longer valid chain |

## Result

Successfully implemented a single-node blockchain using Python and Flask. Transactions were added, blocks were mined using Proof of Work, and blockchain validity was checked using Postman.


# Blockchain Technology – Practical 4 (A, B, C and D)

---

# Practical 4.A – Generate Multiple Blocks in Blockchain

## Aim
To implement a simple blockchain that generates multiple blocks, stores transactions in each block, links blocks using cryptographic hashes and displays the complete blockchain.

## 1. Run the Program

Open the VS Code terminal and type:

```powershell
python prac4a.py
```

## 2. Terminal Inputs

**No manual input is required.**

The program automatically:
- Generates 5 blocks.
- Creates 3 transactions per block.
- Generates hashes for each block.
- Links each block with the previous block's hash.

## 3. Expected Output

The terminal displays:

```text
=== BLOCKCHAIN ===

Block 0
Index: 0
Transactions: []
Previous Hash: 0
Hash: Generated Hash

Block 1
Index: 1
Transactions:
User1 -> User2
User1 -> User2
User1 -> User2

Block 2
Index: 2
Transactions:
User2 -> User3
User2 -> User3
User2 -> User3
```

The remaining blocks are displayed similarly.

*Note: Actual output is displayed in JSON format according to the journal code. Hash values are generated automatically.*

## 4. Result

Thus, a blockchain containing multiple linked blocks and transactions was successfully implemented.

---

# Practical 4.B – Blockchain Integrity Validation

## Aim
To implement a blockchain with multiple blocks and validate its integrity by checking block index, previous hash and current hash.

## 1. Run the Program

Open the VS Code terminal and type:

```powershell
python prac4b.py
```

## 2. Terminal Inputs

**No manual input is required.**

The program automatically:
- Creates a genesis block.
- Generates two additional blocks.
- Adds transactions to the blocks.
- Checks the blockchain's integrity.

## 3. Expected Output

The terminal displays the generated blocks.

At the end, you should see:

```text
Is blockchain valid? True
```

## 4. Result

Thus, blockchain integrity was successfully verified using block index, previous hash and current hash validation.

---

# Practical 4.C – Blockchain Using Proof of Work

## Aim
To implement a blockchain using Proof of Work (PoW), where blocks are mined by finding a nonce that generates a hash satisfying the required difficulty.

## 1. Run the Program

Open the VS Code terminal and type:

```powershell
python prac4c.py
```

## 2. Terminal Inputs

**No manual input is required.**

The program automatically:
- Creates 3 blocks.
- Adds 3 transactions per block.
- Uses a difficulty level of 4.
- Increases the nonce until the generated hash starts with four zeros.
- Mines and displays the blocks.

## 3. Expected Output

The terminal displays the blockchain with block details.

Example:

```text
=== BLOCKCHAIN ===

Block Index: 0
Nonce: ...
Hash: 0000...

Block Index: 1
Nonce: ...
Hash: 0000...

Block Index: 2
Nonce: ...
Hash: 0000...
```

*Note: The actual output format depends on the print statements in your journal code. Nonce and hash values are generated automatically. The mined hashes should start with four zeros.*

## 4. Result

Thus, a blockchain using the Proof of Work consensus mechanism was successfully implemented.

---

# Practical 4.D – Blockchain Using User-Provided Transactions

## Aim
To implement a blockchain that generates multiple linked blocks using user-provided transaction details.

## 1. Run the Program

Open the VS Code terminal and type:

```powershell
python prac4d.py
```

## 2. Enter the Inputs in Terminal

When the program asks:

**Enter number of blocks:**

```text
3
```

**Enter transactions per block:**

```text
2
```

Now enter the transaction details when prompted.

### Block 1 – Transaction 1

```text
Sender: Bob
Recipient: Alice
Amount: 100
```

### Block 1 – Transaction 2

```text
Sender: Rahul
Recipient: Pritam
Amount: 200
```

### Block 2 – Transaction 1

```text
Sender: John
Recipient: David
Amount: 300
```

### Block 2 – Transaction 2

```text
Sender: Sam
Recipient: Alex
Amount: 400
```

### Block 3 – Transaction 1

```text
Sender: Peter
Recipient: Michael
Amount: 500
```

### Block 3 – Transaction 2

```text
Sender: Kevin
Recipient: Ryan
Amount: 600
```

## 3. Expected Output

After entering all the details, the program displays:

```text
=== BLOCKCHAIN ===

Block 0:
Genesis Block

Block 1:
Transactions:
Bob -> Alice : 100
Rahul -> Pritam : 200

Block 2:
Transactions:
John -> David : 300
Sam -> Alex : 400

Block 3:
Transactions:
Peter -> Michael : 500
Kevin -> Ryan : 600
```

*Note: Your actual output will follow the JSON/print format in your Python code and will include automatically generated hash values.*

## 4. Result

Thus, a blockchain was successfully implemented using user-provided transaction details. Multiple blocks were generated and linked using cryptographic hashes.

---

# Important Practical Exam Notes

| Practical | Manual Input Required? | Main Concept |
|---|---|---|
| 4.A | No | Multiple blocks and transactions |
| 4.B | No | Blockchain validation |
| 4.C | No | Proof of Work and mining |
| 4.D | Yes | User-provided transactions |

## Important Terminal Commands

```powershell
python prac4a.py
python prac4b.py
python prac4c.py
python prac4d.py
```

## Important Concepts for Viva

1. **Blockchain:** A chain of blocks linked using cryptographic hashes.
2. **Genesis Block:** The first block in a blockchain.
3. **Hash:** A fixed-length value generated from data using a hashing algorithm.
4. **SHA-256:** A cryptographic hashing algorithm.
5. **Nonce:** A number changed during mining to find a valid hash.
6. **Proof of Work:** A consensus mechanism that requires computational work to mine a block.
7. **Previous Hash:** The hash of the previous block, used to link blocks together.
8. **Blockchain Validation:** Checking whether blocks and their hashes are valid.

