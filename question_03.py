__author__ = 'Chaithra'

notes = """
    This is to make you familiar with in place usage of lists.
"""


#numbers is list of 0's 1's and 2's ina random order.
#Your job is to modify the list in place to sort in increasing order
#Don't use any builtin functions on lists
def sort_0_1_2(numbers):
    if numbers==None:
        return None
    l=len(numbers)
    index_1=l-1
    index_2=l-1
    while index_1>=0:
        if numbers[index_1] not in [0,1,2]:
            return "invalid input"
        if numbers[index_1]==2:
                temp=numbers[index_1]
                numbers[index_1]=numbers[index_2]
                numbers[index_2]=temp
                index_2-=1
                index_1-=1
        else:
            index_1-=1
    l=index_2
    index_1=0
    index_2=0
    while index_1<l+1:
        if numbers[index_1] == 0:
            temp=numbers[index_1]
            numbers[index_1]=numbers[index_2]
            numbers[index_2]=temp
            index_1 += 1
            index_2 += 1
        else:
            index_1 += 1
    return numbers

#write tests to test your solution.
def test_sort_0_1_2():
    assert sort_0_1_2([0,1,2]) == [0,1,2] #sorted input
    assert sort_0_1_2([0,0,0]) == [0,0,0] #input has all 0's
    assert sort_0_1_2([1,1,1]) == [1,1,1] #input has all 1's
    assert sort_0_1_2([2,2,2]) == [2,2,2] #input has all 2's
    assert sort_0_1_2(None) == None  #input is None
    assert sort_0_1_2([]) == [] #empty list
    assert sort_0_1_2([0,2,2,1,1,2,0,0]) == [0,0,0,1,1,2,2,2] #random input
    assert sort_0_1_2([2,2,1,1]) == [1,1,2,2] #input has only 1's and 2's
    assert sort_0_1_2([0,0,0,0,0,1,1,1,1,2,1,2,1,2,1,2,1]) == [0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2] #random input with more numbers
    assert sort_0_1_2([2,0,1,0,2])==[0,0,1,2,2] #extreme case
    assert sort_0_1_2([-1,-1,0,0,2,2])== "invalid input" #negative numbers
    assert sort_0_1_2(['a','/',0,0,1,1,2]) == "invalid input" #characters
    assert sort_0_1_2("anbfhs") == "invalid input" #string as input
    assert sort_0_1_2([2,0,0,0,0,0,0,0,0,0,0,1]) == [0,0,0,0,0,0,0,0,0,0,1,2] #input in order 2,0,1
    assert [0, 0, 0, 1, 1, 2, 2, 2] == sort_0_1_2([0,1,2,0,1,2,2,0])  #even input
    assert [0, 0, 0, 1, 1, 1, 2, 2, 2] == sort_0_1_2([2,2,2,1,1,1,0,0,0]) #odd input
    assert [0, 0, 0, 0, 1, 1, 2, 2, 2] == sort_0_1_2([1,0,2,0,2,1,2,0,0])
    assert [0, 0, 0, 0, 0, 1, 1, 2, 2, 2] == sort_0_1_2([1,2,0,2,0,1,0,2,0,0])
    assert [0, 0, 1, 1, 1, 2, 2, 2]==sort_0_1_2([2,0,2,0,2,1,1,1])


