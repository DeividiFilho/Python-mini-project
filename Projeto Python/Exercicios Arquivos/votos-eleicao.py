def calcular_votos_por_candidato(arquivo):
    votos = {
        100: 0,
        200: 0,
        300: 0,
        400: 0,
        500: 0
    }

    with open(arquivo, 'r') as f:
        for linha in f:
            codigo = int(linha.strip())
            if codigo in votos:
                votos[codigo] += 1

    return votos


def calcular_votos_candidato_mais_votado(votos):
    max_votos = max(votos.values())
    candidatos_mais_votados = [candidato for candidato, num_votos in votos.items() if num_votos == max_votos]
    return candidatos_mais_votados, max_votos


def calcular_votos_candidato_menos_votado(votos):
    min_votos = min(votos.values())
    candidatos_menos_votados = [candidato for candidato, num_votos in votos.items() if num_votos == min_votos]
    return candidatos_menos_votados, min_votos


def calcular_votos_nulos(votos):
    total_votos_nulos = sum(votos.values())
    total_votos_validos = len(votos) - votos[0]
    return total_votos_validos, total_votos_nulos


def main():
    arquivo_votos = 'votos.txt'

    votos_por_candidato = calcular_votos_por_candidato(arquivo_votos)
    print("Quantidade de votos por candidato:")
    for candidato, num_votos in votos_por_candidato.items():
        print(f"Candidato {candidato}: {num_votos}")

    candidatos_mais_votados, max_votos = calcular_votos_candidato_mais_votado(votos_por_candidato)
    print("\nCandidatos mais votados:")
    for candidato in candidatos_mais_votados:
        print(f"Candidato {candidato}: {max_votos} votos")

    candidatos_menos_votados, min_votos = calcular_votos_candidato_menos_votado(votos_por_candidato)
    print("\nCandidatos menos votados:")
    for candidato in candidatos_menos_votados:
        print(f"Candidato {candidato}: {min_votos} votos")

    total_votos_validos, total_votos_nulos = calcular_votos_nulos(votos_por_candidato)
    print("\nResultado dos votos:")
    print(f"Total de votos válidos: {total_votos_validos}")
    print(f"Total de votos nulos: {total_votos_nulos}")


if __name__ == '__main__':
    main()
