#Importações
import pygame, sys, os, random
from pygame.locals import *

#Alinhamento de tela
os.environ['SDL_VIDEO_CENTERED'] = '1'

def principal():
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Educa.py')
    pygame.mixer.init()

    #Audios
    audio_clique=pygame.mixer.Sound('audios/principal/clique.ogg')

    #Imagens
    bmenu1 = pygame.image.load('imagens/principal/bmenu1.png')
    bmenu2 = pygame.image.load('imagens/principal/bmenu2.png')

    bmenu3 = pygame.image.load('imagens/principal/bmenu3.png')
    fundo = pygame.image.load('imagens/principal/educapy.jpeg')
    
    #Tela inicial
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 325 and x < 525 and y > 275 and y < 355:
                        audio_clique.play()
                        telajogos()
                    if x > 325 and x < 525 and y > 365 and y < 445:
                        audio_clique.play()
                        instrucoes()
                    if x > 340 and x < 505 and y > 445 and y < 540:
                        audio_clique.play()
                        creditos()
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(bmenu1,(325, 275))
        tela.blit(bmenu2,(325, 365))
        tela.blit(bmenu3,(325, 445))
        pygame.display.update()
        
def telajogos():
    #Importações
    import gamequiz, labirintoquiz, Palavras_Cruzadas
    
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Tela de Jogos')
    pygame.mixer.init()

    #Audios
    audio_clique=pygame.mixer.Sound('audios/principal/clique.ogg')

    #Cores
    preto = (0, 0, 0)
    
    #Imagens
    bjogo1 = pygame.image.load('imagens/principal/bjogo1.png')
    bjogo2 = pygame.image.load('imagens/principal/bjogo2.png')
    bjogo3 = pygame.image.load('imagens/principal/bjogo3.png')
    fundo = pygame.image.load('imagens/principal/tjogos.jpg')
    voltar = pygame.image.load('imagens/quiz/voltar.png')
    
    #Cores
    preto = (0, 0, 0)
    
    #Textos
    pygame.font.init()
    fonte2 = pygame.font.SysFont('Arial', 20)
    menu = fonte2.render('Menu Principal', 1, preto)
    
    #Tela inicial
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 50 and y > 10 and y < 50:
                        audio_clique.play()
                        principal()
                    if x > 300 and x < 550 and y > 160 and y < 255:
                        audio_clique.play()
                        gamequiz.gamequiz()
                    if x > 300 and x < 550 and y > 290 and y < 385:
                        audio_clique.play()
                        labirintoquiz.inicio1()
                    if x > 300 and x < 550 and y > 420 and y < 515:
                        audio_clique.play()
                        Palavras_Cruzadas.Inicio()
                    if x > 725 and x < 830 and y > 570 and y < 585:
                        audio_clique.play()
                        principal()
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(bjogo1,(300, 160))
        tela.blit(bjogo2,(300, 290))
        tela.blit(bjogo3,(300, 420))
        tela.blit(voltar, (10, 10))
        tela.blit(menu, (725, 570))
        pygame.display.update()

def creditos():
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Créditos')
    pygame.mixer.init()
    #Audios
    audio_clique=pygame.mixer.Sound('audios/quiz/clique.ogg')

    #Cores
    preto = (0, 0, 0)
    
    #Imagens
    fundo = pygame.image.load('imagens/principal/creditos.jpg')
    voltar = pygame.image.load('imagens/quiz/voltar.png')
    #Textos
    pygame.font.init()
    fonte2 = pygame.font.SysFont('Arial', 20)
    menu = fonte2.render('Menu Principal', 1, preto)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 50 and y > 10 and y < 50:
                        audio_clique.play()
                        principal()
                    if x > 725 and x < 830 and y > 570 and y < 590:
                        audio_clique.play()
                        principal()
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(menu, (725, 570))
        pygame.display.update()

def instrucoes():
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Instruções')
    pygame.mixer.init()
    #Audios
    audio_clique=pygame.mixer.Sound('audios/quiz/clique.ogg')

    #Cores
    preto = (0, 0, 0)
    
    #Imagens
    fundo = pygame.image.load('imagens/principal/instrucoes.jpg')
    voltar = pygame.image.load('imagens/quiz/voltar.png')
    #Textos
    pygame.font.init()
    fonte2 = pygame.font.SysFont('Arial', 20)
    menu = fonte2.render('Menu Principal', 1, preto)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 50 and y > 10 and y < 50:
                        audio_clique.play()
                        principal()
                    if x > 725 and x < 830 and y > 570 and y < 590:
                        audio_clique.play()
                        principal()
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(menu, (725, 570))
        pygame.display.update()
        
import educa
educa.principal()
