######################################################################################
#  Module name               : timeConvert.py                                        #
#  Function - incrtime(t,n,d): Creates Hour list and Minute list of time for classes #
#  Coded By                  : Ms. Sana Sampson                                      #
######################################################################################

def incrtime(t,n,d):
    '''
Takes input-
1.time(t) in 'HH:MM'(24hr)format
2.no. of classes(n)
3.duration of class(d)
Creates Hour list and Minute list of time for classes 
    '''
    duration = d
    
    t1 = t.split(":")
    th = int(t1[0])  #hr
    tm = int(t1[1])  #min


    while th > 23 or th < 0 or tm > 59 or tm < 0:
        print( 'ERROR! Please enter a valid time.')
        t = input('\nEnter First period Bell Timing as "HH:MM":')
        t1 = t.split(":")
        th = int(t1[0])  #hr
        tm = int(t1[1])  #min

    else:   
        Minute = []
        Hour = []
      
        
        for i in range(n):
            # --- Push the current time th:tm into the list
            Minute.append(tm)
            Hour.append(th)
##            print('\nProcessing Minute :',tm)
##            print('Processing Hour :',th)

            tempmin = tm + duration

            # --- Generate Next th:tm
            if tempmin >= 60:
                tm = tempmin % 60
                th = (th + 1) % 24 
            else:
                tm = tempmin
                
##            print('\nNext TIME in list .......')

            
        m = Minute
        h = Hour
        return m,h

    
##For running this function--

##t = '23:47'
##M,H = incrtime(t,5,10)
##print(M,H)

