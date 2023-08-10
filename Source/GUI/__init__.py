import sys
import pygame

# Configuration
pygame.init()
fps = 60
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont('Arial', 40)

objects = []


# work meeting notes - separate if statements, instead of nested if statements
#Test for onePress instead onclickFunction

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

  def draw(self, screen):
    pass


def myFunction():
  print('Button Pressed')

#create button instances

#continue game
idleButton = Button(125, 150, 400, 80, 'CONTINUE GAME?', myFunction)

#title screen buttons
trivialButton = Button(125, 150, 400, 80, 'TRIVIAL COMPUTE', myFunction)
startButton = Button(225, 300, 200, 40, 'START', myFunction)
quitButton = Button(500, 400, 100, 50, 'QUIT', myFunction, True)

#main menu buttons
mainMenuButton = Button(10, 10, 300, 50, 'MAIN MENU        ', myFunction)
playButton = Button(50, 80, 350, 150, 'PLAY               ', myFunction)
continueButton = Button(50, 240, 200, 220, 'CONTINUE', myFunction)
questionsButton = Button(410, 80, 200, 300, 'QUESTIONS', myFunction)
helpButton = Button(260, 390, 350, 70, '       HELP & OPTIONS', myFunction)
backButton = Button(225, 500, 300, 80, 'BACK', myFunction)

#play screen and continue game buttons
configurationButton = Button(10, 10, 300, 50, 'CONFIGURATION      ', myFunction)
chemistryButton = Button(225, 300, 50, 50, 'CHEMISTRY', myFunction)
sportsButton = Button(225, 300, 200, 40, 'SPORTS', myFunction)
musicButton = Button(225, 300, 300, 40, 'MUSIC', myFunction)
mathButton = Button(225, 300, 400, 40, 'MATH', myFunction)
historyButton = Button(225, 300, 400, 40, 'HISTORY', myFunction)
geographyButton = Button(225, 300, 400, 40, 'GEOGRAPHY', myFunction)
nextButton = Button(500, 400, 100, 50, 'NEXT', myFunction)

#add players buttons
selectButton = Button(10, 10, 400, 50, 'SELECT CHARACTER', myFunction)

# DRAW CIRCLES
pygame.draw.circle(screen, (255, 211, 67), (100, 200), 40)
pygame.draw.circle(screen, (255, 0, 0), (250, 200), 40)
pygame.draw.circle(screen, (0, 0, 255), (400, 200), 40)
pygame.draw.circle(screen, (0, 255, 0), (550, 200), 40)

# ENTER NAME
name1Button = Button(10, 250, 150, 50, 'PLAYER 1', myFunction)
name2Button = Button(170, 250, 150, 50, 'PLAYER 2', myFunction)
name3Button = Button(330, 250, 150, 50, 'PLAYER 3', myFunction)
name4Button = Button(490, 250, 150, 50, 'PLAYER 4', myFunction)

# OTHER
readyButton = Button(510, 420, 125, 50, 'READY', myFunction)
back2Button = Button(10, 420, 100, 50, 'BACK', myFunction)

#question settings buttons
# (excluded)settingButton = Button(10, 10, 400, 50, 'QUESTION SETTINGS', myFunction)
select2Button = Button(10, 10, 400, 50, 'SELECT A CATEGORY', myFunction)
addButton = Button(50, 150, 150, 100, '+', myFunction)
sports2Button = Button(225, 150, 150, 100, 'SPORTS', myFunction)
music2Button = Button(400, 150, 150, 100, 'MUSIC', myFunction)
math2Button = Button(650, 150, 150, 100, 'MATH', myFunction)
history2Button = Button(50, 300, 150, 100, 'HISTORY', myFunction)
artButton = Button(225, 300, 150, 100, 'ART', myFunction)
# (excluded)geographyButton = Button(225, 300, 150, 100, 'GEOGRAPHY', myFunction)
scienceButton = Button(400, 300, 150, 100, 'SCIENCE', myFunction)
# (excluded)chemistryButton = Button(400, 300, 150, 100, 'CHEMISTRY', myFunction)
back3Button = Button(525, 420, 100, 50, 'BACK', myFunction)

#help buttons
help2Button = Button(0, 10, 350, 50, '   HELP AND OPTIONS      ', myFunction)
play3Button = Button(30, 80, 350, 300, 'HOW TO PLAY', myFunction)
settingOneButton = Button(410, 80, 200, 80, 'SETTING', myFunction)
settingTwoButton = Button(410, 190, 200, 80, 'SETTING', myFunction)
settingThreeButton = Button(410, 300, 200, 80, 'SETTING', myFunction)
back4Button = Button(525, 420, 100, 50, 'BACK', myFunction)

#Title screen and start
while True:

    screen.fill((255, 255, 255))
    trivialButton.draw(screen)
    startButton.draw(screen)
    quitButton.draw(screen)


    #check if start button is pressed
    if startButton.onePress:

      pygame.display.update()
      mainMenuButton.draw(screen)
      playButton.draw(screen)
      continueButton.draw(screen)
      questionsButton.draw(screen)
      helpButton.draw(screen)
      backButton.draw(screen)


    #playButton pressed
    if playButton.onePress:
      pygame.display.update()
      configurationButton.draw(screen)
      chemistryButton.draw(screen)
      sportsButton.draw(screen)
      musicButton.draw(screen)
      mathButton.draw(screen)
      historyButton.draw(screen)
      geographyButton.draw(screen)
      nextButton.draw(screen)

    #continue game is pressed
    if continueButton.onePress:
      pygame.display.update()
      configurationButton.draw(screen)
      chemistryButton.draw(screen)
      sportsButton.draw(screen)
      musicButton.draw(screen)
      mathButton.draw(screen)
      historyButton.draw(screen)
      geographyButton.draw(screen)
      nextButton.draw(screen)

    #questions button is pressed
    if questionsButton.onePress:
      pygame.display.update()
      select2Button.draw(screen)
      addButton.draw(screen)
      sports2Button.draw(screen)
      music2Button.draw(screen)
      math2Button.draw(screen)
      history2Button.draw(screen)
      artButton.draw(screen)
      scienceButton.draw(screen)
      back3Button.draw(screen)

    if helpButton.onePress:
      pygame.display.update()
      help2Button.draw(screen)
      play3Button.draw(screen)
      settingOneButton.draw(screen)
      settingTwoButton.draw(screen)
      settingThreeButton.draw(screen)
      back4Button.draw(screen)

    if backButton.onePress:
      pygame.display.update()
      trivialButton.draw(screen)
      startButton.draw(screen)
      quitButton.draw(screen)
  #else:
      #idleButton.draw(screen)


    #event handler
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    for object in objects:
      object.process()

    pygame.display.flip()
