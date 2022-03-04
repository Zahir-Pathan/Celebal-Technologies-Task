'''
Problem Statement
Write a python function, check_anagram() which accepts two strings and returns True, if one string is a special anagram of another string. Otherwise returns False.

The two strings are considered to be a special anagram if they contain repeating characters but none of the characters repeat at the same position. The length of the strings should be the same.

Note: Perform case insensitive comparison wherever applicable.

Sample Input

Expected Output

eat, tea

True

backward,drawback

False 
(Reason: character 'a' repeats at position 6, not an anagram)

Reductions,discounter

True

About, table

False

 
'''
#lex_auth_0127382206342184961397

def check_anagram(data1,data2):
    #start writing your code here
    list1=[]
    list2=[]
    d1=data1.lower()
    d2=data2.lower()
    for ele in d1:
        list1.append(ele)
    for elem in d2:
        list2.append(elem)
    for a in list1:
        for b in list2:
            if a==b:
                i=a.index()
                j=b.index()
                
                if i==j:
                     return False
                else:
                    return True
                    
            else:
                return False
    

print(check_anagram("eat","tea"))