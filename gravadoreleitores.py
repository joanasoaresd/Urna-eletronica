import os
from pygame import mixer


def graveEleitores(eleitores):
    arqEleitores = open("eleitores.txt", 'w')
    for e in eleitores:
        arqEleitores.write("%s;%s;%s\n" % (e[0], e[1], e[2]))
    arqEleitores.close()


def recuperaEleitores():
    eleitores = []
    if (os.path.exists("eleitores.txt")):
        arqEleitores = open("eleitores.txt", 'r')
        for linha in arqEleitores:
            eleitor = linha.strip().split(";")
            eleitores.append(eleitor)
        arqEleitores.close()
    return eleitores


def graveCandidatos(candidatos):
    arqCandidatos = open("candidatos.txt", 'w')
    for c in candidatos:
        arqCandidatos.write("%s;%s;%s;%s\n" % (c[0], c[1], c[2], c[3]))
    arqCandidatos.close()


def recuperaCandidatos():
    candidatos = []
    if (os.path.exists("candidatos.txt")):
        arqCandidatos = open("candidatos.txt", 'r')
        for linha in arqCandidatos:
            candidato = linha.strip().split(";")
            candidatos.append(candidato)
        arqCandidatos.close()
    return candidatos


def cadastroEleitor(eleitores):
    nome = input("Informe o nome:\n").upper()
    matr = input("Informe a matricula:\n")
    eleitores.append([nome, matr, "Não Votou"])
    print("ELEITOR CADASTRADO COM SUCESSO!")


def listarEleitores(eleitores):
    print("___________________________________________________________________\n"
          "                       LISTA DE ELEITORES                          \n"
          "___________________________________________________________________")
    for e in eleitores:
        print("Nome:", e[0])
        print("Matricula:", e[1], "\n")


def cadastrarCandidato(candidatos):
    nomeC = input("Informe o nome do candidato:\n").upper()
    num = input("Informe o número do candidato:\n")
    vice = input("Informe o nome do vice candidato:\n").upper()
    voto = 0
    candidatos.append([nomeC, num, vice, voto])
    print("CANDIDATO CADASTRADO COM SUCESSO!")


def listarCandidatos(candidatos):
    print("___________________________________________________________________\n"
          "                       LISTA DE CANDIDATOS                         \n"
          "___________________________________________________________________")
    for c in candidatos:
        print("Canditado:", c[0])
        print("Número do Candidato:", c[1])
        print("Vice:", c[2], "\n")


def alterarEleitor(eleitores):
    print("___________________________________________________________________\n"
          "                       ALTERAR DADOS DO ELEITOR                    \n"
          "___________________________________________________________________")
    dados = input("Informe a matricula para efetuar a alteração\n")
    for e in eleitores:
        if dados == e[1]:
            del e[0]
            nome = input("Informe o nome para alteração:\n").upper()
            e.insert(0, nome)
            del e[1]
            matr = input("Informe a matricula para alteração:\n")
            e.insert(1, matr)
            print("ALTERAÇÃO CONCLUÍDA COM SUCESSO!")


def alterarCandidato(candidatos):
    print("___________________________________________________________________\n"
          "                    ALTERAR DADOS DO CANDIDATO                     \n"
          "___________________________________________________________________")
    perg = input("Você tem certeza que quer efetuar esta operação?\n"
                 "1.Sim\n2.Não\n").upper()
    if (perg == "SIM" or perg == "1"):
        dados = input("Informe o Número do candidato para efetuar a alteração\n")
        for c in candidatos:
            if dados == c[1]:
                del c[0]
                nomeC = input("Confirme o nome do candidato\n").upper()
                c.insert(0, nomeC)
                del c[1]
                num = input("Confirme o número do candidato\n")
                c.insert(1, num)
                del c[2]
                vice = input("Confirme o vice candidato\n").upper()
                c.insert(2, vice)
                print("ALTERAÇÃO CONCLUÍDA COM SUCESSO!")
    else:
        print("OPERAÇÃO CANCELADA X")


def registrarVoto(eleitores, candidatos):
    print("___________________________________________________________________\n"
          "                      VOTAÇÃO PRESIDENTE                           \n"
          "___________________________________________________________________")

    informe = input("Digite o número da sua matricula:\n")
    for i in eleitores:
        if informe == i[1]:
            a = input("Informe dois números para efetuar sua votação para presidente:\n")
            p = input("1.Confirmar\n2.Cancelar\n").upper()
            if (p == "1" or p == "CONFIRMAR"):
                del i[2]
                novo = "Votou"
                i.insert(2, novo)
                for c in candidatos:
                    if a == c[1]:
                        voto = int(c[3])
                        voto += 1
                        c.insert(3, voto)
                        print("VOTO CADASTRADO COM SUCESSO!")
                        mixer.init()
                        mixer.music.load("somUrna.mp3")
                        mixer.music.play()
            else:
                print("OPERAÇÃO CANCELADA X")


def consultarVotos(candidatos):
    print("___________________________________________________________________\n"
          "                      VOTOS OBTIDOS POR CANDIDATO                  \n"
          "___________________________________________________________________")
    p = input("Digite o número do candidato: \n")
    for c in candidatos:
        if p == c[1]:
            print("CANDIDATO:", c[0], "\nVotos:", c[3])


def consultarEleitVotaram(eleitores):
    print("___________________________________________________________________\n"
          "                     NÚMERO DE ELEITORES QUE JÁ VOTARAM           \n"
          "___________________________________________________________________")
    cont = 0
    for el in eleitores:
        if el[2] == "Votou":
            cont += 1
    print(cont, "eleitores já votaram")


def consutarEleitNVotaram(eleitores):
    print("___________________________________________________________________\n"
          "                NÚMERO DE ELEITORES QUE NÃO VOTARAM               \n"
          "___________________________________________________________________")
    cont = 0
    for el in eleitores:
        if el[2] == "Não Votou":
            cont += 1
    print(cont, "eleitores não votaram")
