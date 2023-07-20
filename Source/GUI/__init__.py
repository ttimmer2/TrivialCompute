# Import
import sys
import pygame

# Configuration
pygame.init()
fps = 60
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []


class Button():
  def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.onclickFunction = onclickFunction
    self.onePress = onePress

    self.fillColors = {
      'normal': '#DEDEDE',
      'hover': '#666666',
      'pressed': '#333333',
    }

    self.buttonSurface = pygame.Surface((self.width, self.height))
    self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

    self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

    self.alreadyPressed = False

    objects.append(self)

  def process(self):

    mousePos = pygame.mouse.get_pos()

    self.buttonSurface.fill(self.fillColors['normal'])
    if self.buttonRect.collidepoint(mousePos):
      self.buttonSurface.fill(self.fillColors['hover'])

      if pygame.mouse.get_pressed(num_buttons=3)[0]:
        self.buttonSurface.fill(self.fillColors['pressed'])

        if self.onePress:
          self.onclickFunction()

        elif not self.alreadyPressed:
          self.onclickFunction()
          self.alreadyPressed = True

      else:
        self.alreadyPressed = False

    self.buttonSurface.blit(self.buttonSurf, [
      self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
      self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
    ])
    screen.blit(self.buttonSurface, self.buttonRect)


def myFunction():
  print('Button Pressed')


# Game loops.

#Title screen and start
  def titleScreen():
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          #sys.exit()
        screen.fill((255, 255, 255))

        trivialButton = Button(125, 150, 400, 80, 'TRIVIAL COMPUTE', myFunction)
        startButton = Button(225, 300, 200, 40, 'START', myFunction)
        quitButton = Button(500, 400, 100, 50, 'QUIT', myFunction, True)

        pygame.display.update()
        pygame.display.flip()

#Main menu - Play, Continue Game, Question Setting, Help & Options, Back
  def mainMenu():
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.fill((255, 255, 255))

        playButton = Button(225, 300, 100, 40, 'PLAY', myFunction)
        continueButton = Button(225, 300, 200, 40, 'CONTINUE GAME', myFunction)
        settingButton = Button(225, 300, 300, 40, 'QUESTION SETTINGS', myFunction)
        helpButton = Button(225, 300, 400, 40, 'HELP & OPTIONS', myFunction)

        pygame.display.update()
        pygame.display.flip()

  def selectPlay():
    while True:

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.fill((255, 255, 255))

        chemistryButton = Button(225, 300, 100, 40, 'CHEMISTRY', myFunction)
        sportsButton = Button(225, 300, 200, 40, 'SPORTS', myFunction)
        musicButton = Button(225, 300, 300, 40, 'MUSIC', myFunction)
        mathButton = Button(225, 300, 400, 40, 'MATH', myFunction)
        historyButton = Button(225, 300, 400, 40, 'HISTORY', myFunction)
        geographyButton = Button(225, 300, 400, 40, 'GEOGRAPHY', myFunction)
        nextButton = Button(500, 400, 100, 50, 'NEXT', myFunction)

  def continueGame():
    while True:
      screen.fill((255, 255, 255))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.fill((255, 255, 255))

        addButton = Button(225, 300, 100, 40, 'ADD', myFunction)
        chemistryButton = Button(225, 300, 100, 40, 'CHEMISTRY', myFunction)
        sportsButton = Button(225, 300, 200, 40, 'SPORTS', myFunction)
        musicButton = Button(225, 300, 300, 40, 'MUSIC', myFunction)
        mathButton = Button(225, 300, 400, 40, 'MATH', myFunction)
        historyButton = Button(225, 300, 400, 40, 'HISTORY', myFunction)
        geographyButton = Button(225, 300, 400, 40, 'GEOGRAPHY', myFunction)
        nextButton = Button(500, 400, 100, 50, 'NEXT', myFunction)

  def questionSettings():
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.fill((255, 255, 255))

        addButton = Button(225, 300, 100, 40, 'ADD', myFunction)
        chemistryButton = Button(225, 300, 100, 40, 'CHEMISTRY', myFunction)
        sportsButton = Button(225, 300, 200, 40, 'SPORTS', myFunction)
        musicButton = Button(225, 300, 300, 40, 'MUSIC', myFunction)
        mathButton = Button(225, 300, 400, 40, 'MATH', myFunction)
        historyButton = Button(225, 300, 400, 40, 'HISTORY', myFunction)
        geographyButton = Button(225, 300, 400, 40, 'GEOGRAPHY', myFunction)
        nextButton = Button(500, 400, 100, 50, 'NEXT', myFunction)

  def helpOptions():
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()

        screen.fill((255, 255, 255))

        chemistryButton = Button(225, 300, 100, 40, 'CHEMISTRY', myFunction)
        sportsButton = Button(225, 300, 200, 40, 'SPORTS', myFunction)
        musicButton = Button(225, 300, 300, 40, 'MUSIC', myFunction)

  for object in objects:
    object.process()

  pygame.display.flip()
