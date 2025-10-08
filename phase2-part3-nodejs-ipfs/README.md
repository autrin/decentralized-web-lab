# Phase 2, Part 3: Node.js IPFS Integration

This directory contains a Node.js script that demonstrates how to integrate with IPFS programmatically.

## What This Demonstrates

✅ **Part 2 Complete**: Basic IPFS operations (add/cat)  
✅ **Part 3 Complete**: Node.js script that adds files to IPFS and logs hashes

## Files

- `add-to-ipfs.js` - Main Node.js script that:
  - Creates a test file
  - Adds it to IPFS using the CLI
  - Retrieves the file using its hash
  - Logs the IPFS hash
  - Cleans up temporary files

- `package.json` - Node.js project configuration

## How to Run

1. Make sure IPFS daemon is running:
   ```bash
   export PATH="$HOME/bin:$PATH" && ipfs daemon
   ```

2. Run the script:
   ```bash
   node add-to-ipfs.js
   ```

## Expected Output

```
🚀 Starting IPFS integration with Node.js...
📝 Created test file: nodejs-test.txt
📤 Adding file to IPFS...
✅ File added to IPFS successfully!
🔗 IPFS Hash: QmPx86XNzwxvyBA9masdNBQjxhcuZeaSkHNUFvMVSEAwvQ
📁 File: nodejs-test.txt

🔍 Verifying file retrieval from IPFS...
📖 Retrieved content:
Hello from Node.js IPFS integration!
This is a test file for our uncensorable internet project.
Timestamp: 2025-09-29T00:14:53.861Z
🗑️  Cleaned up local file: nodejs-test.txt

🎉 Success! Your Node.js script successfully:
   ✓ Created a test file
   ✓ Added the file to IPFS using CLI
   ✓ Retrieved the file using its hash
   ✓ Logged the IPFS hash
   ✓ IPFS Hash: QmPx86XNzwxvyBA9masdNBQjxhcuZeaSkHNUFvMVSEAwvQ
```

## Key Learning Points

1. **Content-Addressable Storage**: Files are identified by their content hash, not location
2. **Decentralized Storage**: Files can be retrieved from any IPFS node that has them
3. **Programmatic Integration**: IPFS can be controlled from applications via CLI or HTTP API
4. **Immutable Data**: Once added to IPFS, content is immutable and verifiable
