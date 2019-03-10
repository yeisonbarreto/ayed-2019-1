from sys import stdin
def robot(grid):
    
    solution = [[0]*len(grid[0]) for i in grid]
    
    if grid[0][0] == 0:
        solution[0][0] = 1
        
    for i in range(1,len(grid)):
        
        if grid[i][0] == 0:
            solution[i][0] = solution[i-1][0]
            
    for j in range(1,len(grid[0])):
        if grid[0][j] == 0:
            solution[0][j] = solution[0][j-1]
            
    for i in range(1, len(grid)): 
      for j in range(1, len(grid[0])): 
        if grid[i][j] == 0: 
          solution[i][j] = solution[i-1][j] + solution[i][j-1]
          
    return solution[-1][-1]
    
            
def main():
    grid = eval(stdin.readline().strip())
    print(robot(grid))
main()

    
