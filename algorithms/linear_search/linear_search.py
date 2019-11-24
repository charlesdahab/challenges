# Search function with parameter list name 
# and the value to be searched 
def linear_search(list_elements, element):
    """
    Linear Search Algorithm
    Returns the position of a specific element in a list.

    Args:
        list_elements (list): Array of Elements.
        element (int): Element that needs to be found.

    Returns:
        bool: True for success, False otherwise.
    """
    try:
        for i in range(len(list_elements)):
            if list_elements[i] == element:
                return True
        return False
    except Exception as exception:
        print(f'Something went Wrong. Messsage: {exception}')

if __name__ == "__main__":
    list = [1,2,3,4,5,6,7,8,9]
    element = 4
    if linear_search(list, element):
        print('Element Found.')
    else:
        print('Element Not Found.')