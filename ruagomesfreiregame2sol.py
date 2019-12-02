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
                self.alpha = 0.1
                self.gamma = 0.9

                self.explored = [[0 for i in range(nS)] for i in range(nS)]
                self.Q = [[-math.inf for i in range(nA)] for i in range(nS)] 
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
                min_freq = math.inf
                min_i = math.inf
                explored = math.inf
                for i, aux in enumerate(aa):
                        if self.explored[st][aux] < min_freq:
                                min_freq = self.explored[st][aux]
                                min_i = i
                                explored = aux

                a = min_i

                self.explored[st][explored] += 1

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
                a = 0
                for i, a_aux in enumerate(aa):
                        if self.Q[st][i] > self.Q[st][a]:
                                a = i
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
                bestB = max(self.Q[nst])
                thisQ = self.Q[st][a]
                self.Q[st][a] = thisQ + self.alpha * (r + self.gamma * bestB - thisQ) 
                return
