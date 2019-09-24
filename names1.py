with open('names.txt', 'r+' ) as file1:
    with open('email.txt','r+') as file2:
        names = file1.readlines()
        a=[]
        for i in range(0, 100):
            names[i] = names[i].lower()
            a =  names[i].split(' ')
            if(len(a) > 2):
                last_name = a[0]
                second_name = a[1]
                first_name = a[2]
                email=last_name+first_name[0]+second_name[0]+'@rknec.edu'+'\n'
            elif(len(a) == 2):
                last_name = a[0]
                first_name = a[1]
                email=last_name+first_name[0]+'@rknec.edu'+'\n'
            file2.write(email)






            
            

