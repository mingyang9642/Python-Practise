import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework


#random.seed(2)
random.seed(2)



f = open("M:/Python/Fourth Step - Animation/in.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
f.close()
#print(environment)

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

for i in range(num_of_agents):
        agents.append(agentframework.Agent(environment, agents, neighbourhood))

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

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_function)

matplotlib.pyplot.show()















