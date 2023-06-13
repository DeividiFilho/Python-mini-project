def ler_notas_arquivo():
    notas = []
    
    try:
        arquivo = open("notas_AP2S2.txt", "r")
        for linha in arquivo:
            nota = float(linha.strip())
            notas.append(nota)
        arquivo.close()
    except IOError:
        print("Erro ao ler o arquivo de notas.")
    
    return notas

def calcular_media_geral(notas):
    quantidade_alunos = len(notas)
    soma_notas = sum(notas)
    media_geral = soma_notas / quantidade_alunos if quantidade_alunos > 0 else 0
    
    return media_geral

def calcular_porcentagem_aprovados(notas):
    quantidade_aprovados = sum(1 for nota in notas if nota >= 6.0)
    porcentagem_aprovados = (quantidade_aprovados / len(notas)) * 100 if len(notas) > 0 else 0
    
    return porcentagem_aprovados

def calcular_porcentagem_reprovados(notas):
    quantidade_reprovados = sum(1 for nota in notas if nota < 4.0)
    porcentagem_reprovados = (quantidade_reprovados / len(notas)) * 100 if len(notas) > 0 else 0
    
    return porcentagem_reprovados

def calcular_porcentagem_ifs(notas):
    quantidade_ifs = sum(1 for nota in notas if 4.0 <= nota <= 5.9)
    porcentagem_ifs = (quantidade_ifs / len(notas)) * 100 if len(notas) > 0 else 0
    
    return porcentagem_ifs

def main():
    notas = ler_notas_arquivo()
    media_geral = calcular_media_geral(notas)
    porcentagem_aprovados = calcular_porcentagem_aprovados(notas)
    porcentagem_reprovados = calcular_porcentagem_reprovados(notas)
    porcentagem_ifs = calcular_porcentagem_ifs(notas)
    
    print("Média geral da turma:", media_geral)
    print("Porcentagem de alunos aprovados:", porcentagem_aprovados)
    print("Porcentagem de alunos reprovados:", porcentagem_reprovados)
    print("Porcentagem de alunos que farão IFS:", porcentagem_ifs)

if __name__ == "__main__":
    main()
