import time
import pygame

def get_data(filename='input.txt'):
    points, velocities = [], []
    with open(filename, 'r') as f:
        for p, v in [l.split(' ') for l in f.read().strip('\n').split('\n')]:
            points.append([int(n) for n in p[2:].split(',')])
            velocities.append([int(n) for n in v[2:].split(',')])
    board_dim = [101, 103]
    return (points, velocities, board_dim) 

def get_quadrants(board_dim):
    quad1 = (board_dim[1]//2, board_dim[1], -1, board_dim[0]//2)
    quad2 = (-1, board_dim[1]//2, -1, board_dim[0]//2)
    quad3 = (-1, board_dim[1]//2, board_dim[0]//2, board_dim[0])
    quad4 = (board_dim[1]//2, board_dim[1], board_dim[0]//2, board_dim[0])
    return (quad1, quad2, quad3, quad4)

def part_a():
    points, velocities, board_dim = get_data()
    for p, v in zip(points, velocities):
        p[0] = (p[0] + v[0]*100) % board_dim[0]
        p[1] = (p[1] + v[1]*100) % board_dim[1]
    quads = get_quadrants(board_dim)
    ans = [0, 0, 0, 0]
    # quadrants structured as minX, maxX, minY, maxY (exclusive)
    for p in points:
        for i, quad in enumerate(quads):
            if (quad[0] < p[1] < quad[1] and quad[2] < p[0] < quad[3]):
                ans[i] += 1
    # print(ans)
    print(ans[0] * ans[1] * ans[2] * ans[3])

def part_b():
    points, velocities, board_dim = get_data()
    pygame.init()
    cell_size = 4
    screen = pygame.display.set_mode((cell_size * board_dim[0], cell_size * board_dim[1]))
    pygame.display.set_caption("day 14 visualizer")
    BLACK = (0, 0, 0)
    FILLED_COLOR = (255, 0, 0)
    running = True
    seconds = 8000
    for p, v in zip(points, velocities):
        p[0] = (p[0] + v[0]*seconds) % board_dim[0]
        p[1] = (p[1] + v[1]*seconds) % board_dim[1]
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for p, v in zip(points, velocities):
                        p[0] = (p[0] - v[0]) % board_dim[0]
                        p[1] = (p[1] - v[1]) % board_dim[1]
                    seconds -= 1
                    print(seconds)
                elif event.key == pygame.K_RIGHT:
                    for p, v in zip(points, velocities):
                        p[0] = (p[0] + v[0]) % board_dim[0]
                        p[1] = (p[1] + v[1]) % board_dim[1]
                    seconds += 1
                    print(seconds)
        screen.fill(BLACK)
        for p in points:
            pygame.draw.rect(screen, FILLED_COLOR, (p[0]*cell_size, p[1]*cell_size, cell_size, cell_size))
        pygame.display.flip()

start_time_a = time.time()
part_a()
end_time_a = time.time()
start_time_b = time.time()
part_b()
pygame.quit()
end_time_b = time.time()
print(f'\npart a completed in {end_time_a-start_time_a}')
print(f'part b completed in {end_time_b-start_time_b}')

