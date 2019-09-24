with open('names.txt', 'r+' ) as file1:
    with open('email.txt','r+') as file2:
        names = file1.readlines()
        for i in range(100):
            names[i]=names[i].lower()            
        for name in names:
            splitted_name = name.split()
            if (len(splitted_name) > 2):
                third_name = splitted_name[0]
                second_name = splitted_name[1]
                first_name = splitted_name[2]
                email=third_name+first_name[0]+second_name[0]+'@rknec.edu'+'\n'
            
            elif (len(splitted_name) == 2):
                third_name = splitted_name[0]
                first_name = splitted_name[1]
                email = third_name+first_name[0]+'@rknec.edu'+'\n'
            file2.write(email)   
        
        
        


