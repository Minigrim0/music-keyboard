import pygame

from src.constant import fonts, DURATION_MAX


class channel(object):
    def __init__(self, s, duration=8, instrument="piano", volume=1, pan=0):
        self.duration = duration
        self.instrument_name = instrument
        self.instrument = s.new_part(instrument)
        self.pan = pan
        self.volume = volume
        self.selected = False
        self.generate()

    def generate(self):
        self.text_image = fonts[15].render(
            self.instrument_name, 1, (200, 200, 200))
        self.selected_text_image = fonts[15].render(
            self.instrument_name, 1, (100, 200, 100))

        self.background_rect = pygame.Surface((600, 40))
        pygame.draw.rect(
            self.background_rect,
            (150, 150, 150),
            pygame.Rect(
                (0, 0),
                (600, 40)
            )
        )
        for x in range(DURATION_MAX*10):
            if (x % 10) != 0:
                pygame.draw.line(
                    self.background_rect,
                    (0, 0, 0),
                    (x*(600/(DURATION_MAX*10)), 0),
                    (x*(600/(DURATION_MAX*10)), (2+abs(x % 10-5)))
                )
            else:
                pygame.draw.line(
                    self.background_rect,
                    (150, 0, 0),
                    (x*(600/(DURATION_MAX*10)), 0),
                    (x*(600/(DURATION_MAX*10)), 12)
                )

    def select(self, selected=False):
        self.selected = selected

    def changeVolume(self, deltaVolume):
        self.volume += deltaVolume

    def playNote(self, note):
        self.instrument.play_note(note, 1, 1, blocking=False)

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

        screen.blit(self.background_rect, (100, 55 + Nb*45))
