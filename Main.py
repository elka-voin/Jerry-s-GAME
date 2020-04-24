import pygame, class_balloon
pygame.init()

#nastroyki эkrana#\
w = 600
h = 750
gamedisplay = pygame.display.set_mode((w,h))
pygame.display.set_caption("Jarry's Game")

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

false = 0

balloons = pygame.sprite.LayeredUpdates()

game = True
while game:   
    clock.tick(FPS)
    gamedisplay.fill((30, 80, 227, 0.59))  
    balloons.draw(gamedisplay)
    balloons.update()

    now_ticks = pygame.time.get_ticks()
    #time = now_ticks - start_ticks
    #print (time//1000)
    cooll_douwn = 1000 - false * 50 
    if now_ticks - spawn_time > cooll_douwn:
        pygame.event.post(spawn)
        

    events = pygame.event.get()
    for e in events:

        if e.type==pygame.QUIT:
            game = False

        if e.type==pygame.USEREVENT:
            b = class_balloon.Balloon()
            balloons.add(b)
            spawn_time = now_ticks

        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button==1:
                
                click_balloon = balloons.get_sprites_at(e.pos)
                for b in click_balloon:
                    b.kill()

    for b in balloons:
        if b.check_pos() == False:
            b.kill()
            false += 1

    text = f.render("false: " + str(false),1,(100,250,220))
    gamedisplay.blit(text,(0,0))

    pygame.display.update()

pygame.quit()           