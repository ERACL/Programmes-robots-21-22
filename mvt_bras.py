from cmath import *
from math import *
import matplotlib.pyplot as plt
import numpy as np 


l1 = 194
l2 = 147
lp = 40

# Angle de décalage par rapport au 0
theta10, theta20 = -30*pi/180,-140*pi/180


def angle_moteur(x,y):
    A = x
    B = y
    D = (-(l2+lp)**2+(x**2+y**2+l1**2))/(2*l1)
    r = sqrt(A**2+B**2)

    if abs(D)>r:
        return 'Pas de solution possible pour theta 1'

    if  x<0:
        alpha = atan(B/A)+pi
        theta1 = -acos(D/r)+alpha
    else:
        alpha = atan(B/A)
        theta1 = acos(D/r)+alpha
  
    
    theta2_sin = asin((y-l1*sin(theta1))/(l2+lp))-theta1
    theta2_cos = acos((x-l1*cos(theta1))/(l2+lp))-theta1
    
    # On regarde les erreurs suivant x et y selon l'angle obtenu avec acos ou asin
    err_cos_x = abs(x-l1*cos(theta1)-(l2+lp)*cos(theta1+theta2_cos))
    err_cos_y = abs(y-l1*sin(theta1)-(l2+lp)*sin(theta1+theta2_cos))
    err_sin_x = abs(x-l1*cos(theta1)-(l2+lp)*cos(theta1+theta2_sin))
    err_sin_y = abs(y-l1*sin(theta1)-(l2+lp)*sin(theta1+theta2_sin))
    
    if sqrt(err_cos_x**2+err_cos_y**2)<sqrt(err_sin_x**2+err_sin_y**2):
        theta2 = theta2_cos
        err = sqrt(err_cos_x**2+err_cos_y**2) # Erreur de position du point
    else:
        theta2 = theta2_sin
        err = sqrt(err_sin_x**2+err_sin_y**2) # Erreur de position du point
        
    #print(theta1,theta2,'x='+str(l1*cos(theta1)+(l2+lp)*cos(theta1+theta2)),'y='+str(l1*sin(theta1)+(l2+lp)*sin(theta1+theta2)))

    if (theta1>pi+theta10 or theta1<0+theta10)or(theta2<0+theta20 or theta2>pi+theta20):
        if x<0:
            alpha = atan(B/A)+pi
            theta1 = acos(D/r)+alpha
      
        
        theta2_sin = asin((y-l1*sin(theta1))/(l2+lp))-theta1
        theta2_cos = acos((x-l1*cos(theta1))/(l2+lp))-theta1
        
        # On regarde les erreurs suivant x et y selon l'angle obtenu avec acos ou asin
        err_cos_x = abs(x-l1*cos(theta1)-(l2+lp)*cos(theta1+theta2_cos))
        err_cos_y = abs(y-l1*sin(theta1)-(l2+lp)*sin(theta1+theta2_cos))
        err_sin_x = abs(x-l1*cos(theta1)-(l2+lp)*cos(theta1+theta2_sin))
        err_sin_y = abs(y-l1*sin(theta1)-(l2+lp)*sin(theta1+theta2_sin))
        if sqrt(err_cos_x**2+err_cos_y**2)<sqrt(err_sin_x**2+err_sin_y**2):
            theta2 = theta2_cos
            err = sqrt(err_cos_x**2+err_cos_y**2) # Erreur de position du point
        else:
            theta2 = theta2_sin
            err = sqrt(err_sin_x**2+err_sin_y**2) # Erreur de position du point
            
        if (theta1>pi+theta10 or theta1<0+theta10)or(theta2<0+theta20 or theta2>pi+theta20):
            return(0,0,err)  

    return [theta1*180/pi,theta2*180/pi,err]# [(theta1-theta10)*180/pi,(theta2-theta20)*180/pi,err]


# On dessine en noir la droite limite du domaine de theta1
plt.plot([0, 3*l1*cos(theta10)],[0, 3*l1*sin(theta10)],'k-')
plt.plot([0, 3*l1*cos(theta10+pi)],[0, 3*l1*sin(theta10+pi)],'k-')

L1 = [[250,230],[200,0],[250,0],[280,0],[100,200],[100,150],[100,250],[70,330],[50,330]]
L2 = [[200,-80],[180,-220],[200,-200],[250,-100]]
L3 = [[-352,65],[-50,250],[-100,300],[-320,200],[-300,220],[-330,80],[-350,100]]
M_x = []
M_y = []

for a in L1+L2+L3:
    theta1, theta2, err = angle_moteur(a[0],a[1])
    plt.plot([0,l1*cos(theta1*pi/180),l1*cos(theta1*pi/180)+(l2+lp)*cos((theta1+theta2)*pi/180)],[0,l1*sin(theta1*pi/180),l1*sin(theta1*pi/180)+(l2+lp)*sin((theta1+theta2)*pi/180)])
    M_x += [0,l1*cos(theta1*pi/180),l1*cos(theta1*pi/180)+(l2+lp)*cos((theta1+theta2)*pi/180)]
    M_y += [0,l1*sin(theta1*pi/180),l1*sin(theta1*pi/180)+(l2+lp)*sin((theta1+theta2)*pi/180)]
    
    
    print(theta1,theta2,"\u001B[1;36m"+'x='+str(l1*cos(theta1*pi/180)+(l2+lp)*cos((theta1+theta2)*pi/180))+u"\u001b[0m","\u001B[1;34m"+'y='+str(l1*sin(theta1*pi/180)+(l2+lp)*sin((theta1+theta2)*pi/180))+u"\u001b[0m")
    print("\u001B[1;31m"+str(err)+u"\u001b[0m")

# Bras au repos
plt.plot([0,l1*cos(2*pi/5-theta10),l1*cos(2*pi/5-theta10)+(l2+lp)*cos((2*pi/5-theta10+0+theta20))],[0,l1*sin(2*pi/5-theta10),l1*sin(2*pi/5-theta10)+(l2+lp)*sin(2*pi/5-theta10+0+theta20)])

plt.grid(True)
#plt.show()
    

for t1 in np.linspace(theta10, pi+theta10,100):
    for t2 in np.linspace(theta20, pi+theta20,100):
        plt.plot([l1*cos(t1)+(l2+lp)*cos(t1+t2)],[l1*sin(t1)+(l2+lp)*sin(t1+t2)],'rp',ms = 0.5)

plt.xlim(-(l1+l2+lp+10),(l1+l2+lp+10))
plt.xlabel('x (mm)')
plt.ylim(-(l1+l2+lp-50),(l1+l2+lp+10))
plt.ylabel('y (mm)')
plt.title('Domaine atteignable Bras LILO')
plt.show()
    

# D = (-(l2+lp)**2+(150**2+(-100)**2+l1**2))/(2*l1)
# r = sqrt(150**2+(-100)**2)
# theta1 = acos(D/r)+atan(100/150)
# tsin = asin((100-l1*sin(theta1))/(l2+lp))-theta1
# tcos = acos((150-l1*cos(theta1))/(l2+lp))-theta1

# print(l1*cos(theta1)+(l2+lp)*cos(theta1+tcos))
# print(l1*sin(theta1)+(l2+lp)*sin(theta1+tsin))

# print(tcos)
# print(tsin)