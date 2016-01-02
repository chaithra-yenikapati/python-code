__author__ = 'Chaithra'

# assume indexes i and j are non-negative and within bounds of array.
# shift the section [i, j] to the beginning of the array in place
def shuffle(inp, i, j):
    inp[0:i]=reverse(inp[0:i])
    inp[i:j+1]=reverse(inp[i:j+1])
    inp=reverse(inp[0:j+1])+inp[j+1:]
    return inp

def reverse(inp):
    i=0
    l=len(inp)
    while i<l/2:
        temp=inp[i]
        inp[i]=inp[l-i-1]
        inp[l-i-1]=temp
        i+=1
    return inp

def test_shuffle():
    input = [1, 2, 3, 4, 5, 6]
    input = shuffle(input, 1, 2)
    assert [2, 3, 1, 4, 5, 6] == input

    input = [1, 2, 3, 4, 5, 6]
    input = shuffle(input, 4, 5)
    assert [5, 6, 1, 2, 3, 4] == input

    input = [1, 2, 3, 4, 5, 6]
    input = shuffle(input, 0, 3)
    assert [1, 2, 3, 4, 5, 6] == input

    input = [1, 2, 3, 4, 5, 6]
    input = shuffle(input, 1, 5)
    assert [2, 3, 4, 5, 6, 1] == input


