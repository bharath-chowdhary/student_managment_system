dic={}
def addd():
    d=int(input('Enter Student ID: '))
    b=input('Enter Student Name: ')
    f=input('Enter Branch: ')
    c=float(input('Enter Student Grade: '))
    dic[d]=(d,b,f,c)
    
def updatee():
    pp=int(input('Enter Student RollNo: '))
    if pp not in dic:
        print('Student Not Found With This Roll No')
        print('-------------------------------------')
    else:
        print('__________________')
        print('1. Update Name')
        print('2. Update Branch')
        print('3. Update Grade')
        p=int(input('Enter the Number of Above What U Wanna Update: '))
        if p==1:k=input('Enter the Updated Value: ')
        elif p==3:k=float(input('Enter the Updated Value: '))
        dic[pp]=list(dic[pp])
        dic[pp][p]=k

def deletee():
    d=int(input('Enter Student Rollnumber: '))
    if d not in dic:
        print('Student Not Found With This Roll No')
        print('------------------------------------')
    else:
        dic.pop(d)
    
def vieww():
    for j in dic.values():
        print('___________________________')
        St,na,br,gr=j
        print('Student ID:',St)
        print('Student Name:',na)
        print('Branch:',br)
        print('Grade:',gr)
        print('---------------')

def search():
    enter=int(input('Enter Rollno: '))
    if enter not in dic:
        print('-----------------------------------')
        print('Student Not Found With This Roll No')
    else:
        print('___________________________')
        lst=[]
        lst.append(dic[enter])
        for j in lst:
            St,na,br,gr=j
            print('Student ID:',St)
            print('Student Name:',na)
            print('Branch:',br)
            print('Grade:',gr)
            print('---------------')

a=0
while a!=6:
    print('Student Grade Mangament System')
    print('1. Add Student')
    print('2. Update Student')
    print('3. Delete Student')
    print('4. View Student')
    print('5. Search Student')
    print('6. Exit')
    a=int(input('Enter the Choice: '))
    if a==1:
        addd()
    elif a==2:
        updatee()
    elif a==3:
        deletee()
    elif a==4:
        vieww()
    elif a==5:
        search()
    else:
        break

