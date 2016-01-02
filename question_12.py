__author__ = 'Chaithra'

# rotate the input list by number times in place.
# don't use any new intermediate lists if possible.
def rotate_right(input, number):
    input[0:len(input)-number]=reverse(input[0:len(input)-number])
    input[len(input)-number:]=reverse(input[len(input)-number:])
    return reverse(input)

def reverse(inp):
    i=0
    l=len(inp)
    while i<l/2:
        temp=inp[i]
        inp[i]=inp[l-i-1]
        inp[l-i-1]=temp
        i+=1
    return inp
def test_rotate():
    input = range(1,7)
    input = rotate_right(input, 2)
    assert [5,6,1,2,3,4] == input

    input = range(1,7)
    input = rotate_right(input, 3)
    assert [4,5,6,1,2,3] == input

    input = range(1,7)
    input = rotate_right(input, 1)
    assert [6,1,2,3,4,5] == input




