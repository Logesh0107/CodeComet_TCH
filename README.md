## Steps to Run

1. Download version 20.11.1 with LTS 
2. Download from https://nodejs.org.
3. Installing Node.js in linux:

Open a terminal.
Update the package repository information:


sudo apt update
Install Node.js and npm (Node Package Manager) using the following command:

sudo apt install nodejs npm
Verify the installation by checking the installed versions:


node -v
npm -v
    
3. Download Ganache, a personal blockchain for Ethereum development
4. Install Ganache from https://truffleframework.com/ganache.
5. Install Truffle, a development environment for Ethereum, using NPM (Node Package Manager).
6. Install truffle using NPM using the command npm i -g truffle.
7. Install and launch Ganache. In Ganache settings, configure the port to 9545.
8. This ensures that Ganache's blockchain is running on the specified port
10. Now we have to set up the Ethereum network.
11. Open Ganache and create a new workspace. 
12. Configure the Ethereum network by specifying the host and port settings.
13. Connect Ganache to your Truffle project by setting the network parameters in the Truffle configuration file (truffle-config.js).
