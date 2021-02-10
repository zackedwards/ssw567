'''
Created on Feb 3, 2021

@author: Zack Edwards
'''
import unittest     # this makes Python unittest module available

def classify(int1, int2, int3):
    #check for scalene, isoceles or equilateral, and right
    
    #first check for strings, then check strings to look for numeric string
    if(isinstance(int1, str) or isinstance(int2, str) or isinstance(int3, str)):
        #if the strings are numbers, convert them 
        if(isinstance(int1, str)):
            if(int1.isnumeric()):
                int1 = float(int1)
            else:
                #must have valid numbers to continue
                return'invalid'
        if(isinstance(int2, str)):
            if(int2.isnumeric()):
                int2 = float(int2)
            else:
                return'invalid'
        if(isinstance(int3, str)):
            if(int3.isnumeric()):
                int3 = float(int3)
            else:
                return'invalid'

    if(int1 <= 0 or int2 <= 0 or int3 <= 0):
        #test for negative numbers
        return 'invalid'
    
    #make a list for determining order    
    mylist = [int1, int2, int3]
    #check for equilateral
    if int1 == int2 and int2 == int3:
        return "equilateral"
    #check for isosceles
    elif int1 == int2 or int1 == int3 or int2 == int3:
        #find largest number
        mylist.sort(key=None, reverse=True)
        #check for right triangle
        if(mylist[0]**2 == mylist[1]**2 + mylist[2]**2):
            return "isosceles, right"
        else:
            return "isosceles"
    #if its not equilateral or isosceles, it must be scalene
    else:
        #check for right triangle again
        mylist.sort(key=None, reverse=True)
        if(mylist[0]**2 == mylist[1]**2 + mylist[2]**2):
            return "right"
        else:
            return "scalene"

    
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classify(a,b,c),sep="")

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSetEquilateral(self): # test invalid inputs
        #Testing for equilateral triangle detection
        self.assertEqual(classify(1,1,1),'equilateral','1,1,1 should be equilateral')
        self.assertEqual(classify(27,27,27),'equilateral','27,27,27 should be equilateral')
        self.assertNotEqual(classify(8,8,9),'equilateral','8,8,9 should not be equilateral')
        
    def testMyTestSetScalene(self): 
        #Testing for scalene triangle detection
        self.assertEqual(classify(1,88,9),'scalene','Should be Scalene')
        self.assertEqual(classify(10,15,30),'scalene','Should be Scalene')
        self.assertEqual(classify(1,88,9),'scalene','Should be Scalene') 
    
    def testMySetScaleneRight(self):
        #Testing for right triangle detection
        self.assertEqual(classify(5,12,13), "right", "Should be a scalene, right triangle")
        self.assertEqual(classify(6,8,10), "right", "Should be a scalene, right triangle")
        self.assertEqual(classify(12,35,37), "right", "Should be a scalene, right triangle")
        self.assertNotEqual(classify(3,4,6),'right','3,4,6 is not a right scalene triangle')
    
    def testMySetIsoceles(self):
        #Testing for isoscles triangle detection
        self.assertEqual(classify(10,10,15),'isosceles','Should be isoceles')
        self.assertEqual(classify(4,6,4),'isosceles','Should be isoceles')
        self.assertNotEqual(classify(10,10,10),'isosceles','Should not be isoceles')
        
    def testMySetInvalid(self):
        #Testing for invalid entries such as words or negatives
        self.assertEqual(classify("a",10,15),'invalid','Should be invalid')
        self.assertEqual(classify(5,10,'b'),'invalid','Should be invalid')
        self.assertNotEqual(classify("7",10,15),'invalid','Should not be invalid')
        self.assertNotEqual(classify('5','5','7'),'invalid','Should not be invalid')
        self.assertEqual(classify(5,10,'four'),'invalid','Should be invalid')
        self.assertEqual(classify(5,10,-9),'invalid','Should be invalid')

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(3,4,5)
    runClassifyTriangle(3,5,5)
    runClassifyTriangle(1,1,2**(1/2))
    runClassifyTriangle('s', 't', 'b')
    runClassifyTriangle('5', '6', '4')

    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder