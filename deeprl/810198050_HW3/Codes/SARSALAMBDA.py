# Machine Learning
# Fall 98
# Third Assignment
# Kourosh Mahmoudi ID: 810198050
# Pronlem 1 part C
#-------------------------------
import matplotlib.pyplot as plt
import FrozenLake
import numpy as np
#-------------------------------
# Initializing Parameter
env = FrozenLake.FrozenLakeEnv()
gamma = .9            # Discount Factor
Num_Sates = env.nS    # number of states
Num_Actions = env.nA  # number of actions
episodes = 600
M = 1                # number of repetitions for each n
Lambda = [0,.3,1]
p1 = [.5,.5,.01]
p2 = [.7,.8,.9]
N = len(Lambda)        # Lambdas (SARSA(lambda))
OptimalPolicy = np.load('OP.npy')
#------------------------------
# Variable Initializing and Functions

Actions = range(Num_Actions)                      # Possible Actions
Regret = np.zeros([N,M,episodes])               # Rergret
Regret_Mean = np.zeros([N,episodes])            # Mean Rergret

# Epsilon Greedy Soft Policy
def Soft_Policy (State,eps) :
    p = (eps/Num_Actions)*np.ones((1,Num_Actions)) 
    I = np.max(Q_Values[State,:])
    l = [i for i,x in enumerate(Q_Values[State,:]) if x==I]
    J = np.random.choice(l)
    p[0,J] = 1 - eps + eps/Num_Actions 
    a = np.random.choice(Actions,p=p.ravel())
    return a

#-----------------------------
# Main
for n in range(len(Lambda)):
    #print(n)
    for m in range(M):
        #print(m)
        Q_Values = np.zeros([Num_Sates , Num_Actions])  # Action-Values
        alphas = np.ones([Num_Sates,Num_Actions])       # Learning Rate
        AccumulatedRegret = 0
        eps = 1                          # Epsilon (Epsilon Greedy Soft Policy)
        for e in range(episodes):
            #print(e)
            Eligibility = np.zeros([Num_Sates , Num_Actions])  # Eligibility
            Terminal_State = False
            env.reset()
            State_Seq = [0]
            eps = np.exp(-e)       
            Action = Soft_Policy(State_Seq[0],eps)
            Reward_Seq = [0]
            Action_Seq = []
            Action_Seq.append(Action)
            t = 0
            while Terminal_State == False:
                next_State , reward, Terminal_State , info = env.step(Action)
                State_Seq.append(next_State)
                Reward_Seq.append(reward)                    
                Action = Soft_Policy (next_State,eps)
                Action_Seq.append(Action)
                G = reward + gamma * Q_Values[State_Seq[t+1],Action_Seq[t+1]]-Q_Values[State_Seq[t],Action_Seq[t]]
                Eligibility[State_Seq[t],Action_Seq[t]] += 1
                for s in range(Num_Sates):
                    for a in range(Num_Actions):
                        Q_Values[s,a] += alphas[s,a] * G * Eligibility[s,a]
                        Eligibility[s,a] *= gamma*Lambda[n] 
                alphas[State_Seq[t],Action_Seq[t]] = p1[n]*(e+1)**(-p2[n])
                t += 1
            episodeRegret = 0 
            for i in range(len(State_Seq)-1):
                C = env.P[State_Seq[i]][Action_Seq[i]] # Chosen Action
                D = env.P[State_Seq[i]][OptimalPolicy[State_Seq[i]]] # Best Action
                C_Value = 0 
                D_Value = 0
                for j in range(len(C)):
                    C_Value +=  C[j][0]*C[j][2]
                    D_Value +=  D[j][0]*D[j][2]
                episodeRegret += D_Value - C_Value
            AccumulatedRegret += episodeRegret
            Regret[n,m,e] = AccumulatedRegret
        
    Regret_Mean[n,:] = np.mean(Regret[n,:,:],axis=0)         

Labels = ['lambda=0','lambda=0.3','lambda=1']
fig, ax = plt.subplots()
for n in range(0,N):
    ax.plot(Regret_Mean[n,:],label=Labels[n])
ax.set_xlabel('trials')
ax.set_ylabel('Regret')
ax.set_title(r'Average Regret (100 Repeats)')
ax.grid(axis='y')
plt.legend(loc=4, shadow=True, fontsize='small')
plt.show()