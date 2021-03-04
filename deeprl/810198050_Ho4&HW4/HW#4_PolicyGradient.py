# Machine Learning
# Fall 98
# Hands On # 4
# Kourosh Mahmoudi ID: 810198050
# Pronlem 1 part C :  Policy Gradient Method using Actor-Critic with Eligibility Trace Algorithm
#                    /RBF_Linear state coding/ /RBF Policy Coding/
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
    def __init__(self, env,actions,action_means,d1,d2,d):
        self.env = env
        self.velocityLimit = np.array([self.env.observation_space.low[1], self.env.observation_space.high[1]])
        self.positionLimit = np.array([self.env.observation_space.low[0], self.env.observation_space.high[0]])
        self.dim = np.shape(env.observation_space.low)[0]
        self.d1 = d1
        self.d2 = d2
        self.d_A = d
        self.alpha_theta = 0.005
        self.alpha_W = 0.005
        self.actions = actions
        self.action_means = action_means
        self.Lambda_theta = 0.5
        self.Lambda_W = 0.5
        self.gamma = 0.98
        self.alphaDecay = 0.999
        self.theta = np.zeros((self.d1*self.d2*self.d_A,1))
        self.W = np.zeros((self.d1*self.d2+1,1))        
        self.RewardSum = []
    # multivariate RBF+Linear Function
    def RBF_Linear_State(self,s):
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
                sigmaV = np.random.uniform(low=1,high=1)
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
    
    def RBF_State_Action(self,s,a):
        x = np.zeros([self.d1*self.d2 * self.d_A,1])
        mean = list()
        cov = list()
        mean_p = np.linspace(self.positionLimit[0] , self.positionLimit[1], self.d1)
        mean_v = np.linspace(self.velocityLimit[0] , self.velocityLimit[1], self.d2)
        mean_A = self.action_means
        for i in mean_p:
            for j in mean_v:
                for k in mean_A:
                    mean.append((i,j,k))
        for i in range(self.d1*self.d2 * self.d_A):
            while True:
                sigmaP = np.random.uniform(low=1,high=1)
                sigmaV = np.random.uniform(low=1,high=1)
                sigmaA = np.random.uniform(low=2,high=2)
#                row = np.random.uniform(low=0,high=0)
                A = np.array([[sigmaP**2,0,0],[0,sigmaV**2,0],[0,0,sigmaA**2]])
                if np.linalg.matrix_rank(A)==self.dim+1:
                    if np.all(np.linalg.eigvals(A) > 0):
                        break
            cov.append(A)
            y = np.append(s,a)
            x[i] = np.sqrt(((2*math.pi)**(self.dim+1))*(np.linalg.det(cov[i])))*\
                           scipy.stats.multivariate_normal.pdf(y,mean[i],cov[i])
        return x

    def State_Action_PreferenceGenerator(self, State, Action):
        x = self.RBF_State_Action(State,Action)
        Preference = self.theta.T.dot(x)
        return Preference
    
    def State_valueGenerator(self, State):
        x = self.RBF_Linear_State(State)
        V = self.W.T.dot(x)
        return V
    
    def State_Action_Preference(self, State):
        vector = []
        for i in self.actions:
            vector.append(np.exp(self.State_Action_PreferenceGenerator(State, i)))                        
        return vector    
    
    def Policy(self, State):
        preference = self.State_Action_Preference(State)
        summation = sum(preference)
        p = [float(x) / float(summation) for x in preference]
        return p
    
    def Choose_Action(self,State):
        p = self.Policy(State)
        a = np.random.choice(self.actions,p=p)
        return a

    def gradient_of_NaturalLogarithm_of_policy(self, State, Action):
        x_s_a = self.RBF_State_Action(State, Action)
        summation = 0
        for i in self.actions:
            summation += self.Policy(State)[i] * self.RBF_State_Action(State, i)
        G = x_s_a - summation 
        return G    

    def Update_Algorithm(self):
        state = self.env.reset()
#        self.env.render()
        Z_theta = np.zeros([self.d1*self.d2*self.d_A,1])
        Z_W = np.zeros([self.d1*self.d2 +1,1])
        I = 1
        t = 0
        done=False
        while  state[0] < 0.5:
            if (t%100) == 0:
                print(t)
            if (t%1000) == 0:
                self.alpha_W = max(0.0, self.alpha_W * self.alphaDecay)
                self.alpha_theta = max(0.0, self.alpha_theta * self.alphaDecay)
            chosen_action = self.Choose_Action(state)
            next_state, reward, done, info = self.env.step(chosen_action)
#            self.env.render()
            if done:
                self.RewardSum.append(-t)
            if next_state[0] > 0.49:
                reward = 100
            State_Value = self.State_valueGenerator(state)
            Next_State_Value = self.State_valueGenerator(next_state)
            delta = reward + self.gamma * Next_State_Value - State_Value
            Z_W = self.gamma * self.Lambda_W * Z_W + self.RBF_Linear_State(state)
            Z_theta = self.gamma * self.Lambda_theta * Z_theta + I * \
                      self.gradient_of_NaturalLogarithm_of_policy(state,chosen_action)
            self.W += self.alpha_W * delta * Z_W
            self.theta += self.alpha_theta * delta * Z_theta
            I *= self.gamma
            state = next_state
            t += 1
        self.alpha_W = max(0.0, self.alpha_W * self.alphaDecay)
        self.alpha_theta = max(0.0, self.alpha_theta * self.alphaDecay)
#-------------------------------
# Learning episodes
actions = [0,1,2]
action_means = [.5,1.5]
env = gym.make("MountainCar-v0")
#env = Monitor(env,'D:\g',video_callable =lambda episode_id: episode_id%50==0, force=True, resume=True)
d1 = 5
d2 = 3
d = 2
Episode = RL(env, actions,action_means, d1, d2, d)
numEpisodes = 30
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