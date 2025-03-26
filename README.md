Problem: You need to implement the algorithm for the project selection problem. You are given
a set of 𝑛 projects, indexed from 1 to 𝑛. Each project 𝑖 ∈ [𝑛] has a specific weight 𝑤𝑖 ∈ 𝑍, which
can be positive or negative. Additionally, there are precedence constraints between the projects:
if project 𝑖 precedes project 𝑗, then to select 𝑗, you must also select 𝑖. The precedence
constraints do not induce cycles; that is, if we draw a directed edge (𝑖, 𝑗) if 𝑖 precedes 𝑗, then the
resulting directed graph does not contain a directed cycle. The goal of the problem is to select a
subset of projects such that the total weight of the selected projects is maximized, while
satisfying all the precedence constraints.

Input:
• The input is taken from the standard input (console).
• The first line of the input contains two integers n and m, indicating the number of projects
and the number of precedence constraints respectively.
• The second line contains 𝑛 integers representing the weights of the projects, with the 𝑖-th
number denoting the weight of project 𝑖.
• The next 𝑚 lines contain the 𝑚 precedence constraints. Each line contains two integers
𝑖, 𝑗 ∈ [𝑛], 𝑖 ≠ 𝑗, indicating a precedence constraint where project 𝑖 precedes project 𝑗.

Output:
• The output is printed onto the standard output (console).
• The output contains a single integer representing the maximum total weight of the
selected subset of projects.

Constraints:
• 1 ≤ 𝑛 ≤ 1000.
• 1 ≤ 𝑚 ≤ 10000.
• −106 ≤ 𝑤𝑖 ≤ 106.
• It is expected that your program will terminate in 10 seconds.
