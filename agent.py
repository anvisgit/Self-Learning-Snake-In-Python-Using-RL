import torch 
import numpy as np
import random 
from game import SnakeGameAI, Direction, Point
from collections import deque

MAX_MEMORY=100_000
BATCH_SIZE=1000
LR=0.001

class Agent:
    def __init__(self):
        slef.n_games=0
        self.epsilon=0 #randomness
        self.gamma=0 #disc rate
        self.memory= deque(maxlen=MAX_MEMORY)#popleft

    def get_state(self,game):
        pass
    def remember(self, state, action, reward,next_state, done ):
        pass
    def train_long_memory(self):
        pass
    def train_short_memory(self, state, action, reward, next_state, done):
        pass
    def get_action(self,state):
        pass
def train():
    plot_scores=[]
    plot_mean_scores=[]
    totalscore=0
    rec=0
    agent=Agent()
    game=SnakeGameAI()
    while True:
        state_old=agent.get_state(game)
        final_move=agent.get_action(state_old)
        reward, done, score=game.play_step(final_move)
        state_new=agent.get_state(game)

        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            game.reset()
            agent.n_games+=1
            agent.train_long_memory()

            if score>record:
                record=score
            print('Game: ', agent.n_games, 'Score: ', score, 'Record: ', record)





if __name__=='__main__':
    train()

