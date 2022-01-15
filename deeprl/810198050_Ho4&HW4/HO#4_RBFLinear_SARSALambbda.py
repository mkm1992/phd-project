# Machine Learning
# Fall 98
# Hands On # 4
# Kourosh Mahmoudi ID: 810198050
# Pronlem 1 part A : RBF_Linear state coding _ SARSA(Lambda)
#-------------------------------
import gym
from gym.wrappers import Monitor
import numpy as np
import scipy.stats 
import math
import matplotlib.pyplot as plt
#-------------------------------
# Reinforcement Learning

class RL:
    def __init__(self, env,actions,d1,d2):
        self.env = env
        self.velocityLimit = np.array([self.env.observation_space.low[1], self.env.observation_space.high[1]])
        self.positionLimit = np.array([self.env.observation_space.low[0], self.env.observation_space.high[0]])
        self.dim = np.shape(env.observation_space.low)[0]
        self.d1 = d1
        self.d2 = d2
        self.alpha = 0.01
        self.actions = actions
        self.eps = 0.1
        self.Lambda = 0.8
        self.gamma = 0.98
        self.alphaDecay = 0.999
        self.epsDecay = 0.995
        self.W = np.zeros((len(actions),self.d1*self.d2 +1))
        self.RewardSum = []
    # multivariate RBF+Linear Function
    def RBF_Linear(self,s):
        x = np.zeros([self.d1*self.d2 +1,1])
        mean = list()
        cov = list()
        mean_p = np.linspace(self.positionLimit[0] , self.positionLimit[1], self.d1)
        mean_v = np.linspace(self.velocityLimit[0] , self.velocityLimit[1], self.d2)
        for i in mean_p:
            for j in mean_v:
                mean.append((i,j))
        for i in range(self.d1*self.d2):
            while True:
                sigmaP = np.random.uniform(low=1,high=1)
                sigmaV = np.random.uniform(low=.1,high=.1)
                row = np.random.uniform(low=0,high=0)
                A = np.array([[sigmaP**2,row*sigmaP*sigmaV],[row*sigmaP*sigmaV,sigmaV**2]])
                if np.linalg.matrix_rank(A)==self.dim:
                    if np.all(np.linalg.eigvals(A) > 0):
                        break
            cov.append(A)
            x[i] = np.sqrt(((2*math.pi)**self.dim)*(np.linalg.det(cov[i])))*\
                           scipy.stats.multivariate_normal.pdf(s,mean[i],cov[i])
        x[-1] = 0.5*s[0] + 10 * s[1]
        return x
   
    def State_Action_ValueGenerator(self, State, Action):
        x = self.RBF_Linear(State)
        w = self.W[self.actions.index(Action)]
        Q_value = w.T.dot(x)
        return Q_value
    
    def State_Action_Value(self, State):
        Q_Values = []
        for i in self.actions:
            Q_Values.append(self.State_Action_ValueGenerator(State, i))
        return Q_Values
    
    # Epsilon Greedy Soft Policy
    def Soft_Policy (self,State,epsilon):
        Num_Actions = len(self.actions)
        p = (epsilon/Num_Actions)*np.ones((1,Num_Actions))
        Q_Values = self.State_Action_Value(State)
        I = np.max(Q_Values)
        l = [i for i,x in enumerate(Q_Values) if x==I]
        J = np.random.choice(l)
        p[0,J] = 1 - epsilon + epsilon/Num_Actions 
        a = np.random.choice(self.actions,p=p.ravel())
        return a

    def Update_Algorithm(self):
        state = self.env.reset()
        self.env.render()
        epsilon = self.eps
        chosen_action = self.Soft_Policy(state,epsilon)
        x = self.RBF_Linear(state)
        Z = np.zeros([self.d1*self.d2 +1,1])
        Q_old = 0
        alphat = self.alpha
        t = 0
        done=False
        while done==False:
#            if (t%100) == 0:
#                print(t)
#            if (t%200) == 0:
#                self.eps = max(0.0, self.eps * self.epsDecay)
#                self.alpha = max(0.0, self.alpha * self.alphaDecay)
            next_state, reward, done, info = self.env.step(chosen_action)
            self.env.render()
            if done:
                self.RewardSum.append(-t)
            next_action = self.Soft_Policy(next_state,self.eps)
            x_prime = self.RBF_Linear(next_state)
            Q = self.W[self.actions.index(chosen_action)].T.dot(x)
            Q_prime = self.W[self.actions.index(next_action)].T.dot(x_prime)
            delta = reward + self.gamma * Q_prime - Q
            Z = self.gamma * self.Lambda * Z + (1-alphat * self.gamma \
                                                * self.Lambda * Z.T.dot(x)) * x
            w = self.W[self.actions.index(chosen_action)]
            w = w.reshape(self.d1*self.d2 +1, 1)  
            w = w + self.alpha * (delta + Q - Q_old) * Z - self.alpha * \
                                                       (Q - Q_old) * x
            self.W[self.actions.index(chosen_action)] = w.reshape(self.d1*self.d2 +1)
            Q_old = Q_prime
            x = x_prime
            chosen_action = next_action
            state = next_state
            t += 1
        self.eps = max(0.0, self.eps * self.epsDecay)
        self.alpha = max(0.0, self.alpha * self.alphaDecay)
#-------------------------------
# Learning episodes
actions = [0,1,2]
env = gym.make("MountainCar-v0")
env = Monitor(env,'D:\g',video_callable =lambda episode_id: episode_id%50==0, force=True, resume=True)
d1 = 5
d2 = 3
Episode = RL(env, actions, d1, d2)
numEpisodes = 1000
for i in range(numEpisodes):
    print(i)
    Episode.Update_Algorithm()
env.close()
# plot       
fig, ax = plt.subplots(figsize = (18, 8))
plt.plot(Episode.RewardSum[:],'.')
plt.yticks(range(-110, -210, -10))
plt.ylabel("reward")
plt.xlabel("episode_number")
plt.grid()
plt.show()

avgReward = []
for i in range(10, numEpisodes):
    avgReward.append(np.mean(Episode.RewardSum[i - 10:i]))
fig, ax = plt.subplots(figsize = (18, 8))
plt.plot(avgReward)
plt.yticks(range(-110, -210, -10))
plt.ylabel("Avg reward for last 10 episodes")
plt.xlabel("episode_number")
plt.grid()
plt.show()