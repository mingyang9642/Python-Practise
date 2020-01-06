# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:28:13 2019

@author: gy19my
"""
import matplotlib
import requests
import bs4
import csv
import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import tkinter
import matplotlib.backends.backend_tkagg

matplotlib.use('TkAgg')

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

f = open("M:/Python/GUI/in.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
f.close()
matplotlib.pyplot.imshow(environment)

# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment,20,agents,x,y))
    
# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):   
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours()

#def distance_between(self, agent):
#    return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5



    
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True	
	
def update(frame_number):
    print("Iteration", frame_number)
    fig.clear()   
    global carry_on
  
    for j in range(num_of_iterations):
        for i in range(num_of_agents):   
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours()
            
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        matplotlib.pyplot.imshow(environment)

def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a			
        a = a + 1
        

carry_on = True	

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

root = tkinter.Tk()
root.wm_title("Pretty")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()

"""
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()


for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        print(distance)
"""





