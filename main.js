const Web3 = require('web3');

// Connect to the Ethereum network using an RPC server
const rpcServerAddress = 'https://rpc.sepolia.org';
const web3 = new Web3(rpcServerAddress);

// Define the address we want to filter transactions for
const address = '0x45A616Fe04b73fD9B8d3D3172578981C1ea7D1eE';

// Create a filter that matches transactions where the 'from' or 'to' address is equal to our address
const filter = web3.eth.filter({address: address });

// Define a function that will be called whenever a new transaction is detected
function handleTransaction(error, event) {
//   if (error) {
//     console.error(error);
//     return;
//   }
  console.log('New transaction detected:');
  console.log(`  Hash: ${event.transactionHash}`);
  web3.eth.getTransaction(event.transactionHash, (error, transaction) => {
    console.log(transaction);
  });
}

// Start listening for new transactions
filter.watch(handleTransaction);