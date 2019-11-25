#!/usr/bin/python3

def binary_search(item_list,item):
    """
    Binary Search Algorithm

    Args:
        item_list (list): Array of Elements.
        item (int): Element that needs to be found.

    Returns:
        bool: True for success, False otherwise.
    """
    try:
        first = 0
    	last = len(item_list)-1
    	found = False
    	while( first<=last and not found):
    		mid = (first + last)//2
    		if item_list[mid] == item :
    			found = True
    		else:
    			if item < item_list[mid]:
    				last = mid - 1
    			else:
    				first = mid + 1
    	return found
    except Exception as exception:
        print(f'Something went Wrong. Messsage: {exception}')

if __name__ == "__main__":
    list = [1,2,3,5,8]
    element = 5
    if binary_search(list, element):
        print('Element Found.')
    else:
        print('Element Not Found.')
