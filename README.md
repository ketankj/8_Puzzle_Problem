# 8-Puzzle Solver: Iterative Deepening Search (IDS) & A* Algorithm

## Overview
This project implements **Iterative Deepening Search (IDS)** and **A* Algorithm** to solve the **8-Puzzle Problem** efficiently. It explores state-space search strategies using **depth-first search with iterative deepening** and **heuristic-based informed search**.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Algorithms Implemented](#algorithms-implemented)
- [Installation](#installation)
- [Usage](#usage)
- [Limitations](#limitations)
- [Example](#example)

## Features
✔ **Iterative Deepening Search (IDS)**  
✔ **A* Algorithm with misplaced tile heuristic**  
✔ **State-space exploration with valid neighbor generation**  
✔ **Optimal path tracking to reach the goal state**  

## Algorithms Implemented

### **1. Iterative Deepening Search (IDS)**
- Uses **depth-first search (DFS)** with **incremental depth limits**.
- Generates **neighboring states** to explore valid moves.
- **Backtracks when necessary** and increases depth limit until a solution is found.
- **Outputs the sequence of moves** leading to the goal state.

### **2. A* Algorithm**
- Implements **best-first search** with a **priority queue**.
- Uses a **misplaced tile heuristic** to estimate the cost to reach the goal.
- Prioritizes exploration of states with lower estimated costs.
- **Finds the optimal solution** while keeping track of the search path.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/8-puzzle-solver.git
   cd 8-puzzle-solver
## Usage
Run the script to solve the 8-puzzle problem using IDS or A*:


python puzzle_solver.py

## Limitations
⚠ Fixed Depth Limit in IDS – IDS uses a maximum depth limit of 20, which may restrict deeper solutions.
⚠ Heuristic Dependency in A* – The misplaced tile heuristic is simple and may not always provide an accurate estimate.
⚠ Memory Usage – A* requires more memory to manage the priority queue for optimal node selection.

## Example
Initial State:
1 2 3
4 5 6
7 8 0

Goal State:
1 2 3
4 5 6
7 8 0

Final Path for IDS / A*:
[(2, 2) -> (2, 1)]  
[(2, 1) -> (1, 1)]  
...
(Solution Path Printed)