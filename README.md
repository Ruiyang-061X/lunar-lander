# Lunar Lander
## INTRODUCTION
Lunar Lander is about landing a spacecraft on a specific landing area on moon safely.
<br>**Gymnasium** is a open-source toolkit for reinforcement learning, which contains various reinforcement learning environments and provides a standard development procedure of reinforcement learning. It originates from OpenAI's **gym**. Refer to [their website](https://gymnasium.farama.org/) for more information.

## METHOD
The actions of spacecraft contain:
- do nothing
- fire left orientation engine
- fire main engine
- fire right orientation engine

The rules of award:
- increased the closer the lander is to the landing pad
- increased the slower the lander is moving
- increased the more the lander is horizontal
- increased by 10 points for each leg that is in contact with the ground
- decreased by 0.03 points each frame a side engine is firing
- decreased by 0.3 points each frame the main engine is firing

The spacecraft is trained by DDPG(Deep Deterministic Policy Gradient), which is a extension of DQN(Deep Q-Network) aiming to solve the problem of continuous control. 

## ENVIRONMENT
The core dependencies are listed below.
- python 3.11
- torch 2.0.1+cu117
- gymnasium 0.29.0
- tensorboardX 2.6.1
- cost of GPU is around 1GB

## TRAINING
```
python main.py
```

## TESTING
```
python load.py
```
There is a ready-to-use model in this repo. Run the command above to see the result.

## DEMO
[Video Link](https://github-production-user-asset-6210df.s3.amazonaws.com/48590144/255906151-cc0e03f4-7352-4573-874b-e6c6564d37dc.mp4)

## ACKNOWLEDGEMENT
The code is mainly based on [drl-ddpg-lunar-lander](https://github.com/leonjovanovic/drl-ddpg-lunar-lander). Thanks the aurther for the excellent work.

## AND
Feel free to raise an issue if you encounter any problem :).
