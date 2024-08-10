from random import randint
import pygame
from pygame import font
from pygame import display
from pygame import image
from pygame.image import load
from pygame.transform import scale
from pygame.sprite import Sprite, Group, GroupSingle, groupcollide
from pygame import event
from pygame.locals import QUIT, KEYUP, K_SPACE
from pygame.time import Clock

pygame.init()

tamanho = (800,600)

fonte = font.SysFont('comicsans', 30,)
fonte_perdeu = font.SysFont('comicsans', 300)


superficie = display.set_mode(
    size = tamanho,
    display = 1
)
display.set_caption(
    'Isaac Newton e Suas Maças'
)

fundo = scale(
    load('images/windows-xp.jpg'),
    tamanho
)

class IssacFausto(Sprite):
    def __init__(self,macas):
        super().__init__()
        self.image = load('images/small_preview_rev_1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (tamanho[0] // 2, tamanho[1] - self.rect.height // 2 - 25)
        self.macas = macas
        self.velocidade = 5



    def update(self):
        keys = pygame.key.get_pressed()

        macas_fonte = fonte.render(f'Maças: {100 - len(self.macas)}',
            True,
            (0, 0, 0)
        )
        superficie.blit(macas_fonte,(20,20))

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocidade

        # Restringe os limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > tamanho[0]:
            self.rect.right = tamanho[0]
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > tamanho[1]:
            self.rect.bottom = tamanho[1]

# Defina a classe Maca
class Maca(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = image.load('images/apple.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidade = 1

    def update(self):
        self.rect.y += self.velocidade

        if self.rect.y > tamanho[1]:
            self.kill()


# Imagem do Virus
class Virus(Sprite):
    def __init__(self, macas):
        super().__init__()
        self.image = load('images/desenho-de-arvore_preview_rev_1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (tamanho[0] // 2, self.rect.height // 2)
        self.macas = macas

    def update(self):
        if randint(0, 100) < 2:
            # Faz as maçãs surgirem em posições x aleatórias da largura da tela
            x_position = randint(0, tamanho[0])
            # As maçãs surgem da metade superior da árvore
            y_position = self.rect.top + randint(0, self.rect.height // 2)
            self.macas.add(Maca(x_position, y_position))


grupo_macas = Group()
issacfausto = IssacFausto(grupo_macas)
grupo_issac = GroupSingle(issacfausto)

virus = Virus(grupo_macas)
grupo_inimigos = Group(virus)

clock = Clock()
perdeu = False



# Main loop flag
running = True

# Main loop
while running:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            running = False

    # Desenhar fundo
    superficie.blit(fundo, (0, 0))

    # Atualiza Issac e maças
    issacfausto.update()
    issacfausto.macas.update()
    grupo_inimigos.update()

    # Desenha os sprites
    grupo_inimigos.draw(superficie)  # Desenha a árvore (Virus)
    superficie.blit(issacfausto.image, issacfausto.rect)  # Desenha Isaac primeiro
    issacfausto.macas.draw(superficie)  # Desenha as maçãs por último, na frente da árvore

    if pygame.sprite.spritecollide(issacfausto, grupo_macas, True):
        perdeu = True

    # Update the display
    display.update()

    clock.tick(60)

pygame.quit()
