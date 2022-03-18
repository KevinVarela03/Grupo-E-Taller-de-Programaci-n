def cifrado(num):
    suma = 0
    nuevo_dig = 0
    nuevo_cifrado = num
    num_final = 0
    num_final_2 = 0
    num_cifrado = 0
    num_final_3 = 0
    num_desc = num
    num_desc2 = 0

    while num > 0:
        dig = num%10
        num = num//10
        suma = suma + dig
    print(suma)

    while suma > 10:
        dig = suma%10
        nuevo_dig = dig
        suma = suma//10
    print(nuevo_dig)

    while nuevo_cifrado > 0:
        dig = nuevo_cifrado%10
        dig = dig + nuevo_dig
        nuevo_cifrado = nuevo_cifrado//10
        if dig >= 10:
            dig = dig%10
            num_final = (num_final*10) +dig
        elif dig <=9: 
            num_final = (num_final*10) + dig
    while num_final > 0:
        dig = num_final%10
        num_final = num_final//10
        num_final_2 = (num_final_2*10) + dig
        num_cifrado = (num_final_2*10) + nuevo_dig
    print(num_final_2)
    
    nuevo_num_desc = 0
    num_final_def = 0
    while num_final_2 > 0:
        dig = num_final_2%10
        num_desc = (dig*10) + 1
        num_final_2 = num_final_2//10
        num_desc2 = 0
        while num_desc > 0:
            dig2 = num_desc%10
            num_desc = num_desc//10
            num_desc2 = (num_desc2*10) + dig2
        num_final = num_desc2 - nuevo_dig
        num_final_def = (num_final_def*10) + num_final

    num_final_def2 = 0
    while num_final_def > 0:
        dig = num_final_def%10
        num_final_def2 = (num_final_def2*10) + dig
        num_final_def = num_final_def//10
    print(num_final_def2)
    
cifrado(12345)