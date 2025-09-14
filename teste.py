import pygame

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Janela Teste Pygame")

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((0, 0, 0))  # Fundo preto
    pygame.display.update()

pygame.quit()
