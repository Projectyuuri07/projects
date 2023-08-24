from classes import*

while True:
    x = 1
    try:
        print("-------------------------------------------------------------- \n\n Bem-vindo ao Text-RPG! \n\n -------------------------------------------------------------- \n\n")
        jogador = int(input("Escolha um personagem: \n [1] Guerreiro \n [2] Mago \n [3] Sair \nSua escolha: "))
        match jogador:
            case 1:
                jogador = Guerreiro()
                print("Guerreiro selecionado! Menor poder e mais defesa.")
                print ("O guerreiro possui 13 de vida e 8 de dano. \n Além disso, o guerreiro pode utilizar de sua grande habilidade com o escudo quando um perigo eminente o ameaçar.")
                os.system("pause")
                os.system("cls")
                x = 2

            case 2:
                jogador = Mago()
                print("Mago selecionado! Maior poder e menos defesa.")
                print("O mago possui 7 de vida e 13 de dano. \n Além disso, o mago possui uma habilidade de longo alcance que é ativada quando um grande perigo espreita.")
                os.system("pause")
                os.system("cls")
                x = 2

            case 3:
                break
        
    except Exception as erro:
        print("Opção selecionada inválida!")
        os.system("pause")
        os.system("cls")
        
    while x == 2:
        try:
            print('O reino enfrenta uma terrível praga que ameaça a todos. A única esperança é uma poção mágica escondida nas profundezas da masmorra.')
            espera()
            print('O Conselho dos Sábios revela que uma poção mágica pode curar a praga, mas está escondida em uma caverna perigosa.')
            espera()
            print('Você é um aventureiro que se ofereceu para entrar na caverna e trazer a poção para salvar o reino.')
            espera()
            print("O herói adentra a caverna e acaba se perdendo em meio a escuridão, e acaba colidindo contra uma rocha, caindo no chão e ficando desacordado.")
            espera()
            print("Você acorda sozinho na caverna, e escuta inimigos a espreita...")
            escolha1 = int(input("[1] Fugir da caverna \n[2] Explorar \nSua escolha: "))
            match escolha1:
                case 1:
                    print("Fugiu do local!")
                    os.system("pause")
                    os.system("cls")
                    x = 0 

                case 2:
                    try:
                        os.system("cls")
                        while True:
                            print("Você adentra a caverna e... ENCONTRA UM INIMIGO!")
                            ação = int(input("[1] Lutar \n[2] Fugir \nSua escolha: "))
                            match ação:
                                case 1:
                                    inimigo = Ini_fraco()
                                    print("Você inicia o combate. \n")
                                    print(f"Você ataca o inimigo, causando {jogador.dano()} de dano!\n")
                                    if jogador.dano() > inimigo.vida_inimigo():
                                        print("Você eliminou o inimigo! Parabéns! O reino todo contará suas épicas histórias!")
                                        os.system("pause")
                                        os.system("cls")
                                        x = 0
                                        break

                                    else:
                                        print("Você morreu! :(")
                                        os.system("pause")
                                        os.system("cls")
                                        x = 0
                                        break


                                case 2:
                                    inimigo = Ini_forte()
                                    print("Você foi pego de surpresa por um inimigo formidável!. Sua única opção é lutar. \n\n ")

                                    if isinstance(jogador, Mago):
                                        print("Você conjura uma magia de longo alcance para se defender!")
                                        if (jogador.longo_alcance()) + (jogador.dano()) > inimigo.vida():
                                            print("Você conjura uma magia sombria que garante sua vitória! O reino todo contará as épicas histórias do Mago Sombrio do Rei!")
                                            os.system("pause")
                                            os.system("cls")
                                            x = 0
                                            break

                                    elif isinstance (jogador, Guerreiro):
                                        print("Você ergue seu escudo para se defender!")
                                        if jogador.defesa() > inimigo.dano():
                                            print("Você se defende e enfrenta o inimigo, assim matando-o! Parabéns! O reino todo contará as épicas histórias do Grande Escudo do Rei!")
                                            os.system("pause")
                                            os.system("cls")
                                            x = 0
                                            break

                                    elif jogador.dano() > inimigo.vida_inimigo():
                                        print("Você eliminou o inimigo! Parabéns!")
                                        os.system("pause")
                                        os.system("cls")
                                        x = 0
                                        break
                                            
                                    else:
                                        print("Você morreu! :(")
                                        os.system("pause")
                                        os.system("cls")
                                        x = 0
                                        break

                    except Exception as erro:
                        print("Opção selecionada inválida!")
                        os.system("pause")
                        os.system("cls")               

        except Exception as erro:
            print("Opção selecionada inválida!")
            os.system("pause")
            os.system("cls") 
    while x == 0:
        break