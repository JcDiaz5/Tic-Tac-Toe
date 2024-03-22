import pygame
import sys

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 3
XO_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

WHITE = (255, 255, 255)
RED = (176, 2, 13)
BLUE = (2, 47, 184)
CYAN = (3, 122, 145)
GRAY = (59, 59, 59)
LIGHT_CYAN = (195, 241, 247)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize the board
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def draw_board(current_player):
    screen.fill(LIGHT_CYAN)

    # Draw banner
    pygame.draw.rect(screen, CYAN, (0, 0, WIDTH, 50))

    # Display message on banner
    font = pygame.font.Font(None, 30)
    turn_text = font.render("Player {}'s turn".format(current_player), True, WHITE)
    text_rect = turn_text.get_rect(center=(WIDTH // 2, 25))
    screen.blit(turn_text, text_rect)

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            pygame.draw.rect(screen, CYAN, (col * SQUARE_SIZE, row * SQUARE_SIZE + 50, SQUARE_SIZE, SQUARE_SIZE), LINE_WIDTH)
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 70),
                                 ((col + 1) * SQUARE_SIZE - 20, (row + 1) * SQUARE_SIZE + 50 - 20), XO_WIDTH)
                pygame.draw.line(screen, RED, ((col + 1) * SQUARE_SIZE - 20, row * SQUARE_SIZE + 70),
                                 (col * SQUARE_SIZE + 20, (row + 1) * SQUARE_SIZE + 50 - 20), XO_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2 + 50), SQUARE_SIZE // 2 - 20, XO_WIDTH)

    pygame.display.update()

# Adjust the height of the screen to accommodate the banner
HEIGHT += 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def check_winner():
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

# Display winner
def display_winner(winner):
    screen.fill(CYAN)
    font = pygame.font.Font(None, 50)
    winner_title = font.render("Player  {}  wins!".format(winner), True, WHITE)
    text_rect = winner_title.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(winner_title, text_rect)
    pygame.display.update()
    pygame.time.wait(5000)  # Display for 10 seconds before closing the game
    pygame.quit()
    sys.exit()

# Display draw
def display_draw():
    screen.fill(CYAN)
    font = pygame.font.Font(None, 50)
    draw_title = font.render("It's a draw!", True, WHITE)
    text_rect = draw_title.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(draw_title, text_rect)
    pygame.display.update()
    pygame.time.wait(5000)  # Display for 10 seconds before closing the game
    pygame.quit()
    sys.exit()


def main():
    global board
    current_player = 'X'
    game_over = False
    game_started = False  # Flag to indicate if the game has started

    # Display game title
    screen.fill(CYAN)
    font = pygame.font.Font(None, 50)
    title_text = font.render("Tic Tac Toe", True, WHITE)
    text_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))

    # Display "Click to start" message
    font = pygame.font.Font(None, 20)
    start_text = font.render("Click to start", True, WHITE)
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.95))

    screen.blit(title_text, text_rect)
    screen.blit(start_text, start_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if not game_started:  # Start game only after the first click
                    game_started = True
                else:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    clicked_row = (mouseY - 50) // SQUARE_SIZE
                    clicked_col = mouseX // SQUARE_SIZE
                    if board[clicked_row][clicked_col] == '':
                        board[clicked_row][clicked_col] = current_player
                        if current_player == 'X':
                            current_player = 'O'
                        else:
                            current_player = 'X'
                        winner = check_winner()
                        if winner:
                            display_winner(winner)
                            game_over = True
                        elif all(board[row][col] != '' for row in range(BOARD_ROWS) for col in range(BOARD_COLS)):
                            display_draw()
                            game_over = True

        if game_started:  # Draw the board only after the first click
            draw_board(current_player)
            pygame.display.update()

if __name__ == "__main__":
    main()
