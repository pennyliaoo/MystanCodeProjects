"""
File: babygraphics.py
Name: Penny
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    margin = (width-2*GRAPH_MARGIN_SIZE)/len(YEARS)
    x_corrdinate = GRAPH_MARGIN_SIZE + margin*year_index
    return x_corrdinate

def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    #top line
    canvas.create_line(GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE)
    # bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # vertical line
    linemargin = (CANVAS_WIDTH-2*GRAPH_MARGIN_SIZE)/len(YEARS)
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE+linemargin*i,0,GRAPH_MARGIN_SIZE+linemargin*i,CANVAS_HEIGHT)
    for j in range(len(YEARS)):
        canvas.create_text(GRAPH_MARGIN_SIZE+TEXT_DX+linemargin*j,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,text=YEARS[j],anchor = tkinter.NW)



def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    for name in lookup_names:
        # find the name index for color
        k = lookup_names.index(name)
        color = COLORS[k]
        for i in range(len(YEARS)-1):
            last_year = str(YEARS[i])
            year = str(YEARS[i+1])
            # if last year outside 1000
            if last_year not in name_data[name]:
                # last year outside 1000 and year outside 1000
                if year not in name_data[name]:
                     canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i),
                                        CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                        get_x_coordinate(CANVAS_WIDTH, i + 1),
                                        CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                        width=LINE_WIDTH, fill=COLORS[k])
                # last year in 1000 and year outside 1000
                else:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i),
                                        CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                        get_x_coordinate(CANVAS_WIDTH, i + 1),
                                        (int(name_data[name][year]))*CANVAS_HEIGHT/1000+GRAPH_MARGIN_SIZE,
                                        width=LINE_WIDTH, fill=COLORS[k])
                # year and last year all in 1000
            else:
                if year not in name_data[name]:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i),
                                       (int(name_data[name][last_year])) * CANVAS_HEIGHT / 1000 + GRAPH_MARGIN_SIZE,
                                       get_x_coordinate(CANVAS_WIDTH, i + 1),
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       width=LINE_WIDTH, fill=COLORS[k])
                else:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), (int(name_data[name][last_year]))*CANVAS_HEIGHT/1000+GRAPH_MARGIN_SIZE,
                                    get_x_coordinate(CANVAS_WIDTH, i+1), (int(name_data[name][year]))*CANVAS_HEIGHT/1000+GRAPH_MARGIN_SIZE,
                                    width = LINE_WIDTH,fill = COLORS[k])
            # Owing to sequence different so create new loop for text
        for j in range(len(YEARS)):
            year = str(YEARS[j])
            if year not in name_data[name]:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                    text=name + '*', anchor=tkinter.SW, fill = COLORS[k])
            else:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j), (int(name_data[name][year]))*CANVAS_HEIGHT/1000+GRAPH_MARGIN_SIZE,
                                    text=name + name_data[name][year], anchor=tkinter.SW, fill = COLORS[k])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
