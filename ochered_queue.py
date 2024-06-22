import threading
from threading import Thread
import queue
import time
class Table:
    def __init__(self, number:int):
        self.number = number
        self.is_busy = False

class Cafe:

    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()
        self.cust_th_list = []

    def customer_arrival(self):
        for i in range(1, 21):
            print(f'Посетитель номер {i} прибыл.')
            self.serve_customer(i)
            time.sleep(1)


    def serve_customer(self, customer):
        free_table = False
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель номер {customer} сел за стол {table.number}')
                cust_th = Customer(customer, self, self.queue, table)
                cust_th.start()
                self.cust_th_list.append(cust_th)
                free_table = True
                return
        if not free_table:
            print(f'Посетитель номер {customer} ожидает свободный стол.')
            self.queue.put(customer)

class Customer(Thread):
    def __init__(self, number, cafe, queue, table):
        super().__init__()
        self.cafe = cafe
        self.number = number
        self.table = table
        self.queue = queue

    def run(self):
        time.sleep(5)
        print(f'Посетитель номер {self.number} покушал и ушёл.')
        self.table.is_busy = False
        if not self.queue.empty():
            next_custom = self.queue.get()
            self.cafe.serve_customer(next_custom)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
print(tables)
cafe = Cafe(tables)

th = Thread(target=cafe.customer_arrival)
th.start()
th.join()

for i in cafe.cust_th_list:
    i.join()

print(threading.enumerate())
