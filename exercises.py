def digits(num):
    if int(len(num))!=0:
        print (len(num))
    else:
        print ("please enter number")

def words(word):
   a= word.count(" ")
   print(a+1)

def biggest():
    print ("enter number seperated by comma")
    lt=list(input(">>>").split(","))
    lt.sort()
    print (lt[-1])

def biggest_smallest():
    print("enter the number seperated by comma")
    lt=list(input(">>>").split(","))
    lt.sort()
    print((int(lt[0]),int(lt[2])))

def tables():
    print (">>> tables ",end='')
    m,n=map(int,input().split(","))
    if m!=0:
        for i in range(1,n+1):
                print (m,"*",i,"= ",m*i)
                i+=1
                
    else:
        print ("Please enter a number")
        tables()

def tables2():
    m=int(input("please enter number  "))
    for i in range(1,m+1):
        for j in range(1,m+1):
            print (i*j,end='\t')  
        print()

def average():
        lit=list(map(int,input(">>>average ").split(",")))
        leng=len(lit)
        sums=0
        for i in lit:
            sums+=i
        print (sums/leng)

def fuzzbuzz():
    limit=int(input(">>> fuzzbuzz "))
    for i in range(1,limit+1):
        if i%15==0:
            print("fuzzbuzz")         
        elif i%5==0:
            print("buzz")
        elif i%3==0:
            print ("fuzz")
        else:
            print(i)

def maximum():
    lit=list(map(int,input(">>>maximum ").split(",")))
    lit.sort()
    print(lit[-1])

def panagram():
    import string
    strings=input(">>> panagram ")
    stringp=strings.split(" ")
    length=len(stringp)
    t_length=0
    for i in range(0,length):
        t_length+=len(stringp[i])
    
    if t_length<26:
       print (False)  
    else:
        checker=list(string.ascii_lowercase)
        checker.append(" ")
        entered_list=list(strings)
        for i in checker:
            b=False
            if i in entered_list:
                b=True
        if b:
            print(True)
        else:
            print(False)

def freq():
    string=input(">>>freq- ")
    lit=list(string)
    dic={}
    for i in lit:
        dic[i]=string.count(i)
    print (dic)

def abbreviate():
    lit=list(input("abbreviate  ").split(" "))
    string=''
    for i in lit:
        if i[0] in i.upper():
            string+=i[0]
        else:
            pass
    print (string)
    
def ari():

    with open("moby-dick.txt") as file:
        
        data_infile2=file.read().replace("\n"," ")
        data_infile=data_infile2.replace("   "," ")
    number_of_sentence=list(data_infile.split("."))
    number_of_space=data_infile.count(" ")
    words=list(data_infile.split(" "))
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    y=0
    for i in words:
        for x in alphabet:
            n=i.count(x)
            y=y+n
            
    c=data_infile.count("  ")
    b=data_infile.count("   ")
    y=y- number_of_space 
    orginal_space=number_of_space+c+b
    a=4.71*(y/ orginal_space) + 0.5*(orginal_space / len(number_of_sentence)) - 21.43
    integer=int(a)
    integer= integer + 1
    if integer==1:
        print("Kindergarten")
    elif integer==2:
        print("First/Second Grade")
    elif integer ==3:
        print("Third Grade")
    elif integer==4:
        print("Fourth Grade")
    elif integer ==5:
        print("Fifth Grade")
    elif integer==6:
        print("Sixth Grade")
    elif integer ==7:
        print("Seventh Grade")
    elif integer==8:
        print("Eighth Grade")
    elif integer==9:
        print("Ninth Grade")
    elif integer==10:
        print("Tenth Grade")
    elif integer==11:
        print("Eleventh Grade")
    elif integer==12:
        print("Twelfth Grade")
    elif integer==13:
        print("College student")
    else:
        print("Professor")
        
    file.close()



def median():
    numbers=list(map(int,input("median ").split(",")))
    numbers.sort()
    length=len(numbers)
    m=int(length/2)
    if length%2==0:
        a=numbers[m-1]
        b=numbers[m]
        print((a+b)/2)
    else:
      
        print(numbers[m])


def mode():
    import operator
    string=input("mode ")
    numbers=list(map(int,string.split(",")))
    dic={}
    for i in numbers:
        dic[i]=string.count(str(i))

    updated_list=list(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
    x,y=updated_list[0]
    print (x)


def breakdown():
    number=int(input("breakdown "))
    if number>2000:
        x=int(number/2000)
        print("2000 *",x,"=",2000*x,"(",number%2000,"left )")
        number =number%2000

    if number>500:
        x=int(number/500)
        print("500 *",x,"=",500*x,"(",number%500,"left )")
        number =number%500

    if number>200:
        x=int(number/200)
        print("200 *",x,"=",200*x,"(",number%200,"left )")
        number =number%200

    if number>100:
        x=int(number/100)
        print("100 *",x,"=",100*x,"(",number%100,"left )")
        number =number%100

    if number>50:
        x=int(number/50)
        print("50 *",x,"=",50*x,"(",number%50,"left )")
        number =number%50

    if number>20:
        x=int(number/20)
        print("20 *",x,"=",20*x,"(",number%20,"left )")
        number =number%20

    if number>10:
        x=int(number/10)
        print("10 *",x,"=",10*x,"(",number%10,"left )")
        number =number%10

    if number>5:
        x=int(number/5)
        print("5 *",x,"=",5*x,"(",number%5,"left )")
        number =number%5

    if number>1:
        x=int(number)
        print("1*",x,"=",1*x,"(",number%1,"left )")
    else:
        print("error")
            

