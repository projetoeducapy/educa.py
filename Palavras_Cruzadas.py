import pygame, sys
from pygame.locals import *
from time import sleep
import educa

pygame.init()

Size = [850, 600]
Fundo = pygame.display.set_mode(Size)
pygame.display.set_caption('Palavras Cruzadas')

def Inicio():
    pygame.mixer.init()
    Audio_Escolha = pygame.mixer.Sound('audios/cruzadas/DingBop.ogg')
    Screen = pygame.image.load('imagens/cruzadas/Fundos/Fundo.jpg')
    SAIR = True
    
    while(SAIR):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                SAIR = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == True:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if (x > 10 and x < 40 and y > 10 and y < 40):
                            Audio_Escolha.play()
                            educa.telajogos()
                        if(x > 190 and x < 340 and y > 310 and y < 350):
                            Audio_Escolha.play()
                            Inicio2()
                        if(x > 175 and x < 425 and y > 465 and y < 515):
                            Audio_Escolha.play()
                            Instrucoes()
                        
        pygame.time.Clock().tick(30)
        Fundo.blit(Screen, (0, 0))        
        pygame.display.update()

def Inicio2():
    pygame.mixer.init()
    Audio_Escolha = pygame.mixer.Sound('audios/cruzadas/DingBop.ogg')
    global ESCOLHA_DIFICULDADE
    Screen = pygame.image.load('imagens/cruzadas/Fundos/Fundo2.jpg')
    SAIR = True
    
    while(SAIR):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                SAIR = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == True:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if (x > 10 and x < 40 and y > 10 and y < 40):
                            Audio_Escolha.play()
                            Inicio()
                        if(x > 175 and x < 425 and y > 465 and y < 515):
                            Audio_Escolha.play()
                            Instrucoes()
                        if(x > 260 and x < 355 and y > 355 and y < 445):
                            if(x > 260 and x < 355 and y > 355 and y < 375):
                                Audio_Escolha.play()
                                ESCOLHA_DIFICULDADE = 'FACIL'
                            if(x > 260 and x < 355 and y > 385 and y < 410):
                                Audio_Escolha.play()
                                ESCOLHA_DIFICULDADE = 'MEDIO'
                            if(x > 260 and x < 355 and y > 415 and y < 445):
                                Audio_Escolha.play()
                                ESCOLHA_DIFICULDADE = 'DIFICIL'
                            Inicio3(ESCOLHA_DIFICULDADE)

        pygame.time.Clock().tick(30)
        Fundo.blit(Screen, (0, 0))        
        pygame.display.update()

def Inicio3(ESCOLHA_DIFICULDADE):
    pygame.mixer.init()
    Audio_Escolha = pygame.mixer.Sound('audios/cruzadas/DingBop.ogg')
    Screen = pygame.image.load('imagens/cruzadas/Fundos/Fundo3.jpg')
    SAIR = True
    global ESCOLHA_DISCIPLINA
    while(SAIR):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                SAIR = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == True:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if (x > 10 and x < 40 and y > 10 and y < 40):
                            Audio_Escolha.play()
                            Inicio2()
                        if(x > 190 and x < 340 and y > 310 and y < 350):
                            Audio_Escolha.play()
                            Inicio2()
                        if(x > 475 and x < 650 and y > 355 and y < 390):
                            Audio_Escolha.play()
                            ESCOLHA_DISCIPLINA = 'PORTUGUES'
                            Jogar(ESCOLHA_DIFICULDADE, ESCOLHA_DISCIPLINA)
                        if(x > 475 and x < 650 and y > 400 and y < 435):
                            Audio_Escolha.play()
                            ESCOLHA_DISCIPLINA = 'MATEMATICA'
                            Jogar(ESCOLHA_DIFICULDADE, ESCOLHA_DISCIPLINA)
                        if(x > 175 and x < 425 and y > 465 and y < 515):
                            Audio_Escolha.play()
                            Instrucoes()
                        
        pygame.time.Clock().tick(30)
        Fundo.blit(Screen, (0, 0))        
        pygame.display.update()

def Instrucoes():
    pygame.mixer.init()
    Audio_Escolha = pygame.mixer.Sound('audios/cruzadas/DingBop.ogg')
    preto = (0, 0, 0)
    fonte1 = pygame.font.SysFont('Arial Black', 30)
    fonte2 = pygame.font.SysFont('Arial', 25)
    Titulo = fonte1.render('Palavras Cruzadas...', 2, preto)
    Instrucao = ['Consiste em encontrar as palavras usando as dicas disponíveis.',
                 'Conforme algumas palavras são preenchidas, algumas letras de outras',
                 'palavras automaticamente aparecem, facilitando a resolução.',
                 '',
                 'Para iniciar basta apertar em jogar, escolher um dos três',
                 'níveis e a disciplina desejada.',
                 '',
                 'Em relação aos níveis, o fácil contém 5 palavras, o médio',
                 '7 palavras e o difícil 9.',
                 '',
                 'Para preencher a palavra desejada, dê um click em cima do número, se',
                 'esta estiver certa você escutará um som de correta, caso contrário',
                 'um som de incorreta.',
                 'Se todas as palavras forem completadas corretamente, você vencerá a fase e',
                 'a tela mudará, em seguida você será redirecionado para o início.',
                 '',
                 'Bom Jogo!']
    Screen = pygame.image.load('imagens/cruzadas/Fundos/FundoPrincipal.jpg')
    SAIR = True
    
    while(SAIR):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                SAIR = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == True:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if (x > 10 and x < 40 and y > 10 and y < 40):
                            Audio_Escolha.play()
                            Inicio()
                        
        pygame.time.Clock().tick(30)
        Fundo.blit(Screen, (0, 0))
        Fundo.blit(Titulo, (50, 50))
        p = 50
        k = 100
        for i in Instrucao:            
            texto = fonte2.render(i, 3, preto)
            Fundo.blit(texto, (p, k))
            k += 25
        pygame.display.update()



def Jogar(ESCOLHA_DIFICULDADE, ESCOLHA_DISCIPLINA):
    if(ESCOLHA_DIFICULDADE == 'FACIL'):
        if(ESCOLHA_DISCIPLINA == 'PORTUGUES'):
            PortuguesFacil()
        elif(ESCOLHA_DISCIPLINA == 'MATEMATICA'):
            MatematicaFacil()
    elif(ESCOLHA_DIFICULDADE == 'MEDIO'):
        if(ESCOLHA_DISCIPLINA == 'PORTUGUES'):
            PortuguesMedio()
        elif(ESCOLHA_DISCIPLINA == 'MATEMATICA'):
            MatematicaMedio()
    elif(ESCOLHA_DIFICULDADE == "DIFICIL"):
        if(ESCOLHA_DISCIPLINA == 'PORTUGUES'):
            PortuguesDificil()
        elif(ESCOLHA_DISCIPLINA == 'MATEMATICA'):
            MatematicaDificil()

def PortuguesFacil():
    pygame.mixer.init()
    Audio_Escolha = pygame.mixer.Sound('audios/cruzadas/DingBop.ogg')
    Audio_Correta = pygame.mixer.Sound('audios/cruzadas/respostaCerta.ogg')
    Audio_Errada = pygame.mixer.Sound('audios/cruzadas/respostaErrada.ogg')

    fonte2 = pygame.font.SysFont('Arial Black', 15)
    preto = (0,0,0)
    
    Screen = pygame.image.load('imagens/cruzadas/Cruzadas/Portugues/PortFacil2.jpg')

    Respostas = ('PRONOME', 'INFORMAL', 'COESAO', 'ADJETIVO', 'AGUDO')
    Respostas_2 =['', '', '', '', '']
    Corretas = 0
    
    SAIR = True
    Atualizar = 0
    while(SAIR):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                SAIR = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == True:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if (x > 10 and x < 40 and y > 10 and y < 40):
                            Audio_Escolha.play()
                            Inicio()   
                        #Escolha da palavra com o click
                        if(x >= 420 and x <= 465 and y >= 60 and y <= 95):
                            palavra = ''
                            k = 70
                            for i in range(len(Respostas[0])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 435
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortFacil(Respostas, Respostas_2)
                                k += 40
                                pygame.display.update()
                            if(palavra == Respostas[0]):
                                Respostas_2[0] = Respostas[0]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                                pygame.display.update()
                        if(x >= 155 and x <= 200 and y >= 260 and y <= 295):
                            palavra = ''
                            p = 178
                            for i in range(len(Respostas[1])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 270
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortFacil(Respostas, Respostas_2)
                                p += 51
                                pygame.display.update()
                            if(palavra == Respostas[1]):
                                Respostas_2[1] = palavra
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                                pygame.display.update()
                        if(x >= 315 and x <= 360 and y >= 220 and y <= 255):
                            palavra = ''
                            k = 230
                            for i in range(len(Respostas[2])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 330
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortFacil(Respostas, Respostas_2)
                                k += 40
                                pygame.display.update()
                            if(palavra == Respostas[2]):
                                Respostas_2[2] = palavra
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                                pygame.display.update()
                        if(x >= 50 and x <= 95 and y >= 140 and y <= 175):
                            palavra = ''
                            p = 73
                            for i in range(len(Respostas[3])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 150
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortFacil(Respostas, Respostas_2)
                                p += 51
                                pygame.display.update()
                            if(palavra == Respostas[3]):
                                Respostas_2[3] = palavra
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                                pygame.display.update()
                        if(x >= 105 and x <= 150 and y >= 425 and y <= 460):
                            palavra = ''
                            p = 125
                            for i in range(len(Respostas[4])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 430
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortFacil(Respostas, Respostas_2)
                                p += 51
                                pygame.display.update()
                            if(palavra == Respostas[4]):
                                Respostas_2[4] = palavra
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                                pygame.display.update()
                                
        pygame.time.Clock().tick(30)
        Fundo.blit(Screen, (0, 0))
        if(Atualizar == 0):
            pygame.display.update()
            Atualizar += 1
        if(Corretas == len(Respostas)):
            Completou()

def PreenchimentoPortFacil(Respostas, Respostas_2):
    fonte2 = pygame.font.SysFont('Arial Black', 15)
    preto = (0, 0, 0) 
    if(Respostas[0] == Respostas_2[0]):
        k = 70
        for i in range(len(Respostas[0])):
            letra = Respostas[0][i]
            p = 435
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 40
    if(Respostas[1] == Respostas_2[1]):
        p = 178
        for i in range(len(Respostas[1])):
            letra = Respostas[1][i]
            k = 270
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 51
    if(Respostas[2] == Respostas_2[2]):
        k = 230
        for i in range(len(Respostas[2])):
            letra = Respostas[2][i]
            p = 330
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 40
    if(Respostas[3] == Respostas_2[3]):
        p = 73
        for i in range(len(Respostas[3])):
            letra = Respostas[3][i]
            k = 150
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 51
    if(Respostas[4] == Respostas_2[4]):
        p = 125
        for i in range(len(Respostas[4])):
            letra = Respostas[4][i]
            k = 430
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 51
    

def PortuguesMedio():
    pygame.mixer.init()
    Audio_Escolha = pygame.mixer.Sound('audios/cruzadas/DingBop.ogg')
    Audio_Correta = pygame.mixer.Sound('audios/cruzadas/respostaCerta.ogg')
    Audio_Errada = pygame.mixer.Sound('audios/cruzadas/respostaErrada.ogg')
    
    Screen = pygame.image.load('imagens/cruzadas/Cruzadas/Portugues/PortMedio2.jpg')

    fonte2 = pygame.font.SysFont('Arial Black', 15)
    preto = (0,0,0)
    
    Respostas = ('ARTIGO', 'VERBO', 'LENDA', 'INDIRETO', 'MISTA', 'COERENCIA', 'SUBSTANTIVO')
    Respostas_2 = ['', '', '', '', '', '', '']
    Corretas = 0
    
    SAIR = True
    Atualizar = 0
    while(SAIR):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                SAIR = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == True:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if (x > 10 and x < 40 and y >= 10 and y < 40):
                            Audio_Escolha.play()
                            Inicio()
                        #Escolha da palavra com o click
                        if(x >= 615 and x <= 660 and y >= 220 and y <= 255):
                            palavra = ''
                            k = 225
                            for i in range(len(Respostas[0])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 635
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 42
                            if(palavra == Respostas[0]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[0] = Respostas[0]
                            else:
                                Audio_Errada.play()
                                pygame.display.update()
                        if(x >= 285 and x <= 330 and y >= 95 and y <= 125):
                            palavra = ''
                            p = 303
                            for i in range(len(Respostas[1])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 100
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 56
                            if(palavra == Respostas[1]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[1] = Respostas[1]
                            else:
                                Audio_Errada.play()
                                pygame.display.update()
                        if(x >= 230 and x <= 275 and y >= 220 and y <= 255):
                            palavra = ''
                            p = 250
                            for i in range(len(Respostas[2])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 225
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 55
                            if(palavra == Respostas[2]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[2] = Respostas[2]
                            else:
                                Audio_Errada.play()
                                pygame.display.update()
                        if(x >= 395 and x <= 440 and y >= 260 and y <= 295):
                            palavra = ''
                            p = 410
                            for i in range(len(Respostas[3])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 268
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 56
                            if(palavra == Respostas[3]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[3] = Respostas[3]
                            else:
                                Audio_Errada.play()
                                pygame.display.update()
                        if(x >= 560 and x <= 600 and y >= 345 and y <= 380):
                            palavra = ''
                            p = 578
                            for i in range(len(Respostas[4])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 352
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 55
                            if(palavra == Respostas[4]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[4] = Respostas[4]
                            else:
                                Audio_Errada.play()
                                pygame.display.update()
                        if(x >= 340 and x <= 390 and y >= 10 and y <= 45):
                            palavra = ''
                            k = 15
                            for i in range(len(Respostas[5])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 358
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 42
                            if(palavra == Respostas[5]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[5] = Respostas[5]
                            else:
                                Audio_Errada.play()
                                pygame.display.update()
                        if(x >= 450 and x <= 500 and y >= 10 and y <= 45):
                            palavra = ''
                            k = 16
                            for i in range(len(Respostas[6])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 468
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 42
                            if(palavra == Respostas[6]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[6] = Respostas[6]
                            else:
                                Audio_Errada.play()
                                pygame.display.update()

        pygame.time.Clock().tick(30)
        Fundo.blit(Screen, (0, 0))
        if(Atualizar == 0):
            pygame.display.update()
            Atualizar += 1
        if(Corretas == len(Respostas)):
            Completou()

def PreenchimentoPortMedio(Respostas, Respostas_2):
    fonte2 = pygame.font.SysFont('Arial Black', 15)
    preto = (0, 0, 0) 
    if(Respostas[0] == Respostas_2[0]):
        k = 225
        for i in range(len(Respostas[0])):
            letra = Respostas[0][i]
            p = 635
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 42
    if(Respostas[1] == Respostas_2[1]):
        p = 305
        for i in range(len(Respostas[1])):
            letra = Respostas[1][i]
            k = 100
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 55
    if(Respostas[2] == Respostas_2[2]):
        p = 247
        for i in range(len(Respostas[2])):
            letra = Respostas[2][i]
            k = 225
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 56
    if(Respostas[3] == Respostas_2[3]):
        p = 410
        for i in range(len(Respostas[3])):
            letra = Respostas[3][i]
            k = 268
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 56
    if(Respostas[4] == Respostas_2[4]):
        p = 578
        for i in range(len(Respostas[4])):
            letra = Respostas[4][i]
            k = 352
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 55
    if(Respostas[5] == Respostas_2[5]):
        k = 15
        for i in range(len(Respostas[5])):
            letra = Respostas[5][i]
            p = 358
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 42
    if(Respostas[6] == Respostas_2[6]):
        k = 16
        for i in range(len(Respostas[6])):
            letra = Respostas[6][i]
            p = 468
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 42

def PortuguesDificil():
    pygame.mixer.init()
    Audio_Escolha = pygame.mixer.Sound('audios/cruzadas/DingBop.ogg')
    Audio_Correta = pygame.mixer.Sound('audios/cruzadas/respostaCerta.ogg')
    Audio_Errada = pygame.mixer.Sound('audios/cruzadas/respostaErrada.ogg')
    
    Screen = pygame.image.load('imagens/cruzadas/Cruzadas/Portugues/PortDificil3.jpg')

    fonte2 = pygame.font.SysFont('Arial Black', 15)
    preto = (0,0,0)

    Respostas = ('CONJUGACAO', 'SIMPLES', 'CONCRETO',
                 'TRANSITIVO', 'INDEFINIDO', 'POEMA',
                 'FABULA', 'PRIMITIVO', 'RADICAL')
    Respostas_2 = ['', '', '', '', '', '', '', '', '']
    Corretas = 0

    Atualizar = 0
    SAIR = True
    
    while(SAIR):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                SAIR = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == True:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if (x > 10 and x < 40 and y > 10 and y < 40):
                            Audio_Escolha.play()
                            Inicio()
                        #Escolha da palavra com o click
                        if(x >= 140 and x <= 185 and y >= 85 and y <= 115):
                            palavra = ''
                            p = 160
                            for i in range(len(Respostas[0])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 90
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 47
                            if(palavra == Respostas[0]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[0] = Respostas[0]
                            else:
                                Audio_Errada.play()
                        if(x >= 380 and x <= 420 and y >= 120 and y <= 150):
                            palavra = ''
                            k = 126
                            for i in range(len(Respostas[1])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 393
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 36
                            if(palavra == Respostas[1]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[1] = Respostas[1]
                            else:
                                Audio_Errada.play()
                        if(x >= 330 and x <= 375 and y >= 375 and y <= 405):
                            palavra = ''
                            p = 345
                            for i in range(len(Respostas[2])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 380
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 47
                            if(palavra == Respostas[2]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[2] = Respostas[2]
                            else:
                                Audio_Errada.play()
                        if(x >= 520 and x <= 565 and y >= 15 and y <= 45):
                            palavra = ''
                            k = 18
                            for i in range(len(Respostas[3])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 535
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 36
                            if(palavra == Respostas[3]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[3] = Respostas[3]
                            else:
                                Audio_Errada.play()
                        if(x >= 665 and x <= 705 and y >= 50 and y <= 80):
                            palavra = ''
                            k = 55
                            for i in range(len(Respostas[4])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 680
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 36
                            if(palavra == Respostas[4]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[4] = Respostas[4]
                            else:
                                Audio_Errada.play()
                        if(x >= 285 and x <= 325 and y >= 300 and y <= 330):
                            palavra = ''
                            p = 300
                            for i in range(len(Respostas[5])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 305
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 47
                            if(palavra == Respostas[5]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[5] = Respostas[5]
                            else:
                                Audio_Errada.play()
                        if(x >= 190 and x <= 230 and y >= 265 and y <= 295):
                            palavra = ''
                            p = 205
                            for i in range(len(Respostas[6])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 270
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 47
                            if(palavra == Respostas[6]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[6] = Respostas[6]
                            else:
                                Audio_Errada.play()
                        if(x >= 235 and x <= 280 and y >= 195 and y <= 225):
                            palavra = ''
                            p = 250
                            for i in range(len(Respostas[7])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 198
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 47
                            if(palavra == Respostas[7]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[7] = Respostas[7]
                            else:
                                Audio_Errada.play()
                        if(x >= 520 and x <= 565 and y >= 50 and y <= 80):
                            palavra = ''
                            p = 535
                            for i in range(len(Respostas[8])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 55
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoPortDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 47
                            if(palavra == Respostas[8]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[8] = Respostas[8]
                            else:
                                Audio_Errada.play()

        pygame.time.Clock().tick(30)
        Fundo.blit(Screen, (0, 0))
        if(Atualizar == 0):
            pygame.display.update()
            Atualizar += 1
        if(Corretas == len(Respostas)):
            Completou()

def PreenchimentoPortDificil(Respostas, Respostas_2):
    fonte2 = pygame.font.SysFont('Arial Black', 15)
    preto = (0, 0, 0) 
    if(Respostas[0] == Respostas_2[0]):
        p = 160
        for i in range(len(Respostas[0])):
            letra = Respostas[0][i]
            txt = fonte2.render(letra, 1, preto)
            k = 90
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 47
    if(Respostas_2[1] == Respostas[1]):
        k = 126
        for i in range(len(Respostas[1])):
            letra = Respostas[1][i]
            txt = fonte2.render(letra, 1, preto)
            p = 393
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 36
    if(Respostas_2[2] == Respostas[2]):
        p = 345
        for i in range(len(Respostas[2])):
            letra = Respostas[2][i]
            txt = fonte2.render(letra, 1, preto)
            k = 380
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 47
    if(Respostas[3] == Respostas_2[3]):
        k = 18
        for i in range(len(Respostas[3])):
            letra = Respostas[3][i]
            txt = fonte2.render(letra, 1, preto)
            p = 535
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 36
    if(Respostas_2[4] == Respostas[4]):
        k = 55
        for i in range(len(Respostas[4])):
            p = 680
            letra = Respostas[4][i]
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 36
    if(Respostas_2[5] == Respostas[5]):
        p = 300
        for i in range(len(Respostas[5])):
            letra = Respostas[5][i]
            txt = fonte2.render(letra, 1, preto)
            k = 305
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 47
    if(Respostas_2[6] == Respostas[6]):
        p = 205
        for i in range(len(Respostas[6])):
            letra = Respostas[6][i]
            txt = fonte2.render(letra, 1, preto)
            k = 270
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 47
    if(Respostas_2[7] == Respostas[7]):
        p = 250
        for i in range(len(Respostas[7])):
            letra = Respostas[7][i]
            txt = fonte2.render(letra, 1, preto)
            k = 198
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 47
    if(Respostas_2[8] == Respostas[8]):
        p = 535
        for i in range(len(Respostas[8])):
            letra = Respostas[8][i]
            txt = fonte2.render(letra, 1, preto)
            k = 55
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 47
            
def MatematicaFacil():
    pygame.mixer.init()
    Audio_Escolha = pygame.mixer.Sound('audios/cruzadas/DingBop.ogg')
    Audio_Correta = pygame.mixer.Sound('audios/cruzadas/respostaCerta.ogg')
    Audio_Errada = pygame.mixer.Sound('audios/cruzadas/respostaErrada.ogg')

    Screen = pygame.image.load('imagens/cruzadas/Cruzadas/Matematica/MatFacil2.jpg')

    fonte2 = pygame.font.SysFont('Arial Black', 15)
    preto = (0,0,0)

    Respostas = ('NATURAIS', 'ANTECESSOR', 'PRODUTO', 'SEQUENCIA', 'IMPAR')
    Respostas_2 = ['', '', '', '', '']
    Corretas = 0

    SAIR = True
    Atualizar = 0
    
    while(SAIR):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                SAIR = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == True:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if (x > 10 and x < 40 and y > 10 and y < 40):
                            Audio_Escolha.play()
                            Inicio()
                        #Escolha da palavra com o click
                        if(x >= 170 and x <= 215 and y >= 100 and y <= 130):
                            palavra = ''
                            k = 105
                            for i in range(len(Respostas[0])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 187
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatFacil(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 39
                            if(palavra == Respostas[0]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[0] = Respostas[0]
                            else:
                                Audio_Errada.play()
                        if(x >= 325 and x <= 370 and y >= 60 and y <= 90):
                            palavra = ''
                            k = 62
                            for i in range(len(Respostas[1])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 338
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatFacil(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 39
                            if(palavra == Respostas[1]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[1] = Respostas[1]
                            else:
                                Audio_Errada.play()
                        if(x >= 225 and x <= 270 and y >= 375 and y <= 405):
                            palavra = ''
                            p = 237
                            for i in range(len(Respostas[2])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 378
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatFacil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 51
                            if(palavra == Respostas[2]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[2] = Respostas[2]
                            else:
                                Audio_Errada.play()
                        if(x >= 20 and x <= 60 and y >= 220 and y <= 250):
                            palavra = ''
                            p = 33
                            for i in range(len(Respostas[3])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 222
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatFacil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 51
                            if(palavra == Respostas[3]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[3] = Respostas[3]
                            else:
                                Audio_Errada.play()
                        if(x >= 20 and x <= 60 and y >= 295 and y <= 325):
                            palavra = ''
                            p = 36
                            for i in range(len(Respostas[4])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 298
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatFacil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 51
                            if(palavra == Respostas[4]):
                                Audio_Correta.play()
                                Corretas += 1
                                Respostas_2[4] = Respostas[4]
                            else:
                                Audio_Errada.play()

        pygame.time.Clock().tick(30)
        Fundo.blit(Screen, (0, 0))
        if(Atualizar == 0):
            pygame.display.update()
            Atualizar += 1
        if(Corretas == len(Respostas)):
            Completou()

def PreenchimentoMatFacil(Respostas, Respostas_2):
    fonte2 = pygame.font.SysFont('Arial Black', 15)
    preto = (0, 0, 0)
    if(Respostas_2[0] == Respostas[0]):
        k = 103
        for i in range(len(Respostas[0])):
            letra = Respostas[0][i]
            p = 185
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 39
    if(Respostas_2[1] == Respostas[1]):
        k = 63
        for i in range(len(Respostas[1])):
            letra = Respostas[1][i]
            p = 340
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 39
    if(Respostas_2[2] == Respostas[2]):
        p = 237
        for i in range(len(Respostas[2])):
            letra = Respostas[2][i]
            k = 378
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 51
    if(Respostas_2[3] == Respostas[3]):
        p = 33
        for i in range(len(Respostas[3])):
            letra = Respostas[3][i]
            k = 222
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 51
    if(Respostas_2[4] == Respostas[4]):
        p = 36
        for i in range(len(Respostas[4])):
            letra = Respostas[4][i]
            k = 298
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 51

def MatematicaMedio():
    pygame.mixer.init()
    Audio_Escolha = pygame.mixer.Sound('audios/cruzadas/DingBop.ogg')
    Audio_Correta = pygame.mixer.Sound('audios/cruzadas/respostaCerta.ogg')
    Audio_Errada = pygame.mixer.Sound('audios/cruzadas/respostaErrada.ogg')

    Screen = pygame.image.load('imagens/cruzadas/Cruzadas/Matematica/MatMedio2.jpg')
    
    fonte2 = pygame.font.SysFont('Arial Black', 15)
    preto = (0,0,0)

    Respostas = ('SUCESSOR', 'DENOMINADOR', 'PRIMO', 'LITRO', 'PAR', 'IMPROPRIA', 'DECIMAL')
    Respostas_2 = ['', '', '', '', '', '', '']
    Corretas = 0

    SAIR = True
    Atualizar = 0
    
    while(SAIR):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                SAIR = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == True:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if (x > 10 and x < 40 and y > 10 and y < 40):
                            Audio_Escolha.play()
                            Inicio()
                        #Escolha da palavra com o click
                        if(x >= 385 and x <= 435 and y >= 15 and y <= 50):
                            palavra = ''
                            k = 20
                            for i in range(len(Respostas[0])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 402
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 44
                            if(palavra == Respostas[0]):
                                Respostas_2[0] = Respostas[0]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                        if(x >= 215 and x <= 260 and y >= 275 and y <= 310):
                            palavra = ''
                            p = 232
                            for i in range(len(Respostas[1])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 285
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 57
                            if(palavra == Respostas[1]):
                                Respostas_2[1] = Respostas[1]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                        if(x >= 560 and x <= 600 and y >= 190 and y <= 225):
                            palavra = ''
                            p = 575
                            for i in range(len(Respostas[2])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 196
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 57
                            if(palavra == Respostas[2]):
                                Respostas_2[2] = Respostas[2]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                            palavra = ''
                        if(x >= 215 and x <= 260 and y >= 320 and y <= 355):
                            palavra = ''
                            p = 230
                            for i in range(len(Respostas[3])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 330
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 57
                            if(palavra == Respostas[3]):
                                Respostas_2[3] = Respostas[3]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                            palavra = ''
                        if(x >= 615 and x <= 665 and y >= 100 and y <= 135):
                            palavra = ''
                            k = 107
                            for i in range(len(Respostas[4])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 630
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 45
                            if(palavra == Respostas[4]):
                                Respostas_2[4] = Respostas[4]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                        if(x >= 785 and x <= 835 and y >= 15 and y <= 50):
                            palavra = ''
                            k = 21
                            for i in range(len(Respostas[5])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 805
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 44
                            if(palavra == Respostas[5]):
                                Respostas_2[5] = Respostas[5]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                        if(x >= 330 and x <= 375 and y >= 145 and y <= 180):
                            palavra = ''
                            p = 345
                            for i in range(len(Respostas[6])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 152
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatMedio(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 57
                            if(palavra == Respostas[6]):
                                Respostas_2[6] = Respostas[6]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()

        pygame.time.Clock().tick(30)
        Fundo.blit(Screen, (0, 0))
        if(Atualizar == 0):
            pygame.display.update()
            Atualizar += 1
        if(Corretas == len(Respostas)):
            Completou()

def PreenchimentoMatMedio(Respostas, Respostas_2):
    fonte2 = pygame.font.SysFont('Arial Black', 15)
    preto = (0, 0, 0)
    if(Respostas_2[0] == Respostas[0]):
        k = 20
        for i in range(len(Respostas[0])):
            letra = Respostas[0][i]
            p = 402
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 44
    if(Respostas_2[1] == Respostas[1]):
        p = 232
        for i in range(len(Respostas[1])):
            letra = Respostas[1][i]
            k = 285
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 57
    if(Respostas_2[2] == Respostas[2]):
        p = 575
        for i in range(len(Respostas[2])):
            letra = Respostas[2][i]
            k = 196
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 57
    if(Respostas_2[3] == Respostas[3]):
        p = 230
        for i in range(len(Respostas[3])):
            letra = Respostas[3][i]
            k = 330
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 57
    if(Respostas_2[4] == Respostas[4]):
        k = 107
        for i in range(len(Respostas[4])):
            letra = Respostas[4][i]
            p = 630
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 45
    if(Respostas_2[5] == Respostas[5]):
        k = 21
        for i in range(len(Respostas[5])):
            letra = Respostas[5][i]
            p = 805
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 44
    if(Respostas_2[6] == Respostas[6]):
        p = 345
        for i in range(len(Respostas[6])):
            letra = Respostas[6][i]
            k = 152
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 57
    
def MatematicaDificil():
    pygame.mixer.init()
    Audio_Escolha = pygame.mixer.Sound('audios/cruzadas/DingBop.ogg')
    Audio_Correta = pygame.mixer.Sound('audios/cruzadas/respostaCerta.ogg')
    Audio_Errada = pygame.mixer.Sound('audios/cruzadas/respostaErrada.ogg')
    
    Screen = pygame.image.load('Imagens/cruzadas/Cruzadas/Matematica/MatDificil2.jpg')
        
    fonte2 = pygame.font.SysFont('Arial Black', 13)
    preto = (0,0,0)

    Respostas = ('POTENCIA', 'NUMERADOR', 'MISTA',
                 'METRO', 'IRREDUTIVEL', 'PROPRIA',
                 'QUILO', 'DIFERENCA', 'COMPOSTO')
    Respostas_2 = ['', '', '',
                   '', '', '',
                   '', '', '']
    Corretas = 0

    SAIR = True
    Atualizar = 0

    
    while(SAIR):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                SAIR = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == True:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if (x > 10 and x < 40 and y > 10 and y < 40):
                            Audio_Escolha.play()
                            Inicio()
                        #Escolha da palavra com o click
                        if(x >= 235 and x <= 275 and y >= 455 and y <= 485):
                            palavra = ''
                            p = 245
                            for i in range(len(Respostas[0])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 462
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 48
                            if(palavra == Respostas[0]):
                                Respostas_2[0] = Respostas[0]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                        if(x >= 570 and x <= 610 and y >= 20 and y <= 50):
                            palavra = ''
                            k = 27
                            for i in range(len(Respostas[1])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 580
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 36
                            if(palavra == Respostas[1]):
                                Respostas_2[1] = Respostas[1]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                        if(x >= 235 and x <= 275 and y >= 385 and y <= 415):
                            palavra = ''
                            p = 247
                            for i in range(len(Respostas[2])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 389
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 48
                            if(palavra == Respostas[2]):
                                Respostas_2[2] = Respostas[2]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                        if(x >= 570 and x <= 610 and y >= 385 and y <= 415):
                            palavra = ''
                            p = 579
                            for i in range(len(Respostas[3])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 389
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 48
                            if(palavra == Respostas[3]):
                                Respostas_2[3] = Respostas[3]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                        if(x >= 615 and x <= 655 and y >= 55 and y <= 85):
                            palavra = ''
                            k = 64
                            for i in range(len(Respostas[4])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 627
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 36
                            if(palavra == Respostas[4]):
                                Respostas_2[4] = Respostas[4]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                        if(x >= 280 and x <= 320 and y >= 200 and y <= 230):
                            palavra = ''
                            p = 293
                            for i in range(len(Respostas[5])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 208
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 48
                            if(palavra == Respostas[5]):
                                Respostas_2[5] = Respostas[5]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                        if(x >= 280 and x <= 320 and y >= 310 and y <= 340):
                            palavra = ''
                            k = 315
                            for i in range(len(Respostas[6])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 295
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 37
                            if(palavra == Respostas[6]):
                                Respostas_2[6] = Respostas[6]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                        if(x >= 425 and x <= 465 and y >= 125 and y <= 155):
                            palavra = ''
                            p = 437
                            for i in range(len(Respostas[7])):
                                letra = VerificaLetra()
                                palavra += letra
                                k = 136
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                p += 48
                            if(palavra == Respostas[7]):
                                Respostas_2[7] = Respostas[7]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()
                        if(x >= 375 and x <= 415 and y >= 165 and y <= 195):
                            palavra = ''
                            k = 172
                            for i in range(len(Respostas[8])):
                                letra = VerificaLetra()
                                palavra += letra
                                p = 390
                                txt = fonte2.render(letra, 1, preto)
                                Fundo.blit(txt, (p, k))
                                PreenchimentoMatDificil(Respostas, Respostas_2)
                                pygame.display.update()
                                k += 36
                            if(palavra == Respostas[8]):
                                Respostas_2[8] = Respostas[8]
                                Audio_Correta.play()
                                Corretas += 1
                            else:
                                Audio_Errada.play()

        pygame.time.Clock().tick(30)
        Fundo.blit(Screen, (0, 0))
        if(Atualizar == 0):
            pygame.display.update()
            Atualizar += 1
        if(Corretas == len(Respostas)):
            Completou()

def PreenchimentoMatDificil(Respostas, Respostas_2):
    fonte2 = pygame.font.SysFont('Arial Black', 13)
    preto = (0, 0, 0)
    if(Respostas_2[0] == Respostas[0]):
        p = 245
        for i in range(len(Respostas[0])):
            letra = Respostas[0][i]
            k = 462
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 48
    if(Respostas_2[1] == Respostas[1]):
        k = 27
        for i in range(len(Respostas[1])):
            letra = Respostas[1][i]
            p = 580
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 36
    if(Respostas_2[2] == Respostas[2]):
        p = 247
        for i in range(len(Respostas[2])):
            letra = Respostas[2][i]
            k = 389
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 48
    if(Respostas_2[3] == Respostas[3]):
        p = 579
        for i in range(len(Respostas[3])):
            letra = Respostas[3][i]
            k = 389
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 48
    if(Respostas_2[4] == Respostas[4]):
        k = 64
        for i in range(len(Respostas[4])):
            letra = Respostas[4][i]
            p = 627
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 36
    if(Respostas_2[5] == Respostas[5]):
        p = 293
        for i in range(len(Respostas[5])):
            letra = Respostas[5][i]
            k = 208
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 48
    if(Respostas_2[6] == Respostas[6]):
        k = 315
        for i in range(len(Respostas[6])):
            letra = Respostas[6][i]
            p = 295
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 37
    if(Respostas_2[7] == Respostas[7]):
        p = 437
        for i in range(len(Respostas[7])):
            letra = Respostas[7][i]
            k = 136
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            p += 48
    if(Respostas_2[8] == Respostas[8]):
        k = 172
        for i in range(len(Respostas[8])):
            letra = Respostas[8][i]
            p = 390
            txt = fonte2.render(letra, 1, preto)
            Fundo.blit(txt, (p, k))
            pygame.display.update()
            k += 36
    
def VerificaLetra():
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_a):
                    return 'A'
                if(event.key == pygame.K_b):
                    return 'B'
                if(event.key == pygame.K_c):
                    return 'C'
                if(event.key == pygame.K_d):
                    return 'D'
                if(event.key == pygame.K_e):
                    return 'E'
                if(event.key == pygame.K_f):
                    return 'F'
                if(event.key == pygame.K_g):
                    return 'G'
                if(event.key == pygame.K_h):
                    return 'H'
                if(event.key == pygame.K_i):
                    return 'I'
                if(event.key == pygame.K_j):
                    return 'J'
                if(event.key == pygame.K_k):
                    return 'K'
                if(event.key == pygame.K_l):
                    return 'L'
                if(event.key == pygame.K_m):
                    return 'M'
                if(event.key == pygame.K_n):
                    return 'N'
                if(event.key == pygame.K_o):
                    return 'O'
                if(event.key == pygame.K_p):
                    return 'P'
                if(event.key == pygame.K_q):
                    return 'Q'
                if(event.key == pygame.K_r):
                    return 'R'
                if(event.key == pygame.K_s):
                    return 'S'
                if(event.key == pygame.K_t):
                    return 'T'
                if(event.key == pygame.K_u):
                    return 'U'
                if(event.key == pygame.K_v):
                    return 'V'
                if(event.key == pygame.K_w):
                    return 'W'
                if(event.key == pygame.K_x):
                    return 'X'
                if(event.key == pygame.K_y):
                    return 'Y'
                if(event.key == pygame.K_z):
                    return 'Z'

def Completou():
    sleep(2)
    pygame.mixer.init()
    AudioCompletado = pygame.mixer.Sound('audios/cruzadas/Vitoria.ogg')
    AudioCompletado.play()
    verde = (0,250,154)
    branco = (255, 255, 255)
    fonte = pygame.font.SysFont('Arial Black', 30)
    Vitoria = fonte.render('Parabéns! Você acertou todas as palavras!', 1, branco)
    Fundo.fill(verde)
    Fundo.blit(Vitoria, (50, 270))
    pygame.display.update()
    sleep(5)
    Inicio()
