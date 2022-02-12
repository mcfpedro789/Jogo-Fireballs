from graphics import *
import time
import random

def fundo(win):
    win.setBackground(color_rgb(247, 182, 88)) 
    imagem = Image(Point(425, 190), "sprites/city.png")
    imagem.draw(win)
    
def desenha_chao(win):
    imagem = Image(Point(100,480), "sprites/Tile.png")
    imagem.draw(win)
    imagem = Image(Point(350,480), "sprites/Tile.png")
    imagem.draw(win)
    imagem = Image(Point(600,480), "sprites/Tile.png")
    imagem.draw(win)
    imagem = Image(Point(850,480), "sprites/Tile.png")
    imagem.draw(win)



    


class Personagem:
    def __init__(self, janela):
        self.janela = janela
        self.imagem = Image(Point(100,340), "sprites/player-idle-1.png")
        self.rect = Rectangle(Point(100-8.5,340-9.5),Point(100+8.5,340+9.5))
        self.rect.setOutline(color_rgb(247, 182, 88))
        self.centro = self.imagem.getAnchor()
        self.cont_parado = 0
        self.cont_correndo = 0

        self.aleatorio = random.randrange(0,350)
        self.fireball = Image(Point(840,self.aleatorio),'sprites/fireball.png')
        self.rectfire = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
        self.rectfire.setOutline(color_rgb(247, 182, 88))
        self.rectfire.draw(janela)
        self.fireball.draw(janela)

        self.aleatorio = random.randrange(0,350)
        self.fireball2 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
        self.rectfire2 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
        self.rectfire2.setOutline(color_rgb(247, 182, 88))
        self.rectfire2.draw(janela)
        self.fireball2.draw(janela)

        self.aleatorio = random.randrange(0,350)
        self.fireball3 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
        self.rectfire3 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
        self.rectfire3.setOutline(color_rgb(247, 182, 88))
        self.rectfire3.draw(janela)
        self.fireball3.draw(janela)

        self.aleatorio = random.randrange(0,350)
        self.fireball4 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
        self.rectfire4 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
        self.rectfire4.setOutline(color_rgb(247, 182, 88))
        self.rectfire4.draw(janela)
        self.fireball4.draw(janela)

        self.aleatorio = random.randrange(0,350)
        self.fireball5 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
        self.rectfire5 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
        self.rectfire5.setOutline(color_rgb(247, 182, 88))
        self.rectfire5.draw(janela)
        self.fireball5.draw(janela)
            
        self.aleatorio = random.randrange(0,350)
        self.fireball6 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
        self.rectfire6 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
        self.rectfire6.setOutline(color_rgb(247, 182, 88))
        self.rectfire6.draw(janela)
        self.fireball6.draw(janela)

        self.aleatorio = random.randrange(0,350)
        self.fireball7 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
        self.rectfire7 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
        self.rectfire7.setOutline(color_rgb(247, 182, 88))
        self.rectfire7.draw(janela)
        self.fireball7.draw(janela)

        self.aleatorio = random.randrange(0,350)
        self.fireball8 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
        self.rectfire8 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
        self.rectfire8.setOutline(color_rgb(247, 182, 88))
        self.rectfire8.draw(janela)
        self.fireball8.draw(janela)

        self.aleatorio = random.randrange(0,350)
        self.fireball9 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
        self.rectfire9 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
        self.rectfire9.setOutline(color_rgb(247, 182, 88))
        self.rectfire9.draw(janela)
        self.fireball9.draw(janela)

        self.aleatorio = random.randrange(0,350)
        self.fireball10 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
        self.rectfire10 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
        self.rectfire10.setOutline(color_rgb(247, 182, 88))
        self.rectfire10.draw(janela)
        self.fireball10.draw(janela)        

        self.score = 0
        
    def movimento(self,win,para,corre):


        while True:

            self.verifica = self.janela.checkKey()
            print(self.verifica)

            self.fireball.move(-16,0)
            self.rectfire.move(-16,0)
            self.fireball2.move(-16,0)
            self.rectfire2.move(-16,0)
            self.fireball3.move(-16,0)
            self.rectfire3.move(-16,0)
            self.fireball4.move(-16,0)
            self.rectfire4.move(-16,0)
            self.fireball5.move(-16,0)
            self.rectfire5.move(-16,0)
            self.fireball6.move(-16,0)
            self.rectfire6.move(-16,0)
            self.fireball7.move(-16,0)
            self.rectfire7.move(-16,0)
            self.fireball8.move(-16,0)
            self.rectfire8.move(-16,0)
            self.fireball9.move(-16,0)
            self.rectfire9.move(-16,0)
            self.fireball10.move(-16,0)
            self.rectfire10.move(-16,0)

            rect_x = self.rect.getCenter().getX()
            rect_y = self.rect.getCenter().getY()
            rect_width = 17
            rect_height = 19


            rectfire_x = self.rectfire.getCenter().getX()
            rectfire_y = self.rectfire.getCenter().getY()
            rectfire_width = 55
            rectfire_height = 32

            rectfire2_x = self.rectfire2.getCenter().getX()
            rectfire2_y = self.rectfire2.getCenter().getY()
            rectfire2_width = 55
            rectfire2_height = 32

            rectfire3_x = self.rectfire3.getCenter().getX()
            rectfire3_y = self.rectfire3.getCenter().getY()
            rectfire3_width = 55
            rectfire3_height = 32

            rectfire4_x = self.rectfire4.getCenter().getX()
            rectfire4_y = self.rectfire4.getCenter().getY()
            rectfire4_width = 55
            rectfire4_height = 32

            rectfire5_x = self.rectfire5.getCenter().getX()
            rectfire5_y = self.rectfire5.getCenter().getY()
            rectfire5_width = 55
            rectfire5_height = 32

            rectfire6_x = self.rectfire6.getCenter().getX()
            rectfire6_y = self.rectfire6.getCenter().getY()
            rectfire6_width = 55
            rectfire6_height = 32

            rectfire7_x = self.rectfire7.getCenter().getX()
            rectfire7_y = self.rectfire7.getCenter().getY()
            rectfire7_width = 55
            rectfire7_height = 32

            rectfire8_x = self.rectfire8.getCenter().getX()
            rectfire8_y = self.rectfire8.getCenter().getY()
            rectfire8_width = 55
            rectfire8_height = 32

            rectfire9_x = self.rectfire9.getCenter().getX()
            rectfire9_y = self.rectfire9.getCenter().getY()
            rectfire9_width = 55
            rectfire9_height = 32

            rectfire10_x = self.rectfire10.getCenter().getX()
            rectfire10_y = self.rectfire10.getCenter().getY()
            rectfire10_width = 55
            rectfire10_height = 32

#---------------------------------------------------VERIFICA COLISÕES----------------------------------------------------------------------------------------------------------#
            
            if rect_y < rectfire_y-19 or rect_y > rectfire_y+19 or rect_x < rectfire_x-17 or rect_x > rectfire_x+17:
                print('nao colidiu')
            elif rect_x < rectfire_x + rect_width and rect_x + rectfire_width > rectfire_x and rect_y < rectfire_y + rect_height and rect_height + rect_y > rectfire_height :
                win.close()
                menumorte(self)


            if rect_y < rectfire2_y-19 or rect_y > rectfire2_y+19 or rect_x < rectfire2_x-17 or rect_x > rectfire2_x+17:
                print('nao colidiu')
            elif rect_x < rectfire2_x + rect_width and rect_x + rectfire2_width > rectfire2_x and rect_y < rectfire2_y + rect_height and rect_height + rect_y > rectfire2_height :
                win.close()
                menumorte(self)


            if rect_y < rectfire3_y-19 or rect_y > rectfire3_y+19 or rect_x < rectfire3_x-17 or rect_x > rectfire3_x+17:
                print('nao colidiu')
            elif rect_x < rectfire3_x + rect_width and rect_x + rectfire3_width > rectfire3_x and rect_y < rectfire3_y + rect_height and rect_height + rect_y > rectfire3_height :
                win.close()
                menumorte(self)


            if rect_y < rectfire4_y-19 or rect_y > rectfire4_y+19 or rect_x < rectfire4_x-17 or rect_x > rectfire4_x+17:
                print('nao colidiu')
            elif rect_x < rectfire4_x + rect_width and rect_x + rectfire4_width > rectfire4_x and rect_y < rectfire4_y + rect_height and rect_height + rect_y > rectfire4_height :
                win.close()
                menumorte(self)


            if rect_y < rectfire5_y-19 or rect_y > rectfire5_y+19 or rect_x < rectfire5_x-17 or rect_x > rectfire5_x+17:
                print('nao colidiu')
            elif rect_x < rectfire5_x + rect_width and rect_x + rectfire5_width > rectfire5_x and rect_y < rectfire5_y + rect_height and rect_height + rect_y > rectfire5_height :
                win.close()
                menumorte(self)


            if rect_y < rectfire6_y-19 or rect_y > rectfire6_y+19 or rect_x < rectfire6_x-17 or rect_x > rectfire6_x+17:
                print('nao colidiu')
            elif rect_x < rectfire6_x + rect_width and rect_x + rectfire6_width > rectfire6_x and rect_y < rectfire6_y + rect_height and rect_height + rect_y > rectfire6_height :
                win.close()
                menumorte(self)


            if rect_y < rectfire7_y-19 or rect_y > rectfire7_y+19 or rect_x < rectfire7_x-17 or rect_x > rectfire7_x+17:
                print('nao colidiu')
            elif rect_x < rectfire7_x + rect_width and rect_x + rectfire7_width > rectfire7_x and rect_y < rectfire7_y + rect_height and rect_height + rect_y > rectfire7_height :
                win.close()
                menumorte(self)


            if rect_y < rectfire8_y-19 or rect_y > rectfire8_y+19 or rect_x < rectfire8_x-17 or rect_x > rectfire8_x+17:
                print('nao colidiu')
            elif rect_x < rectfire8_x + rect_width and rect_x + rectfire8_width > rectfire8_x and rect_y < rectfire8_y + rect_height and rect_height + rect_y > rectfire8_height :
                win.close()
                menumorte(self)


            if rect_y < rectfire9_y-19 or rect_y > rectfire9_y+19 or rect_x < rectfire9_x-17 or rect_x > rectfire9_x+17:
                print('nao colidiu')
            elif rect_x < rectfire9_x + rect_width and rect_x + rectfire9_width > rectfire9_x and rect_y < rectfire9_y + rect_height and rect_height + rect_y > rectfire9_height :
                win.close()
                menumorte(self)


            if rect_y < rectfire10_y-19 or rect_y > rectfire10_y+19 or rect_x < rectfire10_x-17 or rect_x > rectfire10_x+17:
                print('nao colidiu')     
            elif rect_x < rectfire10_x + rect_width and rect_x + rectfire10_width > rectfire10_x and rect_y < rectfire10_y + rect_height and rect_height + rect_y > rectfire10_height :
                win.close()
                menumorte(self)
                
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
            # verificando a tecla pressionada, caso for a seta direita, move para direita
            if self.verifica == "Right":
                self.imagem.move(15,0)
                self.rect.move(15,0)
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, corre[self.cont_correndo])
                self.imagem.draw(self.janela)
                self.rect.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.rect.undraw()
                self.cont_correndo+=1
                time.sleep(.001)
                if self.cont_correndo >= 3:
                    self.cont_correndo = 0

            # verificando a tecla pressionada, caso for a seta esquerda, move para esquerda 
            elif self.verifica == "Left":
                self.imagem.move(-15, 0)
                self.rect.move(-15,0)
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, corre[self.cont_correndo])
                self.imagem.draw(self.janela)
                self.rect.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.rect.undraw()
                self.cont_correndo+=1
                time.sleep(.001)
                if self.cont_correndo >= 3:
                    self.cont_correndo = 0

            # verificando a tecla pressionada, caso for a seta para cima, move para cima            
            elif self.verifica == "Up":
                self.imagem.move(0,-15)
                self.rect.move(0,-15)
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, corre[self.cont_correndo])
                self.imagem.draw(self.janela)
                self.rect.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.rect.undraw()
                self.cont_correndo+=1
                time.sleep(.001)
                if self.cont_correndo >= 3:
                    self.cont_correndo = 0

            # verificando a tecla pressionada, caso for a seta para baixo, move para baixo 
            elif self.verifica == "Down":
                self.imagem.move(0, 15)
                self.rect.move(0,15)
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, corre[self.cont_correndo])
                self.imagem.draw(self.janela)
                self.rect.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.rect.undraw()
                self.cont_correndo+=1
                time.sleep(.001)
                if self.cont_correndo >= 3:
                    self.cont_correndo = 0
            
            ## retângulo anda junto com boneco
            elif rect_y >= 355:
                self.imagem.move(0,-50)
                self.rect.move(0,-50)
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, corre[self.cont_correndo])
                self.imagem.draw(self.janela)
                self.rect.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.rect.undraw()
                self.cont_correndo +=1
                time.sleep(.001)
                if self.cont_correndo >=3:
                    self.cont_correndo = 0

            ## retângulo anda junto com boneco
            elif rect_y <= 0:
                self.imagem.move(0,50)
                self.rect.move(0,50)
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, corre[self.cont_correndo])
                self.imagem.draw(self.janela)
                self.rect.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.rect.undraw()
                self.cont_correndo +=1
                time.sleep(.001)
                if self.cont_correndo >=3:
                    self.cont_correndo = 0


                
            # se a bola de fogo ja saiu da tela, cria uma nova onda de bolas de fogo
            ## desenha o score
            elif rectfire_x == -56:
                if self.score == 0:
                    self.score += 1
                    text_ = Text(Point(220,30),self.score)
                    text_.setSize(36)
                    text_.setFace('helvetica')
                    text_.setStyle('bold')
                    text_.draw(self.janela)
               
                # se o score ja for maior que um, apaga e desenha novamente               
                else:
                    text_.undraw()
                    self.score += 1
                    text_ = Text(Point(220,30),self.score)
                    text_.setSize(36)
                    text_.setFace('helvetica')
                    text_.setStyle('bold')
                    text_.draw(self.janela)                    


                self.aleatorio = random.randrange(0,350)
                self.fireball = Image(Point(840,self.aleatorio),'sprites/fireball.png')
                self.rectfire = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
                self.rectfire.setOutline(color_rgb(247, 182, 88))
                self.rectfire.draw(win)
                self.fireball.draw(win)

                self.aleatorio = random.randrange(0,350)
                self.fireball2 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
                self.rectfire2 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
                self.rectfire2.setOutline(color_rgb(247, 182, 88))
                self.rectfire2.draw(win)
                self.fireball2.draw(win)

                self.aleatorio = random.randrange(0,350)
                self.fireball3 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
                self.rectfire3 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
                self.rectfire3.setOutline(color_rgb(247, 182, 88))
                self.rectfire3.draw(win)
                self.fireball3.draw(win)

                self.aleatorio = random.randrange(0,350)
                self.fireball4 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
                self.rectfire4 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
                self.rectfire4.setOutline(color_rgb(247, 182, 88))
                self.rectfire4.draw(win)
                self.fireball4.draw(win)

                self.aleatorio = random.randrange(0,350)
                self.fireball5 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
                self.rectfire5 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
                self.rectfire5.setOutline(color_rgb(247, 182, 88))
                self.rectfire5.draw(win)
                self.fireball5.draw(win)
                    
                self.aleatorio = random.randrange(0,350)
                self.fireball6 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
                self.rectfire6 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
                self.rectfire6.setOutline(color_rgb(247, 182, 88))
                self.rectfire6.draw(win)
                self.fireball6.draw(win)

                self.aleatorio = random.randrange(0,350)
                self.fireball7 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
                self.rectfire7 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
                self.rectfire7.setOutline(color_rgb(247, 182, 88))
                self.rectfire7.draw(win)
                self.fireball7.draw(win)

                self.aleatorio = random.randrange(0,350)
                self.fireball8 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
                self.rectfire8 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
                self.rectfire8.setOutline(color_rgb(247, 182, 88))
                self.rectfire8.draw(win)
                self.fireball8.draw(win)

                self.aleatorio = random.randrange(0,350)
                self.fireball9 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
                self.rectfire9 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
                self.rectfire9.setOutline(color_rgb(247, 182, 88))
                self.rectfire9.draw(win)
                self.fireball9.draw(win)

                self.aleatorio = random.randrange(0,350)
                self.fireball10 = Image(Point(840,self.aleatorio),'sprites/fireball.png')
                self.rectfire10 = Rectangle(Point(840-27.5,self.aleatorio-16),Point(840+27.5,self.aleatorio+16))
                self.rectfire10.setOutline(color_rgb(247, 182, 88))
                self.rectfire10.draw(win)
                self.fireball10.draw(win)

            #animação personagem parado                
            else:
                if self.cont_parado >= 3:
                    self.cont_parado = 0
                self.imagem = Image(self.centro, para[self.cont_parado])
                self.imagem.draw(self.janela)
                self.rect.draw(self.janela)
                time.sleep(.09)
                self.imagem.undraw()
                self.rect.undraw()
                self.cont_parado+=1

#função principal
def main (Titulo: str, largura: int, altura:int,autoflush=True):
    #cria janela 
    win = GraphWin(Titulo, largura, altura)
    #desenha fundo e o chão
    #menu(win)

    fundo(win)
    desenha_chao(win)
    #cria objeto, instanciando a classe
    heroi = Personagem(win)

    text_ = Text(Point(100,30),'SCORE:')
    text_.setSize(36)
    text_.setFace('helvetica')
    text_.setStyle('bold')
    text_.draw(win)   

    #heroi.verificador(win)
    #listas com as sprites do personagem, cada string é o nome de uma imagem
    parado = ["sprites/player-idle-1.png", "sprites/player-idle-2.png", "sprites/player-idle-3.png"]
    correndo = ["sprites/player-run-1.png", "sprites/player-run-2.png", "sprites/player-run-3.png"]
    #chamando a função para realizar o movimento do personagem
    heroi.movimento(win, parado, correndo)


    
    win.getMouse()
    win.close()


def menumorte(self):
    menuumorte = GraphWin('Menu', 850, 478)
    imagem = Image(Point(425,250),'sprites/gameover.png')
    imagem.draw(menuumorte)
    iniciar = Rectangle(Point(550,224),Point(800,274))
    iniciar.setFill('yellow3')
    iniciar.draw(menuumorte)
    text_ = Text(Point(675,249),'RESTART')
    text_.setSize(36)
    text_.setFace('helvetica')
    text_.setStyle('bold')
    text_.draw(menuumorte)

    score = Text(Point(200,249),'SCORE = {}' .format(self.score))
    score.setSize(36)
    score.setFace('helvetica')
    score.setStyle('bold')
    score.draw(menuumorte)


    mouse = menuumorte.getMouse()
    X = mouse.getX()
    Y = mouse.getY()

    def check():
        if X > 550 and X < 800 and Y > 224 and Y < 274:
            menuumorte.close()
            main("Animação", 850, 478)
        else:
            check()
    check()

    menuumorte.getMouse()
    menuumorte.close()


def menu():
    menuu = GraphWin('Menu', 850, 478)
    imagem = Image(Point(425,0),'sprites/citymenu.png')
    imagem.draw(menuu)
    #win.setBackground('blue')
    iniciar = Rectangle(Point(300,70),Point(550,120))
    iniciar.setFill('yellow3')
    iniciar.draw(menuu)
    text_ = Text(Point(425,95),'JOGAR')
    text_.setSize(36)
    text_.setFace('helvetica')
    text_.setStyle('bold')
    text_.draw(menuu)

    text_ = Text(Point(425,25),'FIREBALLS!')
    text_.setSize(36)
    text_.setFace('helvetica')
    text_.setStyle('bold')
    text_.setTextColor('blue')
    text_.draw(menuu)

    tutorial = Text(Point(425,300),'Jogabilidade:\nSETAS')
    tutorial.setSize(36)
    tutorial.setFace('helvetica')
    tutorial.setStyle('bold')
    tutorial.setTextColor('orange')
    tutorial.draw(menuu)

    mouse = menuu.getMouse()
    X = mouse.getX()
    Y = mouse.getY()

    def check():
        if X > 300 and X < 550 and Y > 70 and Y < 120:
            menuu.close()
            main("Animação", 850, 478)
        else:
            check()
    check()

    menuu.getMouse()
    menuu.close()

menu()