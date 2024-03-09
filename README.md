# Block Chain And KYC
## Steps to Run

1. *Download and Install Node.js:*
   - Ensure you have Node.js version 10.11.1 with LTS installed. If not, download and install it from [Node.js website](https://nodejs.org).

2. *Download Ganache:*
   - Download Ganache, a personal blockchain for Ethereum development, from [Truffle Framework](https://truffleframework.com/ganache).

3. *Install Truffle:*
   - Install Truffle, a development environment for Ethereum, using NPM (Node Package Manager). Run the following command in your terminal: npm i -g truffle.

4. *Configure Ganache:*
   - Install and launch Ganache. In Ganache settings, configure the port to 9545. This ensures that Ganache's blockchain is running on the specified port.

5. *Set Up Ethereum Network:*
   - Open Ganache and create a new workspace. Configure the Ethereum network by specifying the host and port settings. Connect Ganache to your Truffle project by setting the network parameters in the Truffle configuration file (truffle-config.js).

6. *Install Project Dependencies:*
   - Navigate to the project root directory in the terminal. Run npm install to install project dependencies based on the specifications defined in the package.json file.

7. *Compile Smart Contracts:*
   - Execute the command truffle compile to compile the smart contracts in your project. This step generates the bytecode that will be deployed to the Ethereum network.

8. *Migrate Contracts to Blockchain:*
   - Deploy and migrate the compiled contracts to the blockchain by running the truffle migrate command. This step initializes the smart contracts on the Ethereum network.

9. *Set Environment Variables:*
   - Configure any required environment variables for your project. This may include setting up Ethereum provider URLs, API keys, database connections, or other configuration settings.

10. *Configure the Connection:*
    - If your project involves a front-end application interacting with the Ethereum blockchain, ensure that the Web3 connection is properly configured. Update the Web3 provider with the Ethereum network details.

11. *Build and Run Project:*
    - Run the command npm run buildandrun in a new terminal within the project root. This command may perform tasks such as bundling assets, starting a development server, or initiating other build processes.

12. *Access the Application:*
    - Open your web browser and navigate to [http://localhost/](http://localhost/) to access the running application.

13. *Explore Application Features:*
    - Familiarize yourself with the application features and functionalities. Ensure that the KYC innovation aspects are working as expected.

14. *Testing:*
    - Perform any necessary testing procedures to ensure that the KYC process and deepfake detection mechanisms are functioning properly.
