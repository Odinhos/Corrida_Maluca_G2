import pygame
from tkinter import Tk, Label
from PIL import Image, ImageTk
import time
import random
import os
os.system('cls')

pygame.init()
tamanho = (807,635)
#tamanho1 =(628,723)
clock = pygame.time.Clock()

tela = pygame.display.set_mode( tamanho )
#tela1 = pygame.display.set_mode( tamanho1 )
icone = pygame.image.load("recursos/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
preta = (0,0,0)
fundo = pygame.image.load("Recursos/fundo.png")
carro1 = pygame.image.load("Recursos/carro1.png")
carro2 = pygame.image.load("Recursos/carro2.png")
carro3 = pygame.image.load("Recursos/carro3.png")
bandeiras = pygame.image.load("Recursos/bandeiras.png")



movXCar1 = 0
movXCar2 = 0
movXCar3 = 0
posYCar1 = 50
posYCar2 = 130
posYCar3 = 225
vitoria = pygame.mixer.Sound("Recursos/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("Recursos/trilha.mp3")
pygame.mixer.music.play(-1) #-1 looping, 1,2 3 vezes
acabou = False
somDaVitoria = False
'''
def mostrar_bandeira():
    janela = Tk()
    janela.title("Fim da Corrida")

    # Carregando a imagem (substitua pelo caminho da sua imagem)
    imagem = Image.open("bandeiras.png")
    imagem = imagem.resize((628, 723))  # Redimensionar se necessário
    img = ImageTk.PhotoImage(imagem)

    # Adicionar a imagem a um rótulo
    label = Label(janela, image=img)
    label.pack()

    # Exibir a janela
    janela.mainloop()

# Exemplo de uso:
if __name__ == "__main__":
    print("Corrida finalizada!")
   # mostrar_bandeira()

'''

def mostrar_classificacao(lider, segundo, terceiro, dist1, dist2):
    """
    Exibe a pista e a posição dos carros.
    """
    print("\n" + "=" * 60)
    print("🏎️  CORRIDA MALUCA  🏁")
    print("=" * 60)

    # Mostra a pista com os carros
    pista = ["-" * 50 for _ in range(3)]
    pista[0] = f"{lider} {'-' * (50 - len(lider) - 2)}🥇"
    pista[1] = f"{segundo} {'-' * (50 - len(segundo) - 2)}🥈"
    pista[2] = f"{terceiro} {'-' * (50 - len(terceiro) - 2)}🥉"

    for linha in pista:
        print(linha)

    print("=" * 60)
    print(f"Líder: {lider}")
    print(f"Segundo: {segundo} (Distância para o líder: {dist1:.2f} segundos)")
    print(f"Terceiro: {terceiro} (Distância para o líder: {dist2:.2f} segundos)")
    print("=" * 60)

# Simulação de corrida
carros = ["Carro 3 - Azul", "Carro 2 - Amarelo ", "Carro 1 - Vermelho"]
lider = random.choice(carros)
segundo = random.choice([carro for carro in carros if carro != lider])
terceiro = random.choice([carro for carro in carros if carro != lider and carro != segundo])
dist1 = random.uniform(1.0, 5.0)  # Distância entre líder e segundo
dist2 = dist1 + random.uniform(1.0, 5.0)  # Distância entre líder e terceiro

for _ in range(5):  # Simula 5 atualizações de corrida
    mostrar_classificacao(lider, segundo, terceiro, dist1, dist2)
    time.sleep(2)  # Atualiza a cada 2 segundos
    # Atualiza as distâncias (aleatório para a simulação)
    dist1 = max(0, dist1 + random.uniform(-0.5, 0.5))
    dist2 = max(dist1, dist2 + random.uniform(-0.5, 0.5))


while True:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            quit()
   
    tela.fill( branco )
    tela.blit(fundo, (0,0))
    tela.blit(carro1, (movXCar1,posYCar1))
    tela.blit(carro2, (movXCar2,posYCar2))
    tela.blit(carro3, (movXCar3,posYCar3))
       

 
    
    
    if not acabou :
        movXCar1 = movXCar1 + random.randint(0,10)
        movXCar2 = movXCar2 + random.randint(0,10)
        #movXCar2 = movXCar2 + random.randint(0,10)
        movXCar3 = movXCar3 + random.randint(0,10)
    else:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            
            somDaVitoria = True

        # Abrir a imagem
            imagem = Image.open("Recursos/bandeiras.png")

# Redimensionar a imagem
            imagem_redimensionada = imagem.resize((628,723))
 
 #Exibir a imagem redimensionada
            
            imagem_redimensionada.show() 
            print("Corrida finalizada!")
            janela = Tk()
            janela.title("Fim da Corrida")
        
    
    if movXCar1 > 1000:
        movXCar1 = 0
        posYCar1 = 350
        
    if movXCar2 > 1000:
        movXCar2 = 0
        posYCar2 = 450

    if movXCar3 > 1000:
        movXCar3 = 0
        posYCar3 = 540 
    
    fonte = pygame.font.Font("freesansbold.ttf",60)
    textoVermelho = fonte.render("Vermelho Ganhou!", True, branco)
    textoAmarelo = fonte.render("Amarelo Ganhou!",True, branco)
    textoAzul = fonte.render("Azul Ganhou! ",True, branco)
    bandeiras = fonte.render("PARABÉNS! ",True, branco)
    
    if posYCar1 == 350 and movXCar1 >= 900 and movXCar1 > movXCar2 > movXCar3:
        
        tela.blit(textoVermelho, (200,40))
              
        acabou = True
             
                      
    elif posYCar2 == 450 and movXCar2 >= 900 and movXCar2 > movXCar1 > movXCar3:
        tela.blit(textoAmarelo, (240,135))
    
        acabou = True


    elif posYCar3 == 540 and movXCar3 >= 900 and movXCar3> movXCar2 > movXCar1:
        tela.blit(textoAzul, (230,230))
        acabou = True

    
    pygame.display.update()

    
    clock.tick(60)
    

pygame.quit()

 





