def Calcular_salario(qt_horas:int, vl_hora:float)->float:
    if qt_horas <= 40:
        return qt_horas * vl_hora
    else:
        return 40*vl_hora + (qt_horas-40)*vl_hora*1.5
