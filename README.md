# BlockVerify — Blockchain-Based Student Record Verification System

BlockVerify is a blockchain-based student record verification system designed to securely store and verify academic records.

## Features

- Add and store student academic records
- Store each record as a blockchain block
- SHA-256 hash-based data integrity
- Blockchain verification
- Tamper detection
- Blockchain explorer
- Simple web-based interface

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- SHA-256 Hashing
- Blockchain

## How It Works

1. A student record is entered through the web application.
2. The record is stored as a new block.
3. Each block contains the hash of the previous block.
4. SHA-256 is used to generate block hashes.
5. The blockchain can be verified for integrity.
6. If a block is modified, the system detects the tampering.

## Project Structure

```text
BlockVerify/
├── app.py
├── blockchain/
│   ├── block.py
│   └── blockchain.py
├── templates/
├── static/
├── requirements.txt
└── README.md
Live Demo

https://blockverify-1.onrender.com/

Source Code

GitHub Repository:

https://github.com/BhavanaReddy1001/BlockVerify

Conclusion

BlockVerify provides a secure and reliable way to store and verify student academic records using blockchain technology and SHA-256 hashing.
