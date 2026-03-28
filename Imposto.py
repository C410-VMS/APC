def Calcular_imposto(pagamento:float)->int:
    if pagamento > 5000:
        imposto = pagamento * 0.27
    else:
        imposto = 0
    return imposto
