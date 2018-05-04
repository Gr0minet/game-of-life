# Game of Life

This is [Conway's Game of Life] (https://en.wikipedia.org/wiki/Conway's_Game_of_Life) written with python3 and curses. This is a very brief example to show how curses works with python.

I will assume you have basic knowledge of python syntax. If you are looking for a crash course, you can find [one here] (https://learnxinyminutes.com/docs/python3/). No need to read everything about the latter, as we won't use any class or advanced stuff here.

## Curses with python

Have you ever wondered how programs like top or nano work ? Well, they all use a [terminal user interface] (https://en.wikipedia.org/wiki/Text-based_user_interface) library : [curses] (https://en.wikipedia.org/wiki/Curses_(programming_library)). 

These software use the C library curses. As we are coding with python here, we will use the python wrapper for curses.

You can find a very good tutorial on how curses with python works [here] (https://docs.python.org/3/howto/curses.html). I will sum up briefly how the python module curses works.

### Initializing curses

Start by importing curses :

```python
import curses
```

In order to initialize the curses environment, we have to use several functions like :
* `initscr()` to create a window object
* `noecho()` to turn off echoing of keys on the screen
* `cbreak()` to react to keys instantly, without having to press Enter key

But be careful : if you don't restore the original state of the terminal at the end of your program, the curses environment will live on after the program dies. That means you won't see the letters you write on the screen, because of `noecho()` ! :(

Therefore, you have to call functions like `echo()`, `nocbreak()` before exiting your program, and it becomes tedious.

Fortunately, there is a much simplier way to handle a curses environment, with the `wrapper()` function.

All you have to do, is define a function that you want to call after the initialization of curses. That will be our main function :

```python
def main (stdscr):
	# Play with curses
	# ...

curses.wrapper(main)
```

The `wrapper` function will do all the initialization stuff we talked about, before calling our main function. It will also restore the terminal original state before exiting. Wicked !

### Playing with curses

Now we can start using curses :)

Curses allows you to split the terminal screen in multiple rectangular areas, called windows. The `stdscr` argument of our main function will be one of these windows objects, representing the entire screen. It is set by `wrapper()` before calling main.

As we don't need to split the screen, we will stick with `stdscr`, and print everything directly on this window.

Handling the window is very easy. You can use `clear()` to erase everything on it. Then, the `addstr()` function is used to display a string at any position (i, j) on the window.

Be careful : the coordinates are reversed from standard notation :

```python
stdscr.addstr(y, x, 'X')
```

This will print 'X' at the position (x, y) on the `stdscr` window.

But the text will not show up on the screen immediately, and you will have to call `stdscr.refresh()` to make it visible. It was useful back in the days when computer were slow and needed this kind of buffer optimization.

Now, we know how to print text. What about interacting with the user input keys ? Well, that is once again very simple : the only function you have to know is `getkey()`.

It will wait for the user to press a key, and will return a string according to the key pressed : for instance, 'a' or '-'.

## The Game of Life

Ok, now we are ready to build our Game of Life (GoL) with curses ! Let's list what we want :

* Generate several starting GoL cells randomly on the screen
* Update the GoL cells according to the rules of the game
* Wait for the user to press a key before the next update
* Quit the game if the user press 'q'

But first of all, we need to know what is the size of the terminal window. You can use curses.COLS, and curses.LINES in order to know that :

```python
	(w, h) = (curses.COLS - 1, curses.LINES - 1)
```

Then, we need to have a data structure to store the current GoL state. We will use a simple 2-dimensional array : 

```python
    state = [[False for _ in range(h)] for _ in range(w)]
```

`state[i][j]` is *True*  if there is a cell at the (i, j) position, False otherwise.

Now it's time to add several starting cells on the screen. In order to do that, `randrange()` from the python module `random` will be useful. For instance, `randrange(10)` will give us a pseudo-random integer between 0 and 9 included.

I won't detail every single function because it is already very simple and self-explanatory. Here is a short list of what we use :

* `random_state()` is used for adding *n* cells randomly to the GoL state
* `neigh_num()` calculates the number of neighbours for a given cell
* `evolve()` updates the state of the game according to GoL rules
* `print_state()` will print the GoL state on stdscr

Now you must be able to understand the whole code !

## Improvements

Here are some ideas to improve the program :

* Allow the user to set up the starting state as he wishes
* Try to simulate a real Game of Life with infinite space (ours is limited by the window borders)
* Add some colours to make it look better !

Feel free to try to implement these !
