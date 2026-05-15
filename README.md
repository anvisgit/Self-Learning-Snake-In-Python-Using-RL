# Self-Learning-Snake-In-Python-Using-RL
A complete Python project where an AI learns to master Snake using Deep Q Learning with PyTorch and Pygame, yada yada yada 

The outputs show a classic reinforcement learning progression curve, long stretches of mediocrity interrupted by sudden bursts of competence. Early on, between Games 58–69, the agent performs inconsistently, mostly scoring between 0 and 2. That phase suggests the model is still heavily exploring the environment rather than exploiting learned behavior. The low record of 2 persisting for multiple games indicates that whatever policy it had learned was still unstable and weak. Around Games 70–80, the behavior changes noticeably. Scores become more varied and significantly higher-- 7, 6, 5, 10.The increase is not smooth because RL training rarely is. Instead, learning appears in spikes. The agent discovers a strategy, partially forgets it, rediscovers a stronger variant, and gradually stabilizes.

I stopped at Game 85 mostly because I was too lazy to let it continue training longer. Realistically, given the trajectory, the scores probably would have stabilized higher with more episodes and tuning.
