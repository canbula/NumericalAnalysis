import pygame
import sys
import numpy as np


WIDTH = 800
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Finite Difference Derivative")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)


class Blackboard:
    def __init__(self, x: int, y: int, width: int, height: int, colour: tuple[int, int, int]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = ""
        self.text_colour = (0, 0, 0)
        self.text_rect = pygame.Rect(self.x + 5, self.y + 5, self.width - 10, self.height - 10)

    def draw(self):
        pygame.draw.rect(screen, self.colour, self.rect)
        text_surface = font.render(self.text, True, self.text_colour)
        screen.blit(text_surface, self.text_rect)


class Grid:
    def __init__(self, center_position: tuple[int, int], step_size: float, color: tuple[int, int, int]):
        self.center_position = center_position
        self.step_size = step_size
        self.color = color

    def draw(self):
        for x in range(0, HEIGHT, int(self.step_size)):
            pygame.draw.line(screen, self.color, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, int(self.step_size)):
            pygame.draw.line(screen, self.color, (0, y), (HEIGHT, y))
        pygame.draw.line(screen, self.color, (self.center_position[0], 0), (self.center_position[0], HEIGHT))
        pygame.draw.line(screen, self.color, (0, self.center_position[1]), (HEIGHT, self.center_position[1]))


class Axis:
    def __init__(self, center_position: tuple[int, int], width, height, color: tuple[int, int, int]):
        self.center_position = center_position
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pygame.draw.line(screen, self.color, (self.center_position[0], 0), (self.center_position[0], self.height), 2)
        pygame.draw.line(screen, self.color, (0, self.center_position[1]), (self.width, self.center_position[1]), 2)


class Point:
    def __init__(self, position: tuple[int, int], color: tuple[int, int, int]):
        self.position = position
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, self.position, 10)


class RegressionLine:
    def __init__(self, points_: list[Point], color: tuple[int, int, int], degree: int):
        self.points = points_
        self.color = color
        self.degree = degree
        self.coefficients = None

    def draw(self):
        x_points = []
        y_points = []
        for point_ in self.points:
            x_points.append(point_.position[0])
            y_points.append(point_.position[1])
        self.coefficients = np.polyfit(x_points, y_points, self.degree)
        x = np.linspace(0, WIDTH, 100)
        y = np.polyval(self.coefficients, x)
        for i in range(len(x) - 1):
            pygame.draw.line(screen, self.color, (x[i], y[i]), (x[i + 1], y[i + 1]), 3)


class RegressionDegree:
    def __init__(self, position: tuple[int, int], color: tuple[int, int, int], degree: int):
        self.position = position
        self.color = color
        self.degree = degree

    def draw(self):
        text_surface = font.render(f"Degree: \\/ {self.degree} /\\", True, self.color)
        screen.blit(text_surface, self.position)


class DerivativeOfRegressionLine:
    def __init__(self, regression_line_: RegressionLine, at_point, color: tuple[int, int, int]):
        self.regression_line = regression_line_
        self.color = color
        self.at_point = at_point

    def draw(self):
        dy = np.polyder(self.regression_line.coefficients)
        dy_at_point = np.polyval(dy, self.at_point[0])
        x1 = self.at_point[0]
        y1 = np.polyval(self.regression_line.coefficients, self.at_point[0])
        x2 = self.at_point[0] + 1
        y2 = y1 + dy_at_point
        # find the slope of the line
        m = (y2 - y1) / (x2 - x1)
        # find the y-intercept of the line
        b = y1 - m * x1
        x = np.linspace(0, WIDTH, 100)
        y = m * x + b
        for i in range(len(x) - 1):
            pygame.draw.line(screen, self.color, (x[i], y[i]), (x[i + 1], y[i + 1]), 3)


class DerivativePoint:
    def __init__(self, position: tuple[int, int], color: tuple[int, int, int], point_index: int):
        self.position = position
        self.color = color
        self.point_index = point_index

    def draw(self):
        text_surface = font.render(f"Derivative @ < {self.point_index} >", True, self.color)
        screen.blit(text_surface, self.position)


class EquationText:
    def __init__(self, position: tuple[int, int], color: tuple[int, int, int], coefficients: list[float]):
        self.position = position
        self.color = color
        self.coefficients = coefficients

    def draw(self):
        equation = ""
        for i in range(len(self.coefficients)):
            if i == 0:
                equation += f"{self.coefficients[i]}"
            elif i == 1:
                equation += f" + {self.coefficients[i]}x"
            else:
                equation += f" + {self.coefficients[i]}x^{i}"
        text_surface = font.render(f"Equation: {equation}", True, self.color)
        screen.blit(text_surface, self.position)


blackboard = Blackboard(0, 0, 600, 600, (255, 232, 115))
grid = Grid((300, 300), 20, (100, 100, 100))
axis = Axis((300, 300), 600, 600, (0, 0, 0))
regression_degree = RegressionDegree((620, 20), (0, 0, 0), 2)
derivative_point = DerivativePoint((620, 50), (0, 0, 0), 0)


def mark_point_with_mouse(e):
    if e.type == pygame.MOUSEBUTTONDOWN:
        mouse_position = pygame.mouse.get_pos()
        if blackboard.rect.collidepoint(mouse_position) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
            return Point(mouse_position, (0, 0, 0))
    return None


def remove_point_with_mouse(e):
    if e.type == pygame.MOUSEBUTTONDOWN:
        mouse_position = pygame.mouse.get_pos()
        if blackboard.rect.collidepoint(mouse_position) and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            for point_ in points:
                if point_.position[0] - 10 < mouse_position[0] < point_.position[0] + 10 and \
                        point_.position[1] - 10 < mouse_position[1] < point_.position[1] + 10:
                    points.remove(point_)
                    return True
    return False


points = []

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        point = mark_point_with_mouse(event)
        if point is not None:
            points.append(point)
        remove_point_with_mouse(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                regression_degree.degree += 1
            elif event.key == pygame.K_DOWN:
                if regression_degree.degree > 1:
                    regression_degree.degree -= 1
            elif event.key == pygame.K_RIGHT:
                if derivative_point.point_index < len(points) - 1:
                    derivative_point.point_index += 1
            elif event.key == pygame.K_LEFT:
                if derivative_point.point_index > 0:
                    derivative_point.point_index -= 1
    screen.fill((75, 139, 190))
    blackboard.draw()
    grid.draw()
    axis.draw()
    regression_degree.draw()
    derivative_point.draw()
    for point in points:
        if point is not None:
            point.draw()
    if len(points) > regression_degree.degree:
        regression_line = RegressionLine(points, (0, 0, 0), regression_degree.degree)
        regression_line.draw()
        derivative_of_regression_line = DerivativeOfRegressionLine(
            regression_line,
            points[derivative_point.point_index].position,
            (255, 0, 0)
        )
        derivative_of_regression_line.draw()
    pygame.display.update()
    clock.tick(60)
