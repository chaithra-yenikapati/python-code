__author__ = 'Chaithra'

notes = """
    This is to introduce you to think on optimizing the solution by iterating down the code written
"""


#Given a list of numbers, modify the list so that each element has the product of all elements except the number
#ex: Input:[1,2,3,4,5]
#output:[120,60,40,30,24]
#Return the list of products
def product_of_list_elements(input):
  len_input=len(input)
  if len_input>1:
   if 0 not in input:
    l=[0]*len_input
    r=[0]*len_input
    l[0]=input[0]
    for i in range(1,len_input):
        l[i]=l[i-1]*input[i]
    r[len_input-1]=input[len_input-1]
    r[0]=l[len_input-1]
    for i in range(len_input-2,0,-1):
        r[i]=r[i+1]*input[i]
        input[i]=(l[i]*r[i])/(input[i]*input[i])
    input[len_input-1]=l[len_input-2]
    input[0]=l[len_input-1]/input[0]
   else:
       if input.count(0)>1:
           return [0]*len_input
       else:
           p=1
           for i in range(0,len_input):
               if input[i]!=0:
                   p*=input[i]
               else:
                   continue
           input=[0]*len_input
           input[input.index(0)]=p
   return input
  else:
      return input

def test_product_of_list_elements():
    assert [120, 60, 40, 30, 24] == product_of_list_elements([1, 2, 3, 4, 5])
    assert [0, 0, 0, 0, 0] == product_of_list_elements([0, 0, 0, 0, 0])
    assert [1] == product_of_list_elements([1])
    assert [72, 0, 0, 0, 0] == product_of_list_elements([0, 3, 1, 8, 3])
    assert [98, 42, 147, -294, -42] == product_of_list_elements([-3, -7, -2, 1, 7])
    assert [] == product_of_list_elements([])
    assert [0] == product_of_list_elements([0])
    assert [4.2, 2.4000000000000004, 2.52, 5.04] == product_of_list_elements([1.2, 2.1, 2, 1])