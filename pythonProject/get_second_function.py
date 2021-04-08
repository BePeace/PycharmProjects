
def get_second_element(mylist):
    if len(mylist) > 1:
        return mylist[1]
    else:
        return 'List length is less than 2'


list1 = [1]
print(get_second_element(list1))