print('khurram khalil')
user = input('1- dd-mm-yy\n2-mm-dd-yy\nwhich date formate you want to check: ')
'''enter 1 or 2 '''
if user=='1' or 'i' or 'one':
    print('enter date in dd,mm,yy formate by using function date1(dd,mm,yy)')
    def date1(dd,mm,yy):
        '''enter 2 digit number of day month and year example 22,12,19 and etc'''
        print('you want to check date','(',dd,'-',mm,'-',yy,')')
        thirty1=[1,3,5,7,8,10,12]
        thirty=[4,6,9,11]
        leap=[2]
        ran1=31
        ran2=30
        ran3=28
        if mm==leap and (dd in range(1,29)) and (yy in range(1,100)):
            print('this is valid date')
        elif mm==thirty1 and (dd in range(1,32)) and (yy in range(1,100)):
            print('this is valid date')
        elif mm==thirty and (dd in range(1,31)) and (yy in range(1,100)):
            print('this is valid date')
        elif (dd in range(1,28)) and (mm in range(1,13)) and (yy in range(1,100)):
            print('this is valid date')
        else:
            print('this is invalid date \ncheck wether \n 1-the months are in range \n 2-days are in range')
else:
    print('we dont deal with anyother type of formate')

if user=='2' or 'ii' or 'two':
    print('enter date in mm,dd,yy formate by using function date2(mm,dd,yy)')
    def date2(mm,dd,yy):
        '''enter 2 digit number of day month and year example 22,12,19 and etc'''
        print('you want to check date','(',dd,'-',mm,'-',yy,')')
        thirty1=[1,3,5,7,8,10,12]
        thirty=[4,6,9,11]
        leap=[2]
        ran1=31
        ran2=30
        ran3=28
        if mm==leap and (dd in range(1,29)) and (yy in range(1,100)):
            print('this is valid date')
        elif mm==thirty1 and (dd in range(1,32)) and (yy in range(1,100)):
            print('this is valid date')
        elif mm==thirty and (dd in range(1,31)) and (yy in range(1,100)):
            print('this is valid date')
        elif (dd in range(1,28)) and (mm in range(1,13)) and (yy in range(1,100)):
            print('this is valid date')
        else:
            print('this is invalid date \ncheck wether \n 1-the months are in range \n 2-days are in range')
else:
    print('we do not deal with anyother type of formate')
