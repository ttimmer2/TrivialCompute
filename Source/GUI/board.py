import pygame

POSITIONS = [
    (0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0),
    (0,1),                      (4,1),                      (8,1),
    (0,2),                      (4,2),                      (8,2),
    (0,3),                      (4,3),                      (8,3),
    (0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4), (8,4),
    (0,5),                      (4,5),                      (8,5),
    (0,6),                      (4,6),                      (8,6),
    (0,7),                      (4,7),                      (8,7),
    (0,8), (1,8), (2,8), (3,8), (4,8), (5,8), (6,8), (7,8), (8,8)
]


ROLL_AGAIN = [0,8,36,44]

HOME = [22]

HQ = [4,18,26,40]

C0 = [4,9,11,21,25,27,29,31,38,42]
C1 = [18,1,5,10,14,24,28,32,37,41]
C2 = [40,2,6,13,15,17,19,23,33,35]
C3 = [26,3,7,12,16,20,30,34,39,43]

SQUARE_DIM   = 70

# square colors
BLUE  = (0,0,255)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)
RED   = (178,34,34)
GREEN = (0,128,0)
BLACK = (0,0,0)

# square margins
X_MARGIN = 50
Y_MARGIN = 50

# token colors
ORANGE = (255,140,0)
GRAY = (192,192,192)
PURPLE = (128, 0, 128)
BLACK = (0,0,0)
PINK = (255,105,180)
BROWN = (210,105,30)

class Token_image():
    def __init__(self, position, color, number):
        self.position = position
        self.color = color
        self.number = number

    def set_pos(self, pos):
        if pos <= len(POSITIONS) and pos >= 0:
            self.position = pos

    def draw_token(self, window):
        x = self.position[0]*SQUARE_DIM + X_MARGIN
        y = self.position[1]*SQUARE_DIM + Y_MARGIN

        offset = SQUARE_DIM / 4 
        match self.number:
            case 0:
                x += offset
                y += offset
            case 1:
                x += offset * 3
                y += offset
            case 2:
                x += offset
                y += offset * 3
            case 3:
                x += offset * 3
                y += offset * 3

        pygame.draw.circle(window, self.color, (int(x),int(y)), int(SQUARE_DIM/4))


class Player():
    def __init__(self, name, number):
        self.name = name
        self.number = number

        self.categories = [False,False,False,False]

        self.set_location()

    def set_category_value(self, category):
        if category > 3 or category < 0:
            raise Exception("Category must be an int between 0 & 3")
        self.categories[category] = True

    def set_location(self):
        location = None
        match self.number:
            case 0:
                location = (2,2)
            case 1:
                location = (2,6)
            case 2:
                location = (6,2)
            case 3:
                location = (6,6)
        self.location = location

    def get_name(self):
        return self.name


    def draw_player_representation(self, window, font):
        tl_x = self.location[0] * SQUARE_DIM + X_MARGIN
        tl_y = self.location[1] * SQUARE_DIM + Y_MARGIN
        number_bitmap = font.render( self.name, False, BLACK )
        margin = 20
        window.blit( number_bitmap, ( tl_x - margin, tl_y - margin ) )

        # draw completed squares
        cats = self.categories
        if cats[0]:
            rectangle = ( tl_x, tl_y, SQUARE_DIM/2, SQUARE_DIM/2)
            pygame.draw.rect( window, RED, rectangle, border_radius=1 ) 
        if cats[1]:
            rectangle = ( tl_x + SQUARE_DIM/2, tl_y, SQUARE_DIM/2, SQUARE_DIM/2)
            pygame.draw.rect( window, YELLOW, rectangle, border_radius=1 )
        if cats[2]:
            rectangle = ( tl_x, tl_y + SQUARE_DIM/2, SQUARE_DIM/2, SQUARE_DIM/2)
            pygame.draw.rect( window, BLUE, rectangle, border_radius=1 )           
        if cats[3]:
            rectangle = ( tl_x + SQUARE_DIM/2, tl_y + SQUARE_DIM/2, SQUARE_DIM/2, SQUARE_DIM/2)
            pygame.draw.rect( window, GREEN, rectangle, border_radius=1 )


def get_rectangle_color(pos):
    if pos in C0:
        return RED
    elif pos in C1:
        return YELLOW
    elif pos in C2:
        return BLUE
    elif pos in C3:
        return GREEN
    else:
        return WHITE

def get_square_string(pos):
    if pos in HOME:
        return "TC"
    else:
        return "Roll Again"



def draw_tokens(tokens, window):
    for token in tokens:
        token.draw_token(window)

def draw_players(players, window, font):
    for player in players:
        player.draw_player_representation(window, font)

def draw_board(window, number_font, tokens, players):
    for i, pos in enumerate(POSITIONS):
        tl_x = pos[0]*SQUARE_DIM + X_MARGIN
        tl_y = pos[1]*SQUARE_DIM + Y_MARGIN
        rectangle = ( tl_x, tl_y, SQUARE_DIM, SQUARE_DIM)
        color = get_rectangle_color(i)
        pygame.draw.rect( window, color, rectangle, border_radius=1 ) 
        if (i in HOME) or (i in ROLL_AGAIN):
            square_string = get_square_string(i)
            number_bitmap = number_font.render( square_string, True, BLACK )
            margin = 10
            window.blit( number_bitmap, ( tl_x + margin, tl_y + margin ) )
        draw_tokens(tokens, window)
        draw_players(players,window, font)



if __name__ == "__main__":

    P0 = Token_image(POSITIONS[30], PINK, 0)
    Player_0 = Player("Douglas",0)
    P1 = Token_image(POSITIONS[3],BROWN, 1)
    Player_1 = Player("Violet",1)
    P2 = Token_image(POSITIONS[1], PURPLE, 2)
    Player_2 = Player("Milhouse",2)    
    P3 = Token_image(POSITIONS[12], ORANGE, 3)
    Player_3 = Player("Bartholomew",3)

    for i in range(0,4):
        Player_3.set_category_value(i)
    for i in range(0,2):
        Player_1.set_category_value(i)
    for i in range(0,3):
        Player_2.set_category_value(i)
    for i in range(0,1):
        Player_0.set_category_value(i)

    tokens = [P0,P1,P2,P3]
    players = [Player_0,Player_1,Player_2,Player_3]

    pygame.init()
    pygame.font.init()

    drawing_window = pygame.display.set_mode()
    drawing_window.fill(WHITE)

    font = pygame.font.SysFont( None, 18, bold =pygame.font.Font.bold)
    
    
    screen = pygame.display.set_mode((1080, 1080))
    screen.fill(WHITE)

    clock = pygame.time.Clock()   # used to govern the max MAX_FPS
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board( drawing_window, font, tokens, players )

        pygame.display.update()

        clock.tick( 60 )

    pygame.quit()