def main():
    # choosing option to do crud operations
    selection = raw_input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')
        
    if selection == '1':
        insert()
    elif selection == '2':
        update()
    elif selection == '3':
        read()
    elif selection == '4':
        delete()
    else:
        print '\n INVALID SELECTION \n'

def insert():
    print ('You chose insert')

def update():
    print ('You chose update')

def read():
    print ('You chose read')

def delete():
    print ('You chose delete')

