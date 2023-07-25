import time
import gymnasium as gym
import numpy as np
import torch
import Config
import NNs

PATH_MODEL = 'models/model25.18.7.57.p'

env = gym.make(Config.env_name, continuous=True, render_mode="rgb_array")
env = gym.wrappers.RecordEpisodeStatistics(env)
env = gym.wrappers.RecordVideo(env, "bestRecordings", name_prefix="rl-video" + PATH_MODEL[12:22], )
state, _ = env.reset()

device = 'cuda' if torch.cuda.is_available() else 'cpu'
policy_nn = NNs.PolicyNN(input_state=state.shape[0], output_action=env.action_space.shape[0]).to(device)
policy_nn.load_state_dict(torch.load(PATH_MODEL))
print("Episodes done [", end="")
for n_episode in range(Config.test_episodes):
    print(str(n_episode) + " ", end="")
    env.start_video_recorder()
    begin_time = time.time()
    while True:
        env.render()
        actions = policy_nn(torch.tensor(state, dtype=torch.float, device=device))
        new_state, reward, done, _, _ = env.step(actions.cpu().detach().numpy())
        state = new_state
        if done:
            state, _ = env.reset()
            print(env.return_queue[n_episode])
            break
        now_time = time.time()
        if now_time - begin_time >= 60:
            state, _ = env.reset()
            print('time out, exceed 60 seconds!')
            break
    env.close_video_recorder()
print("]")
print(env.return_queue)
print("  Mean 100 test reward: " + str(np.round(np.mean(env.return_queue), 2)))
