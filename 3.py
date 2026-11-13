import pygame
import math
import random
import imageio
import numpy as np
import os

# Настройки для сохранения
OUTPUT_FILENAME = "neon_border.gif"
FRAMES_TO_GENERATE = 90  # Количество кадров в итоговой гифке
FPS = 30  # Частота кадров

# Инициализация Pygame в скрытом режиме
os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 720, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Настройки эффектов
BORDER_WIDTH = 120
WAVE_COLORS = [(0, 255, 255), (138, 43, 226), (0, 255, 127)]  # Циан, Фиолетовый, Изумрудный


class Particle:
    def __init__(self):
        self.reset()

    def reset(self):
        if random.choice([True, False]):
            self.x = random.randint(0, WIDTH)
            self.y = random.randint(0, BORDER_WIDTH) if random.choice([True, False]) else random.randint(
                HEIGHT - BORDER_WIDTH, HEIGHT)
        else:
            self.x = random.randint(0, BORDER_WIDTH) if random.choice([True, False]) else random.randint(
                WIDTH - BORDER_WIDTH, WIDTH)
            self.y = random.randint(0, HEIGHT)

        self.size = random.randint(1, 4)
        self.color = random.choice(WAVE_COLORS)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
        self.life = random.randint(30, 80)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.life -= 2

        # Защита пустого центра
        if BORDER_WIDTH < self.x < WIDTH - BORDER_WIDTH and BORDER_WIDTH < self.y < HEIGHT - BORDER_WIDTH:
            self.life = 0

        if self.life <= 0:
            self.reset()

    def draw(self, surface):
        alpha = max(0, min(255, int((self.life / 80) * 255)))
        color_with_alpha = (*self.color, alpha)

        surf = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, color_with_alpha, (self.size, self.size), self.size)
        surface.blit(surf, (int(self.x - self.size), int(self.y - self.size)))


def draw_neon_waves(surface, time):
    points_left, points_right = [], []
    points_top, points_bottom = [], []

    for i in range(0, HEIGHT + 1, 15):
        offset = math.sin(i * 0.01 + time) * 25 + math.cos(i * 0.02 - time * 1.5) * 15
        points_left.append((BORDER_WIDTH // 2 + offset, i))
        points_right.append((WIDTH - BORDER_WIDTH // 2 - offset, i))

    for i in range(0, WIDTH + 1, 15):
        offset = math.sin(i * 0.01 + time) * 25 + math.cos(i * 0.02 - time * 1.5) * 15
        points_top.append((i, BORDER_WIDTH // 2 + offset))
        points_bottom.append((i, HEIGHT - BORDER_WIDTH // 2 - offset))

    for color in WAVE_COLORS:
        for thickness in [8, 4, 1]:
            pygame.draw.lines(surface, color, False, points_left, thickness)
            pygame.draw.lines(surface, color, False, points_right, thickness)
            pygame.draw.lines(surface, color, False, points_top, thickness)
            pygame.draw.lines(surface, color, False, points_bottom, thickness)


# Создание частиц
particles = [Particle() for _ in range(250)]

# Список для хранения кадров
frames = []
time_counter = 0

print(f"Генерация {FRAMES_TO_GENERATE} кадров...")

for frame_num in range(FRAMES_TO_GENERATE):
    screen.fill((0, 0, 0))  # Черный фон

    for p in particles:
        p.update()
        p.draw(screen)

    draw_neon_waves(screen, time_counter)

    # Строго очищаем центр
    pygame.draw.rect(screen, (0, 0, 0),
                     (BORDER_WIDTH, BORDER_WIDTH, WIDTH - BORDER_WIDTH * 2, HEIGHT - BORDER_WIDTH * 2))

    # Получаем массив пикселей экрана (Pygame возвращает формат X, Y, Color)
    # Нужно транспонировать его в Y, X, Color для ImageIO
    view = pygame.surfarray.array3d(screen)
    view = np.transpose(view, (1, 0, 2))
    frames.append(view)

    time_counter += 0.1

    # Прогресс
    if (frame_num + 1) % 10 == 0:
        print(f"Сгенерировано {frame_num + 1}/{FRAMES_TO_GENERATE} кадров")

pygame.quit()

print("Сборка GIF файла (это может занять несколько секунд)...")
# Сохраняем собранные кадры в GIF
imageio.mimsave(OUTPUT_FILENAME, frames, fps=FPS, loop=0)
print(f"Готово! Анимация сохранена в файл: {OUTPUT_FILENAME}")