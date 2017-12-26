add_library('sound')
import os, random
path=os.getcwd() 
import time
platformImage =loadImage(path+'/platform.png')
scoreFile = open(path+"\scores.txt", "a")
scoreFile.close()
name = ""

class Game:
    def __init__(self,w,h,g):
        self.w=w #width
        self.h=h #height 
        self.g=g #ground level
        self.male=Male(100,100,92,self.g,"male.png",184,184,8) #Change the radious to the size of the height of the person, because it is taller than it is wider. 
        #self.gameOverSound=SoundFile(this,path+'\\gameOverSound.mp3') # windows '\\'
        #self.music.play() #We put it here so that the music will only play once
        self.x = 0 #The position in the screen, it begins at zero
        self.enemies=[]
        self.pause=False
        self.bg=[]
        self.state='menu'
        self.name=""
        self.stage=1
        self.loadStage()
        self.musicSound = SoundFile(this,path+'\\musicSound.mp3')
        self.raindropcnt = 0
        
    
        

    
    def loadStage(self): #Make one for each group of collectibles or make one for each bigger category
        self.platforms = []
        self.enemies = []
        self.collectibles = []
        self.avoid = []
        self.bg = []
        self.girl=[]
        self.powerUps= []
        self.raindrops = []
        self.bills= []
        self.messages = []
        self.powerUpcnt = 0
        self.raindropcnt = 0
    
        if self.stage == 1: #This is the city stage
            self.bg = []
            self.raindropcnt = 0
            self.g=549
            for i in range(1,9): #There are 1-8 images in this background
                self.bg.append(loadImage(path+'/Citylayer_0'+str(i)+'.png'))
            f = open(path+'/stage'+str(self.stage)+'.csv',"r") #open the stage
            for l in f: #for line in f        the for loop automatically reads through the file line by line
                l=l.strip().split(",") #make it into a list
                if l[0]=='Platform': #if the first element of the line is platform
                    self.platforms.append(Platform(int(l[1]),int(l[2]),int(l[3]),int(l[4])))
                elif l[0]=='Wink':
                    self.collectibles.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0]=='MoneyBag':
                    self.collectibles.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "BadMan":
                    self.enemies.append(BadMan(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7]), self))
                elif l[0] == "Voltage":
                    self.powerUps.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Raindrop":
                    self.raindrops.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Bill":
                    self.bills.append(Bills(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Message":
                    self.messages.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
            f.close()
      
        if self.stage == 3: #This is the forest night stage, the hardest one, originally stage 3
            self.bg = []
            self.raindropcnt = 0
            self.g = 504
            for i in range(1,8):
                self.bg.append(loadImage(path+'/Forestlayer_0'+str(i)+'.png'))
            f = open(path+'/stage'+str(self.stage)+'.csv',"r") #open the stage
            for l in f: #for line in f        the for loop automatically reads through the file line by line
                l=l.strip().split(",") #make it into a list
                if l[0]=='Platform': #if the first element of the line is platform
                    self.platforms.append(Platform(int(l[1]),int(l[2]),int(l[3]),int(l[4])))
                elif l[0]=='Smoke':
                    self.enemies.append(EnemyEmoji(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0]=='Heart':
                    self.collectibles.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "BadMan":
                    self.enemies.append(BadMan(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7]), self))
                elif l[0] == "Lips":
                    self.collectibles.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Avoid":
                    self.avoid.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Girl":
                    self.girl.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Voltage":
                    self.powerUps.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Raindrop":
                    self.raindrops.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Bill":
                    self.bills.append(Bills(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Message":
                    self.messages.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
            f.close()
      
        if self.stage ==2: #This is beach
            self.bg = []
            self.raindropcnt = 0
            self.g = 570
            for i in range(1,7):
                self.bg.append(loadImage(path+'/Beachlayer_0'+str(i)+'.png'))
            f = open(path+'/stage'+str(self.stage)+'.csv',"r") #open the stage
            for l in f: #for line in f        the for loop automatically reads through the file line by line
                l=l.strip().split(",") #make it into a list
                if l[0]=='Platform': #if the first element of the line is platform
                    self.platforms.append(Platform(int(l[1]),int(l[2]),int(l[3]),int(l[4])))
                elif l[0]=='Angry':
                    self.enemies.append(EnemyEmoji(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0]=='Kissy':
                    self.collectibles.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "BadMan":
                    self.enemies.append(BadMan(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7]), self))
                elif l[0] == "HeartEyes":
                    self.collectibles.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Avoid":
                    self.avoid.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Voltage":
                    self.powerUps.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Raindrop":
                    self.raindrops.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Bill":
                    self.bills.append(Bills(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
                elif l[0] == "Message":
                    self.messages.append(Collectibles(int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],int(l[6]),int(l[7])))
            f.close()
    
            
        
    def display(self):          #first display the background and then the remaining stuff
        if self.state == 'menu':
            openImage= loadImage(path+'\\openScreen.png')
            image(openImage,0,0)
            CartoonishFont = createFont(path+"/Cartoonish.ttf",40)
            textFont(CartoonishFont)
            text("Player: "+self.name,20,50)
      
            if game.w//2-100 <= mouseX <= game.w//2+100 and game.h//2+70 <= mouseY <= game.h//2+110: #Change these dimensions because our background is different?
                fill(0,255,0)
            else:
                fill(0,0,123)
                text("Play game",game.w//2-100,game.h//2+100)
            
            scoresDict={}
            inScores=open(path+"\scores.txt", "r")

            inScores.readline()
            for line in inScores:
                scoreList=line.split(",")
                scoresDict[int(scoreList[1])]=scoreList[0]
            inScores.close()
            
            #scores=list(scoresDict.keys())
            scoresSorted=sorted(list(scoresDict.keys()))
            lastScore=game.male.score
            highScore1=scoresSorted[-1]
            highScore2=scoresSorted[-2]
            highScore3=scoresSorted[-3]
            name1=scoresDict.get(highScore1,"No Name")
            name2=scoresDict.get(highScore2,"No Name")
            name3=scoresDict.get(highScore3,"No Name")
            textFont(CartoonishFont)
            text("Previous Score: "+str(lastScore),game.w//2-200,game.h//2+200)
            text("1. "+(name1)+"..."+str(highScore1),10,280)
            text("2. "+(name2)+"..."+str(highScore2),10,380)
            text("3. "+(name3)+"..."+str(highScore3),10,480)
            
            
            
                
        elif self.state=='play':
            for i in range(len(self.bg)):
                try:
                    x = (self.x//(8-2*i))%self.w  # a modular operator that keeps on reiterating the screen over and over, each image will have a different velocity
                except:
                    x = self.x%self.w #Move at the speed of the Male

                image(self.bg[-i-1],0,0,self.w-x,self.h,x,0,self.w,self.h) #Checkered area
                image(self.bg[-i-1],self.w-x-1,0,x,self.h,0,0,x,self.h) #Dashed area, we subtracted one so that the extra pixel would not ruin the image
        
            for p in self.platforms:
                p.display()
        
            for e in self.enemies:
                e.display()
          
            for a in self.avoid:
                a.display()
        
            for g in self.girl:
                g.display()
          
            for c in self.collectibles:
                c.display()
                
            for p in self.powerUps:
                p.display()
            
            for r in self.raindrops:
                r.display()
                
            for m in self.messages:
                m.display()
            
            if self.raindropcnt > 0:
                for b in self.bills:
                    b.display()
            
                
            self.male.display()
            
        
            
            textSize(40)
            fill(0,255,0)
            text("Attractiveness: " + str(self.male.score), 100,100)
            
 
        
        

class Creature:
  def __init__(self,x,y,r,g,img,w,h,F):
    self.x=x
    self.y=y
    self.vx=0 #velocity
    self.vy=0
    self.w=w
    self.h=h
    self.F=F #frames
    self.f=0 #current frame
    self.r=r #radius let's think of the character as a circle for collison detection
    self.g=g #ground
    self.dir=1 #direction = 1, creature is facing right
    self.img=loadImage(path+'\\'+img) # Is this the right way to call it?
    
    
  def gravity(self):  
    if self.y+self.r < self.g:#Whenever the male or other creatures are higher than the absolute ground, they fall.
      self.vy+=0.3 #character accelerates
    else:
      self.vy=0
      
    if self.g-(self.y+self.r) < self.vy: #If the ground minus the creature is less than the position of the creature, use this to avoid a dip undernath the ground
      self.vy = self.g-(self.y+self.r)
      
    for p in game.platforms: #when he jumps, the program measures if the Male is higher than the platform and in the same range of y and if it is, the platform will be the new ground
      if self.x > p.x and self.x < p.x+p.w and self.y+self.r <= p.y:
        self.g=p.y         #the ground changes to the platform
        break
      self.g=game.g
      
  def update(self): #y is the center of the circle, so y + radius to compare to ground level
    self.gravity()
      
    self.x+=self.vx
    self.y+=self.vy
    
  def display(self):
    self.update() #call update here to use in every frame
    if self.vx != 0: #The frame will only change when the guy is running
      self.f=(self.f+0.1)%self.F
    else:
        self.f=4       #standing guy when there is no movement
    
    if self.dir >=0:
        image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f)*self.w,0,int(self.f+1)*self.w,self.h) #subtract r to align image with circle, cropping, we cast this into an integer because frames cant be decimals
    else:
        image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h) #If we are going back, we need to reflect the image, swap the x directions and mirror image
    

class Male(Creature):
    def __init__(self,x,y,r,g,img,w,h,F):
        Creature.__init__(self,x,y,r,g,img,w,h,F)
        self.keyHandler={RIGHT:False,LEFT:False,UP:False}
        self.win = False
        self.gameOver = False
        self.score = 0
        self.gameOverSound=SoundFile(this,path+'\\gameOverSound.mp3') # windows '\\'
        self.collectiblesSound=SoundFile(this,path+'\\collectiblesSound.mp3') # windows '\\
        self.collectiblesSound=SoundFile(this,path+'\\collectiblesSound.mp3') # windows '\\
        self.billSound = SoundFile(this,path+'\\billSound.mp3') # windows '\\
        self.avoidSound = SoundFile(this,path+'\\avoidSound.mp3') # windows '\\
        self.raindropSound = SoundFile(this,path+'\\raindropSound.mp3')
        self.killingSound = SoundFile(this,path+'\\killingSound.mp3')
        self.powerUpSound = SoundFile(this,path+'\\powerUpSound.mp3')
        self.jumpSound = SoundFile(this,path+"\\jumpSound.mp3")
        self.powerUpcnt = 0

    def collision(self):
        for c in game.collectibles:
            if self.distance(c) <= self.r+c.r:
                game.collectibles.remove(c)
                self.score += 100
                self.collectiblesSound.play()
                del c #insert kill sound after this
        
        for a in game.avoid:
            if self.distance(a) <= self.r+a.r: 
                game.avoid.remove(a)
                self.score -= 100
                self.avoidSound.play()
                del a #insert kill sound after this
        
        for g in game.girl:
            if self.distance(g) <= self.r+g.r: 
                game.girl.remove(g)
                self.win = True
                del g
                game.state="win"
                game.musicSound.stop()
                
        
        for p in game.powerUps:
            if self.distance(p) <= self.r+p.r: 
                game.powerUps.remove(p)
                del p #insert powerup sound after this
                self.collectiblesSound.play()
                self.powerUpcnt += 180 #We want him to speed up for 5 seconds
                self.powerUpSound.play()
        
        for r in game.raindrops:
            if self.distance(r) <= self.r+r.r: 
                game.raindrops.remove(r)
                del r #insert kill sound after this
                self.raindropSound.play()
                game.raindropcnt += 1
        
        for b in game.bills: #money sound
            if self.distance(b) <= self.r+b.r: 
                game.bills.remove(b)
                self.score += 200
                self.billSound.play()
                del b #insert kill sound after this
                
            
        for m in game.messages:
            if self.distance(m) <= self.r+m.r:
                game.messages.remove(m)
                del m 
        
    
        for e in game.enemies:
            if self.powerUpcnt == 0: #We only want these things to happen if the male does not have a powerup
                if self.distance(e) <= self.r+e.r: # there is a collision
                    if self.vy > 0 and self.y+self.r < e.y:    #If the enemies clash with the male, the enemies will be removed, velocity has to be greater than zero because I have to be falling down
                        game.enemies.remove(e)
                        del e
                        self.vy=-5  #it bounces when it hits one of the enemies
                        self.score += 500
                        self.killingSound.play()
                    else: # male dies, we need to disable update#We can't simply make male jump because we need more than one frame, we need time to display all the frames for the jump
                        self.vy = -10         #Jumps up
                        game.musicSound.stop()
                        CartoonishFont = createFont(path+"/Cartoonish.ttf",40)                
                        self.gameOverSound.play()
                        game.state = "gameOver"
          
    def update(self): #y is the center of the circle, so y + radius to compare to ground level
        if not self.gameOver:
            self.gravity() 
            self.collision()
            if self.powerUpcnt==0:
                if self.keyHandler[RIGHT]: 
                    self.vx=5
                    self.dir=1 #If male goes right, he will face that direction
                elif self.keyHandler[LEFT]: #velocity in negative direction
                    self.vx=-5
                    self.dir=-1 #If he goes left, the direction changes
                else:
                    self.vx=0
        
                if self.keyHandler[UP] and self.vy==0: #The if conditions are separate because we want the creature to be able to move up and left/right at the same time
                    self.vy=-13 #similar to bouncing #We nnly want him to jumpt whrn the creature is at the grounf
                    self.jumpSound.play()
            else:
                if self.keyHandler[RIGHT]: 
                    self.vx=10
                    self.dir=1 #If male goes right, he will face that direction
                elif self.keyHandler[LEFT]: #velocity in negative direction
                    self.vx=-10
                    self.dir=-1 #If he goes left, the direction changes
                else:
                    self.vx=0
        
                if self.keyHandler[UP] and self.vy==0: #The if conditions are separate because we want the creature to be able to move up and left/right at the same time
                    self.vy=-13 #similar to bouncing #We nnly want him to jumpt whrn the creature is at the grounf
                    #self.jumpSound.play()
        else:       #die conditions: no platform, no movement to sides, jump and fall
            self.vy+=0.4
            self.vx=0 #This will make sure he doesnt move to the sides    
            if self.y-self.r > game.h: # > game height (if male is off the screen)
                game.__init__(game.w,game.h,game.g)        #We restart the game, we reset everything
        
        self.x+=self.vx
        self.y+=self.vy
       
        if self.x >= game.w//2 and self.x < 7000:  #When male reaches the Middle of the screen, the background will shift       
            game.x+=self.vx #The screen will move at male's velocity, everything has to shift at the same velocity (game.x)
    
        if self.x-self.r < 0:
            self.x=self.r
        
        if self.x-self.r > 7000+game.w//2 and game.stage<3: #if the left side of male becomes greater than the end of the screen (7000, when the screen stops moving + half of the width of the game
            game.stage+=1
            self.x=50 #move male to the beginning
            game.x=0  #k0vement of the screen goes back to zero
            game.loadStage()
        
        if self.powerUpcnt > 0: 
            self.powerUpcnt -= 1 #(We subtract one after every frame)
            self.vx=12
        
            
            
    
    
    def distance(self,target):
        return ((self.x-target.x)**2+(self.y-target.y)**2)**0.5

class Platform:
  def __init__(self,x,y,w,h):
    self.x=x
    self.y=y
    self.w=w
    self.h=h


    
  def display(self):
    global platformImage
    image(platformImage,self.x-game.x,self.y,self.w,self.h)



class BadMan(Creature): #Just change the name of the file to change the nemies
    def __init__(self,x,y,r,g,img,w,h,game):
        Creature.__init__(self,x,y,r,g,img,w,h,1)
        self.vx=1
        self.vy=2
        self.y1=200
        self.y2 = game.g
    
    def update(self):
        if self.y < self.y1 or self.y > self.y2-self.r: 
            self.vy*=-1
      
        self.y+=self.vy

    
class EnemyEmoji(Creature): #This enemy emoji will movie back and forth
    def __init__(self,x,y,r,g,img,w,h): #do we take away frames just for the top ones?
        Creature.__init__(self,x,y,r,g,img,w,h,1)
        self.vx=random.choice([1,-1]) 
        self.dir=self.vx
        self.x1=self.x-100 #The range at which it moves
        self.x2=self.x+100  #the enemy moves between these 2 boundaries
        
    def update(self):
        self.gravity()
        if self.x+self.r > self.x2:
            self.vx=-1 #If it reaches x2, it goes in the other direction
            self.dir=-1
        elif self.x-self.r < self.x1:
            self.vx=1
            self.dir=1
        self.x+=self.vx
        self.y+=self.vy
    
    

class Bills(Creature): #we want the bills to fall like rain
    def __init__(self,x,y,r,g,img,w,h): #do we take away frames just for the top ones?
        Creature.__init__(self,x,y,r,g,img,w,h,1)
        #self.vx=random.choice([1,-1])
        self.vx = 0 
        #self.dir=self.vx
        self.x1=self.x #The range at which it moves
        self.x2=self.x+self.w  #the enemy moves between these 2 boundaries
        
    def update(self):
        self.gravity()
        if self.x+self.r > self.x2:
            self.vx=-1 #If it reaches x2, it goes in the other direction
            self.dir=-1
        elif self.x-self.r < self.x1:
           self.vx=1
           self.dir=1
        self.x+=self.vx
        self.y+=self.vy
    

class Collectibles(Creature): #Just change the name of the file to change the nemies
    def __init__(self,x,y,r,g,img,w,h): #do we take away frames just for the top ones?
        Creature.__init__(self,x,y,r,g,img,w,h,1)
        self.vx = 0 
        self.x1=self.x #The range at which it moves
        self.x2=self.x  #the enemy moves between these 2 boundaries 
    
    def display(self):
        image(self.img,self.x-game.x,self.y,self.w,self.h)
    

  
game= Game(1250,703,585)
  
def setup():  
  size(game.w,game.h)
  #Background = loadImage(path+"/emojibackground.jpg")
  background(0)
  
def draw():
    if not game.pause:
        #background(Background)  #Refresh the background so it leaves no trail
        background(0)
        game.display()
        if game.male.win: #If you win
            finalImage=loadImage(path+'//closeScreen.png')
            image(finalImage,0,0)
            CartoonishFont = createFont(path+"/Cartoonish.ttf",40)
            textFont(CartoonishFont)
            text("Your Score: "+str(game.male.score),game.w//2-100,game.h//2+200)
            textFont(CartoonishFont)
            text("Back to Main Screen",460,586)
            # scoreFile = open(path+"\scores.txt", "a")
            # scoreFile.write(name + "," + str(game.male.score))
            # scoreFile.close()
            game.state="win"
            
        elif game.state == "gameOver" and game.stage<=3: #if its gameOver

            scoreFile = open(path+"\scores.txt", "a")
            scoreFile.write(name + "," + str(game.male.score)+"\n")
            scoreFile.close()
            game.state = "menu"
    
            
    else:
        textSize(40)
        fill(255,0,0)
        text("Paused",game.w//2,game.h//2)
    


def keyPressed():
    global name
    if game.state=="menu":
        try:
            if 97 <= ord(key) <= 97+26 or keyCode == 32:
                game.name+=key
            elif keyCode == 8:
                game.name = game.name[:len(game.name)-1]
            name = game.name
        except:
            print("Invalid character")

  
    if keyCode == 80 and game.state!="menu": #ASCII for 'p' #If we press the key P
        if game.pause:
            game.pause=False
        else:
            game.pause=True
            #game.pauseSound.play()
          
    if keyCode == LEFT:
        game.male.keyHandler[LEFT]=True
    elif keyCode == RIGHT:
        game.male.keyHandler[RIGHT]=True
    elif keyCode == UP:
        game.male.keyHandler[UP]=True
  
def keyReleased():
  if keyCode == LEFT:
    game.male.keyHandler[LEFT]=False
  elif keyCode == RIGHT:
    game.male.keyHandler[RIGHT]=False
  elif keyCode == UP:
    game.male.keyHandler[UP]=False
    
def mouseClicked():
    if game.state == "menu" and game.w//2-100 <= mouseX <= game.w//2+100 and game.h//2+70 <= mouseY <= game.h//2+110:
        game.__init__(game.w,game.h,game.g)
        game.state='play'
        game.musicSound.play()
    if game.state=="win" and 460 <= mouseX <= 870 and 520 <= mouseY <=585:
        scoreFile = open(path+"\scores.txt", "a")
        scoreFile.write(name + "," + str(game.male.score)+"\n")
        scoreFile.close()
        game.state="menu"
        game.__init__(game.w,game.h,game.g)

        
  
  