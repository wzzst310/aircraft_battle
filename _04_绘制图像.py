import pygame

pygame.init()
# 创建游戏窗口480*700
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./images/涛哥.png")
# 2> 绘制图像
screen.blit(bg, (0, 0))
# 3> 更新屏幕
pygame.display.update()

while True:
    pass

pygame.quit()
