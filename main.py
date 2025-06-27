import pygame
import random

# Initialize
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Dice Roller")
clock = pygame.time.Clock()

# Fonts
font_dice = pygame.font.SysFont(None, 120)
font_button = pygame.font.SysFont(None, 40)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Initial state
current_roll = random.randint(1, 6)
button_rect = pygame.Rect(125, 300, 150, 50)

def draw_button(hovered=False):
    color = DARK_GRAY if hovered else LIGHT_GRAY
    pygame.draw.rect(screen, color, button_rect)
    label = font_button.render("Roll Dice", True, BLACK)
    label_rect = label.get_rect(center=button_rect.center)
    screen.blit(label, label_rect)

def draw_screen():
    screen.fill(WHITE)
    
    # Render the number
    dice_text = font_dice.render(str(current_roll), True, BLACK)
    dice_rect = dice_text.get_rect(center=(200, 150))

    # Create a square centered around the dice_rect
    side_length = max(dice_rect.width, dice_rect.height) + 40  # Add padding
    square_rect = pygame.Rect(0, 0, side_length, side_length)
    square_rect.center = dice_rect.center

    # Draw the square (cube face)
    pygame.draw.rect(screen, BLACK, square_rect, width=4, border_radius=8)

    # Blit the number after drawing the box
    screen.blit(dice_text, dice_rect)

    mouse_pos = pygame.mouse.get_pos()
    hovered = button_rect.collidepoint(mouse_pos)
    draw_button(hovered)

def animate_dice_roll(duration=0.5, fps=20):
    global current_roll
    frames = int(duration * fps)
    for _ in range(frames):
        current_roll = random.randint(1, 6)
        draw_screen()
        pygame.display.flip()
        clock.tick(fps)

# Main loop
running = True
while running:
    draw_screen()
    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                animate_dice_roll()
                current_roll = random.randint(1, 6)

pygame.quit()
