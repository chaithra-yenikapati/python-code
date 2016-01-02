__author__ = 'Chaithra'

#fill up this routine to test if the 2 words given are anagrams of each other.
def are_anagrams(first, second):
    if(len(first)==len(second)):
        first_list=[0]*26
        second_list=[0]*26
        i=0
        while i<len(first):
            temp=ord(first[i])
            if (temp>=65 and temp<=90):
                first_list[temp-65]+=1

            elif (temp>=97 and temp<=122):
                second_list[temp-97]+=1
            i+=1

        if cmp(first_list,second_list==0):
            return True
        else:
            return False
    else:
        return False



def test_are_anagrams():
    assert True == are_anagrams("Rat", "Tar")
    assert True == are_anagrams("live", "vile")
    assert True == are_anagrams("least", "slate")
    assert False == are_anagrams("big", "small")
    assert False == are_anagrams("big", "gibs")
