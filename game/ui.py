import pygame

TEXT_COLOR = (120, 255, 140)

def wrap_text(text, font, max_width):
    lines = []
    current_line = ""
    words = text.split()

    for word in words:
        if current_line == "":
            test_line = word
        else:
            test_line = current_line + " " + word
        
        line_width, _ = font.size(test_line)

        if line_width <= max_width:
            current_line = test_line
        else:
            if current_line != "":
                lines.append(current_line)
            current_line = word
    
    if current_line != "":
        lines.append(current_line)
        
    return lines

def main():
    pygame.init() # Pygame vorbereiten

    info = pygame.display.Info() # Bildschirmauflösung ermitteln
    WIDTH = int(info.current_w * 0.75)
    HEIGHT = int(info.current_h * 0.75)

    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Fenster + Zeichenfläche erstellen
    pygame.display.set_caption("Ashen Throne - UI Test") # Fenstertitel setzen

    clock = pygame.time.Clock()

    font_system = pygame.font.SysFont("couriernew", 32) #(Schriftname, Schriftgröße)
    font_story = pygame.font.SysFont("couriernew", 26) #(Schriftname, Schriftgröße)
    font_input = pygame.font.SysFont("couriernew", 32) #(Schriftname, Schriftgröße)

    MARGIN = int(WIDTH * 0.03)   # Abstand zum Fensterrand und zwischen den Kästen
    PADDING = 15                 # Luft zwischen Text und Kastenrand

    panel_width = WIDTH - 2 * MARGIN
    header_height = font_system.get_height() + 2 * PADDING
    input_height = font_input.get_height() + 2 * PADDING
    body_height = HEIGHT - header_height - input_height - 4 * MARGIN

    header_rect = pygame.Rect(MARGIN, MARGIN, panel_width, header_height)
    body_rect = pygame.Rect(MARGIN, header_rect.bottom + MARGIN, panel_width, body_height)
    input_rect = pygame.Rect(MARGIN, body_rect.bottom + MARGIN, panel_width, input_height)

    story_texts = [
        "Welcome, exile.",
        "The ash drifts through the ruined hall.",
        "A distant echo moves beneath the stone.",
        "Something is waiting in the dark."
    ]

    current_index = 0
    visible_chars = 0
    frame_counter = 0
    typing_delay = 4
    shown_lines = []

    running = True # bestimmt, ob die Hauptschleife weiterläuft
    while running: # solange True, wird folgende Schleife durchlaufen
        story_text = story_texts[current_index]

        for event in pygame.event.get(): # holt alle aktuellen Ereignisse
            if event.type == pygame.QUIT: # Benutzer will das Fenster schließen
                running = False

            elif event.type == pygame.KEYDOWN: # Tastendruck
                if event.key in (pygame.K_RETURN, pygame.K_SPACE): # Enter
                    if visible_chars < len(story_text):
                        visible_chars = len(story_text)
                    else:
                        if current_index < len(story_texts) -1:
                            shown_lines.append(story_text)
                            current_index += 1
                            visible_chars = 0
                            frame_counter = 0

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (20, 20, 20), header_rect) # Fläche
        pygame.draw.rect(screen, (80, 120, 80), header_rect, 2) # Rand

        pygame.draw.rect(screen, (20, 20, 20), body_rect)
        pygame.draw.rect(screen, (80, 120, 80), body_rect, 2)

        pygame.draw.rect(screen, (20, 20, 20), input_rect)
        pygame.draw.rect(screen, (80, 120, 80), input_rect, 2)

        text_system = font_system.render("SYSTEM INTERFACE ONLINE", True, TEXT_COLOR)
        text_rect = text_system.get_rect(center=header_rect.center)
        screen.blit(text_system, text_rect) # wird auf screen gezeichnet, Postion x, y

        text_x = body_rect.x + PADDING
        text_y = body_rect.y + PADDING
        max_text_width = body_rect.width - 2 * PADDING

        line_spacing = font_story.get_height() + 10  # Zeilenabstand definieren

        # bereits abgeschlossene Texte
        for finished_text in shown_lines:
            for line in wrap_text(finished_text, font_story, max_text_width):
                text_surface = font_story.render(line, True, TEXT_COLOR) # Text, Anti-Aliasing, Textfarbe RGB
                screen.blit(text_surface, (text_x, text_y)) # wird auf screen gezeichnet, Postion x, y
                text_y += line_spacing

        # der Text, der gerade getippt wird
        current_text = story_text[:visible_chars]
        for line in wrap_text(current_text, font_story, max_text_width):
            text_surface = font_story.render(line, True, TEXT_COLOR)
            screen.blit(text_surface, (text_x, text_y))
            text_y += line_spacing

        frame_counter += 1

        if visible_chars < len(story_text) and frame_counter >= typing_delay:
            visible_chars += 1
            frame_counter = 0

        text_input = font_input.render("> awaiting input...", True, TEXT_COLOR)
        text_rect = text_input.get_rect(midleft=(input_rect.x + 20, input_rect.centery))
        screen.blit(text_input, text_rect)

        pygame.display.flip()
        clock.tick(60)

        
    pygame.quit() # Pygame sauber beenden

if __name__ == "__main__": # Datei nur dann starten, wenn sie direkt ausgeführt wird
    main()

# center=... → komplett zentriert
# midleft=... → links mittig
# midright=... → rechts mittig
# topleft=... → oben links
# midtop=... → oben mittig

# # oben links
# text_rect = text_welcome.get_rect(topleft=(body_rect.x + 20, body_rect.y + 20))

# # links mittig
# text_rect = text_welcome.get_rect(midleft=(body_rect.x + 20, body_rect.centery))

# # komplett mittig
# text_rect = text_welcome.get_rect(center=body_rect.center)

# # links unten
# text_rect = text_welcome.get_rect(bottomleft=(body_rect.x + 20, body_rect.bottom - 20))