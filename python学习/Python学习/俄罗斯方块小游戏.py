import pygame
import random

# 初始化Pygame
pygame.init()

# 游戏常量
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
PLAY_WIDTH = GRID_WIDTH * GRID_SIZE
PLAY_HEIGHT = GRID_HEIGHT * GRID_SIZE
PLAY_OFFSET_X = (SCREEN_WIDTH - PLAY_WIDTH) // 2
PLAY_OFFSET_Y = SCREEN_HEIGHT - PLAY_HEIGHT - 20

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

# 方块形状定义
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]  # Z
]

SHAPE_COLORS = [CYAN, YELLOW, PURPLE, ORANGE, BLUE, GREEN, RED]


class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("俄罗斯方块")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

        self.reset_game()

    def reset_game(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.paused = False
        self.fall_time = 0
        self.fall_speed = 0.5  # 初始下落速度（秒）

    def new_piece(self):
        shape_index = random.randint(0, len(SHAPES) - 1)
        shape = SHAPES[shape_index]
        color = SHAPE_COLORS[shape_index]

        return {
            'shape': shape,
            'color': color,
            'x': GRID_WIDTH // 2 - len(shape[0]) // 2,
            'y': 0
        }

    def valid_move(self, piece, x, y):
        for i, row in enumerate(piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    new_x = x + j
                    new_y = y + i

                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT:
                        return False
                    if new_y >= 0 and self.grid[new_y][new_x]:
                        return False
        return True

    def rotate_piece(self, piece):
        # 矩阵转置后反转每一行来实现旋转
        rotated = list(zip(*piece['shape'][::-1]))
        rotated = [list(row) for row in rotated]
        return rotated

    def lock_piece(self):
        piece = self.current_piece
        for i, row in enumerate(piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    x = piece['x'] + j
                    y = piece['y'] + i
                    if y >= 0:
                        self.grid[y][x] = piece['color']

        # 清除完整的行
        self.clear_lines()

        # 生成新的方块
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()

        # 检查游戏是否结束
        if not self.valid_move(self.current_piece, self.current_piece['x'], self.current_piece['y']):
            self.game_over = True

    def clear_lines(self):
        lines_to_clear = []
        for i, row in enumerate(self.grid):
            if all(row):
                lines_to_clear.append(i)

        if lines_to_clear:
            # 从下往上移除完整的行
            for line in sorted(lines_to_clear, reverse=True):
                del self.grid[line]
                self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])

            # 更新分数
            lines_count = len(lines_to_clear)
            self.lines_cleared += lines_count

            # 计分规则
            if lines_count == 1:
                self.score += 100 * self.level
            elif lines_count == 2:
                self.score += 300 * self.level
            elif lines_count == 3:
                self.score += 500 * self.level
            elif lines_count == 4:
                self.score += 800 * self.level

            # 更新等级
            self.level = self.lines_cleared // 10 + 1
            self.fall_speed = max(0.05, 0.5 - (self.level - 1) * 0.05)

    def move_piece(self, dx, dy):
        new_x = self.current_piece['x'] + dx
        new_y = self.current_piece['y'] + dy

        if self.valid_move(self.current_piece, new_x, new_y):
            self.current_piece['x'] = new_x
            self.current_piece['y'] = new_y
            return True
        return False

    def handle_rotation(self):
        rotated = self.rotate_piece(self.current_piece)
        original_shape = self.current_piece['shape']

        if self.valid_move({'shape': rotated, 'x': self.current_piece['x'], 'y': self.current_piece['y']},
                           self.current_piece['x'], self.current_piece['y']):
            self.current_piece['shape'] = rotated
        else:
            # 尝试墙踢
            for offset in [-1, 1, -2, 2]:
                if self.valid_move(
                        {'shape': rotated, 'x': self.current_piece['x'] + offset, 'y': self.current_piece['y']},
                        self.current_piece['x'] + offset, self.current_piece['y']):
                    self.current_piece['shape'] = rotated
                    self.current_piece['x'] += offset
                    return

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(
                    PLAY_OFFSET_X + x * GRID_SIZE,
                    PLAY_OFFSET_Y + y * GRID_SIZE,
                    GRID_SIZE,
                    GRID_SIZE
                )
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, self.grid[y][x], rect)
                pygame.draw.rect(self.screen, GRAY, rect, 1)

    def draw_piece(self, piece):
        for i, row in enumerate(piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    x = PLAY_OFFSET_X + (piece['x'] + j) * GRID_SIZE
                    y = PLAY_OFFSET_Y + (piece['y'] + i) * GRID_SIZE
                    rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
                    pygame.draw.rect(self.screen, piece['color'], rect)
                    pygame.draw.rect(self.screen, WHITE, rect, 2)

    def draw_next_piece(self):
        next_x = PLAY_OFFSET_X + PLAY_WIDTH + 20
        next_y = PLAY_OFFSET_Y + 50

        text = self.small_font.render("Next:", True, WHITE)
        self.screen.blit(text, (next_x, next_y - 30))

        for i, row in enumerate(self.next_piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    x = next_x + j * (GRID_SIZE - 5)
                    y = next_y + i * (GRID_SIZE - 5)
                    rect = pygame.Rect(x, y, GRID_SIZE - 5, GRID_SIZE - 5)
                    pygame.draw.rect(self.screen, self.next_piece['color'], rect)
                    pygame.draw.rect(self.screen, WHITE, rect, 2)

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        level_text = self.small_font.render(f"Level: {self.level}", True, WHITE)
        lines_text = self.small_font.render(f"Lines: {self.lines_cleared}", True, WHITE)

        self.screen.blit(score_text, (PLAY_OFFSET_X + PLAY_WIDTH + 20, PLAY_OFFSET_Y + 200))
        self.screen.blit(level_text, (PLAY_OFFSET_X + PLAY_WIDTH + 20, PLAY_OFFSET_Y + 240))
        self.screen.blit(lines_text, (PLAY_OFFSET_X + PLAY_WIDTH + 20, PLAY_OFFSET_Y + 270))

    def draw_game_over(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))

        game_over_text = self.font.render("GAME OVER", True, RED)
        restart_text = self.small_font.render("Press R to restart", True, WHITE)
        quit_text = self.small_font.render("Press Q to quit", True, WHITE)

        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 40))
        self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))
        self.screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))

    def draw_pause(self):
        pause_text = self.font.render("PAUSED", True, YELLOW)
        self.screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_r:
                        self.reset_game()
                    elif event.key == pygame.K_q:
                        return False
                else:
                    if event.key == pygame.K_LEFT:
                        self.move_piece(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move_piece(1, 0)
                    elif event.key == pygame.K_DOWN:
                        if self.move_piece(0, 1):
                            self.score += 1  # 软降加分
                    elif event.key == pygame.K_UP:
                        self.handle_rotation()
                    elif event.key == pygame.K_SPACE:
                        # 硬降
                        while self.move_piece(0, 1):
                            self.score += 2
                        self.lock_piece()
                    elif event.key == pygame.K_p:
                        self.paused = not self.paused
                    elif event.key == pygame.K_ESCAPE:
                        return False

        return True

    def update(self, dt):
        if self.game_over or self.paused:
            return

        self.fall_time += dt
        if self.fall_time >= self.fall_speed:
            self.fall_time = 0
            if not self.move_piece(0, 1):
                self.lock_piece()

    def draw(self):
        self.screen.fill(BLACK)

        # 绘制游戏区域背景
        play_area = pygame.Rect(PLAY_OFFSET_X, PLAY_OFFSET_Y, PLAY_WIDTH, PLAY_HEIGHT)
        pygame.draw.rect(self.screen, (20, 20, 20), play_area)

        self.draw_grid()
        self.draw_piece(self.current_piece)
        self.draw_next_piece()
        self.draw_score()

        if self.game_over:
            self.draw_game_over()
        elif self.paused:
            self.draw_pause()

        # 绘制控制说明
        controls = [
            "Controls:",
            "← → : Move",
            "↑ : Rotate",
            "↓ : Soft drop",
            "Space: Hard drop",
            "P : Pause",
            "Esc : Quit"
        ]

        y_offset = PLAY_OFFSET_Y + 320
        for control in controls:
            control_text = self.small_font.render(control, True, GRAY)
            self.screen.blit(control_text, (PLAY_OFFSET_X + PLAY_WIDTH + 20, y_offset))
            y_offset += 25

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(60) / 1000.0  # 转换为秒
            running = self.handle_events()
            self.update(dt)
            self.draw()

        pygame.quit()


if __name__ == "__main__":
    game = Tetris()
    game.run()