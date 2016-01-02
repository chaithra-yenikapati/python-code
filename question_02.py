__author__ = 'Chaithra'

notes = """
   This problem is to introduce you to bit manipulations concepts and unit testing.

"""


# zero_ones is a n arbitrary iterable which returns a series of 0's or 1's
# convert it to a python long. So I could pass in a string or list or tuple or generator of 0's and 1's

def binary_to_base10(zero_ones):
    s=iter(zero_ones)
    result = []

    m=0
    try:

        while True:
            item = s.next()
            m=m<<1
            m=m+int(item)
            result.append(m)


    except :
        return result


#Write tests to test your solution for all possible valid inputs
def test_binary_to_base10():
    assert [1,3,6]==binary_to_base10("110")
    assert [1,3,7,15]==binary_to_base10("1111")
    assert [1,3,6,12,25]==binary_to_base10("11001")
    assert [1,2,4,8,17]==binary_to_base10("10001")