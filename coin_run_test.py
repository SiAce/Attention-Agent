import gym
env = gym.make('procgen:procgen-coinrun-v0')
obs = env.reset()
print(f"coinrun action : type = {type(env.action_space.sample())}  \n {env.action_space.sample()}")

# env_car = gym.make('CarRacing-v0')
# obs = env_car.reset()
# print(f"car racing action : type = {type(env_car.action_space.sample())} \n {env_car.action_space.sample()}")

for _ in range(3):
    env.reset()
    while True:
        obs, rew, done, info = env.step(8)
        print(f"observation: type = {type(obs)}, shape = {obs.shape} \n {obs}")
        print(f"reward: type = {type(rew)} \n {rew}")
        env.render()
        if done:
            break