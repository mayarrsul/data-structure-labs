print('mayar')


'''
mayar alhasani 
group 5 
id 446002675 

'''

# h = HashTableChaining(4)
# hh = LinearProbingHashTable()
   
def chaingin():
    print('chaining')
    #h = HashTableChaining(4)

    print ('insert 5336666 -> sara')
    h.put("5336666", "Sara" )
    print('insert 1234567 -> ali')
    h.put("1234567","Ali" )
    print('insert 8761234 -> reem')
    h.put("8761234","Reem")

    print('search 5336666 ', h.get("5336666")) 
    print(' remove 5336666 ', h.remove('5336666'))
    print('contain 5336666 ', h.contains("5336666")) 

    print(h.bucket_lengths())

def linear():
    print ('linear')
    #h = LinearProbingHashTable()
    
    print ('insert 5336666 -> sara')
    hh.put("5336666", "Sara" )
    print('insert 1234567 -> ali')
    hh.put("1234567","Ali" )
    print('insert 8761234 -> reem')
    hh.put("8761234","Reem")

    print('search 5336666 ', hh.get("5336666")) 
    print(' remove 5336666 ', hh.remove('5336666'))
    print('contain 5336666 ', hh.get("5336666")) 

    print(hh.avg())

def meer ():
    #h = HashTableChaining(8)
    #hh = LinearProbingHashTable(8)
    extra = {"5551021": "mayar","5551712": "lamar", "5951013": "anoud", "5551013": "wasan","5551005": "reem",
            "5551001": "Sara", "5551002": "Ali", "5551003": "Reem","5551004": "Mona", "5551005": "John",
            "5551006": "Lina","5551007": "Omar",  "5551008": "Tariq","5551009": "Nora", "5551010": "Hassan",
             "5551011": "Yara","5551012": "Samir", "5551013": "Rana", "5551014": "Khalid","5551015": "Fatima"}

    for phone, name in extra.items():
        h.put(phone, name)
    for phone, name in extra.items():
        hh.put(phone, name)

    h.get("5551002")
    h.remove('5551002')
    hh.get("5551002")
    hh.remove('5551011')

    print('\nafter extra inserts ')
    print(h.bucket_lengths())
    print(hh.avg())



class HashTableChaining:

    MAX_LOAD = 0.75 

    def __init__(self, capacity=8):

        if capacity < 2:
            capacity = 2 
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0 

    def _index(self, key):

        return hash(key) % len(self._buckets)
    
    def _resize(self, new_capacity):
        old_pairs = [pair for bucket in self._buckets for pair in bucket]
        self._buckets = [[] for _ in range(new_capacity)]
        self._size = 0
        for k, v in old_pairs:
            self.put(k, v) 

    def put(self, key, value):

        idx = self._index(key)
        bucket = self._buckets[idx] 
        for i, (k, _) in enumerate(bucket): 
            if k == key:
                bucket[i] = (key, value) 
                return
        bucket.append((key, value)) 
        self._size += 1

        if self.load_factor() > self.MAX_LOAD:
            self._resize(len(self._buckets) * 2)
        

    def get(self, key, default=None):

        idx = self._index(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        return default
    def remove(self, key):

        idx = self._index(key)
        bucket = self._buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return v
        raise KeyError(key)
    def contains(self, key):

        sentinel = object()
        return self.get(key, sentinel) is not sentinel
    def __len__(self):
        return self._size
    def load_factor(self):
        
        return self._size / len(self._buckets)
    
    def bucket_lengths(self):
        i=[len(bucket) for bucket in self._buckets]
        max_len=max(i)
        ave = sum(i)/len(i)

        return f'bucket lengths {i} the max {max_len} the ave {ave}'

        #return [len(bucket) for bucket in self._buckets]
    
    def __repr__(self):

        return f"HashTableChaining(size={self._size},capacity={len(self._buckets)},buckets={self._buckets})"



#------- open addressing ------------

_TOMBSTONE = object()

class LinearProbingHashTable:
    

    MAX_LOAD = 0.5 
    def __init__(self, capacity=11):

        
        self._keys = [None] * capacity 
        self._vals = [None] * capacity
        self._size = 0 
        self._tombs = 0 

        self.puts = 0
        self.gets = 0
        self.removes = 0
        self.put_steps = 0
        self.get_steps = 0
        self.remove_steps = 0

    def avg(self):
        if self.puts ==0 or self.gets ==0 or self.removes ==0:
            raise ValueError("Cannot compute averages: one of the counters is zero")
        aveput= self.put_steps /  self.puts
        aveget= self.get_steps / self.gets
        averemove = self.remove_steps /  self.removes
        return f'the ave put {aveput} the ave get {aveget} the ave remove { averemove}'

    def _index(self, key):

        return hash(key) % len(self._keys)
    
    def _probe(self, key, type):

        n = len(self._keys)
        i = self._index(key) 
        first_tomb = None 
        while True:
            if type == 'remove' :
                self.remove_steps+=1
            elif type == 'get' :
                self.get_steps +=1
            elif type == 'put' :
                self.put_steps +=1

            k = self._keys[i]
            if k is None:

                return (first_tomb if first_tomb is not None else i), False
            if k is _TOMBSTONE:

                if first_tomb is None:
                    first_tomb = i
            elif k == key:
                return i, True

            i = (i + 1) % n
    def _resize(self, new_capacity):

        old_k, old_v = self._keys, self._vals
        self._keys = [None] * new_capacity
        self._vals = [None] * new_capacity
        self._size = 0
        self._tombs = 0
        for k, v in zip(old_k, old_v):
            if k is not None and k is not _TOMBSTONE:
                self.put(k, v)

    def put(self, key, value):
        self.puts += 1
        slot, found = self._probe(key,'put')
        if found:
            self._vals[slot] = value
            return

        if self._keys[slot] is _TOMBSTONE:
            self._tombs -= 1
        self._keys[slot] = key
        self._vals[slot] = value
        self._size += 1

        if (self._size + self._tombs) / len(self._keys) > self.MAX_LOAD:

            self._resize(len(self._keys) * 2 + 1)

    def get(self, key, default=None):
        self.gets += 1

        slot, found = self._probe(key,'get')
        return self._vals[slot] if found else default
    def remove(self, key):
        self.removes += 1

        slot, found = self._probe(key,'remove')
        if not found:
            raise KeyError(key)
        self._keys[slot] = _TOMBSTONE
        self._vals[slot] = None
        self._size -= 1
        self._tombs += 1
    def __len__(self):
        return self._size
    def __repr__(self):
        return f"LinearProbingHashTable(n={len(self._keys)}, size={self._size},tombs={self._tombs}, keys={self._keys}, vals={self._vals})"
    
h = HashTableChaining(4)
hh = LinearProbingHashTable()
chaingin()
linear()
meer()



