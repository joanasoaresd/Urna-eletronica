import gravadoreleitores


sair = False
eleitores = gravadoreleitores.recuperaEleitores()
candidatos = gravadoreleitores.recuperaCandidatos()
while (not sair):
    print("___________________________________________________________________\n"
          "|                         URNA ELETRÔNICA                         |\n"
          "|_________________________________________________________________|")
    opcao = input("|                Digite o número da opção desejada:               |\n"
                  "|_________________________________________________________________|\n"
                  "|           1.Cadastrar Eleitor                                   |\n"
                  "|           2.Listar Eleitores                                    |\n"
                  "|           3.Alterar Dados do eleitor                            |\n"
                  "|           4.Cadastrar Candidato                                 |\n"
                  "|           5.Listar Candidatos                                   |\n"
                  "|           6.Alterar Candidato                                   |\n"
                  "|           7.Registrar Voto                                      |\n"
                  "|           8.Consultar votos obtidos por candidato               |\n"
                  "|           9.Consultar n° de eleitores que já votaram            |\n"
                  "|           10.Consultar n° de eleitores que ainda não votaram    |\n"
                  "|           11.Sair                                               |\n"
                  "|_________________________________________________________________|\n")

    if (opcao == "1"):
        gravadoreleitores.cadastroEleitor(eleitores)
        gravadoreleitores.graveEleitores(eleitores)
        gravadoreleitores.graveCandidatos(candidatos)

    elif (opcao == "2"):
        gravadoreleitores.listarEleitores(eleitores)
        gravadoreleitores.graveEleitores(eleitores)
        gravadoreleitores.graveCandidatos(candidatos)

    elif (opcao == "3"):
        gravadoreleitores.alterarEleitor(eleitores)
        gravadoreleitores.graveEleitores(eleitores)
        gravadoreleitores.graveCandidatos(candidatos)

    elif (opcao == "4"):
        gravadoreleitores.cadastrarCandidato(candidatos)
        gravadoreleitores.graveCandidatos(candidatos)

    elif (opcao == "5"):
        gravadoreleitores.listarCandidatos(candidatos)

    elif (opcao == "6"):
        gravadoreleitores.alterarCandidato(candidatos)
        gravadoreleitores.graveCandidatos(candidatos)

    elif (opcao == "7"):
        gravadoreleitores.registrarVoto(eleitores, candidatos)
        gravadoreleitores.graveEleitores(eleitores)
        gravadoreleitores.graveCandidatos(candidatos)

    elif (opcao == "8"):
        gravadoreleitores.consultarVotos(candidatos)
        gravadoreleitores.graveEleitores(eleitores)
        gravadoreleitores.graveCandidatos(candidatos)

    elif (opcao == "9"):
        gravadoreleitores.consultarEleitVotaram(eleitores)
        gravadoreleitores.graveEleitores(eleitores)
        gravadoreleitores.graveCandidatos(candidatos)

    elif (opcao == "10"):
        gravadoreleitores.consutarEleitNVotaram(eleitores)
        gravadoreleitores.graveEleitores(eleitores)
        gravadoreleitores.graveCandidatos(candidatos)

    elif (opcao == "11"):
        gravadoreleitores.graveEleitores(eleitores)
        gravadoreleitores.graveCandidatos(candidatos)
        print("FIM!")
        break
    else:
        print("Operação não existente!")
