# main.py

import pygame
import sys
from settings import *
from player import Player
from enemies import Anglerfish, GiantEel, Jellyfish

def show_cover_page(screen):
    # Function to display the cover page and instructions
    cover_font = pygame.font.SysFont(None, 40)
    small_font = pygame.font.SysFont(None, 30)
    title_font = pygame.font.SysFont(None, 60)

    # Text content
    title_text = "Underwater Quest: The Crystal Hunt"
    welcome_text = "Welcome, Brave Explorer!"
    instruction_text = (
        "In Underwater Quest: The Crystal Hunt, you are a daring diver on a mission "
        "to find the mystical crystal that can stop a looming invasion threatening "
        "the peaceful underwater realms. Dive deep into the ocean's mysteries, face "
        "formidable creatures, and be the hero who saves the day!"
    )
    controls_text = "Use the arrow keys to move your character."
    password_prompt = "To begin your adventure, please enter the secret password:"

    # Clear screen
    screen.fill(BACKGROUND_COLOR)

    # Render text
    title_surface = title_font.render(title_text, True, WHITE)
    welcome_surface = cover_font.render(welcome_text, True, WHITE)
    instruction_surface = small_font.render(instruction_text, True, WHITE)
    controls_surface = small_font.render(controls_text, True, WHITE)
    password_surface = small_font.render(password_prompt, True, WHITE)

    # Get rectangles
    title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 80))
    welcome_rect = welcome_surface.get_rect(center=(SCREEN_WIDTH // 2, 140))
    instruction_rect = instruction_surface.get_rect(center=(SCREEN_WIDTH // 2, 220))
    controls_rect = controls_surface.get_rect(center=(SCREEN_WIDTH // 2, 300))
    password_rect = password_surface.get_rect(center=(SCREEN_WIDTH // 2, 380))

    # Blit to screen
    screen.blit(title_surface, title_rect)
    screen.blit(welcome_surface, welcome_rect)
    draw_multiline_text(screen, instruction_text, small_font, WHITE, SCREEN_WIDTH // 2, 220, 500)
    screen.blit(controls_surface, controls_rect)
    screen.blit(password_surface, password_rect)
    pygame.display.flip()

def draw_multiline_text(surface, text, font, color, x, y, max_width):
    words = text.split(' ')
    lines = []
    line = ''
    for word in words:
        if font.size(line + word)[0] > max_width:
            lines.append(line)
            line = ''
        line += word + ' '
    if line:
        lines.append(line)
    for i, l in enumerate(lines):
        text_surface = font.render(l, True, color)
        text_rect = text_surface.get_rect(center=(x, y + i * 25))
        surface.blit(text_surface, text_rect)

def main():
    # Initialize Pygame
    pygame.init()

    # Create the display surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)

    # Show cover page
    show_cover_page(screen)

    # Password input loop
    password = ''
    input_active = True
    font = pygame.font.SysFont(None, 40)
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if password.lower() == 'what':
                        input_active = False  # Exit the loop and start the game
                    else:
                        # Incorrect password, display message and exit
                        error_text = "Incorrect password. Exiting the game."
                        error_surface = font.render(error_text, True, RED)
                        error_rect = error_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
                        screen.blit(error_surface, error_rect)
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_BACKSPACE:
                    password = password[:-1]
                else:
                    password += event.unicode

        # Clear the input area
        input_rect = pygame.Rect(0, SCREEN_HEIGHT // 2 + 50, SCREEN_WIDTH, 50)
        pygame.draw.rect(screen, BACKGROUND_COLOR, input_rect)

        # Render the password asterisks
        password_display = '*' * len(password)
        password_surface = font.render(password_display, True, WHITE)
        password_rect = password_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 75))
        screen.blit(password_surface, password_rect)
        pygame.display.flip()

    # Continue with the game setup after password is correct

    # Clock to control the frame rate
    clock = pygame.time.Clock()

    # Load images
    try:
        anglerfish_img = pygame.image.load("assets/images/anglerfish.png").convert_alpha()
        giant_eel_img = pygame.image.load("assets/images/giant_eel.png").convert_alpha()
        jellyfish_img = pygame.image.load("assets/images/jellyfish.png").convert_alpha()
    except pygame.error as e:
        print(f"Error loading images: {e}")
        sys.exit()

    # Scale images (adjust size as needed)
    anglerfish_img = pygame.transform.scale(anglerfish_img, (150, 100))
    giant_eel_img = pygame.transform.scale(giant_eel_img, (300, 80))
    jellyfish_img = pygame.transform.scale(jellyfish_img, (100, 150))

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    # Create player instance
    player = Player()
    all_sprites.add(player)

    # Create enemy instances
    for _ in range(3):
        anglerfish = Anglerfish(anglerfish_img)
        all_sprites.add(anglerfish)
        enemy_sprites.add(anglerfish)

    for _ in range(2):
        eel = GiantEel(giant_eel_img)
        all_sprites.add(eel)
        enemy_sprites.add(eel)

    for _ in range(5):
        jellyfish = Jellyfish(jellyfish_img)
        all_sprites.add(jellyfish)
        enemy_sprites.add(jellyfish)

    # Game loop
    running = True
    while running:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Movement controls
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speed_x = -5
                if event.key == pygame.K_RIGHT:
                    player.speed_x = 5
                if event.key == pygame.K_UP:
                    player.speed_y = -5
                if event.key == pygame.K_DOWN:
                    player.speed_y = 5

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.speed_x < 0:
                    player.speed_x = 0
                if event.key == pygame.K_RIGHT and player.speed_x > 0:
                    player.speed_x = 0
                if event.key == pygame.K_UP and player.speed_y < 0:
                    player.speed_y = 0
                if event.key == pygame.K_DOWN and player.speed_y > 0:
                    player.speed_y = 0

        # Update sprites
        all_sprites.update()

        # Collision detection
        hits = pygame.sprite.spritecollide(player, enemy_sprites, False)
        if hits:
            print("You have been caught by an enemy! Game Over.")
            running = False

        # Rendering
        screen.fill(BACKGROUND_COLOR)  # Background color
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()