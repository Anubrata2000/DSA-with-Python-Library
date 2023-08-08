# Quick sort in Python
def partition(list, low, high):
  piv = low
  lt = low + 1
  rt = high
  while(True):
    while  lt <= rt and list[piv] <= list[rt] :
        rt = rt - 1
    if list[piv] > list[rt]:
        temp=list[piv]
        list[piv]=list[rt]
        list[rt]=temp
        piv = rt
        rt = rt -1
    if  lt > rt:
        return piv
    while lt <= rt and list[piv] >= list[lt]:
        lt = lt+1
    if list[piv]<list[lt]:
        temp=list[piv]
        list[piv]=list[lt]
        list[lt]=temp
        piv = lt
        lt = lt +1
    if  lt > rt:
        return piv

def quickSort(list, low, high):
  if low <= high:
    piv = partition(list, low, high)
    quickSort(list, low, piv - 1)
    quickSort(list, piv + 1, high)
 

li = [8, 7, 2, 1, 0, 9, 6, 67, 47456, 345, 3444,43534, 34554]
print("Unsorted List")
print(li)

size = len(li)

quickSort(li, 0, size - 1)

print('Sorted List in Ascending Order:')
print(li)


'''
class QuickSort:
    def sort(self, arr):
        self._quicksort(arr, 0, len(arr)-1)

    def _quicksort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)

            self._quicksort(arr, low, pi-1)
            self._quicksort(arr, pi+1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
'''