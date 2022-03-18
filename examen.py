# Anios cumplidos desde una fecha A hasta una fecha B
# PSEUDOCODIGO
# La idea es ir dividiendo entre 100 (fecha % 100) para ir sacando el dia, mes y anio. despues se restan los dias con dias, meses con meses, etc y para el resultado solo se imprime el resultado de las operaciones.
def anios_cumplidos(fecha_1,fecha_2):
    dia_1 = fecha_1 % 100
    dia_2 = fecha_2 % 100
    fecha_1 = fecha_1 // 100
    mes_1 = fecha_1 % 100
    mes_2 = fecha_2 % 100
    fecha_1 = fecha_1 // 100
    fecha_2 = fecha_2 // 100
    anio_1 = fecha_1
    anio_2 = fecha_2
    print(dia_1)
    print(mes_1)
    print(anio_1)
    if dia_1 > dia_2:
        dia = dia_1 - dia_2
        print(dia)
    else:
        dia = dia_2 - dia_1
    if mes_1 > mes_2:
        mes = 12 - mes_1
        print(mes)
    else:
        mes = 12 - mes_2
        print(mes)
    anio = anio_1 - anio_2
    print(anio)
    print(anio, mes, dia)

print(anios_cumplidos(19810807,20220314))
