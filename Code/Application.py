################################################################################################
#  Module name             : Application.py                                                    #
#  Standard Imports        : time, os, datetime,winsound, mysql.connector,                     #
#  My imports              : schoolBell, incrtime, Teacher                                     #
#  Function of this Module : Main module to  -                                                 #
#                            1. Run the School Bell program                                    #
#                            2. Teacher Database Management                                    #
#  Coded By                : Sana Sampson                                                      #
################################################################################################

# ---- time : system time
#sleep(seconds) : Delays execution for a given number of seconds. 
import time

#Programs that import and use 'os' stand a better chance of being
#portable between different platforms. 
import os

# ---- time : datetime
#datetime.now() : Returns current date and time
from datetime import datetime

#Establishes connection between MySQL database and Python Interpreter to access table
import mysql.connector as msc

# ---- schoolBell
#Takes input as (Hour,Minute) in 24 hour format and plays a bell sound file as per system time
from Bell import schoolBell

# ---- incrtime
#Creates Hour list and Minute list of time for classes
from timeConvert import incrtime

#Functions to manage Teacher Database
import Teacher as teacher

## -----------------------------PROGRAM STARTS -------------------------------------------------------

try:
    print('\n\n\n******************************   MAIN MENU   *************************************\n')
    print('1 → SCHOOL BELL')
    print('2 → TEACHER DATABASE')
    print('3 → EXIT PROGRAM')
    print('------------------------------------------------------------------------------------')
    ch = int(input('Enter your choice : '))
    print('------------------------------------------------------------------------------------')
    while ch not in [1,2,3]:
        print('Error - Invalid Entry. Please enter again...')
        print('------------------------------------------------------------------------------------')
        ch = int(input('Enter your choice : '))
        print('------------------------------------------------------------------------------------')

    while ch in [1,2,3]:
        if ch == 1:
            try:
                print('\n\n\n******************************   SCHOOL BELL   *************************************\n')
                print('================ Entry of Timetable for Bell to ring ================\n')
                NO_OF_PERIODS = int(input('Enter no. of classes per day: '))
                while NO_OF_PERIODS > 9 or NO_OF_PERIODS < 2:
                    print('Invalid Entry! Please enter again (range 2-9)!\n')
                    NO_OF_PERIODS = int(input('Enter no. of classes per day: '))

                print('\nSubject Codes--->')
                D = {1:'Maths',2:'Chem',3:'English',4:'Physics',5:'CS',6:'P/C/CS Practical',7:'Physical Education',8:'Art',9:'Biology',10:'Break'}
                c = 1
               
                for a in D.values():
                    print(str(c)+'→'+f' {a}')
                    c += 1

                sub = []
                
                print('ENTER Subject CODES for classes\n')
                for i in range(NO_OF_PERIODS):
                    s = int(input(f'Enter Class {i+1}: '))
                    while s < 1 or s > 10:
                        print('\nPlease enter a valid class (refer Subject Codes)!')
                        s = int(input(f'Enter Class {i+1}: '))
                    sub.append(D[s])


                #CONNECTING TO MySQL
                
                mycon = msc.connect(host='localhost',user='root',passwd='$@n@Sampson483',database='school')

##                if mycon.is_connected():
##                    print('Successfully connected to MySQL')

                mycur = mycon.cursor()
                mycur.execute('delete from tt;')
                
                t = input('\n\nEnter First period Bell Timing as "HH:MM" (24 hr time) - ')
                duration = int(input('\nWARNING : Total runtime of program will depend on this entry!\nEnter duration of the class(1-45 minutes):'))
                if duration < 1 or duration > 45:
                    print('Invalid entry! Setting duration as 1 minute!')
                    duration = 1
                Min,Hour = incrtime(t,NO_OF_PERIODS,duration)
                
                ntm = []
            #Adding timetable in ntm
                
                for i in range(0,len(Hour)):
                    if Min[i] < 10:
                        ntm.append(str(Hour[i])+':0'+str(Min[i]))
                    else:
                        ntm.append(str(Hour[i])+':'+str(Min[i]))
                
            #Inserting timetable in SQL database :
                for i in range(0,NO_OF_PERIODS):
                    qu = "INSERT INTO TT VALUES(%d,'%s','%s');"%(i+1,ntm[i],f'{sub[i]}')
                    mycur.execute(qu)
                
                mycur.execute('commit')

                mycur.execute('select * from tt;')
                res = mycur.fetchall()

            #Displaying the timetable:
                
                print('\n-------------TIMETABLE---------------\n')
                data = res
                print('=========================================================')
                hdr = ['Sr.No','Time','Session']

                #Table Header
                for title in hdr:
                    if title == 'Subject':
                        print(title + '\t' + ' ', end = '\t')
                    else:
                        print(title + '\t',end = '\t')
                print()
                print('=========================================================')

                #Table Records
                for i in data:
                    for it in i:
                        if it == 'Computer Science':
                            print(str(it) + ' ',end = '\t')
                        else:
                            print(str(it) + '\t',end = '\t')
                    print()
                    print('---------------------------------------------------------')

                print()
                #Extracting data from MySQL
                sno = list(map(lambda x:x[0],res))
                ltime = list(map(lambda x:x[1],res))
                session = list(map(lambda x:x[2],res))

                TT = {}
                for i in range(len(sno)):
                    TT[i+1] = session[i]
                #print(TT)

                Hr = []
                for i in range(len(ltime)):
                    if ltime[i][1].isdigit() == True:
                        hour = ltime[i][:2]
                        
                    else:
                        hour = ltime[i][:1]
                    Hr.append(hour)

                Min = []
                for j in range(len(ltime)):
                    minute = ltime[j][-2:]
                    Min.append(minute)

                #print(Hr)
                #print(Min)
                
                for k in range(len(Hr)):
                    H = int(Hr[k])
                    M = int(Min[k])
                    print(f'Bell {k+1} will ring at ' + Hr[k] + ':' + Min[k])

                #Calling SchoolBell(for every class)

                    schoolBell(H,M)
                    print('→ Time for {}!! ----------\n'.format(TT[k+1]))

                #For last class:    
                time.sleep((duration * 60) - 15)
               

                now = datetime.now()
                currentHour = now.hour
                currentMin = now.minute

                #Calling Final Bell for Dispersal     
                schoolBell(currentHour,currentMin)
                print('\n\n----------- SCHOOL ENDS!! Final Bell has rung! ------------')

                mycur.close()
                mycon.close()

                print('\n\n\n******************************   MAIN MENU   *************************************\n')
                print('1 → SCHOOL BELL')
                print('2 → TEACHER DATABASE')
                print('3 → EXIT PROGRAM')
                print('------------------------------------------------------------------------------------')
                ch = int(input('Enter your choice : '))
                print('------------------------------------------------------------------------------------')

                
            #Exception Handling - 
            except Exception as ex:
                print(f'\nERROR - {ex}')
                print('\nRestarting SCHOOL BELL...')
                ch == 1

            #Closing connection with MySQL--
            else:
                mycur.close()
                mycon.close()

        elif ch == 2:
            #Teacher's database management
            try:
                print('\n\n\n****************************** TEACHERS DATABASE MANAGEMENT *************************************\n\n')
                print('MENU----')
                ans = 'y'
                while ans != '0':
                    print('=====================================================================================================')
                    print('Enter 1 to ADD new teachers')
                    print('Enter 2 to DELETE a teacher\'s record')
                    print('Enter 3 to MODIFY existing teacher\'s record')
                    print('Enter 4 to DISPLAY all teachers\' records')
                    print('Enter 0 to QUIT')
                    print('=====================================================================================================\n')
                    op = int(input('Enter operation for TEACHER\'S DATABASE - '))
                    print('=====================================================================================================\n')
                    while op > 4 or op < 0:
                        print('Invalid entry!!\n')
                        op = int(input('Enter operation for TEACHER\'S DATABASE - '))
                    else:
                        if op == 1:
                            teacher.add()
                        elif op == 2:
                            teacher.delete()
                        elif op == 3:
                            teacher.modify()
                        elif op == 4:
                            teacher.display()
                        else:
                            print('_______________________________________________________________________\n')
                            ans = input('TO CONFIRM EXIT : Enter 0\nTO CONTINUE : Enter any other character\n→ ')
                            print('_______________________________________________________________________\n')
                else:
                    print('\n\n\n******************************   MAIN MENU   *************************************\n')
                    print('1 → SCHOOL BELL')
                    print('2 → TEACHER DATABASE')
                    print('3 → EXIT PROGRAM')
                    print('------------------------------------------------------------------------------------')
                    ch = int(input('Enter your choice : '))
                    print('------------------------------------------------------------------------------------')

            #Exception Handling - 
            except Exception as ex:
                print(f'ERROR - {ex}')
                print('\nRestarting TEACHER DATABASE...')
                ch = 2

        else:
            print('''Exiting **** SCHOOL BELL Program!! **** \n  Thank you!!\n''')
            break

#Exception Handling - 
except Exception as ex:
    print(f'ERROR - {ex}')
       




    
    
