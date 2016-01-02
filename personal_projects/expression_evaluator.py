__author__ = 'chaithra'
global_varlist=[]
for i in range(26):
    global_varlist.append(False)

def is_letter(c):
    if (c>='a' and c<='z') or (c>='A' and c<='Z'):
        return True
    return False
def is_digit(str):
    if str>='0' and str<='9':
        return True
    return False

def is_operator(c):
    if c=='+' or c=='-' or c=='*' or c=='/':
        return True
    return False

def tokenizer(input_str):
    i=0
    tokens=[]
    l=len(input_str)
    while i<l:
        if is_digit(input_str[i]):
          count=i
          while i<l:
              if is_digit(input_str[i]):
                i+=1
              else:
                  break
          tokens.append(int(input_str[count:i]))
        if i==l:
              break
        if is_letter(input_str[i]):
            tokens.append(input_str[i])

        if is_operator(input_str[i]):
            tokens.append(input_str[i])
        if input_str[i]=='=':
            tokens.append(input_str[i])
        i+=1
    return tokens
def evaluate(op1,op,op2):
    if op == "+":
        return op1+op2
    elif op=="-":
        return op1-op2
    elif op=="*":
        return op1*op2
    elif op=="/":
        return op1/op2

def evaluator(tokens):
  result=0
  if len(tokens)==3:
        if isinstance(tokens[2],int):
            result=int(tokens[2])
        elif global_varlist[ord(tokens[2])-ord('a')]:
            result=global_varlist[ord(tokens[2])-ord('a')]
        else:
            return "invalid string"
  else:
    i=3
    for i in range(3,len(tokens),2):
        if (isinstance(tokens[i-1],int)) and (isinstance(tokens[i+1],int)):
            x= evaluate(int(tokens[i-1]),tokens[i],int(tokens[i+1]))
            result=x
            tokens[i+1]=x
        elif isinstance(tokens[i-1],int) and is_letter(tokens[i+1]):
            if global_varlist[ord(tokens[i+1])-ord('a')]:
                result=tokens[i+1]=evaluate(int(tokens[i-1]),tokens[i],global_varlist[ord(tokens[i+1])-ord('a')])
            else:
                return "invalid string"
        elif is_letter(tokens[i-1]) and isinstance(tokens[i+1],int):
            if global_varlist[ord(tokens[i-1])-ord('a')]:
                result=tokens[i+1]=evaluate(global_varlist[ord(tokens[i-1])-ord('a')],tokens[i],int(tokens[i+1]))
            else:
                return "invalid string"
        elif is_letter(tokens[i-1]) and is_letter(tokens[i+1]):
            if global_varlist[ord(tokens[i-1])-ord('a')] and global_varlist[ord(tokens[i+1])-ord('a')]:
                result=tokens[i+1]=evaluate(global_varlist[ord(tokens[i-1])-ord('a')],tokens[i],global_varlist[ord(tokens[i+1])-ord('a')])
            else:
                return "invalid string"
        else:
            return "invalid string"
        i=i+2
  global_varlist[ord(tokens[0])-ord('a')]=result
  return global_varlist

def syntax_checker(tokens):
    if len(tokens)%2==0 or len(tokens)==1:
      return "invalid string"
    if is_letter(tokens[0]):
        if tokens[1]=='=':
            if is_letter(tokens[2]) or isinstance(tokens[2],int):
                flag=0
                i=3
                while(i+1<=len(tokens)):
                    if is_operator(tokens[i]):
                        if isinstance(tokens[i+1],int) or is_letter(tokens[i+1]):
                            i+=2
                        else:
                            flag=1
                    else:
                        flag=1
                        break
            else:
                flag = 1
            if flag == 0:
                    return "valid string"
            else:
                    return "invalid string"
    return "invalid string"
if __name__=="__main__":
    inp=raw_input("enter an expression\n")
    while True:
        l=tokenizer(inp)
        flag1=syntax_checker(l)
        if flag1!="invalid string":
            flag2=evaluator(l)
            if flag2=="invalid string":
                print flag2
                break
        else:
            break
        i=0
        for i in range(0,26) :
            if global_varlist[i]!=False:
                print chr(i+97),"=",global_varlist[i]
                i+=1
        if raw_input("\ndo you want to continue?\n")=='yes':
            inp=raw_input('enter an expression\n')
            continue
        else:
            break
