# Machine Learning
# Fall 98
# Third Assignment
# Kourosh Mahmoudi ID: 810198050
# Pronlem 1 part A,B
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
N = 5               # Maximum number of steps (n-step SARSA)
M = 1               # number of repetitions for each n
p1 = [0,.1,.05,.05,.01,.01]
p2 = [0,.55,.7,.8,.9,.9]
OptimalPolicy = np.load('OP.npy')
#------------------------------
# Variable Initializing and Functions

Actions = range(Num_Actions)                      # Possible Actions
Regret = np.zeros([N+1,M,episodes])               # Rergret
Regret_Mean = np.zeros([N+1,episodes])            # Mean Rergret

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
for n in range(1,N+1):
    #print(n)
    for m in range(M):
        #print(m)
        Q_Values = np.random.random([Num_Sates , Num_Actions]) # Action-Values
        alphas = np.ones([Num_Sates,Num_Actions])      # Learning Rate  
        eps = 1   
        AccumulatedRegret = 0                 
        for e in range(episodes):
            #print(e)
            Terminal_State = False
            env.reset()
            State_Seq = [0]
            eps = np.exp(-e/(10*n))           # Epsilon (Epsilon Greedy Soft Policy)
            Action = Soft_Policy(State_Seq[0],eps)
            Reward_Seq = [0]
            Action_Seq = []
            Action_Seq.append(Action)
            T = float('inf')
            t = 0
            while True :
                if (t < T) :
                    next_State , reward, Terminal_State , info = env.step(Action)
                    State_Seq.append(next_State)
                    Reward_Seq.append(reward)                    
                    if Terminal_State == True :
                        T = t + 1
                    else :
                        Action = Soft_Policy (next_State,eps)
                        Action_Seq.append(Action)

                Taw = t - n + 1
                if (Taw >= 0) :
                    G = np.sum([gamma**(j-Taw-1) * Reward_Seq[j] for j in range(Taw+1 , min(Taw + n, T)+1)])
                    if (Taw + n < T) :
                        G += (gamma**n) *  Q_Values[State_Seq[Taw+n],Action_Seq[Taw+n]]
                    Q_Values[State_Seq[Taw],Action_Seq[Taw]] += \
                     alphas[State_Seq[Taw],Action_Seq[Taw]] * \
                     (G-Q_Values[State_Seq[Taw],Action_Seq[Taw]])
                    alphas[State_Seq[Taw],Action_Seq[Taw]] = p1[n]*((e+1)**(-p2[n]))
                if (Taw == T - 1) :                                    
                    break
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

Labels = ['n=1','n=2','n=3','n=4','n=5','n=6','n=7','n=8','n=9','n=10']
fig, ax = plt.subplots()
for n in range(1,N+1):
    ax.plot(Regret_Mean[n,:],label=Labels[n-1])
ax.set_xlabel('trials')
ax.set_ylabel('Regret')
ax.set_title(r'Average Regret (100 Repeats)')
ax.grid(axis='y')
plt.legend(loc=4, shadow=True, fontsize='small')
plt.show()