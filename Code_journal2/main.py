import numpy as np
# write a gym template environment
class Environment:
    def __init__(self):
        self.state = None
        self.action = None
        self.reward = None
        self.done = None
        self.info = None

    def reset(self):
        raise NotImplementedError

    def step(self, action):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError
     
# write a gym template agent
class Agent:
    def __init__(self, env, gamma=0.99):
        self.env = env
        self.gamma = gamma
        self.Q = {}
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.01
        self.learning_rate_decay = 0.99
        self.alpha = 0.1
        self.alpha_decay = 0.99
        self.batch_size = 32
        self.memory = []
        self.memory_size = 10000
        self.memory_counter = 0
        self.update_counter = 0
        self.update_frequency = 5
        self.loss = 0
        self.loss_list = []
        self.loss_list_size = 100
        self.loss_list_counter = 0
        self.loss_list_update_frequency = 10
        self.loss_list_update_counter = 0
        self.loss_list_update_counter_max = self.loss_list_size // self.loss_list_update_frequency
        self.loss_list_update_counter_min = self.loss_list_update_counter_max // 2
        self.loss_list_update_counter_range = self.loss_list_update_counter_max - self.loss_list_update_counter_min
        self.loss_list_update_counter_threshold = self.loss_list_update_counter_min + self.loss_list_update_counter_range // 2
        self.loss_list_update_counter_threshold_max = self.loss_list_update_counter_threshold + self.loss_list_update_counter_range // 2
        self.loss_list_update_counter_threshold_min = self.loss_list_update_counter_threshold - self.loss_list_update_counter_range // 2
        self.loss_list_update_counter_threshold_range = self.loss_list_update_counter_threshold_max - self.loss_list_update_counter_threshold_min
        self.loss_list_update_counter_threshold_threshold = self.loss_list_update_counter_threshold_min + self.loss_list_update_counter_threshold_range // 2

    def choose_action(self, state):
        if np.random.rand() <= self.epsilon:
            return np.random.randint(0, self.env.action_space.n)
        else:
            return np.argmax(self.Q[state])
    
    def learn(self):
        if self.memory_counter < self.batch_size:
            return
        batch = np.random.choice(self.memory, self.batch_size)
        for state, action, reward, next_state, done in batch:
            if done:
                self.Q[state][action] = reward
            else:
                self.Q[state][action] = reward + self.gamma * np.max(self.Q[next_state])
        self.loss = 0
        for state, action, reward, next_state, done in batch:
            self.loss += (self.Q[state][action] - self.Q[next_state][action]) ** 2
        self.loss /= self.batch_size
        self.loss_list.append(self.loss)
        self.loss_list_counter += 1
        if self.loss_list_counter >= self.loss_list_size:
            self.loss_list_counter = 0
        if self.loss_list_counter == self.loss_list_update_counter_threshold:
            self.loss_list_update_counter += 1
            if self.loss_list_update_counter >= self.loss_list_update_counter_max:
                self.loss_list_update_counter = 0
            self.loss_list_update_counter_threshold = self.loss_list_update_counter_min + self.loss_list_update_counter_range * self.loss_list_update_counter // self.loss_list_update_counter_max
            self.loss_list_update_counter_threshold_max = self.loss_list_update_counter_threshold + self.loss_list_update_counter_range // 2
            self.loss_list_update_counter_threshold_min = self.loss_list_update_counter_threshold - self.loss_list_update_counter_range // 2

    
# write a DDPG algorithm
class DDPG:
    def __init__(self, env, agent, max_episodes=1000, max_steps=1000, render=False):
        self.env = env
        self.agent = agent
        self.max_episodes = max_episodes
        self.max_steps = max_steps
        self.render = render
        self.episode_rewards = []
        self.episode_lengths = []
        self.episode_losses = []
        self.episode_losses_list = []
        self.episode_losses_list_size = 100
        self.episode_losses_list_counter = 0
        self.episode_losses_list_update_frequency = 10
        self.episode_losses_list_update_counter = 0
        self.episode_losses_list_update_counter_max = self.episode_losses_list_size // self.episode_losses_list_update_frequency
        self.episode_losses_list_update_counter_min = self.episode_losses_list_update_counter_max // 2
        self.episode_losses_list_update_counter_range = self.episode_losses_list_update_counter_max - self.episode_losses_list_update_counter_min
        self.episode_losses_list_update_counter_threshold = self.episode_losses_list_update_counter_min + self.episode_losses_list_update_counter_range // 2
        self.episode_losses_list_update_counter_threshold_max = self.episode_losses_list_update_counter_threshold + self.episode_losses_list_update_counter_range // 2
        self.episode_losses_list_update_counter_threshold_min = self.episode_losses_list_update_counter_threshold - self.episode_losses_list_update_counter_range // 2
        self.episode_losses_list_update_counter_threshold_range = self.episode_losses_list_update_counter_threshold_max - self.episode_losses_list_update_counter_threshold_min
        self.episode_losses_list_update_counter_threshold_threshold = self.episode_losses_list_update_counter_threshold_min + self.episode_losses_list_update_counter_threshold_range // 2
    def run(self):
        for episode in range(self.max_episodes):
            state = self.env.reset()
            for step in range(self.max_steps):
                if self.render:
                    self.env.render()
                action = self.agent.choose_action(state)
                next_state, reward, done, _ = self.env.step(action)
                self.agent.remember(state, action, reward, next_state, done)
                self.agent.learn()
                state = next_state
                if done:
                    self.episode_rewards.append(step)
                    self.episode_lengths.append(step)
                    self.episode_losses.append(self.agent.loss)
                    self.episode_losses_list.append(self.agent.loss)
                    self.episode_losses_list_counter += 1
                    if self.episode_losses_list_counter >= self.episode_losses_list_size:
                        self.episode_losses_list_counter = 0
                    if self.episode_losses_list_counter == self.episode_losses_list_update_counter_threshold:
                        self.episode_losses_list_update_counter += 1
                        if self.episode_losses_list_update_counter >= self.episode_losses_list_update_counter_max:
                            self.episode_losses_list_update_counter = 0
                        self.episode_losses_list_update_counter_threshold = self.episode_losses_list_update_counter_min + self.episode_losses_list_update_counter_range * self.episode_losses_list_update_counter // self.episode_losses_list_update_counter_max
    