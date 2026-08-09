from rag_pipeline import RAGPipeline


rag = RAGPipeline()


while True:
    user_input = input("Ask: ")
    if user_input.lower() in ["exit", "quit"]:
        break


    print("\n--- RESPONSE ---")
    print(rag.query(user_input))
    print("---------------\n")


    import random
import time

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited ${amount}")
        print(f"${amount} added successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew ${amount}")
            print(f"${amount} withdrawn successfully.")

    def transfer(self, other_account, amount):
        if amount > self.balance:
            print("Transfer failed: insufficient funds.")
        else:
            self.balance -= amount
            other_account.balance += amount
            self.history.append(
                f"Transferred ${amount} to {other_account.owner}"
            )
            other_account.history.append(
                f"Received ${amount} from {self.owner}"
            )
            print("Transfer completed successfully.")

    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")

    def show_history(self):
        print(f"\nTransaction History for {self.owner}:")
        for item in self.history:
            print("-", item)


def generate_random_transactions(account, count):
    for _ in range(count):
        action = random.choice(["deposit", "withdraw"])
        amount = random.randint(10, 500)

        if action == "deposit":
            account.deposit(amount)
        else:
            account.withdraw(amount)

        time.sleep(0.1)


def main():
    alice = BankAccount("Alice", 1000)
    bob = BankAccount("Bob", 500)

    alice.show_balance()
    bob.show_balance()

    print("\nGenerating random transactions for Alice...\n")
    generate_random_transactions(alice, 5)

    print("\nManual operations:\n")
    alice.deposit(300)
    alice.withdraw(150)
    alice.transfer(bob, 200)

    print("\nFinal balances:")
    alice.show_balance()
    bob.show_balance()

    alice.show_history()
    bob.show_history()


if __name__ == "__main__":
    main()