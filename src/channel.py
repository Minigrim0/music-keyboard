import pygame

from src.constant import fonts, DURATION_MAX


class channel(object):
    def __init__(self, duration=8, tempo=0.25, instrument="synth", volume=1, pan=0):
        self.duration = duration
        self.tempo = tempo
        self.instrument = instrument
        self.pan = pan
        self.volume = volume
        self.selected = False
        self.generate()

    def generate(self):
        self.text_image = fonts[15].render(
            self.instrument, 1, (200, 200, 200))
        self.selected_text_image = fonts[15].render(
            self.instrument, 1, (100, 200, 100))

    def select(self, selected=False):
        self.selected = selected

    def draw(self, screen, Nb):
        pygame.draw.line(screen, (0, 0, 0), (5, 50), (795, 50))
        if self.selected:
            screen.blit(
                self.selected_text_image,
                (5, 67 + Nb*45)
            )
        else:
            screen.blit(
                self.text_image,
                (5, 67 + Nb*45)
            )

        pygame.draw.rect(
            screen,
            (150, 150, 150),
            pygame.Rect(
                (100, 55 + Nb*45),
                (600, 40)
            )
        )
        for x in range(DURATION_MAX*10):
            if (x % 10) != 0:
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    (100 + x*(600/(DURATION_MAX*10)), 55+Nb*45),
                    (100 + x*(600/(DURATION_MAX*10)), (57+abs(x % 10-5))+Nb*45)
                )
            else:
                pygame.draw.line(
                    screen,
                    (150, 0, 0),
                    (100 + x*(600/(DURATION_MAX*10)), 55+Nb*45),
                    (100 + x*(600/(DURATION_MAX*10)), (67+Nb*45))
                )
