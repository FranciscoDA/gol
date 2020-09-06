# GOL - Game of Life

![Build status](https://api.travis-ci.org/FranciscoDA/gol.svg?branch=master)

Simple implementation of Conway's Game of Life using Pygame and Numpy

### Running the game

You need to install the requirements (numpy and pygame). It's recommended that you do this inside a Python virtual environment:
```py
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

You can run the game as follows:
```py
./gol.py
```
Note that the game starts paused and with a blank board. See below.

### Controls

 * Use the left mouse click to toggle cells.
 * Use the mouse wheel to speed up/slow down time.
 * Press ESC to quit.

### Options

You can configure a few options using the command line. Running `./gol.py --help` will print a list of the supported arguments:

```sh
> ./gol.py --help
usage: gol.py [-h] [--rows ROWS] [--cols COLS] [--theme {default,grid,heatmap,heatmapgrid}] [--resx RESX] [--resy RESY]

optional arguments:
  -h, --help            show this help message and exit
  --rows ROWS           Number of rows in the board
  --cols COLS           Number of columns in the board
  --theme {default,grid,heatmap,heatmapgrid}
                        Theme
  --resx RESX           Vertical resolution
  --resy RESY           Horizontal resolution
```

### Themes

You can select among a few themes:

![Default](https://raw.githubusercontent.com/FranciscoDA/gol/images/images/a.gif "Default theme")

![Heatmap with grid](https://raw.githubusercontent.com/FranciscoDA/gol/images/images/b.gif "Heatmap with grid theme")
