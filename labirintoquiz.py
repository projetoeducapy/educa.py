#Bibliotecas
import pygame, sys, os, random, educa
from pygame.locals import *

#Tela de seleção de disciplinas
def inicio1():
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Labirinto Quiz')

    #Cores
    preto = (0, 0, 0)

    #Imagens
    b1 = pygame.image.load('imagens/labirinto_quiz/sistema/botaog.png')
    b2 = pygame.image.load('imagens/labirinto_quiz/sistema/botaog.png')
    fundo = pygame.image.load('imagens/labirinto_quiz/sistema/fundo.png')
    voltar = pygame.image.load('imagens/labirinto_quiz/sistema/voltar.png')

    #Textos
    fonte1 = pygame.font.SysFont('Arial Black', 30)
    fonte2 = pygame.font.SysFont('Arial', 20)
    portugues = fonte1.render('Português', 1, preto)
    matematica = fonte1.render('Matemática', 1, preto)
    menu = fonte2.render('Menu Principal', 1, preto)

    #Áudios
    clique = pygame.mixer.Sound('audios/labirinto_quiz/clique.ogg')

    #Loop
    while True:

        #Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        clique.play()
                        educa.telajogos()
                    elif x > 100 and x < 350 and y > 330 and y < 430:
                        clique.play()
                        inicio2('português')
                    elif x > 500 and x < 750 and y > 330 and y < 430:
                        clique.play()
                        inicio2('matemática')
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        clique.play()
                        educa.principal()

        #Objetos e tela
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(b1,(100, 330))
        b1.blit(portugues, (36, 20))
        tela.blit(b2,(500, 330))
        b2.blit(matematica, (25, 20))
        tela.blit(menu, (725, 570))
        pygame.display.update()

#Tela de seleção de níveis
def inicio2(disciplina):
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Labirinto Quiz')

    #Cores
    preto = (0, 0, 0)

    #Imagens
    b1 = pygame.image.load('imagens/labirinto_quiz/sistema/botaop.png')
    b2 = pygame.image.load('imagens/labirinto_quiz/sistema/botaop.png')
    b3 = pygame.image.load('imagens/labirinto_quiz/sistema/botaop.png')
    b4 = pygame.image.load('imagens/labirinto_quiz/sistema/botaop.png')
    fundo = pygame.image.load('imagens/labirinto_quiz/sistema/fundo.png')
    voltar = pygame.image.load('imagens/labirinto_quiz/sistema/voltar.png')

    #Textos
    fonte1 = pygame.font.SysFont('Arial Black', 45)
    fonte2 = pygame.font.SysFont('Arial', 20)
    facil = fonte1.render('Fácil', 1, preto)
    medio = fonte1.render('Médio', 1, preto)
    dificil = fonte1.render('Difícil', 1, preto)
    ajuda = fonte1.render('Ajuda', 1, preto)
    menu = fonte2.render('Menu Principal', 1, preto)

    #Áudios
    clique = pygame.mixer.Sound('audios/labirinto_quiz/clique.ogg')

    #Loop
    while True:
        
        #Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        clique.play()
                        inicio1()
                    elif x > 150 and x < 350 and y > 305 and y < 385:
                        clique.play()
                        jogo(disciplina, 'fácil')
                    elif x > 500 and x < 700 and y > 305 and y < 385:
                        clique.play()
                        jogo(disciplina, 'médio')
                    elif x > 150 and x < 350 and y > 430 and y < 510:
                        clique.play()
                        jogo(disciplina, 'difícil')
                    elif x > 500 and x < 700 and y > 430 and y < 510:
                        clique.play()
                        ajuda1(disciplina)
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        clique.play()
                        educa.principal()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    ajuda1(disciplina)

        #Objetos e tela
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(b1,(150, 305))
        b1.blit(facil, (36, 2))
        tela.blit(b2, (500, 305))
        b2.blit(medio, (25, 2))
        tela.blit(b3, (150, 430))
        b3.blit(dificil, (26, 2))
        tela.blit(b4, (500, 430))
        b4.blit(ajuda, (28, 2))
        tela.blit(menu, (725, 570))
        pygame.display.update()

#Tela de ajuda
def ajuda1(disciplina):
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Labirinto Quiz')

    #Cores
    preto = (0, 0, 0)

    #Imagens
    fundo = pygame.image.load('imagens/labirinto_quiz/sistema/fundo.png')
    voltar = pygame.image.load('imagens/labirinto_quiz/sistema/voltar.png')
    ajuda = pygame.image.load('imagens/labirinto_quiz/sistema/ajuda.png')

    #Textos
    fonte = pygame.font.SysFont('Arial', 20)
    menu = fonte.render('Menu Principal', 1, preto)

    #Áudios
    clique = pygame.mixer.Sound('audios/labirinto_quiz/clique.ogg')

    #Loop
    while True:

        #Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        clique.play()
                        inicio2(disciplina)
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        clique.play()
                        educa.principal()

        #Objetos e tela
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(menu, (725, 570))
        tela.blit(ajuda, (50, 250))
        pygame.display.update()

#Jogo
def jogo(disciplina, nivel):
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Labirinto Quiz')

    #Cores
    preto = (0, 0, 0)
    verde = (0, 255, 0)
    azul = (0, 78, 152)
    amarelo = (255, 238, 0)
    vermelho = (226, 0, 37)
    cor = preto

    #Imagens
    fundo = pygame.image.load('imagens/labirinto_quiz/sistema/fundoliso.png')
    voltar = pygame.image.load('imagens/labirinto_quiz/sistema/voltar.png')
    labirinto = pygame.image.load('imagens/labirinto_quiz/sistema/labirinto.png')

    #Textos
    fonte = pygame.font.SysFont('Arial', 20)
    menu = fonte.render('Menu Principal', 1, preto)

    #Áudios
    clique = pygame.mixer.Sound('audios/labirinto_quiz/clique.ogg')

    #Declarações do labirinto
    posicoes = [(162, 195), (162, 375), (205, 375), (205, 335), (288, 335), (288, 376), (501, 376), (501, 336), (628, 336), (628, 376), (670, 376)]
    posicao = 0
    px = posicoes[0][0]
    py = posicoes[0][1]
    movimentos = ['b', 'd', 'c', 'd', 'b', 'd', 'c', 'd', 'b', 'd']
    movimento = False

    #Declarações das perguntas
    if disciplina == 'português':
        if nivel == 'fácil':
            perguntas = {'1': [pygame.image.load('imagens/labirinto_quiz/facil/portugues/p1.png'), pygame.image.load('imagens/labirinto_quiz/facil/portugues/a1.png'), pygame.K_b],
                         '2': [pygame.image.load('imagens/labirinto_quiz/facil/portugues/p2.png'), pygame.image.load('imagens/labirinto_quiz/facil/portugues/a2.png'), pygame.K_a],
                         '3': [pygame.image.load('imagens/labirinto_quiz/facil/portugues/p3.png'), pygame.image.load('imagens/labirinto_quiz/facil/portugues/a3.png'), pygame.K_a],
                         '4': [pygame.image.load('imagens/labirinto_quiz/facil/portugues/p4.png'), pygame.image.load('imagens/labirinto_quiz/facil/portugues/a4.png'), pygame.K_d],
                         '5': [pygame.image.load('imagens/labirinto_quiz/facil/portugues/p5.png'), pygame.image.load('imagens/labirinto_quiz/facil/portugues/a5.png'), pygame.K_a],
                         '6': [pygame.image.load('imagens/labirinto_quiz/facil/portugues/p6.png'), pygame.image.load('imagens/labirinto_quiz/facil/portugues/a6.png'), pygame.K_a],
                         '7': [pygame.image.load('imagens/labirinto_quiz/facil/portugues/p7.png'), pygame.image.load('imagens/labirinto_quiz/facil/portugues/a7.png'), pygame.K_d],
                         '8': [pygame.image.load('imagens/labirinto_quiz/facil/portugues/p8.png'), pygame.image.load('imagens/labirinto_quiz/facil/portugues/a8.png'), pygame.K_c],
                         '9': [pygame.image.load('imagens/labirinto_quiz/facil/portugues/p9.png'), pygame.image.load('imagens/labirinto_quiz/facil/portugues/a9.png'), pygame.K_d],
                         '10': [pygame.image.load('imagens/labirinto_quiz/facil/portugues/p10.png'), pygame.image.load('imagens/labirinto_quiz/facil/portugues/a10.png'), pygame.K_b]}
        elif nivel == 'médio':
            perguntas = {'1': [pygame.image.load('imagens/labirinto_quiz/medio/portugues/p1.png'), pygame.image.load('imagens/labirinto_quiz/medio/portugues/a1.png'), pygame.K_c],
                         '2': [pygame.image.load('imagens/labirinto_quiz/medio/portugues/p2.png'), pygame.image.load('imagens/labirinto_quiz/medio/portugues/a2.png'), pygame.K_b],
                         '3': [pygame.image.load('imagens/labirinto_quiz/medio/portugues/p3.png'), pygame.image.load('imagens/labirinto_quiz/medio/portugues/a3.png'), pygame.K_b],
                         '4': [pygame.image.load('imagens/labirinto_quiz/medio/portugues/p4.png'), pygame.image.load('imagens/labirinto_quiz/medio/portugues/a4.png'), pygame.K_c],
                         '5': [pygame.image.load('imagens/labirinto_quiz/medio/portugues/p5.png'), pygame.image.load('imagens/labirinto_quiz/medio/portugues/a5.png'), pygame.K_b],
                         '6': [pygame.image.load('imagens/labirinto_quiz/medio/portugues/p6.png'), pygame.image.load('imagens/labirinto_quiz/medio/portugues/a6.png'), pygame.K_b],
                         '7': [pygame.image.load('imagens/labirinto_quiz/medio/portugues/p7.png'), pygame.image.load('imagens/labirinto_quiz/medio/portugues/a7.png'), pygame.K_a],
                         '8': [pygame.image.load('imagens/labirinto_quiz/medio/portugues/p8.png'), pygame.image.load('imagens/labirinto_quiz/medio/portugues/a8.png'), pygame.K_b],
                         '9': [pygame.image.load('imagens/labirinto_quiz/medio/portugues/p9.png'), pygame.image.load('imagens/labirinto_quiz/medio/portugues/a9.png'), pygame.K_a],
                         '10': [pygame.image.load('imagens/labirinto_quiz/medio/portugues/p10.png'), pygame.image.load('imagens/labirinto_quiz/medio/portugues/a10.png'), pygame.K_d]}
        elif nivel == 'difícil':
            perguntas = {'1': [pygame.image.load('imagens/labirinto_quiz/dificil/portugues/p1.png'), pygame.image.load('imagens/labirinto_quiz/dificil/portugues/a1.png'), pygame.K_a],
                         '2': [pygame.image.load('imagens/labirinto_quiz/dificil/portugues/p2.png'), pygame.image.load('imagens/labirinto_quiz/dificil/portugues/a2.png'), pygame.K_a],
                         '3': [pygame.image.load('imagens/labirinto_quiz/dificil/portugues/p3.png'), pygame.image.load('imagens/labirinto_quiz/dificil/portugues/a3.png'), pygame.K_a],
                         '4': [pygame.image.load('imagens/labirinto_quiz/dificil/portugues/p4.png'), pygame.image.load('imagens/labirinto_quiz/dificil/portugues/a4.png'), pygame.K_d],
                         '5': [pygame.image.load('imagens/labirinto_quiz/dificil/portugues/p5.png'), pygame.image.load('imagens/labirinto_quiz/dificil/portugues/a5.png'), pygame.K_a],
                         '6': [pygame.image.load('imagens/labirinto_quiz/dificil/portugues/p6.png'), pygame.image.load('imagens/labirinto_quiz/dificil/portugues/a6.png'), pygame.K_c],
                         '7': [pygame.image.load('imagens/labirinto_quiz/dificil/portugues/p7.png'), pygame.image.load('imagens/labirinto_quiz/dificil/portugues/a7.png'), pygame.K_d],
                         '8': [pygame.image.load('imagens/labirinto_quiz/dificil/portugues/p8.png'), pygame.image.load('imagens/labirinto_quiz/dificil/portugues/a8.png'), pygame.K_a],
                         '9': [pygame.image.load('imagens/labirinto_quiz/dificil/portugues/p9.png'), pygame.image.load('imagens/labirinto_quiz/dificil/portugues/a9.png'), pygame.K_a],
                         '10': [pygame.image.load('imagens/labirinto_quiz/dificil/portugues/p10.png'), pygame.image.load('imagens/labirinto_quiz/dificil/portugues/a10.png'), pygame.K_c]}
    elif disciplina == 'matemática':
        if nivel == 'fácil':
            perguntas = {'1': [pygame.image.load('imagens/labirinto_quiz/facil/matematica/p1.png'), pygame.image.load('imagens/labirinto_quiz/facil/matematica/a1.png'), pygame.K_b],
                         '2': [pygame.image.load('imagens/labirinto_quiz/facil/matematica/p2.png'), pygame.image.load('imagens/labirinto_quiz/facil/matematica/a2.png'), pygame.K_c],
                         '3': [pygame.image.load('imagens/labirinto_quiz/facil/matematica/p3.png'), pygame.image.load('imagens/labirinto_quiz/facil/matematica/a3.png'), pygame.K_c],
                         '4': [pygame.image.load('imagens/labirinto_quiz/facil/matematica/p4.png'), pygame.image.load('imagens/labirinto_quiz/facil/matematica/a4.png'), pygame.K_a],
                         '5': [pygame.image.load('imagens/labirinto_quiz/facil/matematica/p5.png'), pygame.image.load('imagens/labirinto_quiz/facil/matematica/a5.png'), pygame.K_d],
                         '6': [pygame.image.load('imagens/labirinto_quiz/facil/matematica/p6.png'), pygame.image.load('imagens/labirinto_quiz/facil/matematica/a6.png'), pygame.K_a],
                         '7': [pygame.image.load('imagens/labirinto_quiz/facil/matematica/p7.png'), pygame.image.load('imagens/labirinto_quiz/facil/matematica/a7.png'), pygame.K_c],
                         '8': [pygame.image.load('imagens/labirinto_quiz/facil/matematica/p8.png'), pygame.image.load('imagens/labirinto_quiz/facil/matematica/a8.png'), pygame.K_d],
                         '9': [pygame.image.load('imagens/labirinto_quiz/facil/matematica/p9.png'), pygame.image.load('imagens/labirinto_quiz/facil/matematica/a9.png'), pygame.K_c],
                         '10': [pygame.image.load('imagens/labirinto_quiz/facil/matematica/p10.png'), pygame.image.load('imagens/labirinto_quiz/facil/matematica/a10.png'), pygame.K_c]}
        elif nivel == 'médio':
            perguntas = {'1': [pygame.image.load('imagens/labirinto_quiz/medio/matematica/p1.png'), pygame.image.load('imagens/labirinto_quiz/medio/matematica/a1.png'), pygame.K_c],
                         '2': [pygame.image.load('imagens/labirinto_quiz/medio/matematica/p2.png'), pygame.image.load('imagens/labirinto_quiz/medio/matematica/a2.png'), pygame.K_c],
                         '3': [pygame.image.load('imagens/labirinto_quiz/medio/matematica/p3.png'), pygame.image.load('imagens/labirinto_quiz/medio/matematica/a3.png'), pygame.K_a],
                         '4': [pygame.image.load('imagens/labirinto_quiz/medio/matematica/p4.png'), pygame.image.load('imagens/labirinto_quiz/medio/matematica/a4.png'), pygame.K_b],
                         '5': [pygame.image.load('imagens/labirinto_quiz/medio/matematica/p5.png'), pygame.image.load('imagens/labirinto_quiz/medio/matematica/a5.png'), pygame.K_b],
                         '6': [pygame.image.load('imagens/labirinto_quiz/medio/matematica/p6.png'), pygame.image.load('imagens/labirinto_quiz/medio/matematica/a6.png'), pygame.K_a],
                         '7': [pygame.image.load('imagens/labirinto_quiz/medio/matematica/p7.png'), pygame.image.load('imagens/labirinto_quiz/medio/matematica/a7.png'), pygame.K_a],
                         '8': [pygame.image.load('imagens/labirinto_quiz/medio/matematica/p8.png'), pygame.image.load('imagens/labirinto_quiz/medio/matematica/a8.png'), pygame.K_b],
                         '9': [pygame.image.load('imagens/labirinto_quiz/medio/matematica/p9.png'), pygame.image.load('imagens/labirinto_quiz/medio/matematica/a9.png'), pygame.K_a],
                         '10': [pygame.image.load('imagens/labirinto_quiz/medio/matematica/p10.png'), pygame.image.load('imagens/labirinto_quiz/medio/matematica/a10.png'), pygame.K_c]}
        elif nivel == 'difícil':
            perguntas = {'1': [pygame.image.load('imagens/labirinto_quiz/dificil/matematica/p1.png'), pygame.image.load('imagens/labirinto_quiz/dificil/matematica/a1.png'), pygame.K_b],
                         '2': [pygame.image.load('imagens/labirinto_quiz/dificil/matematica/p2.png'), pygame.image.load('imagens/labirinto_quiz/dificil/matematica/a2.png'), pygame.K_d],
                         '3': [pygame.image.load('imagens/labirinto_quiz/dificil/matematica/p3.png'), pygame.image.load('imagens/labirinto_quiz/dificil/matematica/a3.png'), pygame.K_b],
                         '4': [pygame.image.load('imagens/labirinto_quiz/dificil/matematica/p4.png'), pygame.image.load('imagens/labirinto_quiz/dificil/matematica/a4.png'), pygame.K_d],
                         '5': [pygame.image.load('imagens/labirinto_quiz/dificil/matematica/p5.png'), pygame.image.load('imagens/labirinto_quiz/dificil/matematica/a5.png'), pygame.K_c],
                         '6': [pygame.image.load('imagens/labirinto_quiz/dificil/matematica/p6.png'), pygame.image.load('imagens/labirinto_quiz/dificil/matematica/a6.png'), pygame.K_b],
                         '7': [pygame.image.load('imagens/labirinto_quiz/dificil/matematica/p7.png'), pygame.image.load('imagens/labirinto_quiz/dificil/matematica/a7.png'), pygame.K_c],
                         '8': [pygame.image.load('imagens/labirinto_quiz/dificil/matematica/p8.png'), pygame.image.load('imagens/labirinto_quiz/dificil/matematica/a8.png'), pygame.K_d],
                         '9': [pygame.image.load('imagens/labirinto_quiz/dificil/matematica/p9.png'), pygame.image.load('imagens/labirinto_quiz/dificil/matematica/a9.png'), pygame.K_b],
                         '10': [pygame.image.load('imagens/labirinto_quiz/dificil/matematica/p10.png'), pygame.image.load('imagens/labirinto_quiz/dificil/matematica/a10.png'), pygame.K_a]}
    sorteio = random.randint(1, len(perguntas))
    sorteados = []
    sorteados.append(sorteio)
    colorm = colort = correto = incorreto = False
    
    #Loop
    while True:

        #Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x > 48 and x < 802 and y > 435 and y < 463 and colort == False:
                    colorm = True
                    evento = 'a'
                elif x > 48 and x < 802 and y > 464 and y < 492 and colort == False:
                    colorm = True
                    evento = 'b'
                elif x > 48 and x < 802 and y > 493 and y < 521 and colort == False:
                    colorm = True
                    evento = 'c'
                elif x > 48 and x < 802 and y > 522 and y < 550 and colort == False:
                    colorm = True
                    evento = 'd'
                else:
                    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                    colorm = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        clique.play()
                        inicio2(disciplina)
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        clique.play()
                        educa.principal()
                    elif x > 48 and x < 802 and y > 435 and y < 463:
                        clique.play()
                        colort = True
                        evento = 'a'
                        if perguntas[str(sorteio)][2] == pygame.K_a:
                            
                            correto = True
                        else:
                            incorreto = True
                    elif x > 48 and x < 802 and y > 464 and y < 492:
                        clique.play()
                        colort = True
                        evento = 'b'
                        if perguntas[str(sorteio)][2] == pygame.K_b:
                            correto = True
                        else:
                            incorreto = True
                    elif x > 48 and x < 802 and y > 493 and y < 521:
                        clique.play()
                        colort = True
                        evento = 'c'
                        if perguntas[str(sorteio)][2] == pygame.K_c:
                            correto = True
                        else:
                            incorreto = True
                    elif x > 48 and x < 802 and y > 522 and y < 550:
                        clique.play()
                        colort = True
                        evento = 'd'
                        if perguntas[str(sorteio)][2] == pygame.K_d:
                            correto = True
                        else:
                            incorreto = True
            if event.type == pygame.KEYDOWN:
                if posicao != len(posicoes) - 1:
                    if event.key == K_a:
                        clique.play()
                        colort = True
                        evento = 'a'
                        if perguntas[str(sorteio)][2] == pygame.K_a:
                            correto = True
                        else:
                            incorreto = True
                    elif event.key == K_b:
                        clique.play()
                        colort = True
                        evento = 'b'
                        if perguntas[str(sorteio)][2] == pygame.K_b:
                            correto = True
                        else:
                            incorreto = True
                    elif event.key == K_c:
                        clique.play()
                        colort = True
                        evento = 'c'
                        if perguntas[str(sorteio)][2] == pygame.K_c:
                            correto = True
                        else:
                            incorreto = True
                    elif event.key == K_d:
                        clique.play()
                        colort = True
                        evento = 'd'
                        if perguntas[str(sorteio)][2] == pygame.K_d:
                            correto = True
                        else:
                            incorreto = True
                    else:
                        fim(disciplina)
            if correto == True:
                cor = verde
                if movimentos[posicao] == 'b':
                    a = py
                    b = posicoes[posicao + 1][1]
                    tipo = 'b'
                elif movimentos[posicao] == 'c':
                    b = py
                    a = posicoes[posicao + 1][1]
                    tipo = 'c'
                elif movimentos[posicao] == 'd':
                    a = px
                    b = posicoes[posicao + 1][0]
                    tipo = 'd'
                elif movimentos[posicao] == 'e':
                    b = px
                    a = posicoes[posicao + 1][0]
                    tipo = 'e'
                movimento = True
                posicao += 1
                pygame.event.set_blocked(pygame.KEYDOWN)
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                correto = False
            if incorreto == True:
                if posicao != 0:
                    cor = vermelho
                    if movimentos[posicao - 1] == 'b':
                        b = py
                        a = posicoes[posicao - 1][1]
                        tipo = 'c'
                    elif movimentos[posicao - 1] == 'c':
                        a = py
                        b = posicoes[posicao - 1][1]
                        tipo = 'b'
                    elif movimentos[posicao - 1] == 'd':
                        b = px
                        a = posicoes[posicao - 1][0]
                        tipo = 'e'
                    elif movimentos[posicao - 1] == 'e':
                        a = px
                        b = posicoes[posicao - 1][0]
                        tipo = 'e'
                    movimento = True
                    posicao -= 1
                    pygame.event.set_blocked(pygame.KEYDOWN)
                    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                else:
                    sorteio = random.randint(1, len(perguntas))
                    while sorteio in sorteados:
                        if len(sorteados) == len(perguntas):
                            sorteados = []
                        sorteio = random.randint(1, len(perguntas))
                    sorteados.append(sorteio)
                    pygame.draw.rect(tela, vermelho, (px, py, 20, 20))
                    pygame.display.update()
                    pygame.time.delay(500)
                incorreto = False

        #Objetos e tela              
        #pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(menu, (725, 570))
        tela.blit(perguntas[str(sorteio)][0], (40, 40))
        tela.blit(labirinto, (40, 185))
        tela.blit(perguntas[str(sorteio)][1], (40, 425))
        pygame.draw.rect(tela, cor, (px, py, 20, 20))
        if movimento == True:
            if tipo == 'b':
                if a + 5 > b:
                    py += 1
                    a = py
                else:
                    py += 5
                    a = py
            elif tipo == 'c':
                if a + 5 > b:
                    py -= 1
                    b = py
                else:
                    py -= 5
                    b = py
            elif tipo == 'd':
                if a + 5 > b:
                    px += 1
                    a = px
                else:
                    px += 5
                    a = px
            elif tipo == 'e':
                if a + 5 > b:
                    px -= 1
                    b = px
                else:
                    px -= 5
                    b = px
            if a == b:
                cor = preto
                movimento = False
                colort = False
                colotm = True
                pygame.event.set_allowed(None)
                if posicao == len(posicoes) - 1:
                    i = 0
                    pygame.display.update()
                    while i < 50:
                        pygame.time.delay(300)
                        pygame.draw.rect(tela, preto, (px, py, 20, 20))
                        pygame.display.update()
                        pygame.time.delay(300)
                        pygame.draw.rect(tela, verde, (px, py, 20, 20))
                        pygame.display.update()
                        i += 10
                    fim1(disciplina)
                sorteio = random.randint(1, len(perguntas))
                while sorteio in sorteados:
                    if len(sorteados) == len(perguntas):
                        sorteados = []
                    sorteio = random.randint(1, len(perguntas))
                sorteados.append(sorteio)
        if colorm == True:
            if evento == 'a':
                pygame.draw.circle(tela, azul, (67, 447), 13)
            elif evento == 'b':
                pygame.draw.circle(tela, amarelo, (67, 477), 13)
            elif evento == 'c':
                pygame.draw.circle(tela, vermelho, (67, 507), 13)
            elif evento == 'd':
                pygame.draw.circle(tela, verde, (67, 537), 13)
            if movimento == True and colort == True:
                colorm = False
        if colort == True:
            if evento == 'a':
                pygame.draw.circle(tela, azul, (67, 447), 13)
            elif evento == 'b':
                pygame.draw.circle(tela, amarelo, (67, 477), 13)
            elif evento == 'c':
                pygame.draw.circle(tela, vermelho, (67, 507), 13)
            elif evento == 'd':
                pygame.draw.circle(tela, verde, (67, 537), 13)
            if posicao == 0 and movimento == False:
                colort = False
        pygame.display.update()

def fim1(disciplina):
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Labirinto Quiz')

    #Cores
    preto = (0, 0, 0)

    #Imagens
    estrela = pygame.image.load('imagens/labirinto_quiz/sistema/0stars.png')
    parabens = pygame.image.load('imagens/labirinto_quiz/sistema/parabens.png')
    fim = pygame.image.load('imagens/labirinto_quiz/sistema/fim.png')
    fundo = pygame.image.load('imagens/labirinto_quiz/sistema/fundoliso.png')
    voltar = pygame.image.load('imagens/labirinto_quiz/sistema/voltar.png')

    #Textos
    fonte1 = pygame.font.SysFont('Arial Black', 25)
    fonte2 = pygame.font.SysFont('Arial', 20)
    avalie = fonte1.render('Gostou do jogo?', 1, preto)
    menu = fonte2.render('Menu Principal', 1, preto)

    #Áudios
    clique = pygame.mixer.Sound('audios/labirinto_quiz/clique.ogg')

    #Declarações
    votado = False

    #Loop
    while True:

        #Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if votado == False:
                    if x > 275 and x < 335 and y > 490 and y < 560:
                        estrela = pygame.image.load('imagens/labirinto_quiz/sistema/1stars.png')
                    elif x > 335 and x < 395 and y > 490 and y < 560:
                        estrela = pygame.image.load('imagens/labirinto_quiz/sistema/2stars.png')
                    elif x > 395 and x < 455 and y > 490 and y < 560:
                        estrela = pygame.image.load('imagens/labirinto_quiz/sistema/3stars.png')
                    elif x > 455 and x < 515 and y > 490 and y < 560:
                        estrela = pygame.image.load('imagens/labirinto_quiz/sistema/4stars.png')
                    elif x > 515 and x < 575 and y > 490 and y < 560:
                        estrela = pygame.image.load('imagens/labirinto_quiz/sistema/5stars.png')
                    else:
                        estrela = pygame.image.load('imagens/labirinto_quiz/sistema/0stars.png')
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        clique.play()
                        inicio2(disciplina)
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        clique.play()
                        educa.principal()
                    if votado == False:
                        if x > 275 and x < 335 and y > 490 and y < 560:
                            clique.play()
                            estrela = pygame.image.load('imagens/labirinto_quiz/sistema/1stars.png')
                            votado = True
                        elif x > 335 and x < 395 and y > 490 and y < 560:
                            clique.play()
                            estrela = pygame.image.load('imagens/labirinto_quiz/sistema/2stars.png')
                            votado = True
                        elif x > 395 and x < 455 and y > 490 and y < 560:
                            clique.play()
                            estrela = pygame.image.load('imagens/labirinto_quiz/sistema/3stars.png')
                            votado = True
                        elif x > 455 and x < 515 and y > 490 and y < 560:
                            estrela = pygame.image.load('imagens/labirinto_quiz/sistema/4stars.png')
                            votado = True
                        elif x > 515 and x < 575 and y > 490 and y < 560:
                            clique.play()
                            estrela = pygame.image.load('imagens/labirinto_quiz/sistema/5stars.png')
                            votado = True

        #Objetos e tela
        #pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(parabens, (217, 60))
        tela.blit(fim, (40, 180))
        tela.blit(avalie, (315, 450))
        pygame.draw.rect(tela, preto, (275, 485, 300, 5))
        tela.blit(estrela, (275, 490))
        tela.blit(menu, (725, 570))
        pygame.display.update()
