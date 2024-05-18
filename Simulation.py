from numpy import random

class Agent:
    def __init__(self, world, kind):
        self.world= world
        self.kind= kind
        self.location= None

    def move(self):
        vacancies= self.world.find_vacant()
        if vacancies:
            new_location= random.choice(vacancies)
            self.world.grid[self.location]= None
            self.world.grid[new_location]= self.kind
            self.location= new_location

class World:
    def __init__(self, size=5, num_agents=5):
        self.size= size
        self.grid= [None]*(size*size)
        self.agents= [Agent(self, 'X' if i % 2 == 0 else 'O') for i in range(num_agents)]
        self.init_world()

    def find_vacant(self):
        return [i for i, spot in enumerate(self.grid) if spot is None]

    def init_world(self):
        for agent in self.agents:
            loc= random.choice(self.find_vacant())
            self.grid[loc]= agent.kind
            agent.location= loc

    def run(self):
        for _ in range(5): 
            for agent in self.agents:
                agent.move()

if __name__ == '__main__':
    world = World()
    world.run()
    print("job done, grid's here:")
    print(world.grid)
