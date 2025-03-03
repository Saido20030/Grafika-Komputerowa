import pygame
import math

# Inicjalizacja pygame
pygame.init()
win = pygame.display.set_mode((600, 600))  # Ustawienie okna gry o wymiarach 600x600 pikseli
pygame.display.set_caption("Polygon Transformations")  # Tytuł okna

# Definicja kolorów
yellow = (255, 255, 0)  # Kolor tła
fill_color = (216, 191, 216)  # Kolor wypełnienia wielokąta

# Parametry wielokąta
wierzcholki = 9  # Liczba boków wielokąta 
radius = 150  # Promień wielokąta

# Parametry transformacji
global scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position
scale_factor_x = 1.0  # Skalowanie w osi X
scale_factor_y = 1.0  # Skalowanie w osi Y
angle = -45  # Kąt obrotu
shear_factor_x = 0.0  # Współczynnik ścinania w osi X
shear_factor_y = 0.0  # Współczynnik ścinania w osi Y
position = (300, 300)  # Pozycja wielokąta na ekranie

# Funkcja do generowania punktów regularnego wielokąta
def generate_polygon_points(center, radius, sides):
    points = []
    for i in range(sides):
        posX = int(radius * math.cos(i * 2 * math.pi / sides) + center[0])
        posY = int(radius * math.sin(i * 2 * math.pi / sides) + center[1])
        points.append((posX, posY))
    return points

# Funkcja do transformacji wielokąta
def transform_polygon(points, scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position):
    transformed_points = []
    for x, y in points:
        # Przesunięcie do środka (300, 300)
        x -= 300
        y -= 300
        
        # Skalowanie
        x *= scale_factor_x  
        y *= scale_factor_y  
        
        # Obrót punktów względem (0,0)
        new_x = math.cos(math.radians(angle)) * x - math.sin(math.radians(angle)) * y
        new_y = math.sin(math.radians(angle)) * x + math.cos(math.radians(angle)) * y
        
        # Ścinanie
        new_x += shear_factor_x * new_y
        new_y += shear_factor_y * new_x
        
        # Przesunięcie do nowej pozycji
        new_x += position[0]  
        new_y += position[1]  
        
        transformed_points.append((new_x, new_y))
    
    return transformed_points

# Pętla gry
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # Obsługa klawiszy zmieniających parametry transformacji
            if event.key == pygame.K_1:
                scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position = 0.5, 0.5, -45, 0.0, 0.0, (300, 300)
            elif event.key == pygame.K_2:
                scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position = 1.0, 1.0, 0, 0.0, 0.0, (300, 300)
            elif event.key == pygame.K_3:
                scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position = 1.0, 1.0, 225, 0.0, 0.0, (300, 300)
            elif event.key == pygame.K_4:
                scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position = 1.0, 1.0, -45, 0.4, 0.0, (300, 300)
            elif event.key == pygame.K_5:
                scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position = 1.0, 0.6, 0, 0.0, 0.0, (300, 30)
            elif event.key == pygame.K_6:
                scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position = 1.0, 1.0, 45, 0.4, 0.4, (300, 300)
            elif event.key == pygame.K_7:
                scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position = -1.0, 1.0, 225, 0.0, 0.0, (300, 300)
            elif event.key == pygame.K_8:
                scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position = 1.0, 1.0, -40, 0.0, 0.0, (200, 400)
            elif event.key == pygame.K_9:
                scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position = 1.0, 1.0, 158, 0.4, 0.0, (535, 300)
            else:
                scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position = 1.0, 1.0, 0, 0.0, 0.0, (300, 300)

    # Generowanie punktów wielokąta
    points = generate_polygon_points((300, 300), radius, wierzcholki)
    
    # Transformacja punktów wielokąta
    transformed_points = transform_polygon(points, scale_factor_x, scale_factor_y, angle, shear_factor_x, shear_factor_y, position)
    
    # Czyszczenie ekranu
    win.fill(yellow)
    
    # Rysowanie przekształconego wielokąta
    pygame.draw.polygon(win, (0, 0, 0), transformed_points, 10)  # Czarna ramka
    pygame.draw.polygon(win, fill_color, transformed_points)  # Wypełnienie kolorem
    
    pygame.display.update()

# Zakończenie gry
pygame.quit()
