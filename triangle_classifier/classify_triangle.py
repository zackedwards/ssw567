'''
Created on Feb 3, 2021

@author: Zack Edwards
'''

def classify(int1, int2, int3):
    #check for scalene, isoceles or equilateral
    mylist = [int1, int2, int3]
    if int1 == int2 and int2 == int3:
        equilateral = 'e'
        mylist.sort(key=None, reverse=True)
        if(mylist[0]**2 == mylist[1]**2 + mylist[2]**2):
            print("This is an equilateral triangle, and a right triangle.")
            right = 'r'
            return equilateral, right
        else:
            print("This is an equilateral triangle")
            right = 'n'
            return equilateral, right
    elif int1 == int2 or int1 == int3 or int2 == int3:
        isosceles = 'i'
        mylist.sort(key=None, reverse=True)
        if(mylist[0]**2 == mylist[1]**2 + mylist[2]**2):
            print("This is an isosceles triangle, and a right triangle.")
            right = 'r'
            return isosceles, right
        else:
            print("This is an isosceles triangle")
            right = 'n'
            return isosceles, right
    else:
        scalene = 's'
        mylist.sort(key=None, reverse=True)
        if(mylist[0]**2 == mylist[1]**2 + mylist[2]**2):
            print("This is a scalene triangle, and a right triangle.")
            right = 'r'
            return scalene, right
        else:
            print("This is a scalene triangle")
            right = 'n'
            return scalene, right
classify(3, 4, 5)
classify(8,8,8)
classify(6,9,9)
