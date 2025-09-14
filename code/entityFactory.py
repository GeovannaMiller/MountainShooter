# #!/usr/bin/python
# # -*- coding: utf-8 -*-
#
# # from code.background import Background
# #
# # class EntityFactory:
# #     # def __init__(self):
# #     #     pass
# #
# #     @staticmethod
# #     def get_entity(entity_name: str, position=(0,0)):
# #         match entity_name:
# #             case 'Level1Bg':
# #                 list_bg = []
# #                 for i in range(10):
# #                     list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
# #                 return list_bg
# #         return None
# #
# TESTE:

#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import os
from code.background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                total_imgs = 10
                loaded_images = []

                # 1. Carrega todas as imagens
                for i in range(total_imgs):
                    file_name = f'Level1Bg{i}.png'
                    path = os.path.join('./asset', file_name)
                    if os.path.isfile(path):
                        img = pygame.image.load(path).convert()
                        loaded_images.append(img)
                    else:
                        print(f"Imagem não encontrada: {file_name}")

                if not loaded_images:
                    return None

                # 2. Calcula dimensões totais da imagem original
                img_width, img_height = loaded_images[0].get_size()
                total_width = img_width * len(loaded_images)

                # 3. Cria superfície temporária para colar tudo lado a lado
                full_surface = pygame.Surface((total_width, img_height))
                for idx, img in enumerate(loaded_images):
                    full_surface.blit(img, (idx * img_width, 0))

                # 4. Redimensiona para caber na tela do jogo (ex: 600x480)
                scaled_surface = pygame.transform.scale(full_surface, (WIN_WIDTH, WIN_HEIGHT))

                # 5. Cria um Background com a imagem final
                bg = Background("Level1Bg", (0, 0))
                bg.surf = scaled_surface
                bg.rect = scaled_surface.get_rect(topleft=(0, 0))

                return [bg]
        return None
