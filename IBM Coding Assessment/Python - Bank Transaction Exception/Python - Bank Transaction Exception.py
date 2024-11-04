class InsufficientFundsError(Exception):
    """Custom exception raised when a withdrawal exceeds the available balance."""
    def __init__(self, transaction_amount, balance):
        self.message = f"Not enough funds to withdraw {transaction_amount}. Current balance: {balance}"
        self.status_code = 400
        super().__init__(self.message)


class InvalidTransactionType(Exception):
    """Custom exception raised when an invalid transaction type is provided."""
    def __init__(self, transaction_type):
        self.message = f"Invalid transaction type '{transaction_type}'. Accepted types: deposit, withdraw, view_transaction_history"
        self.status_code = 400
        super().__init__(self.message)


class Transaction:
    def __init__(self, transaction_type, amount, balance):
        """
        Initializes a new transaction object.
        
        Parameters:
        - transaction_type (str): Type of the transaction, e.g., "deposit" or "withdraw".
        - amount (float): The transaction amount.
        - balance (float): The balance after the transaction.
        """
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance

    def __str__(self):
        """Returns a string representation of the transaction."""
        return f"Type: {self.transaction_type}, Amount: {self.amount}, Balance: {self.balance}"


class BankAccount:
    def __init__(self, initial_balance=1500.0):
        """
        Initializes a bank account with the specified initial balance.
        
        Parameters:
        - initial_balance (float): The starting balance for the account.
        """
        self.balance = initial_balance
        self.transaction_history = []

    def process_transaction(self, transaction_amount, transaction_type):
        """
        Processes a transaction and updates the account balance based on transaction type.
        
        Parameters:
        - transaction_amount (float): The amount for the transaction.
        - transaction_type (str): Type of the transaction, e.g., "deposit" or "withdraw".
        
        Returns:
        - str: Success message or raises an error for insufficient funds or invalid transaction types.
        """
        if transaction_type == "deposit":
            # Deposit transaction
            if transaction_amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            
            self.balance += transaction_amount
            transaction = Transaction(transaction_type, transaction_amount, self.balance)
            self.transaction_history.append(transaction)
            return f"Transaction successful!\nUpdated account balance: {self.balance}"

        elif transaction_type == "withdraw":
            # Withdraw transaction
            if transaction_amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            
            if self.balance >= transaction_amount:
                self.balance -= transaction_amount
                transaction = Transaction(transaction_type, transaction_amount, self.balance)
                self.transaction_history.append(transaction)
                return f"Transaction successful!\nUpdated account balance: {self.balance}"
            else:
                raise InsufficientFundsError(transaction_amount, self.balance)

        else:
            raise InvalidTransactionType(transaction_type)

    def view_transaction_history(self):
        """
        Displays the transaction history in a formatted output.
        
        Returns:
        - str: Formatted transaction history.
        """
        if not self.transaction_history:
            return "No transactions have been made."
        
        history_str = "Transaction History:\n"
        history_str += "\n".join(str(transaction) for transaction in self.transaction_history)
        return history_str
