# MVCP-ShortestHamiltonianPath : Meta-heuristic Algorithm for Elevator Group Scheduling Optimization
Projet Algorithmes pour l'optimisation - Gestion d'ascenseurs

Minimum vertex cover problem implementation (22 nodes)

Shortest hamiltonian Path Tree Graph (100 nodes)

I'll start by reviewing the contents of the newly uploaded Jupyter notebook file to understand the project and highlight any optimizations that have been made. Then, I will provide the requested GitHub commit description.

**Project Description:**
Meta-heuristic Algorithm for Elevator Group Scheduling Optimization project is a Python-based simulation and optimization tool for managing elevator operations in a multi-story building. The goal is to optimize the allocation of elevators to minimize the waiting time of users and improve the overall efficiency of elevator operations. The project implements various algorithms to simulate elevator movement, user waiting times, and optimizations to determine the most efficient paths and allocations.

**How It Works:**
- **Data Structures:** The simulation utilizes matrices and lists to represent the state of elevators, users, and their respective destinations. Each elevator's state and path are calculated based on user requests and the building layout.
- **Algorithm Implementation:** Several algorithms are employed to compute the shortest path and the optimal sequence of stops for each elevator. These algorithms consider the current position of the elevator, the requested floors, and the most efficient route to serve multiple users.
- **Simulation & Output:** The simulation runs multiple iterations, generating output that includes the sequence of stops for each elevator, the order in which users are served, and the total and average waiting times. The results are printed in a detailed, step-by-step format for analysis.

**Optimizations Highlighted:**
- **Matrix Operations:** Efficient matrix multiplication and operations are used to handle large datasets representing elevator states and user requests. This optimization reduces computational overhead.
- **Shortest Path Calculation:** The project implements an optimized version of the Hamiltonian Path algorithm tailored for the elevator scenario, ensuring that the elevators take the shortest possible path to serve all requests with minimal delay.
- **Randomized Initialization:** Elevators start at random floors to simulate real-world scenarios more accurately, adding variability and robustness to the simulation.
- **Parallel Processing:** The algorithm processes requests in parallel where possible, significantly reducing the overall computation time and allowing for faster simulations.

**How to Run:**
1. **Environment Setup:** Ensure that you have the required Python libraries installed. You can install the dependencies using pip:
   ```bash
   pip install numpy
   ```
2. **Running the Simulation:** Load the provided Jupyter notebook and run the cells sequentially. The notebook contains all the necessary code to initialize the simulation, execute the algorithms, and display the results.
3. **Analyzing Results:** After running the simulation, the results will be printed directly in the notebook, showing the optimized paths for each elevator, along with a summary of total and average waiting times.

This commit finalizes the "Ascenseurs" project with implemented optimizations and detailed documentation for running the simulation effectively.
