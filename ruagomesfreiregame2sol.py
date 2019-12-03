import random
import math

# LearningAgent to implement
# no knowledge about the environment can be used
# the code should work even with another environment
class LearningAgent:

        # init
        # nS maximum number of states
        # nA maximum number of action per state
        def __init__(self,nS,nA):

                # define this function
                self.nS = nS
                self.nA = nA
                self.alpha = 0.75
                self.gamma = 0.5

                # counter for each time a stated has been explored
                self.explored = [[0 for i in range(nA)] for i in range(nS)]

                # number of neighbours each state has
                self.neighbours = [nA for i in range(nS)]

                # matrix with the Q values
                self.Q = [[0 for i in range(nA)] for i in range(nS)] 
                # define this function
              
        
        # Select one action, used when learning  
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
                # define this function
                #print("select one action to learn better")

                n_neighbours = len(aa)
                a = self.explored[st].index(min(self.explored[st][:n_neighbours]))

                self.explored[st][a] += 1
                self.neighbours[st] = n_neighbours

                # define this function
                return a

        # Select one action, used when evaluating
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):
                # define this function
                a = self.Q[st].index(max(self.Q[st][:self.neighbours[st]]))
                # print("select one action to see if I learned")
                return a


        # this function is called after every action
        # st - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,st,nst,a,r):
                # define this function
                #print("learn something from this data")
                bestB = max(self.Q[nst][:self.neighbours[nst]]) 
                thisQ = self.Q[st][a]
                self.Q[st][a] = thisQ + self.alpha * (r + self.gamma * bestB - thisQ) 
                return
