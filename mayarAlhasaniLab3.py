import random , time
print('start point')




def main():

    
    data = praperdate()
    equal = True
    if bubble_sort(data) != sorted(data):
        equal = False

    
    timeBubble , timeSorted = timeSort(data)
    print(f"Bubble sort time: {timeBubble} s")
    print(f"sorted() time: {timeSorted} s")
    print(f"Results equal: {equal} ")

def praperdate(n = 10000, valueRange = None , seed = 42):
  
    random.seed(seed)
    if valueRange == None :
        valueRange = n**2

    data = [random.randint(0, valueRange) for _ in range (n)]
    return data 


def bubble_sort(arr):
    ar = arr[:]
    si = len(ar)
    for i in range(si) :
        for j in range(0,si-i - 1):
            if ar[j] > ar[j+1]:
                ar[j],ar[j+1] = ar[j+1],ar[j]

    return ar 

    

def timeSort(ar):
    t = time.time()
    bubble_sort(ar)
    t = time.time() -t

    tt = time.time()
    sorted(ar)
    tt = time.time() -tt

    return t ,tt 



main()





















