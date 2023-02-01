#############################################################################
#  Module name               : Teacher.py                                   #
#  Standard Imports          : pickle                                       #
#  Function - add()          : Adds new teacher record                      #
#  Function - delete()       : Deletes existing teacher record              #
#  Function - modify()       : Modifies existing teacher record             #
#  Function - display()      : Displays all teacher records                 #
#  Coded By                  : Ms. Sana Sampson                             #
#############################################################################

#Creates portable serialized representations of Python objects
#using pickle.load() and pickle.dump()
import pickle

def add():
    '''
Takes inputs from user and then adds a new teacher record to the table
    '''

    try:
        print('\n----------INSERTING A NEW TEACHER-----------\n')
    
        fh = open('teacher.dat','rb')
        res = pickle.load(fh)
       
        fh.close()
        
        ans = 'y'
        while ans == 'y' or ans == 'Y':
            
            a = 'y'
            while a == 'y':
                tid = int(input('Enter ID(max 7 digits): '))
                while len(str(tid)) > 7 or tid < 1:
                    print('Error! Please enter valid ID!\n')
                    tid = int(input('Enter ID(max 7 digits): '))
                L = []
                for r in res:
                    L.append(r[0])
                if tid in L:
                    print('Error! Duplicate value for ID!\n')
                    a = 'y'
                else:
                    a = 'n'
                
                
            tname = input('Enter name (Max 7 characters): ')
            tname = tname[:7]

            tsal = int(input('Enter salary: '))
            while len(str(tsal)) > 6:
                print('Error! Enter max 6 digit no.\n')
                tsal = int(input('Enter salary: '))
            while tsal < 10000:
                print('Error! Enter a valid salary\n')
                tsal = int(input('Enter salary: '))

            td = input('Enter degree (TGT/PGT/PRT): ')
            deg = ['TGT','PGT','PRT']
            while td not in deg:
                print('Error! Please enter a valid DEGREE!\n')
                td = input('Enter degree (TGT/PGT/PRT): ')
                
            subjects = ['Maths','Computer Science','Chemistry','Physics','English','PE','Biology','Art']
            tsub = input('Enter subject among {}: '.format(subjects))
            while tsub not in subjects:
                print('Pls enter a valid subject!')
                tsub = input('\nEnter subject among{}:'.format(subjects))

            new_t = [tid, tname, tsub, td, tsal]
            new_tid = new_t[0] 


            if len(L) == 0:
                res.append(new_t)
                fh = open('teacher.dat','wb')     
                ans = input('\nWould you like to continue adding more teachers? (y/n): ') 
                pickle.dump(res,fh)
                fh.flush()
                fh.close()

            else:
                for i in range(len(res)):
                    if res[i][0] >= new_tid:
                        res.insert(i,new_t)
                        print('\nData inserted!--------------\n')
                        break
                    else:
                        res.append(new_t)
                        print('\nData Appended!--------------\n')
                        break
                fh = open('teacher.dat','wb')     
                ans = input('\nWould you like to continue adding more teachers? (y/n): ')
                res.sort()
                pickle.dump(res,fh)
                fh.flush()
                fh.close()


        
        print('\nData written to file\n')   
        #fh.flush()
        fh.close()

    except EOFError as e01:
        print('EOF Error:',e01)
        print('Closing file!!')
        fh.close()

#---------------------------------------------------------------------------------------------------------------------------------------------------
        
def display():
    '''
Displays the teacher table, with its records
    '''

    try:
        print('\n----------DISPLAYING TEACHERS-----------\n')
        fh = open('teacher.dat','rb')
        res = pickle.load(fh)

        res.sort()
        data = res

        #Table Header
        print('==============================================================================')
        hdr = ['ID', 'Name', 'Subject', 'Degree', 'Salary']
        for title in hdr:
            if title == 'Subject':
                print(title + '\t' + ' ', end = '\t')
            else:
                print(title + '\t',end = '\t')
        print()
        print('==============================================================================')

        #Table Records
        for i in data:
            for it in i:
                if it == 'Computer Science':
                    print('CS' + '\t',end = '\t')
                elif it == 'Chemistry':
                    print('Chem' + '\t',end = '\t')
                else:
                    print(str(it) + '\t',end = '\t')
            print()
            print('______________________________________________________________________________')

        
        fh.close()

    except EOFError as e02:
        print('EOF Error:',e02)
        print('Closing file!!')
        fh.close()

#---------------------------------------------------------------------------------------------------------------------------------------------------

def modify():
    '''
Modifies existing record using Teacher ID
    '''

    try:
        print('\n----------MODIFYING EXISTING TEACHER-----------\n')
        fh = open('teacher.dat','rb')
        res = pickle.load(fh)

        tid_check = []
        for r in res:
            tid_check.append(r[0])
            
       
        if len(tid_check) == 0:
            print('Underflow error! No entry to modify.')
        else:
            tid = int(input('Enter ID to be modified: '))
            while tid not in tid_check:
                print('Please enter valid ID for modification!\n')
                tid = int(input('Enter ID to be modified: '))

            print(f'\n================ Modifying ID {tid} =================\n')
            tname = input('Insert new name: ')
            tname = tname[0:7]
            
            td = input('Enter degree (TGT/PGT/PRT): ')
            deg = ['TGT','PGT','PRT']
            while td not in deg:
                print('Error! Please enter a valid DEGREE!\n')
                td = input('Enter degree (TGT/PGT/PRT): ')
            
            tsal = int(input('Enter new salary: '))
            while len(str(tsal)) > 6:
                print('Error! Enter MAX 6 digit no.\n')
                tsal = int(input('Enter salary: '))
            while tsal < 10000:
                print('Error! Enter a valid salary\n')
                tsal = int(input('Enter salary: '))

                    
            subjects = ['Maths','Computer Science','Chemistry','Physics','English','PE','Biology','Art']
            tsub = input('Enter subject among {}: '.format(subjects))
            while tsub not in subjects:
                print('Pls enter a valid subject!')
                tsub = input('\nEnter subject {}:'.format(subjects))
            print('\n=======================================================\n')

            new_t = [tid, tname, tsub, td, tsal]
            
            for r in res:
                if r[0] == tid:
                    res.remove(r)

            if len(res) == 0:
                res.append(new_t)
                
            else:
                for i in range(len(res)):
                    if res[i][0] >= tid:
                        pos = i
                        res.insert(i,new_t)
                        print(f'\nID - {tid} : {tname}\'s data has been successfully updated!')
                        break
                    else:
                        res.append(new_t)
                        print('Data Appended!')
                        break

            fh = open('teacher.dat','wb')
            res.sort()
            pickle.dump(res,fh)
            print('\nData written to file\n')
            fh.flush()
            fh.close()

    except EOFError as e03:
        print('EOF Error:',e03)
        print('Closing file!!')
        fh.close()

#---------------------------------------------------------------------------------------------------------------------------------------------------

def delete():
    '''
Deletes the record based on Teacher ID. 
    '''

    try:
        print('\n----------DELETING TEACHER-----------\n')

        fh = open('teacher.dat','rb')
        res = pickle.load(fh)
        fh.close()

        if len(res) == 0:
                print(f'Underflow error! No entry in database.')

        else:
            TId = int(input('Enter ID to be deleted: '))

            tid_deleted = 0        
            for r in res:
                if r[0] == TId:
                    res.remove(r)
                    tid_deleted = 1
                    print('\nTeacher successfully deleted!\n')
        
            if tid_deleted == 0:
                print(f'Error! Did not find entry with ID {TId}.')
            
        
        fh = open('teacher.dat','wb')
        pickle.dump(res,fh)
        fh.flush()
        fh.close()

    except EOFError as e04:
        print('EOF Error:',e04)
        print('Closing file!!')
        fh.close()

