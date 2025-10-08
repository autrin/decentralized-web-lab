const { exec } = require('child_process');
const fs = require('fs');
const { promisify } = require('util');

const execAsync = promisify(exec);

async function addFileToIPFS() {
  try {
    console.log('🚀 Starting IPFS integration with Node.js...');

    // Create a test file
    const testContent = 'Hello from Node.js IPFS integration!\nThis is a test file for our uncensorable internet project.\nTimestamp: ' + new Date().toISOString();
    const testFileName = 'nodejs-test.txt';

    // Write the test file
    fs.writeFileSync(testFileName, testContent);
    console.log(`📝 Created test file: ${testFileName}`);

    // Add the file to IPFS using CLI
    console.log('📤 Adding file to IPFS...');
    const { stdout: addOutput } = await execAsync(`export PATH="$HOME/bin:$PATH" && ipfs add ${testFileName}`);

    // Parse the hash from the output
    const hashMatch = addOutput.match(/added\s+(\w+)\s+/);
    if (!hashMatch) {
      throw new Error('Could not parse IPFS hash from output');
    }

    const ipfsHash = hashMatch[1];

    // Log the hash
    console.log('✅ File added to IPFS successfully!');
    console.log(`🔗 IPFS Hash: ${ipfsHash}`);
    console.log(`📁 File: ${testFileName}`);

    // Verify by reading the file back from IPFS
    console.log('\n🔍 Verifying file retrieval from IPFS...');
    const { stdout: catOutput } = await execAsync(`export PATH="$HOME/bin:$PATH" && ipfs cat ${ipfsHash}`);

    console.log('📖 Retrieved content:');
    console.log(catOutput);

    // Clean up the local test file
    fs.unlinkSync(testFileName);
    console.log(`🗑️  Cleaned up local file: ${testFileName}`);

    console.log('\n🎉 Success! Your Node.js script successfully:');
    console.log('   ✓ Created a test file');
    console.log('   ✓ Added the file to IPFS using CLI');
    console.log('   ✓ Retrieved the file using its hash');
    console.log('   ✓ Logged the IPFS hash');
    console.log(`   ✓ IPFS Hash: ${ipfsHash}`);

  } catch (error) {
    console.error('❌ Error:', error.message);
    console.log('\n💡 Make sure your IPFS daemon is running:');
    console.log('   export PATH="$HOME/bin:$PATH" && ipfs daemon');
  }
}

// Run the function
addFileToIPFS();
