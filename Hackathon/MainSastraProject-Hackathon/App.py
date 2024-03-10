from flask import Flask,flash,render_template, request, jsonify
from web3 import Web3
import json
import time

app = Flask(__name__)

# Connect to Ganache (local Ethereum node)
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Load contract ABI
with open('BankingABI.json') as f:
    abi = json.load(f)

# Contract address (deployed on Ganache)
contract_address = "0xc7918359F69E3886dbcEb603CC38FD6670D7fD20"

# Define contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)


@app.route('/')
def index():
    return render_template('Blockchain.html')

@app.route('/deposit', methods=['GET','POST'])
def deposit():
    if request.method == 'POST':
       amount=request.form['amount']
       print(str(web3.eth.accounts[0]))
       tx_hash = contract.functions.deposit().transact({'from':web3.eth.accounts[0], 'value': amount})
       data={'message': 'Deposited successfully...', 'transactionHash': tx_hash.hex()}
       print(data)
       return flash("Deposited Successfully","success")
    return render_template('Bank.html')


@app.route('/withdraw', methods=['GET','POST'])
def withdraw():
    if request.method == 'POST':
       amount = request.form['amount']
    #    if amount is None or not isinstance(amount, int) or amount <= 0:
    #       return jsonify({'error': 'Invalid amount'}) 

       tx_hash = contract.functions.withdraw(int(amount)).transact({'from': web3.eth.accounts[0]})
    # receipt = web3.eth.waitForTransactionReceipt(tx_hash)

       data={'message': 'Withdrawal successfully...', 'transactionHash': tx_hash.hex()}
       print(data)
       return flash("Withdraw Successfully","success")
    return render_template('Bank.html')




@app.route("/createNew", methods=['GET',"POST"])
def create_new_user():
     if request.method == 'POST':
        # account = request.form["account"]
        account = web3.eth.accounts[0]
        initial_balance = request.form["initial_balance"]
        try:
           tx_hash = contract.functions.createNewUser(int(initial_balance)).transact({'from': account})
           user={
            "tf_hash":tx_hash.hex(),
            "msg":"Suucessfully New account Created"
            }
        except Exception as e:
            print('Error--->',e)
            user={
                 "tf_hash":e,
                "msg":"Error occured account Created"
            }
        
        return render_template('index.html',data=user)
     return render_template('AddRecord.html')

@app.route('/addRecord', methods=['GET','POST'])
def Tranactions():
    if request.method == 'POST':
        account = web3.eth.accounts[1]
        amount = int(request.form['amount'])
        

        tx_hash = contract.functions.transfer(account, amount).transact({'from': web3.eth.accounts[0]})

        data={'message': 'Record added successfully', 'transactionHash': tx_hash.hex()}
        print(data)
        return render_template('AddTranac.html',data=data)
    return render_template('AddTranac.html')




@app.route('/dashboard', methods=['GET'])
def Dashboard():
    balance= contract.functions.getBalance(web3.eth.accounts[0]).call()
    history = contract.functions.getTransactionHistory(web3.eth.accounts[0]).call()
    # Convert tuple of struct to dictionary
    history_dict = []
    for tx in history:
        tx_dict = {
            "from": tx[0],
            "to": tx[1],
            "amount": tx[2],
            "timestamp": tx[3]
        }
        history_dict.append(tx_dict)
    return render_template('Dashboard.html',balance=balance,history=history_dict)
    # return jsonify({'Balance':balance,"transaction_history": history_dict})
     


if __name__ == '__main__':
    app.run(debug=True)




 