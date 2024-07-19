

def fade_text(screen, text, position, duration, fade_in=True,text_big = 50,text_color = (255, 255, 255), back_color=(0,0,0)):
    '''让字体显示在pygame里并且淡入淡出,这个函数接受参数：屏幕对象、要显示的文本、文本的位置、渐变效果的持续时间（以帧为单位）,是否淡入,字体大小,字体颜色,背景颜色。函数会根据这些参数，在屏幕上显示一个缓慢淡入和淡出的文本。'''
    import pygame
    import time
    
    # 设置字体和大小
    font = pygame.font.Font(None,text_big)
    text_surface = font.render(text,True,text_color)

    # 获取文本的宽度和高度
    text_rect = text_surface.get_rect()
    text_rect.center = position

    # 设置透明度
    alpha = 0 if fade_in else 255

    # 渐变效果
    for i in range(duration):
        if fade_in:
            alpha += 255 / duration
        else:
            alpha -= 255 / duration

        # 设置透明度
        text_surface.set_alpha(alpha)

        # 在屏幕上绘制文本
        screen.blit(text_surface, text_rect)

        # 更新屏幕
        pygame.display.flip()

        # 暂停一段时间
        time.sleep(0.01)

        screen.fill(back_color)


    # 暂停一段时间
    time.sleep(0.5)




'''
# 初始化Pygame
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((800, 600))

# 设置背景颜色
screen.fill((0, 0, 0))

# 显示淡入效果
fade_text(screen, "Hello, World!", (400, 300), 1000, True)

# 显示淡出效果
fade_text(screen, "Hello, World!", (400, 300), 1000, False)

# 退出Pygame
pygame.quit()


if __name__ == "__main__":
   fade_text(screen, "Hello, World!", (400, 300), 100, True)
'''   