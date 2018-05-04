#!/usr/bin/python3

import curses
from random import randrange

def neigh_num (state, i, j, w, h):
    cnt = 0
    pos = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for (x, y) in pos:
        if i + x >= 0 and i + x < w and j + y >= 0 and j + y < h:
            if state[i + x][j + y]:
                cnt += 1
    return cnt

def evolve (state, w, h):
    new_state = [[False for _ in range(h)] for _ in range(w)]
    for i in range(w):
        for j in range(h):
            cnt = neigh_num(state, i, j, w, h)
            if (state[i][j] and (cnt == 2 or cnt == 3)) or (not state[i][j] and cnt == 3):
                new_state[i][j] = True
    return new_state

def random_state (state, n, w, h):
    for _ in range(n):
        (i, j) = (randrange(w), randrange(h))
        while state[i][j] == True:
            (i, j) = (randrange(w), randrange(h))
        state[i][j] = True

def print_state (stdscr, state, w, h):
    for i in range(w):
        for j in range(h):
            if state[i][j]:
                stdscr.addstr(j, i, 'O') # curses display is reversed : (y, x)

def main (stdscr):
    curses.curs_set(False) # Do not display blinking cursor
    (w, h) = (curses.COLS - 1, curses.LINES - 1)
    state = [[False for _ in range(h)] for _ in range(w)]
    random_state(state, int((w * h) / 10), w, h)

    k = 'a'
    while k != 'q':
        state = evolve(state, w, h)
        stdscr.clear()
        print_state(stdscr, state, w, h)
        stdscr.refresh()
        k = stdscr.getkey()

curses.wrapper(main)
