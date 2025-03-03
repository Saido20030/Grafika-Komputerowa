import pygame  # Import biblioteki pygame

# Inicjalizacja pygame\pygame.init()
window = pygame.display.set_mode((600, 600))  # Tworzenie okna gry
pygame.display.set_caption("Zadanie 2")  # Ustawienie tytułu okna

# Definicja kolorów w formacie RGB
KOLOR_NIEBIESKI = (0, 0, 255)
KOLOR_BIALY = (255, 255, 255)

# Wypełnienie tła na biało
window.fill(KOLOR_BIALY)

# Flaga sterująca główną pętlą gry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Warunek zamknięcia okna
            running = False
    
    # Rysowanie kwadratów tworzących prostokąt
    kwadrat_1 = pygame.Rect(160, 250, 80, 80)
    kwadrat_2 = pygame.Rect(240, 250, 80, 80)
    kwadrat_3 = pygame.Rect(320, 250, 80, 80)
    
    pygame.draw.rect(window, KOLOR_NIEBIESKI, kwadrat_1)
    pygame.draw.rect(window, KOLOR_NIEBIESKI, kwadrat_2)
    pygame.draw.rect(window, KOLOR_NIEBIESKI, kwadrat_3)
    
    # Współrzędne wierzchołków górnego trójkąta
    trojkat_gorny = [(280, 250), (340, 180), (220, 180)]
    
    # Współrzędne wierzchołków dolnego trójkąta
    trojkat_dolny = [(280, 330), (340, 400), (220, 400)]
    
    # Rysowanie trójkątów
    pygame.draw.polygon(window, KOLOR_NIEBIESKI, trojkat_gorny)
    pygame.draw.polygon(window, KOLOR_NIEBIESKI, trojkat_dolny)
    
    # Aktualizacja ekranu
    pygame.display.update()

# Zakończenie pygame
pygame.quit()