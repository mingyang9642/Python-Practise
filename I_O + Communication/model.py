# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:28:13 2019

@author: gy19my
"""
import random
import operator
import matplotlib.pyplot
import agentframework

f = open("M:/Python/I_O + Communication/in.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
f.close()

def distance_between(self, agent):
    return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,neighbourhood,agents))
    
# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):   
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)


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






