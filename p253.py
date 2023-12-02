# --------------253 Proj----------------
from web3 import Web3
# Import time module here
import time
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0xb919E3481a8c945e2f1ed69E341AeA2197fb84Bf'
James_account = '0x697F91a4711F8c01215230e14b944dCAB64429ae'
Ryan_account  = '0x239Ad576CEdD58d31c34C70872270AaAE124973D'


nonce1 = web3_ganache_connection.eth.get_transaction_count(Alice_account)

transaction_data1 = {
    'nonce':nonce1,
    'to':James_account,
    'value':web3_ganache_connection.to_wei(2, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key1 = '0x97663f51a4e1f46de91524c2736034986ffb0aea753bec25ffbe4f8cf13a4cc1'

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash1))



# -----------------
"Define the print statement and" 
"sleep() function here"
# -----------------
print("wait for few second transaction is in progress")
time.sleep(5)


nonce2 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data2 = {
    'nonce':nonce2,
    'to':Ryan_account,
    'value':web3_ganache_connection.to_wei(4,'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(40,'gwei')
}

private_key2 = '0x2f857857a5fc1865552084a8506241e41f64765974cc82c0acfc4c4f694bdbd1'

singed_transaction2 = web3_ganache_connection.eth.account.sign_transaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash2))

