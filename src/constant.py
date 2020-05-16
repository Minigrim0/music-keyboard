import pygame

from src.button import Button

CHANNEL = 0  # CURRENTLY SELECTED CHANNEL
TIME_POS = 0  # POSITION IN TIME

DURATION_MAX = 8  # LOOP DURATION (seconds)
NB_CHANNELS = 6  # NUMBER OF CHANNELS

# Control vars
running = True

# IMAGES

pygame.init()

BACKGROUND_COLOR = (100, 100, 100)

background = pygame.Surface((840, 600))
background.fill(BACKGROUND_COLOR)

# TOP LABELS
# Red circle ON
recording_label = pygame.Surface((40, 40))
recording_label.fill(BACKGROUND_COLOR)
pygame.draw.circle(recording_label, (250, 50, 50), (20, 20), 15)

# Red circle OFF
not_recording_label = pygame.Surface((40, 40))
not_recording_label.fill(BACKGROUND_COLOR)
pygame.draw.circle(not_recording_label, (150, 100, 100), (20, 20), 15)

# White triangle ON
play_label_on = pygame.Surface((40, 40))
play_label_on.fill(BACKGROUND_COLOR)
pygame.draw.polygon(
    play_label_on, (200, 200, 200), [(5, 5), (5, 35), (35, 20)])

# White rects ON
pause_label_on = pygame.Surface((40, 40))
pause_label_on.fill(BACKGROUND_COLOR)
pygame.draw.rect(
    pause_label_on, (200, 200, 200), pygame.Rect((5, 5), (10, 30)))
pygame.draw.rect(
    pause_label_on, (200, 200, 200), pygame.Rect((20, 5), (10, 30)))

# DoubleTriangleBackwards
back_label = pygame.Surface((60, 40))
back_label.fill((BACKGROUND_COLOR))
pygame.draw.rect(back_label, (200, 200, 200), pygame.Rect((5, 5), (5, 30)))
pygame.draw.polygon(back_label, (200, 200, 200), [(7, 20), (25, 5), (25, 35)])
pygame.draw.polygon(back_label, (200, 200, 200), [(20, 20), (38, 5), (38, 35)])

# BUTTONS
recordingButton = Button(
    (5, 5), (40, 40), recording_label, not_recording_label, True)

playButton = Button((50, 5), (40, 40), pause_label_on, play_label_on, True)
back_button = Button((95, 5), (60, 40), back_label, back_label, True)

# FONTS
fonts = {}
for x in [12, 15, 20, 25, 35, 40, 50, 75]:
    fonts[x] = pygame.font.SysFont("monospace", x)
