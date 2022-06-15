
import re
print("                                           password                                                         ")

class NAme:
    def Simple(self):
        gh = input("Enter your Passwprd: ")
        print(gh)


    def name(self):
        l = {
        "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11,"l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25,"z":26,
        "A":270, "B":280, "C":30, "D":40, "E":50, "F":60, "G":70, "H":80, "I":90, "J":100, "K":110,"L":120, "M":130, "N":140, "O":150, "P":160, "Q":170, "R":180, "S":190, "T":200, "U":210, "V":220, "W":230, "X":240, "Y":250,"Z":260
        }

        gh = input("Enter password here: ")
        list(gh)
        cp =[]
        d = len(gh)
        #print(d)

        for i in range (d):
            ao = gh[i]
            if (i%2 != 0):
                if ao in l:
                    ad = l[ao]
                    cp.append(ad)
                else:
                    cp.append(ad)    
            else:
                cp.append(ao)    

        print(*cp, sep = "") 

        
        dp = []
        for i in range (d):
            ao = cp[i]
            if (i%2 != 0):
                if ao <= 27 :
                    for letter, number in l.items():
                        if number == ao:
                            dp.append(letter)

    
                else:
                    dp.append(ao)    
            else:
                dp.append(ao)

        print(''.join(dp))


    def word2ac(self):
        password = input("enter password here: ")
        pattern = r'[0-9]'
        new_string = re.sub(pattern, '-', password)
        for i in password:
            a = print([ord(i)], end= " ")
        print(new_string)
        z = int(password.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()[];:,.<>?\|]~-=_+'}))
        print(a)
    # x = chr(int(a))
    # print(x)
        password = input("enter password here: ")
        ad = [] 
        for i in password:
            a = print(ord(i), end= " ")
            ad.append(a)


        password = input("enter password here: ")
        ascii_values = []
        for character in password:
            ascii_values.append(ord(character))
        res = ""
        for val in ascii_values:
            res = res + chr(val)
        print(ascii_values)
        print(str(res))    
#this func. is for storing Gmail detials
    def Gmail(self):
        print("Please Enter Your Mail :")
        m = input()
        print('''\033[1mSelect the option to save your passcode in the form of:
                1. Noraml
                2. Word To Number
                3. In Comp Code''')
        n = int(input()) 
        
        #n = int(input())
        if n == 1:
            NAme.Sipmle(1)
        elif n==2:
            NAme.name(2)
        elif n == 3:
            NAme.word2ac(3)
        else:
            print("Select Valid ")
            NAme.Gmail(self)       
            
    def Facebook(self):
        print("Please Enter Your Mail :")
        m = input()
        print('''\033[95mSelect the option to save your passcode in the form of:
                1. Noraml
                2. Word To Number
                3. In Comp Code''')
        n = int(input()) 
        
        if n == 1:
            NAme.Sipmle(1)
        elif n==2:
            NAme.name(2)
        elif n == 3:
            NAme.word2ac(3)
        else:
            print("Select Valid ")
            NAme.Facebook(self)
    #this func. is for storing Instagram detials
    def Instagram(self):
        print("Please Enter Your Mail :")
        m = input()
        print('''\033[92mSelect the option to save your passcode in the form of:
                1. Noraml
                2. Word To Number
                3. In Comp Code''')
        n = int(input()) 
       
        if n == 1:
            NAme.Sipmle(1)
        elif n==2:
            NAme.name(2)
        elif n == 3:
            NAme.word2ac(3)
        else:
            print("Select Valid ")
            NAme.Instagram(self)
    #this func. is for storing Snap detials   
    def Snap(self):
        print("Please Enter Your Mail :")
        m = input()
        print('''\033[96mSelect the option to save your passcode in the form of:
                1. Noraml
                2. Word To Number
                3. In Comp Code''')
        n = int(input()) 
        if n == 1:
            NAme.Sipmle(1)
        elif n==2:
            NAme.name(2)
        elif n == 3:
            NAme.word2ac(3)
        else:
            print("Select Valid ")
            NAme.Snap(self)
            
def Option():
    print('''options to save for :
    1. Gmail
    2. Facebook 
    3. Instagram 
    4. Snap
    ''')

    n = input("Enter Option Number :")
    if n == '':
        Option()

    
    elif n in '123456789':

        n=int(n)
        if n==1:
            NAme.Gmail(1)
        elif n==2:
            NAme.Facebook(2)
        elif n== 3 :
            NAme.Instagram(3)
        elif n==4:
            NAme.Snap(4)     
        else:
            print("Invalid Press Enter for Options or 0 to Exit:")
            l = input()
            if l==0:
                exit()
            else:
                Option()
                
    else:
        Option()

Option()