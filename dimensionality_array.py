# Create the game_and_solution 3D array
game_and_solution = np.array([sudoku_game,sudoku_solution])

# Print game_and_solution
print(game_and_solution) 

# Create a second 3D array of another game and its solution 
new_game_and_solution = np.array([new_sudoku_game,new_sudoku_solution])

# Create a 4D array of both game and solution 3D arrays
games_and_solutions = np.array([game_and_solution,new_game_and_solution])

# Print the shape of your 4D array
print(games_and_solutions.shape)

# Flatten sudoku_game
flattened_game = sudoku_game.flatten()

# Print the shape of flattened_game
print(flattened_game.shape)

# Flatten sudoku_game
flattened_game = sudoku_game.flatten()

# Print the shape of flattened_game
print(flattened_game.shape)

# Reshape flattened_game back to a nine by nine array
reshaped_game = flattened_game.reshape((9,9))

# Print sudoku_game and reshaped_game
print(sudoku_game)
print(reshaped_game)
