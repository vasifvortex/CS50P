class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or capacity ==0:
            raise ValueError("Insert positive Integer")
        self.capacity=capacity
        self.size=0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n + self.size <= self.capacity:
            self.size=self.size+n
        else:
            raise ValueError("Too much!")


    def withdraw(self, n):
        if n <= self.size:
            self.size=self.size-n
        else:
            raise ValueError("Too much!")

    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self,capacity):
        self._capacity=capacity

    @size.setter
    def size(self,size):
        self._size=size

def main():
    capacity = int(input("Capacity: "))
    deposit = int(input("Deposit: "))
    withdraw = int(input("Withdraw: "))
    jar=Jar(capacity)
    jar.deposit(deposit)
    jar.withdraw(withdraw)
    print(jar.capacity)
    print(jar.size)


if __name__=="__main__":
    main()
