'''
Created on 28. 6. 2017

@author: patex1987
'''
import os
import MazeException


def cls():
    '''
    Clears the terminal window
    Should work on windows and Linux as well
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def print_maze(maze_2d, fill_length=1):
    '''
    Prints the maze in a pretty form
    '''
    if len(maze_2d) < 2:
        raise MazeException.ImproperMaze
    if len(maze_2d[0]) < 1:
        raise MazeException.ImproperMaze
    base_width = len(maze_2d)
    line_width = ((1+(2*(fill_length))+1)*base_width) + 1
    print('-'*line_width)
    basic_elem = '{fill}|{fill}'.format(fill=' '*fill_length)
    for line in maze_2d:
        line_text = basic_elem.join((str(elem) for elem in line))
        print('|{fill}{data}{fill}|'.format(fill=' '*fill_length,
                                            data=line_text))
        print('-'*line_width)


if __name__ == '__main__':
    MAZE = [[0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 2]]
