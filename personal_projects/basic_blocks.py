__author__ = 'chaithra'
"""
this program is to partition the given set of statements into basic blocks.
each basic block is a statement or set of statements that are executed sequentially without any branching or jumping in to other statements.
each basic block has some entry and exit conditions. if control enters a basic block, it comes out only after all the statements in it are executed.
"""

#specifications:
"""
1. since the basic blocks partition is done after the syntax and semantic analysis phases,
it is assumed that inputs given are syntactically and semantically correct.
2. the partition is done assuming that only if, else and while conditions are given.
"""




#----------takes input and returns set of statements in the form of a list--------------------#
def take_input():
    stmnt_list=[]
    while True:
        input=remove_spaces(raw_input('enter the statement:\n'))
        if input=="end":
            break
        stmnt_list.append(input)
    return stmnt_list
#----------function to partition the given set of statements in to basic blocks----------------#
#----------it takes the list of statements given as input and divides them into blocks---------#

def block_partition(stmnt_list):
    blocks={}# a dictionary which maps the block number with the corresponding list of statements present in that block
    dependency_list=[]
    count=0
    list_index=0
    l=len(stmnt_list)
    while list_index<l:
        if 'if' in stmnt_list[list_index] or 'else' in stmnt_list[list_index] or 'while' in stmnt_list[list_index]:
            if 'else' in stmnt_list[list_index]:
                list_index+=1
                dependency_list.append("block"+str(count-1)+"----->block"+str(count+1))
                count+=1
                blocks[count]=[]
                blocks[count].append(stmnt_list[list_index])
                list_index+=1
                continue
            else:
                count+=1
                dependency_list.append("block"+str(count)+"----->block"+str(count+1))
                blocks[count]=[]
                if 'if' in stmnt_list[list_index]:
                    blocks[count].append(stmnt_list[list_index][2:])
                    list_index+=1
                    count+=1
                    blocks[count]=[]
                    blocks[count].append(stmnt_list[list_index])
                    list_index+=1
                else:
                    blocks[count].append(stmnt_list[list_index][5:])
                    list_index+=1
                    count+=1
                    blocks[count]=[]
                    blocks[count].append(stmnt_list[list_index])
                    list_index+=1
                    blocks[count].append(stmnt_list[list_index])
                    list_index+=1
        else:
            count+=1
            blocks[count]=[]
            while list_index<l and 'if' not in stmnt_list[list_index] and 'else' not in stmnt_list[list_index] and 'while' not in stmnt_list[list_index]:
                blocks[count].append(stmnt_list[list_index])
                list_index+=1
    return blocks,dependency_list

#------------------prints the blocks obtained--------------------------#

def print_blocks(blocks):
    for i in range(1,len(blocks)+1):
        print '---------------------------'
        print "       block",i,'\n'
        for j in range(0,len(blocks[i])):
            print blocks[i][j],'\n'
        print '---------------------------'

def remove_spaces(input_str):
    list_str=list(input_str)
    read_ptr=0
    write_ptr=0
    for i in range(len(list_str)):
        if list_str[read_ptr]==' ':
            read_ptr+=1
        else:
            list_str[write_ptr]=list_str[read_ptr]
            write_ptr+=1
            read_ptr+=1
    return "".join(list_str[:write_ptr])

def main():
    #-----take input on console-----#
    #stmts = take_input()
    #-----static input--------------#
    stmts=['a=10','b=20','ifa<b','a=30','else','a=40','b=30','c=50','while i<20','a+=1','i+=1','d=a+b']
    blocks,dependency_list = block_partition(stmts)
    print_blocks(blocks)
    print "dependency list:"
    for i in (dependency_list):
        print i,'\n'
if __name__=='__main__':
    main()
