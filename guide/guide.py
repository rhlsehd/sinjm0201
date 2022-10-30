# Imports
from re import A
import sys
import pygame
import os
import time
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 480, 640
screen = pygame.display.set_mode((width, height))
color = (164,203,163)
black = (255,255,255)
white = (0,0,0)
font = pygame.font.SysFont('새굴림', 30)
pygame.display.set_caption("한신대학교 신입생 가이드")
objects = []

myFont = pygame.font.SysFont( "새굴림", 50, True, False)

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")
#-----------------------------------------------------------------------
img = pygame.image.load(os.path.join(image_path,"fdfd.png"))
img = pygame.transform.scale(img,(80,80))
img1 = pygame.image.load(os.path.join(image_path,"asdf.png"))
img1 = pygame.transform.scale(img1,(450,450))
img2 = pygame.image.load(os.path.join(image_path,"map.png"))
img2 = pygame.transform.scale(img2,(450,450))
장공관 = pygame.image.load(os.path.join(image_path,"장공관.png"))
장공관  = pygame.transform.scale(장공관,(450,450))
장공관설명 = pygame.image.load(os.path.join(image_path,"장공관설명.png"))
장공관설명 = pygame.transform.scale(장공관설명,(450,120))
필헌관 = pygame.image.load(os.path.join(image_path,"필헌관.png"))
필헌관 = pygame.transform.scale(필헌관,(450,450))
필헌관설명 = pygame.image.load(os.path.join(image_path,"필헌관설명.png"))
필헌관설명 = pygame.transform.scale(필헌관설명,(450,130))
만우관 = pygame.image.load(os.path.join(image_path,"만우관.png"))
만우관 = pygame.transform.scale(만우관,(450,450))
만우관설명 = pygame.image.load(os.path.join(image_path,"만우관설명.png"))
만우관설명 = pygame.transform.scale(만우관설명,(450,130))
샬롬채플관 = pygame.image.load(os.path.join(image_path,"샬롬채플관.png"))
샬롬채플관 = pygame.transform.scale(샬롬채플관,(450,450))
샬롬채플관설명 = pygame.image.load(os.path.join(image_path,"샬롬채플관설명.png"))
샬롬채플관설명 = pygame.transform.scale(샬롬채플관설명,(450,130))
임마누엘관 = pygame.image.load(os.path.join(image_path,"임마누엘관.png"))
임마누엘관 = pygame.transform.scale(임마누엘관,(450,450))
임마누엘관설명 = pygame.image.load(os.path.join(image_path,"임마누엘관설명.png"))
임마누엘관설명 = pygame.transform.scale(임마누엘관설명,(450,130))
경삼관 = pygame.image.load(os.path.join(image_path,"경삼관.png"))
경삼관 = pygame.transform.scale(경삼관,(450,450))
경삼관설명 = pygame.image.load(os.path.join(image_path,"경삼관설명.png"))
경삼관설명 = pygame.transform.scale(경삼관설명,(450,130))
송암관 = pygame.image.load(os.path.join(image_path,"송암관.png"))
송암관 = pygame.transform.scale(송암관,(450,450))
송암관설명 = pygame.image.load(os.path.join(image_path,"송암관설명.png"))
송암관설명 = pygame.transform.scale(송암관설명,(450,130))
소통관 = pygame.image.load(os.path.join(image_path,"소통관.png"))
소통관 = pygame.transform.scale(소통관,(450,450))
소통관설명 = pygame.image.load(os.path.join(image_path,"소통관설명.png"))
소통관설명 = pygame.transform.scale(소통관설명,(450,130))
실습동 = pygame.image.load(os.path.join(image_path,"실습동.png"))
실습동 = pygame.transform.scale(실습동,(450,450))
실습동설명 = pygame.image.load(os.path.join(image_path,"실습동설명.png"))
실습동설명 = pygame.transform.scale(실습동설명,(450,130))
한울관 = pygame.image.load(os.path.join(image_path,"한울관.png"))
한울관 = pygame.transform.scale(한울관,(450,450))
한울관설명 = pygame.image.load(os.path.join(image_path,"한울관설명.png"))
한울관설명 = pygame.transform.scale(한울관설명,(450,130))
성빈학사 = pygame.image.load(os.path.join(image_path,"성빈학사.png"))
성빈학사 = pygame.transform.scale(성빈학사,(450,450))
성빈학사설명 = pygame.image.load(os.path.join(image_path,"성빈학사설명.png"))
성빈학사설명 = pygame.transform.scale(성빈학사설명,(450,130))
새롬터설명 = pygame.image.load(os.path.join(image_path,"새롬터설명.png"))
새롬터설명 = pygame.transform.scale(새롬터설명,(450,130))
해오름관 = pygame.image.load(os.path.join(image_path,"해오름관.png"))
해오름관 = pygame.transform.scale(해오름관,(450,450))
해오름관설명 = pygame.image.load(os.path.join(image_path,"해오름관설명.png"))
해오름관설명 = pygame.transform.scale(해오름관설명,(450,130))
장준하통일관 = pygame.image.load(os.path.join(image_path,"장준하통일관.png"))
장준하통일관 = pygame.transform.scale(장준하통일관,(450,450))
장준하통일관설명 = pygame.image.load(os.path.join(image_path,"장준하통일관설명.png"))
장준하통일관설명 = pygame.transform.scale(장준하통일관설명,(450,130))
늦봄관 = pygame.image.load(os.path.join(image_path,"늦봄관.png"))
늦봄관 = pygame.transform.scale(늦봄관,(450,450))
늦봄관설명 = pygame.image.load(os.path.join(image_path,"늦봄관설명.png"))
늦봄관설명 = pygame.transform.scale(늦봄관설명,(450,130))
#-----------------------------------------------------------------------------

나누리1 = pygame.image.load(os.path.join(image_path,"나누리1.jpg"))
나누리1 = pygame.transform.scale(나누리1,(450,450))
나누리2 = pygame.image.load(os.path.join(image_path,"나누리2.jpg"))
나누리2 = pygame.transform.scale(나누리2,(450,450))
나누리3 = pygame.image.load(os.path.join(image_path,"나누리3.jpg"))
나누리3 = pygame.transform.scale(나누리3,(450,450))
나누리4 = pygame.image.load(os.path.join(image_path,"나누리4.jpg"))
나누리4 = pygame.transform.scale(나누리4,(450,450))
나누리5 = pygame.image.load(os.path.join(image_path,"나누리5.jpg"))
나누리5 = pygame.transform.scale(나누리5,(450,450))
나누리6 = pygame.image.load(os.path.join(image_path,"나누리6.jpg"))
나누리6 = pygame.transform.scale(나누리6,(450,450))
나누리7 = pygame.image.load(os.path.join(image_path,"나누리7.jpg"))
나누리7 = pygame.transform.scale(나누리7,(450,450))
치킨1 = pygame.image.load(os.path.join(image_path,"치킨1.jpg"))
치킨1 = pygame.transform.scale(치킨1,(450,450))
치킨2 = pygame.image.load(os.path.join(image_path,"치킨2.jpg"))
치킨2 = pygame.transform.scale(치킨2,(450,450))
치킨3 = pygame.image.load(os.path.join(image_path,"치킨3.jpg"))
치킨3 = pygame.transform.scale(치킨3,(450,450))
치킨4 = pygame.image.load(os.path.join(image_path,"치킨4.jpg"))
치킨4 = pygame.transform.scale(치킨4,(450,450))
해우리1 = pygame.image.load(os.path.join(image_path,"해우리1.jpg"))
해우리1 = pygame.transform.scale(해우리1,(450,450))
해우리2 = pygame.image.load(os.path.join(image_path,"해우리2.jpg"))
해우리2 = pygame.transform.scale(해우리2,(450,450))
탑노래연습장설명 = pygame.image.load(os.path.join(image_path,"탑노래연습장설명.png"))
탑노래연습장설명 = pygame.transform.scale(탑노래연습장설명,(450,130))
코인노래방설명 = pygame.image.load(os.path.join(image_path,"코인노래방설명.png"))
코인노래방설명 = pygame.transform.scale(코인노래방설명,(450,130))
밥피씨설명 = pygame.image.load(os.path.join(image_path,"밥피씨설명.png"))
밥피씨설명 = pygame.transform.scale(밥피씨설명,(450,130))
스토리피시방설명 = pygame.image.load(os.path.join(image_path,"스토리피시방설명.png"))
스토리피시방설명 = pygame.transform.scale(스토리피시방설명,(450,130))




class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal' : '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                
                if not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
               
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)
    def __del__(self):
       pass
#---------------------------------------------------------------   
global controler
controler = 0

global a
a = 1
#초기화면
def controler0():
    global controler
    controler = 0
    return controler
#학교시설
def controler1():
    global controler
    controler = 1
    return controler
#편의시설
def controler2():
    global controler
    controler = 2
    return controler
#학교약도
def controler3():
    global controler
    controler = 3
    return controler

def controler4():
    global controler
    controler = 4
    return controler

def controler5():
    global controler
    controler = 5
    return controler

def controler6():
    global controler
    controler = 6
    return controler

def controler7():
    global controler
    controler = 7
    return controler

def controler8():
    global controler
    controler = 8
    return controler

def controler9():
    global controler
    controler = 9
    return controler

def controler10():
    global controler
    controler = 10
    return controler

def controler11():
    global controler
    controler = 11
    return controler

def controler12():
    global controler
    controler = 12
    return controler

def controler13():
    global controler
    controler = 13
    return controler

def controler14():
    global controler
    controler = 14
    return controler

def controler15():
    global controler
    controler = 15
    return controler

def controler16():
    global controler
    controler = 16
    return controler

def controler17():
    global controler
    controler = 17
    return controler

def controler18():
    global controler
    controler = 18
    return controler

def controler19():
    global controler
    controler = 19
    return controler

def controler20():
    global controler
    controler = 20
    return controler

def controler21():
    global controler
    controler = 21
    return controler

def controler22():
    global controler
    controler = 22
    return controler

def controler23():
    global controler
    controler = 23
    return controler

def controler24():
    global controler
    controler = 24
    return controler

def controler25():
    global controler
    controler = 25
    return controler

def controler26():
    global controler
    controler = 26
    return controler

def controler27():
    global controler
    controler = 27
    return controler

def controler999():
    global controler
    controler = 999
    return controler

def a_upctr() :
    time.sleep(0.095)
    global a
    a += 1
    return a
def a_downctr() :
    time.sleep(0.095)
    global a
    a -= 1
    return a


while True:
    
    screen.fill(color)
    screen.blit(img,(0,0))
    
    if controler == 0 :

        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 640
        screen = pygame.display.set_mode((width, height))
        color = (164,203,163)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []

        screen.fill(color)
        screen.blit(img,(0,0))
        sc = Button(40, 80, 400, 200, '학교 시설',controler1)
        le = Button(40, 350, 400, 200, '편의 시설',controler2)
        Button(320, 580, 120, 30, '나가기/종료',controler999)

    
    elif controler == 1 :
        time.sleep(0.095)
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 900, 600
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []

        screen.fill(color1)
        screen.blit(img,(0,0))
        
        Button(70, 90, 120, 120, '장공관',controler5)
        Button(230, 90, 120, 120,  '필헌관',controler6)
        Button(390, 90, 120, 120, '만우관',controler7)
        Button(550, 90, 120, 120, '샬롬채플관',controler8)
        Button(710, 90, 120, 120, '임마누엘관',controler9)
        Button(70, 250, 120, 120, '경삼관',controler10)
        Button(230, 250, 120, 120, '송암관',controler11)
        Button(390, 250, 120, 120, '소통관',controler12)
        Button(550, 250, 120, 120, '학과실습동',controler13)
        Button(710, 250, 120, 120, '한울관',controler14)
        Button(70, 410, 120, 120, '성빈학사',controler15)
        Button(230, 410, 120, 120, '새롬터',controler16)
        Button(390, 410, 120, 120, '해오름관',controler17)
        Button(550, 410, 120, 120, '60주년기념관',controler18)
        Button(710, 410, 120, 120, '늦봄관',controler19)
        Button(710, 10, 120, 60, '뒤로가기<-',controler0)
        Button(150, 10, 120, 60, '약도 보기',controler3)
        Button(710, 550, 120, 30, '나가기/종료',controler999)
        
    elif controler == 2 :
        time.sleep(0.095)
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 700, 500
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []

        screen.fill(color1)
        screen.blit(img,(0,0))

        Button(50, 130, 120, 120, '나누리',controler20)
        Button(290, 130, 120, 120,  '해우리',controler21)
        Button(530, 130, 150, 120, '깻잎두마리치킨',controler23)
        Button(50, 290, 120, 120, '탑노래연습장',controler24)
        Button(210, 290, 120, 120, '코인노래방',controler25)
        Button(370, 290, 120, 120, '밥pc방',controler26)
        Button(530, 290, 120, 120, '스토리pc방',controler27)
        Button(150, 10, 120, 60, '약도 보기',controler4)
        Button(530, 10, 120, 60, '뒤로가기<-',controler0)
        Button(530, 450, 120, 30, '나가기/종료',controler999)

    elif controler == 3 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 640
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(img,(0,0))
        screen.blit(img1,(15,100))


    elif controler == 4 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 640
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler2)
        
        screen.fill(color1)
        screen.blit(img2,(15,100))

    elif controler == 5 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        
        
        screen.fill(color1)
        screen.blit(장공관,(15,80))
        screen.blit(장공관설명,(15,550))
       
    elif controler == 6 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(필헌관,(15,80))
        screen.blit(필헌관설명,(15,550))

    elif controler == 7 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(만우관,(15,80))
        screen.blit(만우관설명,(15,550))

    elif controler == 8 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(샬롬채플관,(15,80))
        screen.blit(샬롬채플관설명,(15,550))

    elif controler == 9 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(임마누엘관,(15,80))
        screen.blit(임마누엘관설명,(15,550))

    elif controler == 10 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(경삼관,(15,80))
        screen.blit(경삼관설명,(15,550))

    elif controler == 11 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(송암관,(15,80))
        screen.blit(송암관설명,(15,550))

    elif controler == 12 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(소통관,(15,80))
        screen.blit(소통관설명,(15,550))

    elif controler == 13 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(실습동,(15,80))
        screen.blit(실습동설명,(15,550))

    elif controler == 14 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(한울관,(15,80))
        screen.blit(한울관설명,(15,550))

    elif controler == 15 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(성빈학사,(15,80))
        screen.blit(성빈학사설명,(15,550))

    elif controler == 16 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(새롬터설명,(15,350))
        

    elif controler == 17 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(해오름관,(15,80))
        screen.blit(해오름관설명,(15,550))


    elif controler == 18 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(장준하통일관,(15,80))
        screen.blit(장준하통일관설명,(15,550))

    elif controler == 19 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler1)
        screen.fill(color1)
        screen.blit(늦봄관,(15,80))
        screen.blit(늦봄관설명,(15,550))

    elif controler == 20 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler2)
        Button(40, 550, 60, 60, '<',a_downctr)
        Button(390, 550, 60, 60, '>',a_upctr)
        
        screen.fill(color1)
        
        if a < 1 :
            a = 7
        elif a > 7 :
            a = 1

        if a == 1:
            screen.blit(나누리1,(15,80))
        elif a == 2:
            screen.blit(나누리2,(15,80))
        elif a == 3:
            screen.blit(나누리3,(15,80))
        elif a == 4:
            screen.blit(나누리4,(15,80))
        elif a == 5:
            screen.blit(나누리5,(15,80))
        elif a == 6:
            screen.blit(나누리6,(15,80))
        elif a == 7:
            screen.blit(나누리7,(15,80))
               

    elif controler == 21 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler2)
        Button(40, 550, 60, 60, '<',a_downctr)
        Button(390, 550, 60, 60, '>',a_upctr)
        screen.fill(color1)
        if a < 1 :
            a = 2
        elif a > 2 :
            a = 1

        if a == 1:
            screen.blit(해우리1,(15,80))
        elif a == 2:
            screen.blit(해우리2,(15,80))
    
    elif controler == 23 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler2)
        Button(40, 550, 60, 60, '<',a_downctr)
        Button(390, 550, 60, 60, '>',a_upctr)
        screen.fill(color1)
        
        if a < 1 :
            a = 4
        elif a > 4 :
            a = 1

        if a == 1:
            screen.blit(치킨1,(15,80))
        elif a == 2:
            screen.blit(치킨2,(15,80))
        elif a == 3:
            screen.blit(치킨3,(15,80))
        elif a == 4:
            screen.blit(치킨4,(15,80))
    
    elif controler == 24 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler2)
        screen.fill(color1)
        screen.blit(송암관,(15,80))
        screen.blit(탑노래연습장설명,(15,550))
    
    elif controler == 25 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler2)
        screen.fill(color1)
        screen.blit(송암관,(15,80))
        screen.blit(코인노래방설명,(15,550))
    
    elif controler == 26 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler2)
        screen.fill(color1)
        screen.blit(송암관,(15,80))
        screen.blit(밥피씨설명,(15,550))
    
    elif controler == 27 :
    
        pygame.init()
        fps = 60
        fpsClock = pygame.time.Clock()
        width, height = 480, 700
        screen = pygame.display.set_mode((width, height))
        color1 = (246,248,201)
        font = pygame.font.SysFont('새굴림', 20)
        objects = []
        Button(350, 10, 120, 60, '뒤로가기<-',controler2)
        screen.fill(color1)
        screen.blit(송암관,(15,80))
        screen.blit(스토리피시방설명,(15,550))
    
    elif controler == 999 :
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for object in objects:
        object.process()
    pygame.display.flip()
    fpsClock.tick(fps)