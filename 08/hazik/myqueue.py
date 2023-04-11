#!/usr/bin/env python3


"""
Ebben a programban egy Sor adatszerkezetet implementálunk két Verem felhasználásával.
Az osztályon belül van két verem, de az osztály maga úgy funkcionál, mint egy sor.
"""


class MyQueue:
    def __init__(self):
        self.v1 = []
        self.v2 = []
    

    def append(self, n):
        self.v1.append(n)
    

    def popleft(self) -> str:
        if not self.v1 and not self.v2:
            return "Queue is empty!"
        elif len(self.v1) == 1:
            return self.v1.pop()
        else:
            if not self.v2:
                while self.v1:
                    self.v2.append(self.v1.pop())
                # these prints are good to visualize the workflow
                print(f"Stack1 after popleft: {self.v1}")
                print(f"Stack2 after popleft: {self.v2}")

                res = f"First element in the queue: {self.v2.pop()}"

                # after getting the result, we refill the first stack with the elements in the correct order
                while self.v2:
                    self.v1.append(self.v2.pop())
                
                return res


    def is_empty(self) -> str:
        return f"Is My Queue empty: {not self.v1 and not self.v2}"
    

    def size(self) -> str:
        return f"Size of My Queue: {len(self.v1)}"  
    

    def __str__(self) -> str:
        return f"My Queue: {self.v1} {self.v2}"


def main():
    # test
    q = MyQueue()
    print(q.is_empty())
    print(q)
    print(q.size())
    q.append(1)
    print(q.is_empty())
    print(q)
    q.append(3)
    q.append(5)
    q.append(9)
    print(q.size())
    print(q)

    print(q.popleft())
    print(q)
    print(q.popleft())
    print(q)
    print(q.popleft())
    print(q)
    print(q.popleft())  # after this, the queue is empty
    print(q)
    print(q.popleft())  
    print(q)


if __name__ == "__main__":
    main()