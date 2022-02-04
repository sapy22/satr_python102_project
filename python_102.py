import datetime

# storage
people_list = []
people_list.append({'name':'ali',"date":datetime.datetime(2000,12,22)})
people_list.append({'name':'saeed',"date":datetime.datetime(2001,1,1)})


# functions
def calculate_age(birthdate):
    today = datetime.datetime.today()
    age = (today.year - birthdate.year) - ((today.month,today.day) < (birthdate.month,birthdate.day)) # if today < birthday then subtract age by 1 year
    return age

def add_new_record(record,list):
    list.append(record)
    return True

def sort_by_date(list):
    return sorted(list,key=lambda r: r['date'])


# main program
while True:
    print('')
    print('########################## welcome to people birthday managment system ####################################')
    print('### type (all) to list all people, (o) to list the oldest and the youngest person, (a) to add a new person, (x) to exit the program ###')
    print('')

    command = input('please input a command: ')
    #
    if command == 'all':
        print('')
        if people_list:
            print('Total People:',len(people_list))
            for person in people_list:
                birthdate = person['date']
                age = calculate_age(birthdate)
                birthday = birthdate.strftime('%A')
                print(f"# {person['name']}, is {age} years old and s/he was born in {birthday}")
        else:
            print('there is no record')
        print('')
    #
    elif command == 'o':
        if len(people_list) > 1:
            slist = sort_by_date(people_list)
            oldest = slist[0]
            youngest = slist[-1]
            print('')
            print(f'The oldest one is {oldest["name"]}')
            print(f'The youngest one is {youngest["name"]}')
        else:
            print('There is no oldest or youngest person')
    #   
    elif command == 'a':
        while True:
            num = input('to add a new person input (1) or (0) to return: ')
            if num == '0':
                break
            elif num == '1':
                date = input('please input the new person birthdate like this (dd-mm-yyyy): ')
                try:
                    date = datetime.datetime.strptime(date,'%d-%m-%Y')
                    name = input('please input the new person name: ')
                    record = {}
                    record['name'] = name
                    record['date'] = date
                    r = add_new_record(record,people_list)
                    if r:
                        print('record added')
                except:
                    print('invalid birthdate')   
    #           
    elif command == 'x':
        exit()