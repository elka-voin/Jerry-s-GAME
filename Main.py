import pygame, class_balloon, random, time
pygame.init()

def start_menu():
    gamedisplay.blit(fone3,(0,0))
    play = pygame.image.load("PLAY.png")
    play = pygame.transform.scale(play,(400,400))
    gamedisplay.blit (play,(100,100))
    pygame.display.update()
    #time.sleep(10)
    maus_button = False
    while maus_button == False:
        for e in pygame.event.get():
            if e.type==pygame.MOUSEBUTTONDOWN:
                maus_button = True

#nastroyki эkrana
w = 1000
h = 800
gamedisplay = pygame.display.set_mode((w,h))
pygame.display.set_caption("Jarry's Game")

#фоны
fone1 = pygame.image.load("DISPLAY.jpg")
fone1 = pygame.transform.scale(fone1,(w,h))

fone2 = pygame.image.load("class.jpg")
fone2 = pygame.transform.scale(fone2,(w,h))

fone3 = pygame.image.load("rick.jpg")
fone3 = pygame.transform.scale(fone3,(w,h))
#fone3 = fone3.subsurface((200,0,1000,675))

#второстепенный фон
surface = pygame.Surface((w,h))
surface.fill((0,0,0))
surface.set_alpha(130)

#FPS
clock = pygame.time.Clock()
FPS = 40
#pygame.time.set_timer(pygame.USEREVENT, 1000)

#text
f = pygame.font.SysFont("Goudy Stout",35)

#time
start_ticks = pygame.time.get_ticks()  
spawn = pygame.event.Event(pygame.USEREVENT)
spawn_time = start_ticks
cooll_douwn = 1000

beth = False
jarry = pygame.sprite.Group()
summer = class_balloon.Summer()
kick = 0
fone = fone1
false = 0
balloons = pygame.sprite.LayeredUpdates()
start_menu()
game = True
while game: 
    
    #ticks
    clock.tick(FPS)  
    now_ticks = pygame.time.get_ticks()
    cooll_douwn = 1000 - false * 50 
    if now_ticks - spawn_time > cooll_douwn:
        pygame.event.post(spawn)
  
    #обработка событий
    events = pygame.event.get()
    for e in events:

        if e.type==pygame.QUIT:
            game = False

        if e.type==pygame.KEYDOWN:

            if e.key==pygame.K_1:
                fone = fone1

            if e.key==pygame.K_2:
                fone = fone2

            if e.key==pygame.K_3:
                fone = fone3
        # генерация шариков
        if e.type==pygame.USEREVENT:
            r = random.randint(1,15)
            if r == 7:
                b  = class_balloon.Head()
            elif r == 8:
                b = class_balloon.Jerry()
                jarry.add(b) 
                if len(jarry.sprites()) > 5 and beth == False:
                    b = class_balloon.Beth()
                    beth = True
                    print (7)
                else:
                    b = class_balloon.Jerry()
                    jarry.add(b)

            elif r == 9:
                b = class_balloon.Summer()

            else:

                if false > 5:
                    image = "rick"

                elif kick > 14:
                    image = "morty"
                else:
                    image = "balloon"

                b = class_balloon.Balloon(image)
            balloons.add(b)
            spawn_time = now_ticks

        # убиватель шариков
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button==1:
                
                click_balloon = balloons.get_sprites_at(e.pos)
                for b in click_balloon:
                    b.kill()
                    if type (b) != class_balloon.Jerry:
                        kick += b.cick
                        if type (b) == class_balloon.Summer:
                            for e in balloons:
                                if type (e) == class_balloon.Balloon:
                                    if random.randint (1,2) == 2:
                                        e.kill()
                             

                            if false < 150:
                                false = 0

                            else: 
                                false -= 150
                        elif type (b) == class_balloon.Beth:
                            beth = False
                            for g in jarry:
                                g.kill()
                    else:
                        false += 5
                    


    for b in balloons:
        if b.check_pos() == False:
            b.kill()
            false += 1
    #вывод фона
    gamedisplay.blit(fone,(0,0))
    gamedisplay.blit(surface,(0,0))

    #отрисовка шаров
    balloons.draw(gamedisplay)
    balloons.update()

    #вывод текста
    text = f.render("false: " + str(false),1,(100,250,220))
    gamedisplay.blit(text,(0,0))

    text2 = f.render("kills: " + str(kick),1,(100,250,220))
    text2_rect  = text2.get_rect()
    text2_rect.right = w
    gamedisplay.blit(text2,text2_rect)

    pygame.display.update()

pygame.quit()           
