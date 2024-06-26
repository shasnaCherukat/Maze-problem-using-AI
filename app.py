# app.py

from flask import Flask, render_template
from mazegen import generate_maze, astar

app = Flask(__name__)

@app.route('/')
def index():
    rows, columns = 10, 20
    maze = generate_maze(rows, columns)
    
    # Define start and end points
    start = (0, 0)
    end = (rows - 1, columns - 1)

    # Find the solution path using A*
    solution_path = astar(maze, start, end)

    return render_template('index.html', maze=maze, solution_path=solution_path)

if __name__ == '__main__':
    app.run(debug=True)
