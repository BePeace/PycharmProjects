
def list_product(mylist):
    product = 1
    if len(mylist) > 1:
        for number in mylist:
            product = product * number

    return product

if __name__ == '__main__':
    print(list_product([1,2,3]))
    print(list_product([1,5,3]))

