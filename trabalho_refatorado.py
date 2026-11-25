jogos = []
#jogos = ["GTA", "GTA 2", "GTA 3", "GTA 4", "GTA 5", "GTA 6"]

print("=== CÁTALAGO DE JOGOS ===")

opc = int(input(" 1- Adicionar jogo\n 2- Visualizar catálogo\n 3- Ver quantidade de jogos\n 4- Verificar se um jogo está no catálogo\n 5- Remover jogo\n 0- Sair\n >: "))

while True:
    match opc:
        case 1:
            nome_jogo = input("Digite o nome do jogo: ").upper()
            if nome_jogo not in jogos:
                jogos.append(nome_jogo)
                print("=" * 30)
                print(f"{nome_jogo} adicionado com sucesso!.")
                print("=" * 30)
            else:
                print("=" * 30)
                print(f"{nome_jogo} foi adicionado anteriormente")    
                print("=" * 30)        
        case 2:
            if len(jogos) == 0:
                print("=" * 30)                
                print("Não há jogos cadastrados.")
                print("=" * 30)
            else:
                print("=" * 80)
                print(f"JOGOS CADASTRADOS: {jogos}")
                print("=" * 80)    
        case 3:
            print("=" * 30)
            print(f"SEU CATÁLOGO POSSUI {len(jogos)} jogo(s).")
            print("=" * 30)
        case 4:
            print("=" * 30)
            nome_jogo = input("Digite o nome do jogo: ").upper()
            print("=" * 30)
            if nome_jogo in jogos:
                print("=" * 30)
                print(f"{nome_jogo} foi encontrado na lista.")
                print("=" * 30)
            else:            
                print("=" * 30)
                print(f"{nome_jogo} não está na lista.")
                print("=" * 30)           
        case 5:
            print("=" * 30)
            nome_jogo = input("Digite o nome do jogo que deseja remover: ").upper()
            print("=" * 30)
            if nome_jogo in jogos:
                jogos.remove(nome_jogo)
                print("=" * 30)
                print(f"{nome_jogo} removido com sucesso!")
                print("=" * 30)
            else:            
                print("=" * 30)
                print(f"{nome_jogo} não foi encontrado.")
                print("=" * 30)       
        case 0:
            break
        case _:
            print("=" * 30)
            print("Opção inválida, tente novamente.")
            print("=" * 30)
    opc = int(input(" 1- Adicionar jogo\n 2- Visualizar catálogo\n 3- Ver quantidade de jogos\n 4- Verificar se um jogo está no catálogo\n 5- Remover jogo\n 0- Sair\n >: "))
print("Programa encerrado")                                