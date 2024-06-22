import threading
from time import sleep

class BankAccount(threading.Thread):

    def __init__(self):
        super().__init__()
        self.balance = 1000

    def deposit(self, amount):
        sleep(1)
        self.balance = self.balance + amount
        print(f'Deposited {amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        sleep(1)
        self.balance = self.balance - amount
        print(f'Withdrew {amount}, new balance is {self.balance}')


lock = threading.Lock()
account = BankAccount()
def deposit_task(account, amount):
    for _ in range(5):
        with lock:
            account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        with lock:
            account.withdraw(amount)



deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
