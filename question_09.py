__author__ = 'Chaithra'


def binary_search(input, key):
    def binary(low,high):
        if(low>high):
            return -1
        else:
             middle=(low+high)/2
             if(key<input[middle]):
                 return binary(low,middle-1)
             elif(key>input[middle]):
                 return binary(middle+1,high)
             else:
                 return middle

    if(input==None):
       return -1
    else:
        return binary(0,len(input)-1)


def test_binary_search():
    input = range(10)
    for index, value in enumerate(input):
        assert index == binary_search(input, value)

    assert -1 == binary_search(input, -10)
    assert -1 == binary_search(input, 100)

    assert -1 == binary_search([], 10)
    assert -1 == binary_search(None, 10)
    assert 0 == binary_search([10], 10)
    assert -1 == binary_search([10], 5)


