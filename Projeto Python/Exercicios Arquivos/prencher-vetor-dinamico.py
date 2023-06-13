def preencher_vetor_medias():
    vetor_medias = []

    while True:
        media = input("Digite a média semestral do aluno (ou 'sair' para encerrar): ")
        
        if media.lower() == 'sair':
            break
        
        try:
            media = float(media)
            vetor_medias.append(media)
        except ValueError:
            print("Valor inválido. Digite um número válido ou 'sair' para encerrar.")

    return vetor_medias

def gravar_notas_arquivo(vetor_medias):
    try:
        arquivo = open("notas_AP2S2.txt", "w")
        for media in vetor_medias:
            arquivo.write(str(media) + '\n')
        arquivo.close()
        print("Notas gravadas no arquivo 'notas_AP2S2.txt'.")
    except IOError:
        print("Erro ao gravar as notas no arquivo.")

def main():
    vetor_medias = preencher_vetor_medias()
    gravar_notas_arquivo(vetor_medias)

if __name__ == '__main__':
    main()
