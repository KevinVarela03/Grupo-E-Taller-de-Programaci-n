def ex2(f1,f2,f3):
        if (f1 == 111) or (f2 == 111) or (f3 == 111):
                result = "Ganan las x"
        elif (f1 == 000) or (f2 == 000) or (f3 == 000) :
                result = "Ganan las O"
        elif(f1%10 == 0) and (f2%10 == 0) and (f2%10 == 0):
                result = "Ganan las O"
        elif (f1 == 10) or (f2 == 10) or (f3 == 10):
                result = "Ganan las x"
        elif (f1 == 1) or (f2 == 1) or (f3 == 1):
                result = "Ganan las x"
        else:
                result = "Empate"
       
        return result



print(ex2(111,10,111))