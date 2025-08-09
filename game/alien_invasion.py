import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group

def run_game():
    # 初始化并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #设置背景颜色
    bg_color = (230,230,230)

    #创建一艘飞船,一个编组存储子弹,一个编组存储外星人
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #开始主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        #删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            print(len(bullets))

            gf.update_screen(ai_settings, screen, ship, bullets)

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()

run_game()