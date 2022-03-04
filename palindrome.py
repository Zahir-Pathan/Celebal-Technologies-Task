#lex_auth_012693819159732224162

def check_palindrome(word):
    data=[]
    for ele in word:
        data.append(ele)
    data_new=[]
    for i in range(0,len(data)):
        n=len(data)-i-1
        data_new.append(data[n])
    new_word="".join(data_new) 
    if word==new_word:
        return True
    else:
        return False
        
        
        #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")