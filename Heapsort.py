def MaxHeap(arr):
    ind = len(arr)//2 - 1
    for i in range(ind,-1,-1):
        MaxHeapify(arr,i,len(arr))
        
def MinHeap(arr):
    ind = len(arr)//2 - 1
    for i in range(ind,-1,-1):
        MinHeapify(arr,i,len(arr))
        
def MaxHeapify(arr,i,size):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < size and arr[l] > arr[largest]:
        largest = l
    if r < size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[largest],arr[i]=arr[i],arr[largest]
        MaxHeapify(arr,largest,size)
        
def MinHeapify(arr,i,size):
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = i
    if l < size and arr[l] < arr[smallest]:
        smallest = l
    if r < size and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        arr[smallest],arr[i]=arr[i],arr[smallest]
        MinHeapify(arr,smallest,size)
        
def Heapsort(arr):
   MaxHeap(arr)
   l = len(arr)
   for i in range(l-1,0,-1):
       arr[i],arr[0] = arr[0],arr[i]
       MaxHeapify(arr,0,i)
       
def MinHeapsort(arr):
   MinHeap(arr)
   l = len(arr)
   for i in range(l-1,0,-1):
       arr[i],arr[0] = arr[0],arr[i]
       MinHeapify(arr,0,i)
       
    


arr = [90,85,30,60,86,100,40,54,69,35,95,80,45]
#MaxHeap(arr)
#print(arr)
Heapsort(arr)
print(arr)
MinHeap(arr)
print(arr)
MinHeapsort(arr)
print(arr)
