'''
Created on 28. 6. 2017

@author: patex1987
'''
import os
import time
import copy
import MazeException


def cls():
    '''
    Clears the terminal window
    Should work on windows and Linux as well
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def maze_size(maze):
    '''
    Checks the maze size
    returns a tuple of width, height
    '''
    width = len(maze[0])
    height = len(maze)
    if width < 2:
        raise MazeException.ImproperMaze
    if height < 1:
        raise MazeException.ImproperMaze
    return width, height


def print_maze(maze_2d, base_width, base_height, fill_length=1, wait=1):
    '''
    Prints the maze as a table
    '''
    time.sleep(wait)
    cls()
    human_maze = pretty_maze(maze_2d)
    line_width = ((1+(2*(fill_length))+1)*base_width) + 1
    print('-'*line_width)
    basic_elem = '{fill}|{fill}'.format(fill=' '*fill_length)
    for line in human_maze:
        line_text = basic_elem.join((str(elem) for elem in line))
        empty_line = basic_elem.join((' ' for elem in line))
        for _ in range(fill_length - 1):
            print('|{fill}{data}{fill}|'.format(fill=' '*fill_length,
                                                data=empty_line))
        print('|{fill}{data}{fill}|'.format(fill=' '*fill_length,
                                            data=line_text))
        for _ in range(fill_length - 1):
            print('|{fill}{data}{fill}|'.format(fill=' '*fill_length,
                                                data=empty_line))
        print('-'*line_width)


def recursive_walk(maze, x, y, width, height):
    '''
    Finds the finish position of the maze recursively
    '''
    if maze[x][y] == 0:
        maze[x][y] = 3
    print_maze(maze, width, height, 2, 0.4)
    if maze[x][y] == 2:
        return [(y, x)]
    next_free_blocks = find_next_pos(maze, x, y, width, height)
    if not next_free_blocks:
        pass
    for block in next_free_blocks:
        block_state = recursive_walk(maze, block[0], block[1], width, height)
        if block_state:
            return [(y, x)] + block_state
    return False


def bfs_walk(maze, x, y, width, height):
    '''
    breadth first search walk
    '''
    print('BFS')
    blocks_to_analyze = [(x, y)]
    while blocks_to_analyze:
        act_block = blocks_to_analyze.pop(0)
        if maze[act_block[0]][act_block[1]] == 2:
            return True
        if maze[act_block[0]][act_block[1]] == 0:
            maze[act_block[0]][act_block[1]] = 3
        print_maze(maze, width, height, 2, 0.4)
        next_free_blocks = find_next_pos(maze,
                                         act_block[0],
                                         act_block[1],
                                         width,
                                         height)
        for block in next_free_blocks:
            new_block = tuple(block)
            if new_block not in blocks_to_analyze:
                blocks_to_analyze.append(new_block)
            if maze[new_block[0]][new_block[1]] == 2:
                return True
        print(blocks_to_analyze)
    return False


def find_next_pos(maze, x, y, width, height):
    '''
    returns a list of surrounding free blocks
    '''
    free_positions = []
    if x < width - 1:
        if maze[x+1][y] == 0:
            free_positions.append([x+1, y])
        if maze[x+1][y] == 2:
            return [[x+1, y]]
    if y < height - 1:
        if maze[x][y+1] == 0:
            free_positions.append([x, y+1])
        if maze[x][y+1] == 2:
            return [[x, y+1]]
    if x > 0:
        if maze[x-1][y] == 0:
            free_positions.append([x-1, y])
        if maze[x-1][y] == 2:
            return [[x-1, y]]
    if y > 0:
        if maze[x][y-1] == 0:
            free_positions.append([x, y-1])
        if maze[x][y-1] == 2:
            return [[x, y-1]]
    return free_positions


def pretty_maze(maze):
    '''
    Converts the integers in the maze to chracters
    '''
    in_tab = '0123'
    out_tab = ' XFo'
    transition = str.maketrans(in_tab, out_tab)
    out_maze = [''.join(str(x) for x in line).translate(transition)
                for line
                in maze]
    return out_maze


if __name__ == '__main__':
    ORIG_MAZE = [[0, 1, 0, 1, 0, 1],
                 [2, 0, 0, 0, 0, 0],
                 [1, 1, 0, 1, 0, 1],
                 [0, 0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0]]
    MAZE = copy.deepcopy(ORIG_MAZE)
    BASE_WIDTH, BASE_HEIGHT = maze_size(MAZE)
    print(recursive_walk(MAZE, 5, 5, BASE_WIDTH, BASE_HEIGHT))
    MAZE = copy.deepcopy(ORIG_MAZE)
    bfs_walk(MAZE, 0, 0, BASE_WIDTH, BASE_HEIGHT)
