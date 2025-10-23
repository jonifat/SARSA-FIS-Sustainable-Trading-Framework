# Source Code Folder

This folder contains the implementation of the SARSA reinforcement learning algorithm used in the SARSA-FIS framework.

## File
- **sarsa_v.py** – Python script for SARSA training, environment setup, and Q-table generation.

## Description
The SARSA algorithm iteratively learns trading actions through:
1. State classification using EMA-based deviation thresholds.  
2. Action selection via epsilon-greedy exploration.  
3. Reward updates based on Q-value convergence.  

The resulting Q-table is integrated into the fuzzy inference system for interpretable trading decisions.
