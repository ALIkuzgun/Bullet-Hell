import pygame, random

class Player():
    def __init__(self,x,y,en,boy,speed):  
        self.image = pygame.image.load('ship.png')      
        self.x = x
        self.y = y
        self.en = en
        self.boy = boy
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)
        self.speed = speed
        self.shoot_time = 0
        self.health = 100

    def move(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif key[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif key[pygame.K_UP]:
            self.rect.y -= self.speed
        elif key[pygame.K_DOWN]:
            self.rect.y += self. speed

        self.shoot_time += 1 
        if key[pygame.K_SPACE]:
            if self.shoot_time >= 25:
                bullet = Player_Bullet(self.rect.x+32-5, self.rect.y-4)
                bullets.append(bullet)
                self.shoot_time = 0

    def draw_health_bar(self):
        pygame.draw.rect(ekran,(0,255,0),(self.rect.x-17,self.rect.y+70,self.health,10))

    def draw(self):
        ekran.blit(self.image,self.rect)

    def kill(self):
        global game
        if self.health <= 30:
          game = 0

    def update(self):
        self.draw()
        self.draw_health_bar()
        self.move()
        self.kill()

class Player_Bullet():
    def __init__(self, x, y):        
        self.image = pygame.image.load('bullet.png')      
        self.rect = pygame.Rect(x, y, 8, 8)

    def move(self):
        self.rect.y -= 7

    def eye_hit(self):
        for bullet in bullets:
            if bullet.rect.colliderect(eye.rect):
                eye.health -= 3.5
                bullets.remove(bullet)

    def draw(self):
        ekran.blit(self.image,self.rect)

    def update(self):
        self.move()
        self.draw()
        self.eye_hit()

class Eye_Bullet():
    def __init__(self, x, y):        
        self.image = pygame.image.load('bulleteye.png')      
        self.rect = pygame.Rect(x, y, 8, 8)

    def player_hit(self):
            if player.rect.colliderect(eye_bullet):
                player.health -= 0.015

    def draw(self):
        ekran.blit(self.image,self.rect)

    def update(self):
        self.draw()
        self.player_hit()

class Enemy():
    def __init__(self,x,y,en,boy,speed):  
        self.image = pygame.image.load('eye.png')      
        self.x = x
        self.y = y
        self.en = en
        self.boy = boy
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)
        self.speed = speed
        self.direction = "right"
        self.move_direction = "stay"   
        self.health = 150
        self.died = 0
        self.attack_type = 1
        self.attack_type_time = 0
        # attack1
        self.eye_bullet1 = Eye_Bullet(self.rect.x+32-10, self.rect.y+64)
        self.eye_bullet2 = Eye_Bullet(self.rect.x+32-10, self.rect.y-20)
        self.eye_bullet3 = Eye_Bullet(self.rect.x+64, self.rect.y+32-10)
        self.eye_bullet4 = Eye_Bullet(self.rect.x-20, self.rect.y+32-10)
        # attack2
        self.eye_bullet5 = Eye_Bullet(self.rect.x-14, self.rect.y+64)
        self.eye_bullet6 = Eye_Bullet(self.rect.x+10, self.rect.y+64)
        self.eye_bullet7 = Eye_Bullet(self.rect.x+34, self.rect.y+64)
        self.eye_bullet8 = Eye_Bullet(self.rect.x+58, self.rect.y+64)
        # attack3
        self.eye_bullet9 = Eye_Bullet(self.rect.x+32-10, self.rect.y+64)
        self.eye_bullet10 = Eye_Bullet(self.rect.x+32-10, self.rect.y-20)
        self.eye_bullet11 = Eye_Bullet(self.rect.x+64, self.rect.y+32-10)
        self.eye_bullet12 = Eye_Bullet(self.rect.x-20, self.rect.y+32-10)
        self.eye_bullet13 = Eye_Bullet(self.rect.x-8, self.rect.y-8)
        self.eye_bullet14 = Eye_Bullet(self.rect.x+self.en-12, self.rect.y+self.boy-12)
        self.eye_bullet15 = Eye_Bullet(self.rect.x+self.en-12, self.rect.y-8)
        self.eye_bullet16 = Eye_Bullet(self.rect.x-8, self.rect.y+self.boy-12)
        # attack4
        self.eye_bullet17 = Eye_Bullet(self.rect.x-50, self.rect.y+64)
        self.eye_bullet18 = Eye_Bullet(self.rect.x-74, self.rect.y+64)
        self.eye_bullet19 = Eye_Bullet(self.rect.x-98, self.rect.y+64)
        self.eye_bullet20 = Eye_Bullet(self.rect.x-122, self.rect.y+64)
        self.eye_bullet21 = Eye_Bullet(self.rect.x+self.en+34, self.rect.y+64)
        self.eye_bullet22 = Eye_Bullet(self.rect.x+self.en+58, self.rect.y+64)
        self.eye_bullet23 = Eye_Bullet(self.rect.x+self.en+82, self.rect.y+64)
        self.eye_bullet24 = Eye_Bullet(self.rect.x+self.en+106, self.rect.y+64)
        
    def position_bullet(self):
        # attack1
        self.eye_bullet1 = Eye_Bullet(self.rect.x+32-10, self.rect.y+64)
        self.eye_bullet2 = Eye_Bullet(self.rect.x+32-10, self.rect.y-20)
        self.eye_bullet3 = Eye_Bullet(self.rect.x+64, self.rect.y+32-10)
        self.eye_bullet4 = Eye_Bullet(self.rect.x-20, self.rect.y+32-10)
        # attack2
        self.eye_bullet5 = Eye_Bullet(self.rect.x-14, self.rect.y+64)
        self.eye_bullet6 = Eye_Bullet(self.rect.x+10, self.rect.y+64)
        self.eye_bullet7 = Eye_Bullet(self.rect.x+34, self.rect.y+64)
        self.eye_bullet8 = Eye_Bullet(self.rect.x+58, self.rect.y+64)
        # attack3
        self.eye_bullet9 = Eye_Bullet(self.rect.x+32-10, self.rect.y+64)
        self.eye_bullet10 = Eye_Bullet(self.rect.x+32-10, self.rect.y-20)
        self.eye_bullet11 = Eye_Bullet(self.rect.x+64, self.rect.y+32-10)
        self.eye_bullet12 = Eye_Bullet(self.rect.x-20, self.rect.y+32-10)
        self.eye_bullet13 = Eye_Bullet(self.rect.x-8, self.rect.y-8)
        self.eye_bullet14 = Eye_Bullet(self.rect.x+self.en-12, self.rect.y+self.boy-12)
        self.eye_bullet15 = Eye_Bullet(self.rect.x+self.en-12, self.rect.y-8)
        self.eye_bullet16 = Eye_Bullet(self.rect.x-8, self.rect.y+self.boy-12)
        # attack4
        self.eye_bullet17 = Eye_Bullet(self.rect.x-50, self.rect.y+64)
        self.eye_bullet18 = Eye_Bullet(self.rect.x-74, self.rect.y+64)
        self.eye_bullet19 = Eye_Bullet(self.rect.x-98, self.rect.y+64)
        self.eye_bullet20 = Eye_Bullet(self.rect.x-122, self.rect.y+64)
        self.eye_bullet21 = Eye_Bullet(self.rect.x+self.en+34, self.rect.y+64)
        self.eye_bullet22 = Eye_Bullet(self.rect.x+self.en+58, self.rect.y+64)
        self.eye_bullet23 = Eye_Bullet(self.rect.x+self.en+82, self.rect.y+64)
        self.eye_bullet24 = Eye_Bullet(self.rect.x+self.en+106, self.rect.y+64)

    def draw_health_bar(self):
        pygame.draw.rect(ekran,(255,0,0),(self.x-44,self.y-20,self.health,10))

    def draw(self):
        ekran.blit(self.image,self.rect)

    def kill(self):
        if self.health <= 0:
            self.died = 1

    def attack(self):
        if self.attack_type == 1:
            self.attack_type_time += 1
            eye_bullets.append(self.eye_bullet1)
            eye_bullets.append(self.eye_bullet2)
            eye_bullets.append(self.eye_bullet3)
            eye_bullets.append(self.eye_bullet4)
            self.eye_bullet1.rect.y += 8
            self.eye_bullet2.rect.y -= 8
            self.eye_bullet3.rect.x += 8
            self.eye_bullet4.rect.x -= 8

        if self.attack_type == 2:
            self.attack_type_time += 1
            eye_bullets.append(self.eye_bullet5)
            eye_bullets.append(self.eye_bullet6)
            eye_bullets.append(self.eye_bullet7)
            eye_bullets.append(self.eye_bullet8)
            self.eye_bullet5.rect.y += 8
            self.eye_bullet6.rect.y += 8
            self.eye_bullet7.rect.y += 8
            self.eye_bullet8.rect.y += 8

        if self.attack_type == 3:
            self.attack_type_time += 1
            eye_bullets.append(self.eye_bullet9)
            eye_bullets.append(self.eye_bullet10)
            eye_bullets.append(self.eye_bullet11)
            eye_bullets.append(self.eye_bullet12)
            eye_bullets.append(self.eye_bullet13)
            eye_bullets.append(self.eye_bullet14)
            eye_bullets.append(self.eye_bullet15)
            eye_bullets.append(self.eye_bullet16)
            self.eye_bullet9.rect.y += 8
            self.eye_bullet10.rect.y -= 8
            self.eye_bullet11.rect.x += 8
            self.eye_bullet12.rect.x -= 8
            self.eye_bullet13.rect.y -= 8
            self.eye_bullet13.rect.x -= 8
            self.eye_bullet14.rect.y += 8
            self.eye_bullet14.rect.x += 8
            self.eye_bullet15.rect.y -= 8
            self.eye_bullet15.rect.x += 8
            self.eye_bullet16.rect.y += 8
            self.eye_bullet16.rect.x -= 8

        if self.attack_type == 4:
            self.attack_type_time += 1
            eye_bullets.append(self.eye_bullet17)
            eye_bullets.append(self.eye_bullet18)
            eye_bullets.append(self.eye_bullet19)
            eye_bullets.append(self.eye_bullet20)
            eye_bullets.append(self.eye_bullet21)
            eye_bullets.append(self.eye_bullet22)
            eye_bullets.append(self.eye_bullet23)
            eye_bullets.append(self.eye_bullet24)
            self.eye_bullet17.rect.y += 8
            self.eye_bullet18.rect.y += 8
            self.eye_bullet19.rect.y += 8
            self.eye_bullet20.rect.y += 8
            self.eye_bullet21.rect.y += 8
            self.eye_bullet22.rect.y += 8
            self.eye_bullet23.rect.y += 8
            self.eye_bullet24.rect.y += 8

        if self.attack_type_time >= 70:
            self.attack_type = random.choice([1,2,3,4])
            self.attack_type_time = 0
            self.position_bullet()

    def update(self):
        self.draw()
        self.draw_health_bar()
        self.attack()
        self.kill()

pygame.init()

width = 500
height = 650 
ekran = pygame.display.set_mode((width,height))
pygame.display.set_caption('Bullet Hell')
clock = pygame.time.Clock()

game = 1

player = Player(x=width//2-32,y=500,en=64,boy=64,speed=5)
bullets = []

eye = Enemy(x=width//2-32,y=100,en=64,boy=64,speed=5)
eye_bullets = []

buton = pygame.Rect((60,290,380,90))
def player_kill_menu():
    font = pygame.font.Font(None,100)
    text = font.render('You Died',True,(0,0,0))
    ekran.blit(text,(100,100))
    text_pa = font.render('Play Again',True,(0,0,0))
    ekran.blit(text_pa,(70,300))

def eye_kill_menu():
    font = pygame.font.Font(None,60)
    font2 = pygame.font.Font(None,100)
    text = font.render('The enemy has been',True,(0,0,0))
    ekran.blit(text,(44,100))
    text = font.render('destroyed',True,(0,0,0))
    ekran.blit(text,(150,170))
    text_pa = font2.render('You won',True,(0,0,0))
    ekran.blit(text_pa,(120,330))

def reset():
    player.health = 100
    eye.health = 150
    eye.attack_type_time = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if buton.collidepoint(mouse_pos):
                game = 1
                reset()

    ekran.fill((234,164,108))
    if game == 1:
        eye.update()
        player.update()
        for bullet in bullets:
            bullet.update()
        for eye_bullet in eye_bullets:
            eye_bullet.update()
    if game == 0:
        player_kill_menu()
    if eye.died == 1:
        eye_kill_menu()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()