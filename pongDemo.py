import gym

# env = gym.make("Pong-v0")
# env.reset()
# for _ in range(1000):
#     env.render()
#     action = env.action_space.sample() # take a random action
#     observation, reward, done, info = env.step(action)

# env.close()    

from gym.utils.play import play
env = gym.make("Pong-v0")
play(env, zoom=4)