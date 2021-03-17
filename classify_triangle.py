'''
Created on Feb 3, 2021

@author: Zack Edwards
'''
import unittest     # this makes Python unittest module available

def classify(int1, int2, int3):
    '''
    this function takes in 3 variables representing sides of a triangle
    and calculates what type of triangle it is
    '''
    #check for scalene, isoceles or equilateral, and right
    #first check for strings, then check strings to look for numeric string
    if isinstance(int1, str) or isinstance(int2, str) or isinstance(int3, str):
        try:
            int1 = float(int1)
            int2 = float(int2)
            int3 = float(int3)
        except ValueError: #must have valid numbers to continue
            return'invalid'
    mylist = [int1, int2, int3] #make a list for determining order
    if int1 <= 0 or int2 <= 0 or int3 <= 0:
        #test for negative numbers
        return 'invalid'
    if int1 == int2 and int2 == int3:
         #check for equilateral
        return "equilateral"
    #check for isosceles
    if int1 == int2 or int1 == int3 or int2 == int3:
        #find largest number
        mylist.sort(key=None, reverse=True)
        #check for right triangle
        if int(mylist[0]**2) == int(mylist[1]**2 + mylist[2]**2):
            re_msg= "isosceles, right"
        else:
            re_msg= "isosceles"
        return re_msg
    #if its not equilateral or isosceles, it must be scalene
    #check for right triangle again
    mylist.sort(key=None, reverse=True)
    if mylist[0]**2 == mylist[1]**2 + mylist[2]**2:
        return "right"
    return "scalene"

def run_classify_triangle(a_1, b_1, c_1):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a_1, ',' ,b_1, ',' ,c_1, ')=',classify(a_1,b_1,c_1),sep="")

class TestTriangles(unittest.TestCase):
    '''define multiple sets of tests as functions with names that begin
    with 'test'.  Each function may include multiple tests'''
    def test_set_equilateral(self): # test invalid inputs
        '''Testing for equilateral triangle detection'''
        self.assertEqual(classify(1,1,1),'equilateral','1,1,1 should be equilateral')
        self.assertEqual(classify(27,27,27),'equilateral','27,27,27 should be equilateral')
        self.assertNotEqual(classify(8,8,9),'equilateral','8,8,9 should not be equilateral')

    def test_my_test_set_scalene(self):
        '''Testing for scalene triangle detection'''
        self.assertEqual(classify(1,88,9),'scalene','Should be Scalene')
        self.assertEqual(classify(10,15,30),'scalene','Should be Scalene')
        self.assertEqual(classify(1,88,9),'scalene','Should be Scalene')

    def test_my_set_scalene_right(self):
        '''Testing for right triangle detection'''
        self.assertEqual(classify(5,12,13), "right", "Should be a scalene, right triangle")
        self.assertEqual(classify(6,8,10), "right", "Should be a scalene, right triangle")
        self.assertEqual(classify(12,35,37), "right", "Should be a scalene, right triangle")
        self.assertNotEqual(classify(3,4,6),'right','3,4,6 is not a right scalene triangle')

    def test_my_set_isosceles_right(self):
        '''testing for isosceles right'''
        self.assertEqual(classify(15,15,15*(2**(1/2))),'isosceles, right',"Correct isosceles right")

    def test_my_set_isoceles(self):
        '''Testing for isoscles triangle detection'''
        self.assertEqual(classify(10,10,15),'isosceles','Should be isoceles')
        self.assertEqual(classify(4,6,4),'isosceles','Should be isoceles')
        self.assertNotEqual(classify(10,10,10),'isosceles','Should not be isoceles')

    def test_my_set_invalid(self):
        '''Testing for invalid entries such as words or negatives'''
        self.assertEqual(classify("a",10,15),'invalid','Should be invalid')
        self.assertEqual(classify(5,10,'b'),'invalid','Should be invalid')
        self.assertNotEqual(classify("7",10,15),'invalid','Should not be invalid')
        self.assertNotEqual(classify('5','5','7'),'invalid','Should not be invalid')
        self.assertEqual(classify(5,10,'four'),'invalid','Should be invalid')
        self.assertEqual(classify(5,10,-9),'invalid','Should be invalid')
        self.assertEqual(classify(5,'googoo',-9),'invalid','Should be invalid')

if __name__ == '__main__':
    # run_classify_triangle(1,2,3)
    # run_classify_triangle(1,1,1)
    # run_classify_triangle(3,4,5)
    # run_classify_triangle(3,5,5)
    # run_classify_triangle(1,1,2**(1/2))
    # run_classify_triangle('s', 't', 'b')
    # run_classify_triangle('5', '6', '4')

    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
