#lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    data_list=[]
    

    if(num1<num2):
        
        for ele in range(num1,num2+1):
            sum=0
            a=ele
            
            while(a!=0):
                r=a%10
                sum += r
                a = a // 10
                
            if sum % 3 == 0 and ele % 5 == 0:
                if ele>9 and ele<100:
                    data_list.append(ele)
                    
            
    else:
        return max_num
        
    if len(data_list)>0:
        return data_list[max_num]
    else:
        return max_num
    
    
    

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)