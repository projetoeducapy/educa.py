#Importações
import pygame, sys
from pygame.locals import *
import educa

def gamequiz():
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Game Quiz')
    pygame.mixer.init()

    #Audios
    audio_clique=pygame.mixer.Sound('audios/quiz/clique.ogg')

    #Cores
    preto = (0, 0, 0)
    
    #Imagens
    b1 = pygame.image.load('imagens/quiz/nuvem.png')
    b2 = pygame.image.load('imagens/quiz/nuvem.png')
    fundo = pygame.image.load('imagens/quiz/fundo.jpeg')
    voltar = pygame.image.load('imagens/quiz/voltar.png')

    #Textos
    pygame.font.init()
    fonte1 = pygame.font.SysFont('Arial Black', 45)
    fonte11= pygame.font.SysFont('Arial Black', 35)
    fonte2 = pygame.font.SysFont('Arial', 20)
    menu = fonte2.render('Menu Principal', 1, preto)
    portugues = fonte11.render('Português', 1, preto)
    matematica = fonte11.render('Matemática', 1, preto)

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
                        educa.telajogos()
                    if x > 35 and x < 355 and y > 260 and y < 430:
                        audio_clique.play()
                        inicio2('Português')
                    if x > 430 and x < 750 and y > 260 and y < 430:
                        audio_clique.play()
                        inicio2('Matemática')
                    if x > 725 and x < 830 and y > 570 and y < 590:
                        audio_clique.play()
                        educa.principal()
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(b1,(100, 260))
        b1.blit(portugues, (45, 45))
        tela.blit(b2,(430, 260))
        b2.blit(matematica, (35, 45))
        tela.blit(menu, (725, 570))
        pygame.display.update()

def placar(quantidade,disciplina):
    #Inicialização
    tela = pygame.display.set_mode((850, 600))
    pygame.mixer.init()

    #Audios
    audio_efeito=pygame.mixer.Sound('audios/quiz/efeito.ogg')
    audio_placar=pygame.mixer.Sound('audios/quiz/bateria.ogg')
    audio_perdeu=pygame.mixer.Sound('audios/quiz/errada.ogg')
    #Imagens
    quant0 = pygame.image.load('imagens/quiz/zerou.jpg')
    quant1 = pygame.image.load('imagens/quiz/dez.jpg')
    quant2 = pygame.image.load('imagens/quiz/vinte.jpg')
    quant3 = pygame.image.load('imagens/quiz/trinta.jpg')
    quant4 = pygame.image.load('imagens/quiz/quarenta.jpg')
    quant5 = pygame.image.load('imagens/quiz/cinquenta.jpg')
    quant6 = pygame.image.load('imagens/quiz/sessenta.jpg')
    quant7 = pygame.image.load('imagens/quiz/setenta.jpg')
    quant8 = pygame.image.load('imagens/quiz/oitenta.jpg')
    quant9 = pygame.image.load('imagens/quiz/noventa.jpg')
    quant10 = pygame.image.load('imagens/quiz/cem.jpg') 
    if quantidade==0:
        tela.blit(quant0, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair=True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair=False
        inicio2(disciplina)
                    
    if quantidade==1:
        tela.blit(quant1, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair=True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair=False
        inicio2(disciplina)
    if quantidade==2:
        tela.blit(quant2, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair=True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair=False
        inicio2(disciplina)
    if quantidade==3:
        tela.blit(quant3, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair=True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair=False
        inicio2(disciplina)
    if quantidade==4:
        tela.blit(quant4, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair=True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair=False
        inicio2(disciplina)
    if quantidade==5:
        tela.blit(quant5, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair=True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair=False
        inicio2(disciplina)
    if quantidade==6:
        tela.blit(quant6, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair=True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair=False
        inicio2(disciplina)
    if quantidade==7:
        tela.blit(quant7, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair=True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair=False
        inicio2(disciplina)
    if quantidade==8:
        tela.blit(quant8, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair=True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair=False
        inicio2(disciplina)
    if quantidade==9:
        tela.blit(quant9, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair=True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair=False
        inicio2(disciplina)
    if quantidade==10:
        tela.blit(quant10, (0, 0))
        pygame.display.update()
        audio_placar.play()
        sair=True
        while sair:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        audio_efeito.play()
                        sair=False
        inicio2(disciplina)
    
        
def inicio2(disciplina):
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Game Quiz/{}'.format(disciplina))
    pygame.mixer.init()

    #Audios
    audio_clique=pygame.mixer.Sound('audios/quiz/clique.ogg')

    #Cores
    preto = (0, 0, 0)

    #Imagens
    b1 = pygame.image.load('imagens/quiz/nuvem.png')
    b2 = pygame.image.load('imagens/quiz/nuvem.png')
    b3 = pygame.image.load('imagens/quiz/nuvem.png')
    b4 = pygame.image.load('imagens/quiz/nuvem.png')
    fundo = pygame.image.load('imagens/quiz/fundo.jpeg')
    voltar = pygame.image.load('imagens/quiz/voltar.png')

    #Textos
    pygame.font.init()
    fonte1 = pygame.font.SysFont('Arial Black', 45)
    fonte2 = pygame.font.SysFont('Arial', 20)
    facil = fonte1.render('Fácil', 1, preto)
    medio = fonte1.render('Médio', 1, preto)
    dificil = fonte1.render('Difícil', 1, preto)
    ajuda = fonte1.render('Ajuda', 1, preto)
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
                        gamequiz()
                    if x > 725 and x < 830 and y > 570 and y < 590:
                        audio_clique.play()
                        educa.principal()
                    if x > 100 and x < 370 and y > 235 and y < 385:
                        audio_clique.play()
                        #Inicialização
                        pygame.display.set_caption('Game Quiz/{}/Fácil'.format(disciplina))
                        pygame.mixer.init()

                        #Audios
                        audio_clique=pygame.mixer.Sound('audios/quiz/clique.ogg')
                        audio_efeito=pygame.mixer.Sound('audios/quiz/efeito.ogg')
                        audio_ganhou=pygame.mixer.Sound('audios/quiz/certa.ogg')
                        audio_perdeu=pygame.mixer.Sound('audios/quiz/errada.ogg')
                        #Imagens
                        acertou = pygame.image.load('imagens/quiz/acertou.jpeg')
                        errou = pygame.image.load('imagens/quiz/errou.jpeg')
                        #Imagens de Português
                        pp1 = pygame.image.load('imagens/quiz/pergunta1.jpg')
                        pp2 = pygame.image.load('imagens/quiz/pergunta2.jpg')
                        pp3 = pygame.image.load('imagens/quiz/pergunta3.jpg')
                        pp4 = pygame.image.load('imagens/quiz/pergunta4.jpg')
                        pp5 = pygame.image.load('imagens/quiz/pergunta5.jpg')
                        pp6 = pygame.image.load('imagens/quiz/pergunta6.jpg')
                        pp7 = pygame.image.load('imagens/quiz/pergunta7.jpg')
                        pp8 = pygame.image.load('imagens/quiz/pergunta8.jpg')
                        pp9 = pygame.image.load('imagens/quiz/pergunta9.jpg')
                        pp10 = pygame.image.load('imagens/quiz/pergunta10.jpg')
                        #Imagens de Matemática
                        pm1 = pygame.image.load('imagens/quiz/perguntam1.jpg')
                        pm2 = pygame.image.load('imagens/quiz/perguntam2.jpg')
                        pm3 = pygame.image.load('imagens/quiz/perguntam3.jpg')
                        pm4 = pygame.image.load('imagens/quiz/perguntam4.jpg')
                        pm5 = pygame.image.load('imagens/quiz/perguntam5.jpg')
                        pm6 = pygame.image.load('imagens/quiz/perguntam6.jpg')
                        pm7 = pygame.image.load('imagens/quiz/perguntam7.jpg')
                        pm8 = pygame.image.load('imagens/quiz/perguntam8.jpg')
                        pm9 = pygame.image.load('imagens/quiz/perguntam9.jpg')
                        pm10 = pygame.image.load('imagens/quiz/perguntam10.jpg')
                           
                        #Textos
                        pygame.font.init()
                        fonte = pygame.font.SysFont('Arial', 20)
                        menu = fonte.render('Menu Principal', 1, preto)

                        #Jogo
                        if disciplina=="Português":
                            #1° Questão
                            tela.blit(pp1, (0, 0))
                            pygame.display.update()
                            cont=0
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #2° Questão
                            tela.blit(pp2, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #3° Questão
                            tela.blit(pp3, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #4° Questão
                            tela.blit(pp4, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #5° Questão
                            tela.blit(pp5, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #6° Questão
                            tela.blit(pp6, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #7° Questão
                            tela.blit(pp7, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #8° Questão
                            tela.blit(pp8, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #9° Questão
                            tela.blit(pp9, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #10° Questão
                            tela.blit(pp10, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            placar(cont,disciplina)

                        if disciplina=="Matemática":
                            #1° Questão
                            tela.blit(pm1, (0, 0))
                            pygame.display.update()
                            cont=0
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #2° Questão
                            tela.blit(pm2, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False

                            #3° Questão
                            tela.blit(pm3, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False

                            #4° Questão
                            tela.blit(pm4, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False

                            #5° Questão
                            tela.blit(pm5, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #6° Questão
                            tela.blit(pm6, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #7° Questão
                            tela.blit(pm7, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #8° Questão
                            tela.blit(pm8, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #9° Questão
                            tela.blit(pm9, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #10° Questão
                            tela.blit(pm10, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            placar(cont,disciplina)
                    if x > 430 and x < 700 and y > 235 and y < 385:
                        audio_clique.play()
                        #Inicialização
                        pygame.display.set_caption('Game Quiz/{}/Médio'.format(disciplina))
                        pygame.mixer.init()

                        #Audios
                        audio_efeito=pygame.mixer.Sound('audios/quiz/efeito.ogg')
                        audio_ganhou=pygame.mixer.Sound('audios/quiz/certa.ogg')
                        audio_perdeu=pygame.mixer.Sound('audios/quiz/errada.ogg')
                        
                        #Imagens
                        acertou = pygame.image.load('imagens/quiz/acertou.jpeg')
                        errou = pygame.image.load('imagens/quiz/errou.jpeg')
                        #Imagens de Português
                        pp11 = pygame.image.load('imagens/quiz/pergunta11.jpg')
                        pp12 = pygame.image.load('imagens/quiz/pergunta12.jpg')
                        pp13 = pygame.image.load('imagens/quiz/pergunta13.jpg')
                        pp14 = pygame.image.load('imagens/quiz/pergunta14.jpg')
                        pp15 = pygame.image.load('imagens/quiz/pergunta15.jpg')
                        pp16 = pygame.image.load('imagens/quiz/pergunta16.jpg')
                        pp17 = pygame.image.load('imagens/quiz/pergunta17.jpg')
                        pp18 = pygame.image.load('imagens/quiz/pergunta18.jpg')
                        pp19 = pygame.image.load('imagens/quiz/pergunta19.jpg')
                        pp20 = pygame.image.load('imagens/quiz/pergunta20.jpg')
                        #Imagens de Matemática
                        pm11 = pygame.image.load('imagens/quiz/perguntam11.jpg')
                        pm12 = pygame.image.load('imagens/quiz/perguntam12.jpg')
                        pm13 = pygame.image.load('imagens/quiz/perguntam13.jpg')
                        pm14 = pygame.image.load('imagens/quiz/perguntam14.jpg')
                        pm15 = pygame.image.load('imagens/quiz/perguntam15.jpg')
                        pm16 = pygame.image.load('imagens/quiz/perguntam16.jpg')
                        pm17 = pygame.image.load('imagens/quiz/perguntam17.jpg')
                        pm18 = pygame.image.load('imagens/quiz/perguntam18.jpg')
                        pm19 = pygame.image.load('imagens/quiz/perguntam19.jpg')
                        pm20 = pygame.image.load('imagens/quiz/perguntam10.jpg')
                                                
                        #Textos
                        pygame.font.init()
                        fonte = pygame.font.SysFont('Arial', 20)
                        menu = fonte.render('Menu Principal', 1, preto)
                        #Jogo
                        if disciplina=="Português":
                            #1° Questão
                            tela.blit(pp11, (0, 0))
                            pygame.display.update()
                            cont=0
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #2° Questão
                            tela.blit(pp12, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #3° Questão
                            tela.blit(pp13, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #4° Questão
                            tela.blit(pp14, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #5° Questão
                            tela.blit(pp15, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #6° Questão
                            tela.blit(pp16, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #7° Questão
                            tela.blit(pp17, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #8° Questão
                            tela.blit(pp18, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #9° Questão
                            tela.blit(pp19, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #10° Questão
                            tela.blit(pp20, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            placar(cont,disciplina)
                            
                        if disciplina=="Matemática":
                            #1° Questão
                            tela.blit(pm11, (0, 0))
                            pygame.display.update()
                            cont=0
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #2° Questão
                            tela.blit(pm12, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False

                            #3° Questão
                            tela.blit(pm13, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False

                            #4° Questão
                            tela.blit(pm14, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False

                            #5° Questão
                            tela.blit(pm15, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #6° Questão
                            tela.blit(pm16, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #7° Questão
                            tela.blit(pm17, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #8° Questão
                            tela.blit(pm18, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #9° Questão
                            tela.blit(pm19, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #10° Questão
                            tela.blit(pm20, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            placar(cont,disciplina)
                    if x > 100 and x < 370 and y > 360 and y < 510:
                        audio_clique.play()
                        #Inicialização
                        pygame.display.set_caption('Game Quiz/{}/Difícil'.format(disciplina))
                        pygame.mixer.init()

                        #Audios
                        audio_efeito=pygame.mixer.Sound('audios/quiz/efeito.ogg')
                        audio_ganhou=pygame.mixer.Sound('audios/quiz/certa.ogg')
                        audio_perdeu=pygame.mixer.Sound('audios/quiz/errada.ogg')

                        #Imagens
                        acertou = pygame.image.load('imagens/quiz/acertou.jpeg')
                        errou = pygame.image.load('imagens/quiz/errou.jpeg')
                        #Imagens de Português
                        pp21 = pygame.image.load('imagens/quiz/pergunta21.jpg')
                        pp22 = pygame.image.load('imagens/quiz/pergunta22.jpg')
                        pp23 = pygame.image.load('imagens/quiz/pergunta23.jpg')
                        pp24 = pygame.image.load('imagens/quiz/pergunta24.jpg')
                        pp25 = pygame.image.load('imagens/quiz/pergunta25.jpg')
                        pp26 = pygame.image.load('imagens/quiz/pergunta26.jpg')
                        pp27 = pygame.image.load('imagens/quiz/pergunta27.jpg')
                        pp28 = pygame.image.load('imagens/quiz/pergunta28.jpg')
                        pp29 = pygame.image.load('imagens/quiz/pergunta29.jpg')
                        pp30 = pygame.image.load('imagens/quiz/pergunta30.jpg')
                        #Imagens de Matemática
                        pm21 = pygame.image.load('imagens/quiz/perguntam21.jpg')
                        pm22 = pygame.image.load('imagens/quiz/perguntam22.jpg')
                        pm23 = pygame.image.load('imagens/quiz/perguntam23.jpg')
                        pm24 = pygame.image.load('imagens/quiz/perguntam24.jpg')
                        pm25 = pygame.image.load('imagens/quiz/perguntam25.jpg')
                        pm26 = pygame.image.load('imagens/quiz/perguntam26.jpg')
                        pm27 = pygame.image.load('imagens/quiz/perguntam27.jpg')
                        pm28 = pygame.image.load('imagens/quiz/perguntam28.jpg')
                        pm29 = pygame.image.load('imagens/quiz/perguntam29.jpg')
                        pm30 = pygame.image.load('imagens/quiz/perguntam30.jpg')
                                                
                        #Textos
                        pygame.font.init()
                        fonte = pygame.font.SysFont('Arial', 20)
                        menu = fonte.render('Menu Principal', 1, preto)
                        if disciplina=="Português":
                            #1° Questão
                            tela.blit(pp21, (0, 0))
                            pygame.display.update()
                            cont=0
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #2° Questão
                            tela.blit(pp22, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #3° Questão
                            tela.blit(pp23, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #4° Questão
                            tela.blit(pp24, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #5° Questão
                            tela.blit(pp25, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #6° Questão
                            tela.blit(pp26, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #7° Questão
                            tela.blit(pp27, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #8° Questão
                            tela.blit(pp28, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #9° Questão
                            tela.blit(pp29, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #10° Questão
                            tela.blit(pp30, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            placar(cont,disciplina)

                        if disciplina=="Matemática":
                            #1° Questão
                            tela.blit(pm21, (0, 0))
                            pygame.display.update()
                            cont=0
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #2° Questão
                            tela.blit(pm22, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False

                            #3° Questão
                            tela.blit(pm23, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False

                            #4° Questão
                            tela.blit(pm24, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False

                            #5° Questão
                            tela.blit(pm25, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #6° Questão
                            tela.blit(pm26, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #7° Questão
                            tela.blit(pm27, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #8° Questão
                            tela.blit(pm28, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #9° Questão
                            tela.blit(pm29, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            #10° Questão
                            tela.blit(pm30, (0, 0))
                            pygame.display.update()
                            sair=True
                            while sair:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_b:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_c:
                                            tela.blit(acertou, (0, 0))
                                            pygame.display.update()
                                            audio_ganhou.play()
                                            cont+=1
                                        if event.key == pygame.K_d:
                                            tela.blit(errou, (0, 0))
                                            pygame.display.update()
                                            audio_perdeu.play()
                                        if event.key == pygame.K_RIGHT:
                                            audio_efeito.play()
                                            sair=False
                            placar(cont,disciplina)
                            
                    if x > 430 and x < 700 and y > 360 and y < 510:
                        audio_clique.play()
                        #Inicialização
                        pygame.display.set_caption('Game Quiz/{}/Ajuda'.format(disciplina))
                        #Imagens
                        ajuda = pygame.image.load('imagens/quiz/ajuda.jpg')
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
                                            inicio2(disciplina)
                                        if x > 725 and x < 830 and y > 570 and y < 590:
                                            audio_clique.play()
                                            educa.principal()
                            pygame.time.Clock().tick(30)
                            tela.blit(ajuda, (0, 0))
                            tela.blit(voltar, (10, 10))
                            tela.blit(menu, (725, 570))
                            pygame.display.update()
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(b1,(100, 235))
        b1.blit(facil, (100, 35))
        tela.blit(b2,(430, 235))
        b2.blit(medio, (93, 35))
        tela.blit(b3,(100, 360))
        b3.blit(dificil, (94, 35))
        tela.blit(b4,(430, 360))
        b4.blit(ajuda, (96, 35))
        tela.blit(menu, (725, 570))
        tela.blit(voltar, (10, 10))
        pygame.display.update()

