__author__ = 'Chaithra'

def left_binary_search(input, value):
    def left_binary(low,high):
        if(low>high):
            return -1
        else:
             middle=(low+high)/2
             if(value<input[middle]):
                 return left_binary(low,middle-1)
             elif(value>input[middle]):
                 return left_binary(middle+1,high)
             else:
                 if len(input)==1:
                     return 0
                 else:
                     while input[middle]==input[middle-1]:
                         middle=middle-1
                     return middle
    if(input==None):
       return -1
    else:
        return left_binary(0,len(input)-1)


def test_left_binary_search():
    input = range(10)
    for index, value in enumerate(input):
        assert index == left_binary_search(input, value)
        
    assert -1 == left_binary_search(input, -10)
    assert -1 == left_binary_search(input, 100)

    assert -1 == left_binary_search([], 10)
    assert -1 == left_binary_search(None, 10)
    assert 0 == left_binary_search([10], 10)
    assert -1 == left_binary_search([10], 5)

    input = [1,1,2,2,2]

    assert 0 == left_binary_search(input, 1)
    assert 2 == left_binary_search(input, 2)
