__author__ = 'Chaithra'

notes = """
    This is to refresh your bit manipulation skills.
"""


#Convert integer to binary string and return the string.
#Integers also include negative numbers. So for negative numbers represent in two's complement.
#Integers are 32-bit integers.
def integer_to_binary(input):
    i=31
    x=''
    while i>=0:
           res=str((input>>i)%2)
           x=x+res
           i-=1
    return x


#write tests to test your solution
def test_integer_to_binary():
    assert '00000000000000000000000000000000'==integer_to_binary(0)
    assert '00000000000000000000000011111111'==integer_to_binary(255)
    assert '11111111111111111111111111101100' == integer_to_binary(-20)
    assert '00000000000000000000000000000000'==integer_to_binary(-0)