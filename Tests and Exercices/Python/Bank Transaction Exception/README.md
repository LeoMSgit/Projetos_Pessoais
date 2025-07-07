Create an advanced Python program to simulate banking transactions with various features, including transaction history, advanced security measures, and error handling. Implement two classes.
Transaction Class
__init__(self, transaction_type, amount, balance): Initializes a new transaction object.

__str__(self):  Returns a string representation of the transaction in the format "Type: {self.transaction_type}, Amount: {self.amount}, Balance: {self.balance}


BankAccount Class
__init__(self, initial_balance): Initializes a bank account with the specified initial balance.

process_transaction(self, transaction_amount, transaction_type): Processes a transaction and updates the account balance based on transaction type.

Initial Conditions: The account balance starts at 1500.0.



Transaction Types

deposit:
Adds the transaction amount to the balance if the input is valid.
Updates the transaction history.
Return messages:
		"Transaction successful!"
         "Updated account balance: {self.balance}"


withdraw:
Deducts the transaction amount from the balance, updating the transaction history if sufficient funds are available.
If funds are insufficient, raises an InsufficientFundsError
Return messages:
		"Transaction successful!"
        "Updated account balance: {self.balance}"

view_transaction_history:
Displays transaction history, with each transaction shown in the format: "Type: {self.transaction_type}, Amount: {self.amount}, Balance: {self.balance}"


Custom Exceptions
InsufficientFundsError:Raised when a withdrawal exceeds available funds.
Message: "Not enough funds to withdraw {transaction_amount}. Current balance: {balance}"
status_code: 400

InvalidTransactionType:Raised if an invalid transaction type is provided.
Message: "Invalid transaction type '{transaction_type}'. Accepted types: deposit, withdraw, view_transaction_history"
status_code: 400
