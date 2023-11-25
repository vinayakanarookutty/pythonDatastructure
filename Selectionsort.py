def selectionSort(array):
    for i in range(len(array)):
        minPosition=i
        for j in range(i,len(array)):
            if array[j]<array[minPosition]:
                minPosition=j
                
        temp=array[minPosition]
        array[minPosition]=array[i]
        array[i]=temp   


arrays=[12,5,9,3,6,4]    
selectionSort(arrays)
print(arrays)