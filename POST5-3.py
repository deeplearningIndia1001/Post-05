#I.G : @deeplearningindia
############################# BAR PLOT ################################
from matplotlib import pyplot as plt
from matplotlib import style

style.use('fivethirtyeight') #Also Try using 'ggplot'

x = [5,8,10,2,1] #DataPoints for Class 01
y = [12,16,6,7,3]

x2 = [6,9,11] #DataPoints for Class 02
y2 = [6,15,7]

plt.bar(x,y,linewidth=1 , label ="Class1")
plt.bar(x2,y2,linewidth=1 , label ="Class2")

plt.title('@deeplearningindia')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.show()
