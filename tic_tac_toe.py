jogo = {
    1: ["X","O","O"],
    2: ["O","X","O"],
    3: ["O","O","X"]
}

def condição_vitória(matriz:dict)->str:

    if matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X":
        return "X é o vencedor!"
    elif matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X":
        return "X é o vencedor!"
    elif matriz[3][0] == "X" and matriz[3][1] == "X" and matriz[3][2] == "X":
        return "X é o vencedor!"
    elif matriz[1][0] == "X" and matriz[2][0] == "X" and matriz[3][0] == "X":
        return "X é o vencedor!"
    elif matriz[1][1] == "X" and matriz[2][1] == "X" and matriz[3][1] == "X":
        return "X é o vencedor!"
    elif matriz[1][2] == "X" and matriz[2][2] == "X" and matriz[3][2] == "X":
        return "X é o vencedor!"
    elif matriz[1][0] == "X" and matriz[2][1] == "X" and matriz[3][2] == "X":
        return "X é o vencedor!"
    elif matriz[3][0] == "X" and matriz[2][1] == "X" and matriz[1][2] == "X":
        return "X é o vencedor!"
    elif matriz[3][0] == "O" and matriz[2][1] == "O" and matriz[1][2] == "O":
        return "O é o vencedor!"
    elif matriz[1][0] == "O" and matriz[2][1] == "O" and matriz[3][2] == "O":
        return "O é o vencedor!"
    elif matriz[1][2] == "O" and matriz[2][2] == "O" and matriz[3][2] == "O":
        return "O é o vencedor!"
    elif matriz[1][1] == "O" and matriz[2][1] == "O" and matriz[3][1] == "O":
        return "O é o vencedor!"
    elif matriz[1][0] == "O" and matriz[2][0] == "O" and matriz[3][0] == "O":
        return "O é o vencedor!"
    elif matriz[3][0] == "O" and matriz[3][1] == "O" and matriz[3][2] == "O":
        return "O é o vencedor!"
    elif matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O":
        return "O é o vencedor!"
    elif matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O":
        return "O é o vencedor!"
    else:
        return "Empate!"

print(condição_vitória(jogo))