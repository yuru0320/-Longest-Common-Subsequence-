
#

from pickletools import string1


def LCS( X, Y):
    UPPERLEFT = 1
    UP = 2
    LEFT = 3
    c = [ [ 0 for j in range( 0, len(Y) + 1 ) ] for i in range( 0, len(X) + 1 ) ]
    b = [ [ 0 for j in range( 0, len(Y) + 1 ) ] for i in range( 0, len(X) + 1 ) ]
    for i in range (1, len(X)+1):
        c[i][0] = 0
    for j in range (1, len(Y)+1):
        c[0][j] = 0
    
    for i in range( 1, len(X) + 1 ):
        for j in range( 1, len(Y) + 1 ):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j]  = UPPERLEFT
            else:
                if c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = UP
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = LEFT
    
    i = len(X)
    j = len(Y)
    result = ""
    while i != 0 and j != 0:  
        if b[i][j] == UPPERLEFT:
            result = str( list1[i - 1] ) + result
            i -= 1
            j -= 1
        elif b[i][j] == UP:
            i -= 1
        else:
            j -= 1
    return result

count = 0
while 1 :
    num1, num2 = map(int,input().split())
    if num1 == 0 and num2 == 0 :
           break
    while (num1 < 1  or  num1 >100 ) or (num2 < 1 or  num2 >100 ) :
            print("數字過大，請重新輸入：")
            num1, num2 = map(int,input().split())
    if num1 == 0 and num2 == 0 :
        print("END")
        break
    count+=1

    input_list1 = map(str, input().split()) 
    input_list2 = map(str, input().split()) 
    list1 = [str(i) for i in input_list1 ] # 原始
    list2 = [str(i) for i in input_list2 ] # 原始
    str1 = ""
    str2 = ""
    for j in list1:
        str1 += str(j)  
    for k in list2:
        str2 += str(k)
    print(str1)
    flist1 = False
    flist2 = False
    flist1 = str1.isalpha()
    flist2 = str2.isalpha()
    if not flist1 or not flist2 : 
        print("有非字母，請重新輸入")
        break
    Upper1_list = list(map(str.upper,list1 )) # 大寫
    Upper2_list = list(map(str.upper,list2 )) # 大寫
    #print(num1 ,num2, len(list1),len(list2), len(Upper1_list),len(Upper2_list)  )
    if len(list1) != num1 or len(list2) != num2 : 
        print("Input size ERROR !!")
        break
    result = LCS( Upper1_list, Upper2_list )
    print("Case #",count)
    print("Lenght of LCS = ",len(result))
    print("LCS = ",result)

    
    
