contact_list = []
keys = []
def csv_to_dict(file_path):
    '''
    returns csv as list of dictionaries
    '''
    global contact_list, keys
    with open(file_path) as f:
        rows = f.read().split('\n')
    
    list_of_dicts = []
    keys = rows[0].split(',')

    for row in rows:
        row = row.split(',')
        if row == keys:
            continue
        row_dict = dict(zip(keys, row))
        list_of_dicts.append(row_dict)
        contact_list = list_of_dicts
        

def save_dict_to_csv(source, destination_path):
    '''writes source list of dictionaries to csv at destination path'''
    pass

def find_contact_index(name):
    '''name: dict'''
    global contact_list, keys
    index = None 
    for i in range(len(contact_list)):
        contact = contact_list[i]
        if name == contact['name']:
            index = i
            break
    return index


def create_contact(contact, name):
    global contact_list, keys
    contact_list.append(contact)


def retrieve_contact(name):
    global contact_list, keys
    index = find_contact_index(name)
    if index is not None:
        return contact_list[index]
    return 'contact does not exist'


def update_contact(name, updated_data):
    global contact_list, keys
    index = find_contact_index(name)
    if index is not None:
        contact = contact_list[index]
        contact.update(updated_data)
    else:
        return 'contact does not exist'
    
# def print_all(contact_list):
#     global contact_list
#     for contact in contact_list:
#         print(contact)

def delete_contact(name):
    global contact_list, keys
    index = find_contact_index(name)
    if index is not None:
        contact = contact_list.pop(index)
        return f"removed {contact['name']}"
    return 'contact does not exist'

def repl():
    global contact_list, keys
    valid_inputs = ['c', 'create', 'r', 'read',
                    'd', 'delete', 'x', 'quit', 'exit', 'u', 'update']
    while True:
        print('Welcome to the contact list.')
        
        while True:
            user_in = input(' Enter (c)create, (r)ead, (u)pdate, (d)elete to update, (x) to quit: ').lower().strip()
            if user_in in valid_inputs:
                break

        if user_in.startswith('r') or user_in.startswith('u') or user_in.startswith('d'):
            name = input('Enter the contacts name: ')
        
        if user_in.startswith('c'):
            contact = {}
            for key in keys:
                val = input(f"{key}: ")
                contact[key] = val
            
            
        elif user_in.startswith('r'):
            contact = retrieve_contact(name)
            print(contact)

        elif user_in.startswith('u'):
            contact = {}
            for key in keys:
                val = input(f"{key}: ")
                if val:
                    contact[key] = val
            updated_contact = update_contact(name, contact)
            print(updated_contact)
                    
            print(contact)
            
        
        elif user_in.startswith('d'):
            contact = delete_contact(name)
            print(contact)

        elif user_in in ['x', 'exit', 'quit', 'e','q']:
            break
        
def main():        
    
    csv_to_dict('contacts.csv')
    print(keys)
    repl()
main()
    # print(find_contact_index('Alex'))
    # print(retrieve_contact('Charlie'))
    # contact = {'name': 'Ashley',
    #            'favoritefruit': 'avo', 'favoritecolor': 'red'}
    # create_contact(contact)
    # update_contact('Charlie',{'favoritefruit':'apple'})
    # for item in contact_list:
    #     print(item)
