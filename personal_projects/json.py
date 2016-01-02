__author__ = 'chaithra'

def json_deserializer(temp):
    x=[]
    result=[]
    for j in range(len(temp)):
        a=str(temp[j])
        x=[]
        b=[]
        i=0
        while(i<len(a)):
            if(a[i]=='{'or a[i]==' ' or a[i]==',' or a[i]==":" or a[i]=="'" or a[i]=='[' or a[i]==']' or a[i]=='\n' or a[i]=='"'):
                i=i+1
            elif(a[i]=="}"):
                i=i+1
            else:
                b=[]
                while(a[i]!="{" and a[i]!=":" and a[i]!="}" and a[i]!="," and a[i]!="'"):
                    b.append(a[i])
                    i=i+1
                x.append("".join(b))
        result.append(x)
    return result

def form_number(num):
    if(num==None):
        return
    temp=[]
    for i in range(len(num)):
        if(ord(num[i])>=48 and ord(num[i])<=57):
            temp.append(num[i])
    return "".join(temp)

def avg_age(res):
    mean_of_age=0
    for i in range(len(res)):
        mean_of_age+=(int(res[i].age))
    mean_of_age=mean_of_age/len(res)
    return mean_of_age

def median(res):
    temp=[]
    for i in range(len(res)):
        temp.append(float(res[i].height))
    temp=sorted(temp)
    if(len(temp)%2==0):
        j=len(temp)/2
        return (temp[j]+temp[j-1])/2
    else:
        return temp[(len(temp)-1)/2]

class person:
    def __init__(self):
        self.firstname=""
        self.lastname=""
        self.age=None
        self.height=None
        self.home_no=None
        self.fax_no=None
    def first_name(self,firstname):
        self.firstname=firstname
    def last_name(self,lastname):
        self.lastname=lastname
    def age1(self,age):
        self.age=age
    def height1(self,height):
        self.height=height
    def home1(self,home_no):
        self.home_no=home_no
    def fax1(self,fax_no):
        self.fax_no=fax_no
    def display(self):
        print self.firstname
        print self.lastname
        print self.age
        print self.height
        print self.home_no
        print self.fax_no

def retrieve_data(final):
    res=[]
    for i in range(len(final)):
        temp=final[i]
        o=person()
        j=0
        while j < len(temp):
            if(temp[j]=='firstName'):
                o.first_name(temp[j+1])
                j=j+1
            elif(temp[j]=='lastName'):
                o.last_name(temp[j+1])
                j=j+2
            elif(temp[j]=='age'):
                o.age1(temp[j+1])
                j=j+2
            elif(temp[j]=='height'):
                o.height1(temp[j+1])
                j=j+2
            elif(temp[j]=='home'):
                x=form_number(temp[j+2])
                o.home1(x)
                j=j+3
            elif(temp[j]=='fax'):
                x=form_number(temp[j+2])
                o.fax1(x)
                j=j+3
            else:
                j=j+1
        res.append(o)
    return res

def find_duplicate_home_numbers(input_number):
    temp=[x for x in input_number if input_number.count(x)>1]
    temp=set(temp)
    temp=list(temp)
    for i in range(len(temp)):
        if temp[i]!=None:
            print temp[i]
            for j in range(len(result)):
                if (result[j].home_no) == temp[i]:
                    print result[j].firstname

def find_duplicate_fax_numbers(input_number):
    temp=[x for x in input_number if input_number.count(x)>1]
    temp=set(temp)
    temp=list(temp)
    for i in range(len(temp)):
        if temp[i]!=None:
            print temp[i]
            for j in range(len(result)):
                if (result[j].fax_no) == temp[i]:
                    print result[j].firstname

def find_duplicate_numbers(temp,res):
    for i in range(len(temp)):
        if temp[i]!=None:
            print temp[i]
            j=0
            while j<len(res):
                if (temp[i]==res[j].home_no) :
                    print "home : ",res[j].firstname
                if(temp[i]==res[j].fax_no) :
                    print "fax : ",res[j].firstname
                j=j+1


input=[{
    "age": 44,
    "firstName": "Peri",
    "lastName": "B",
    "height": 5.4,
    "phoneNumbers": [
        {  "type": "home",
           "number": "212 555-123" },
        {  "type": "fax",
           "number": "646 555-4567" }
    ]
       },

{
    "age": 18,
    "firstName": "ram",
    "lastName": "B",
    "height": 5.8,
    "phoneNumbers": [
        {  "type": "home",
           "number": "212 555-1234" },
        {  "type": "fax",
           "number": "646 555-4567" }
    ]
},
{
    "age": 21,
    "firstName": "raghavendra",
    "lastName": "B",
    "height": 6.1,
    "phoneNumbers": [
        {  "type": "home",
           "number": "212 555-1234" },
        {  "type": "fax",
           "number": "6-4-6 555-4567" }
    ]
},
{
    "age": 19,
    "firstName": "udbav",
    "lastName": "B",
    "height": 5.7,
    "phoneNumbers": [
        {  "type": "home",
           "number": "212 5-5-5-12-34" },
        {  "type": "fax",
           "number": "64-6 55-5-45-67" }
    ]
},
{
"firstName": "teja",
"lastName": "B",
"height": 5.11,
"age": 19,
"phoneNumbers": [
    {  "type": "home",
       "number": "212 555-1234" },
    {  "type": "fax",
       "number": "646 555-4567" }
]
},
{
"firstName": "shiva",
             "lastName": "B",
                         "height": 5.9,
                                   "age": 20,
                                          "phoneNumbers": [
{  "type": "home",
   "number": "212 555-1234" },
{  "type": "fax",
   "number": "646 555-4567" }
]
},
{
    "firstName": "pruthvi",
    "lastName": "B",
    "height": 5.10,
                                       "age": 44,
                                              "phoneNumbers": [
{  "type": "home",
   "number": "212 555-1234" },
{  "type": "fax",
   "number": "646 555-4567" }
]
},
{
    "firstName": "abhi",
    "lastName": "B",
    "height": 5.9,
    "age": 20,
    "phoneNumbers": [
{  "type": "home",
   "number": "210 555-1234" },
{  "type": "fax",
   "number": "646 555-4567" }
]
},
{
    "firstName": "manoj",
    "lastName": "B",
    "height": 5.10,
    "age": 44,
    "phoneNumbers": [
{  "type": "home",
   "number": "649 555-4567" },
{  "type": "fax",
   "number": "648 555-4567" }
]
},
{
    "firstName": "murali",
    "lastName": "B",
    "height": 5.7,
    "age": 44,
    "phoneNumbers": [
{  "type": "home",
   "number": "210 555-1234" },
{  "type": "fax",
   "number": "649 555-4567" }
]
}
]

if __name__=="__main__":

    global input
    final=json_deserializer(input)
    result=retrieve_data(final)
    average_age=avg_age(result)
    print "average_age=",average_age
    median_of_height=0
    median_of_height=median(result)
    print "median=",median_of_height
    temp_home=[]
    temp_invalid=[]
    temp_fax=[]
    for i in range(len(result)):
        if(len(form_number(result[i].home_no))!=10):
            temp_invalid.append(result[i].home_no)
            temp_invalid.append(result[i].firstname)
            result[i].home1(None)
        temp_home.append(form_number(result[i].home_no))
        temp_fax.append(form_number(result[i].fax_no))
    print " duplicate home_no:"
    find_duplicate_home_numbers(temp_home)
    print " duplicate fax_no:"
    find_duplicate_fax_numbers(temp_fax)
    print " duplicate numbers:"
    temp_home=list(set(temp_home))
    temp_fax=list(set(temp_fax))
    temp=[val for val in temp_home if val in temp_fax]
    find_duplicate_numbers(temp,result)












