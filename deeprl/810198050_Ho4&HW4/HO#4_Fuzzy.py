# Machine Learning
# Fall 98
# Hands On # 4
# Kourosh Mahmoudi ID: 810198050
# Pronlem 1 part B :  Fuzzy
#-----------------------------------------------------------------------------
import gym
import numpy as np
import random
import matplotlib.pyplot as plt
#-------------------------------
class fuzzy:
    def __init__(self, env,position_label, velocity_label, actions):
        self.env = env
        self.position_label = position_label
        self.velocity_label = velocity_label
        self.alpha = 0.0035
        self.rules = []
        self.actions = actions
        self.sigma_position = 0.01
        self.sigma_velocity = 0.001
        self.epsilon = 1
        self.gamma = 0.9
        self.flag = 0
        for i in self.position_label:
            for j in self.velocity_label:
                self.rules.append((i, j))
        self.q_value = {}

    def get_q(self, position_l, velocity_l, action):
        return self.q_value.get((position_l, velocity_l, action), 0)

    def membership_return(self, x, c, s):
        a = np.exp(-((x - c)**2)/s)
        return a

    def find_rules_min_membership(self, rule, state):
        a1 = self.membership_return(state[0], rule[0], self.sigma_position)
        a2 = self.membership_return(state[1], rule[1], self.sigma_velocity)
        return min(a1, a2)

    def choose_rule_action(self, rule):
        values = [self.get_q(rule[0], rule[1], x) for x in self.actions]
        if random.random() > self.epsilon:
            chosen = self.max_index(values)
        else:
            chosen = random.randrange(len(values))

        return self.actions[chosen]

    def find_firing_rates(self, state):
        rates = []
        for i in self.rules:
            rates.append(self.find_rules_min_membership(i, state))
        return rates

    def find_all_rules_actions(self):
        chosens = []
        for i in self.rules:
            chosens.append(self.choose_rule_action(i))
        return chosens

    def find_rule_max_action_value(self, rule):
        values = [self.get_q(rule[0], rule[1], x) for x in self.actions]
        return max(values)

    def find_all_rules_max_actions_values(self):
        chosens = []
        for i in self.rules:
            chosens.append(self.find_rule_max_action_value(i))
        return chosens

    def Choose_Action(self, state):
        actions = self.find_all_rules_actions()
        rates = self.find_firing_rates(state)
        value = 0
        for i in range(len(rates)):
            value = value + rates[i] * actions[i]

        return value / sum(rates)

    def State_Value(self, state):
        rates = self.find_firing_rates(state)
        actions = self.find_all_rules_actions()
        values = []
        result = 0
        for i in range(len(self.rules)):
            values.append(self.get_q(self.rules[i][0], self.rules[i][1], actions[i]))

        for i in range(len(rates)):
            result = result + rates[i] * values[i]
        return result / sum(rates)

    def State_max_Value(self, state):
        rates = self.find_firing_rates(state)
        max_values = self.find_all_rules_max_actions_values()
        result = 0
        for i in range(len(rates)):
            result = result + rates[i] * max_values[i]
        return result / sum(rates)

    def Update_q(self, rule, action, delta, state, rule_number):
        value = self.get_q(rule[0], rule[1], action)
        rates = self.find_firing_rates(state)
        value = value + self.alpha * (rates[rule_number] / sum(rates)) * delta
        self.q_value[(rule[0], rule[1], action)] = value

    def Update_qs(self, delta, state):
        actions = self.find_all_rules_actions()
        for i in range(len(self.rules)):
            self.Update_q(self.rules[i], actions[i], delta, state, i)

        return

    def Delta(self, reward, state, next_state):
        max_next = self.State_max_Value(next_state)
        chosen = self.State_Value(state)

        return reward + self.gamma * max_next - chosen

    def max_index(self, x):
        m = max(x)
        indexes = [i for i, j in enumerate(x) if j == m]
        return random.choice(indexes)

    def Update_Algorithm(self):
        state = self.env.reset()
        chosen_action = self.Choose_Action(state)
        self.env.render()
        c = 0
        while state[0] < 0.5:
            c = c + 1
            if (c % 1000) == 0:
                print(c)
            Next_State, reward, done, info = self.env.step(np.array([chosen_action]))
            self.env.render()
            if Next_State[0] > 0.49:
                reward = 100
            delta = self.Delta(reward, state, Next_State)
            self.Update_qs(delta, state)

            next_action = self.Choose_Action(Next_State)
            state = Next_State
            chosen_action = next_action
            if self.flag == 1:
                self.epsilon = self.epsilon* 0.9999
                if self.epsilon < 0.1:
                    self.epsilon = 0.1

        print("it converged in {} steps".format(c))
        self.flag = 1

#-------------------------------
# Learning episodes

actions = [-1, 0 , 1]
position_label = [-1, -0.5, 0 , 0.3]
velocity_label = [-0.05, -0.02, 0, 0.02, 0.05]
env = gym.make("MountainCarContinuous-v0")

Episode = fuzzy(env,position_label,velocity_label, actions)
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