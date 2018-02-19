
import pygame
from random import randint
import time
Xa=60
Ya=120
grid = []
class NoD(object):
	
	def __init__(self, x, y,Wal):
		self.x=x
		self.y=y
		self.gCost=0
		self.hCost=0
		self.Padre=None
		self.Ve=[]
		self.Wal=Wal
	def fCost(self):
		a=int(self.gCost+self.hCost)
		return a
	def Rve():
		return self.Ve

def regreso(Ini, Fin):
	reg=[]
	current=Fin
	
	while current != Ini:
		reg.append(current)
		
		current=current.Padre

	reg.reverse()
	return reg

def Ia(Ini, Fin):
	Nini=Ini
	Nfin=Fin
	Lopen=[]
	Lclose=[]
	Lopen.append(Nini)
	while len(Lopen):
		current = Lopen[0]

		
		for nodo in Lopen:
			nodoF=nodo.fCost()
			currentF=current.fCost()
			if nodoF < currentF or nodoF == currentF and nodo.hCost < current.hCost:
				current = nodo
		Lopen.remove(current)
		Lclose.append(current)
		if current == Nfin:
			a = []
			a = regreso(Nini,Nfin)
			

			
			return a
		
		for nodo in current.Ve:
			
			if nodo in Lclose or nodo.Wal==3:
				
				continue
			
			nuevoCosto=current.gCost+dist(current,nodo)
			if nodo not in Lopen or nuevoCosto < nodo.gCost:
				nodo.gCost = nuevoCosto
				nodo.hCost = dist(nodo,Nfin)
				nodo.Padre = current
				if nodo not in Lopen:
					
					Lopen.append(nodo)



def dist(Ini, Fin):
	disX = abs(Ini.x-Fin.x)
	disY = abs(Ini.y-Fin.y)
	return disX+disY
 
class Comida:
    def __init__(self, x, y):
        self.x=int(x)
        self.y=int(y)

class Nodo:
    def __init__(self, x, y, lead):
        self.x=int(x)
        self.y=int(y)
        self.leader=lead
        self.padre=None
    def addp(self, nod):
        self.padre=nod
    def up(self):
        if(self.leader!="SI"):
            self.x=self.padre.x;
            self.y=self.padre.y;
            

class Snake:
    def __init__(self,color):
        x=randint(0,Xa-5)
        y=randint(0,Ya-5)
        cab=Nodo(x,y,"SI")
        pri=Nodo(x,y+1,"NO")
        pri.addp(cab)
        sec=Nodo(x,y+2,"NO")
        sec.addp(pri)
        
        
        self.lis=[]
        self.lis.append(cab)
        self.dir="AR"
        self.color=color
        self.lis.append(pri)
        self.lis.append(sec)
    def lsn(self):
        return self.lis
    def add(self, nod):
        self.lis.append(nod)
    def dir(self, nu):
        self.dir=nu
    def comer(self):
        mnodo=Nodo(self.lis[-1].x, self.lis[-1].y,"NO")
        mnodo.addp(self.lis[-1])
        self.lis.append(mnodo)
    def imp(self,grid):
        for Nod in self.lis:
            grid[Nod.x][Nod.y]=1
    def lim(self,grid):
        for Nod in self.lis:
            grid[Nod.x][Nod.y]=0
    def mov(self):
        
        for nod in reversed(self.lis):
            nod.up()
        if self.dir=="AR":
        	if self.lis[0].x!=0:
        		self.lis[0].x-=1
        	else:
        		self.lis[0].x=Xa-1
        if self.dir=="RG":
        	if self.lis[0].y!=Ya-1:
        		self.lis[0].y+=1
        	else:
        		self.lis[0].y=0
        if self.dir=="DW":
        	if self.lis[0].x!=Xa-1:
        		self.lis[0].x+=1
        	else:
           		self.lis[0].x=0
        if self.dir=="LF":
        	if self.lis[0].y!=0:
        		self.lis[0].y-=1
        	else:
        		self.lis[0].y=Ya-1
def Ia2(Sn,Path,dele):

	if Sn.lis[0].x==0 and Path[0].x==Xa-1 and Sn.lis[0].y == Path[0].y:
		Sn.dir="AR"
	elif Sn.lis[0].x==Xa-1 and Path[0].x==0 and Sn.lis[0].y == Path[0].y:
		Sn.dir="DW"
	elif Sn.lis[0].x == Path[0].x and Sn.lis[0].y == 0 and Path[0].y == Ya-1:
		Sn.dir="LF"
	elif Sn.lis[0].x == Path[0].x and Sn.lis[0].y == Ya-1 and Path[0].y == 0:
		Sn.dir="RG"

	elif Sn.lis[0].x > Path[0].x and Sn.lis[0].y == Path[0].y:
		Sn.dir="AR"
	elif Sn.lis[0].x < Path[0].x and Sn.lis[0].y == Path[0].y:
		Sn.dir="DW"
	elif Sn.lis[0].x == Path[0].x and Sn.lis[0].y > Path[0].y:
		Sn.dir="LF"
	elif Sn.lis[0].x == Path[0].x and Sn.lis[0].y < Path[0].y:
		Sn.dir="RG"
	if dele:
		Path.pop(0)
	pass

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
AZUL = (255, 0, 0)
ROJO = (0, 0, 255)
LARGO  = 10
ALTO = 10

MARGEN = 0



Ngrid = []
N=0
for fila in range(Xa):

    grid.append([])
    Ngrid.append([])
    for columna in range(Ya):
    	m=randint(0,9)
    	if m > 3:
    		grid[fila].append(0)
    	else:
    		grid[fila].append(3)
    	Ngrid[fila].append(NoD(fila,columna,grid[fila][columna]))



for fila in range(Xa):
	for columna in range(Ya):
		if fila==0 and columna!=0 and columna!=Ya-1:
			Ngrid[fila][columna].Ve.append(Ngrid[Xa-1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila+1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][columna+1])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][columna-1])
		elif fila==Xa-1 and columna !=0 and columna!=Ya-1:
			Ngrid[fila][columna].Ve.append(Ngrid[fila-1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[0][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][columna+1])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][columna-1])
		elif columna==0 and fila!=0 and fila!=Xa-1:
			Ngrid[fila][columna].Ve.append(Ngrid[fila-1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila+1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][columna+1])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][Ya-1])
		elif columna==Ya-1 and fila!=0 and fila!=Xa-1:
			Ngrid[fila][columna].Ve.append(Ngrid[fila-1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila+1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][0])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][columna-1])
		elif columna==0 and fila==0:
			Ngrid[fila][columna].Ve.append(Ngrid[Xa-1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila+1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][columna+1])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][Ya-1])
		elif columna==0 and fila==Xa-1:
			Ngrid[fila][columna].Ve.append(Ngrid[fila-1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[0][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][columna+1])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][Ya-1])
		elif columna==Ya-1 and fila==0:
			Ngrid[fila][columna].Ve.append(Ngrid[Xa-1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila+1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][0])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][columna-1])
		elif columna==Ya-1 and fila==Xa-1:
			Ngrid[fila][columna].Ve.append(Ngrid[fila-1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[0][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][0])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][columna-1])
		else:
			Ngrid[fila][columna].Ve.append(Ngrid[fila-1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila+1][columna])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][columna+1])
			Ngrid[fila][columna].Ve.append(Ngrid[fila][columna-1])
for a in range (0,6):
	for fila in range(Xa):
		for columna in range(Ya):
			n=0
			for nodo in Ngrid[fila][columna].Ve:
				if nodo.Wal==3:
					n+=1
			if n >= 3:
				Ngrid[fila][columna].Wal=3
				grid[fila][columna]=3




Sn=Snake("VERDE")
pygame.init()
  
DIMENSION_VENTANA = [1200, 600]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Snake")

hecho = False
 

com=Comida(Sn.lis[0].x,Sn.lis[0].y)
grid[com.x][com.y]=4

reloj = pygame.time.Clock()
start = time.clock() 
# -------- Bucle Principal del Programa-----------
path=[]
flag=True

while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            
            pos = pygame.mouse.get_pos()
            
            columna = pos[0] // (LARGO + MARGEN)
            fila = pos[1] // (ALTO + MARGEN)
            
            grid[fila][columna] = 1
            print("Click ", pos, "Coordenadas de la reticula: ", fila, columna)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and Sn.dir!="DW":
                Sn.dir="AR"
                
            if evento.key== pygame.K_RIGHT and Sn.dir!="LF":
                Sn.dir="RG"
                
            if evento.key== pygame.K_DOWN and Sn.dir!="AR":
                Sn.dir="DW"
                
            if evento.key == pygame.K_LEFT and Sn.dir!="RG":
                Sn.dir="LF"
                
    pantalla.fill(NEGRO)
 
    for fila in range(Xa):
        for columna in range(Ya):
            color = BLANCO
            if grid[fila][columna] == 1:
                color = VERDE
            if grid[fila][columna] == 2:
                color = ROJO
            if grid[fila][columna] == 3:
            	color = NEGRO
            if grid[fila][columna] == 4:
            	color = AZUL
            pygame.draw.rect(pantalla,
                             color,
                             [(MARGEN+LARGO) * columna + MARGEN,
                              (MARGEN+ALTO) * fila + MARGEN,LARGO,
                              ALTO])
     

    pa=Sn.lsn()

    try:
    	Sn.lim(grid)
    	for Nod in path:
    		grid[Nod.x][Nod.y]=0
    except:
    	pass 
    
    
    elapsed = (time.clock() - start)
    
    if elapsed > 0.000001 or flag:
    	if not flag:
    		Sn.mov()

    	flag=False
    	
    	start = time.clock()
    	if pa[0].x==com.x and pa[0].y==com.y:
        	Sn.comer()
        	while True:
        		Cx=randint(0,Xa-1)
        		Cy=randint(0,Ya-1)
        		if grid[Cx][Cy]==0:
        			com=Comida(Cx,Cy)
        			Ini=Ngrid[Sn.lis[0].x][Sn.lis[0].y]
        			Fin=Ngrid[com.x][com.y]
        			path=Ia(Ini,Fin)
        			try:

        				Ia2(Sn,path,False)

        				break
        			except:
        				pass

        

    par=Sn.lsn()
    
    
    Sn.imp(grid)
    
    


    
    Ia2(Sn,path,True)
    for Nod in path:
    	grid[Nod.x][Nod.y]=2

    grid[com.x][com.y]=4
    





    
    reloj.tick(60)
    
    
    
    
    
    
    pygame.display.flip()
    
    
     
pygame.quit()