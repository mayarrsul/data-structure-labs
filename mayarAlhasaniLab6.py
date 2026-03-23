print ('mayar')



def main():
    
    pal('Race car')
    pal('madam')
    pal('hello')
    

def pal(m):
    mer = ArrayDeque()
    for _ in m.replace(" ","").lower() :
        mer.add_rear(_)
    
    
    # for _ in mer.reprr() :
    #     if mer._n == 1 :
    #         break
    #     elif mer.remove_front() != mer.remove_rear():
    #         o=  False 
    #         break     
    # print(f'does {m} a palindrome? ',o)
    
    o=True
    while mer._n >1:
        if mer.remove_front() != mer.remove_rear():
            o=  False 
            break
    print(f'does {m} a palindrome? ',o)



class ArrayDeque:

    def __init__(self, capacity: int = 8):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._data = [None] * capacity
        self._f = 0 
        self._n = 0 

    def capacity(self) -> int:
        return len(self._data)
    def is_empty(self) -> bool:
        return self._n == 0
    def is_full(self) -> bool:
        return self._n == self.capacity()
    def size(self) -> int:
        return self._n
    def peek_front(self):

        if self.is_empty():
            raise IndexError("Deque is empty: nothing at front")
        return self._data[self._f]
    def peek_rear(self):

        if self.is_empty():
            raise IndexError("Deque is empty: nothing at rear")
        rear_index = (self._f + self._n - 1) % self.capacity()
        return self._data[rear_index]
    def add_front(self, value):

        if self.is_full():
            self.grow()
        self._f = (self._f - 1) % self.capacity()
        self._data[self._f] = value
        self._n += 1
    def add_rear(self, value):

        if self.is_full():
            self.grow()
        rear_index = (self._f + self._n) % self.capacity()
        self._data[rear_index] = value
        self._n += 1

    def remove_front(self):

        if self.is_empty():
            raise IndexError("Deque underflow: empty at front")
        value = self._data[self._f]
        self._data[self._f] = None
        self._f = (self._f + 1) % self.capacity()
        self._n -= 1
        return value
    
    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque underflow: empty at rear")
        rear_index = (self._f + self._n - 1) % self.capacity()
        value = self._data[rear_index]
        self._data[rear_index] = None
        self._n -= 1
        return value

    def grow(self):

        old_data = self._data
        old_cap = self.capacity()
        new_cap = 2 * old_cap
        new_data = [None] * new_cap

        for i in range(self._n):
            idx = (self._f + i) % old_cap
            new_data[i] = old_data[idx]
        self._data = new_data
        self._f = 0

    def __repr__(self):
        items = []
        for i in range(self._n):
            idx = (self._f + i) % self.capacity()
            items.append(self._data[idx])
        return f"Deque(front->{items}, cap={self.capacity()})"
    def reprr(self):
        items = []
        for i in range(self._n):
            idx = (self._f + i) % self.capacity()
            items.append(self._data[idx])
        return items


main()


