class BankAccount:
    """
    A simple BankAccount class demonstrating OOP principles.
    """

    def __init__(self, initial_balance=0):
        """Initialize account with optional starting balance (default = 0)."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the given amount if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")
