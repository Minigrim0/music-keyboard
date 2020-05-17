# import sys
import pygame
import time
import pygame.locals as locals
from scamp import Session

# sys.path.insert(0, "src/")

from src.channel import channel
from src.constant import TIME_POS, DURATION_MAX, \
    running, playButton, recordingButton, \
    background, back_button, fonts

instruments = ["piano", "guitar", "trumpet", "violin"]
screen = pygame.display.set_mode((800, 480))

s = Session()
chan = [channel(s, instrument=x) for x in instruments]
chan[0].select(True)
selected_chan = 0

startTime = time.time()
timeElapsed = 0

keys = {pygame.locals.K_a: 48, 97: 60, 113: 72,
        pygame.locals.K_TAB: 49, 122: 61, 115: 73,
        9: 50, 101: 62, 100: 74,
        39: 51, 114: 63, 102: 75,
        40: 52, 116: 64, 103: 76,
        167: 53, 121: 65, 104: 77,
        232: 54, 117: 66, 106: 78,
        33: 55, 105: 67, 107: 79,
        231: 56, 111: 68, 108: 80,
        224: 57, 112: 69, 109: 81,
        41: 58, 94: 70, 249: 82,
        45: 59, 36: 71, 181: 83}

while running:

    startTime = time.time()

    # UPDATING TIMEBAR
    if playButton.getValue():
        TIME_POS += timeElapsed
        if TIME_POS > DURATION_MAX:
            TIME_POS = TIME_POS % DURATION_MAX

    # Handling events
    for event in pygame.event.get():
        if event.type == locals.QUIT:
            running = False
        else:
            if event.type == locals.KEYDOWN:
                if event.key == locals.K_SPACE:
                    recordingButton.toggle()
                elif event.key == locals.K_RETURN:
                    playButton.toggle()
                elif event.key == locals.K_UP:
                    chan[selected_chan].select(False)
                    selected_chan -= 1
                    if selected_chan < 0:
                        selected_chan = len(chan)-1
                    chan[selected_chan].select(True)
                elif event.key == locals.K_DOWN:
                    chan[selected_chan].select(False)
                    selected_chan += 1
                    if selected_chan == len(chan):
                        selected_chan = 0
                    chan[selected_chan].select(True)
                elif event.key in keys.keys():
                    chan[selected_chan].playNote(keys[event.key])
                else:
                    print(event.key)

    # Displaying
    screen.blit(background, (0, 0))

    recordingButton.draw(screen)
    playButton.draw(screen)
    back_button.draw(screen)

    for x in range(len(chan)):
        chan[x].draw(screen, x)

    pygame.draw.line(
        screen, (255, 0, 0), (100 + 600*(TIME_POS/DURATION_MAX), 53),
        (100 + 600*(TIME_POS/DURATION_MAX), 415))

    timeImage = fonts[35].render(str(TIME_POS)[:5], 1, (255, 255, 255))
    screen.blit(timeImage, (795-timeImage.get_width(), 5))
    pygame.display.flip()

    timeElapsed = time.time() - startTime
    startTime = time.time()
