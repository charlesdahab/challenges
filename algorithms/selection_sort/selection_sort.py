def selection_sort(slist):

   for i in range(len(slist)):

      # Find the minimum element in remaining
       min_position = i

       for j in range(i+1, len(slist)):
           if slist[min_position] > slist[j]:
               min_position = j

       # Swap the found minimum element with minPosition
       temp = slist[i]
       slist[i] = slist[min_position]
       slist[min_position] = temp

   return slist

print(selectionSort([5,2,1,9,0,4,6]))
