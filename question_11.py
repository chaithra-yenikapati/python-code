__author__ = 'Chaithra'

def right_binary_search(input, value):
    def right_binary(low,high):
        if(low>high):
            return -1
        else:
             middle=(low+high)/2
             if(value<input[middle]):
                 return right_binary(low,middle-1)
             elif(value>input[middle]):
                 return right_binary(middle+1,high)
             else:
                 if len(input)==1:
                     return 0
                 else:
                     try:
                        while input[middle]==input[middle+1]:
                            middle=middle+1
                     except:
                       return middle
                 return middle
    if(input==None):
       return -1
    else:
        return right_binary(0,len(input)-1)


def test_right_binary_search():
    input = range(10)
    for index, value in enumerate(input):
        assert index == right_binary_search(input, value)
        
    assert -1 == right_binary_search(input, -10)
    assert -1 == right_binary_search(input, 100)

    assert -1 == right_binary_search([], 10)
    assert -1 == right_binary_search(None, 10)
    assert 0 == right_binary_search([10], 10)
    assert -1 == right_binary_search([10], 5)

    input = [1,1,2,2,2]

    assert 1 == right_binary_search(input, 1)
    assert 4 == right_binary_search(input, 2)
