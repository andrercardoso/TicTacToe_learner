# TicTacToe_learner

Python system which learns how to play Tic Tac Toe through Reinforcement Learning



## How to use?

Run training.py to train a computer agent through 50,000 games against a static player (It's a computer player, who knows some basic rules, but who does not learn during time). It was used a static player in order to see graphically the evaluation of our computer agent during the games. 

Run play.py to play against a computer agent trained through 100,000 games against another computer agent. Challenges you to try to beat the agent player.



## Reinforcement Learning algorithm

It was used Q-learning, a model-free reinforcement learning algorithm, to learn the value of an action in a particular state of the game. The Q(s,a), which represent the expected reward given at the end of the game if the agent picks action 'a' in state 's', was calculated based on the Bellman Equation. 



![image](https://user-images.githubusercontent.com/98130096/158215465-1118929e-139f-441d-8640-b29a7b3278c1.png)

Where:
  - The last term looks into the future and returns the largest Q value that is available, ŝ is the state that is the new state after performing action a. Then, action â is the best action in the next state ŝ.
  - The learning rate α decides to what extent that we overwrite the old value.
  - The discount factor γ decides how much future rewards should be weighted compared to rewards that are present at the current time step t.
  - The R(s,a) is the reward function which it will be very simple. If the agent performs an action â that wins the game from s, then R(s,â) = 1. Else if the agent makes a mistake and picks the wrong action ã such that it loses the game then R(s,ã) = -1. Otherwise, the reward is simply R(s,a) = 0.
 



