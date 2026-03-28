def verificar_string(A:str,B:str)->bool:
    for i in range(len(A)):
        j = 0
        while j < len(B) and A[i+j] == B[j]:
            j +=1
        if j == len(B):
            return True
    return False