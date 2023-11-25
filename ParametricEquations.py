import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import time as t

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
line1 = []
line2 = []
plt.title('Parametric Equations')

def para_intersection(line1,line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    # Parametric representation: line1[0] + t1 * (line1[1] - line1[0]) = line2[0] + t2 * (line2[1] - line2[0])
    # Solve for t1 and t2 using a system of linear equations

    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3

    det = dx1 * dy2 - dx2 * dy1

    if det == 0:
        return 0

    t1 = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / det
    t2 = ((x3 - x1) * dy1 - (y3 - y1) * dx1) / det

    if 0 <= t1 <= 1 and 0 <= t2 <= 1:
        return 1

    return 0

def draw_point(x, y):
    ax.scatter(x, y, color='red')
    fig.canvas.draw()

def on_click(event):
    x, y = event.xdata, event.ydata
    if x is not None and y is not None:
        if len(line1) < 2:
            line1.append((x, y))
            # print(f"Clicked at: ({x}, {y}) for line1")
        elif len(line2) < 2:
            line2.append((x, y))
            # print(f"Clicked at: ({x}, {y}) for line2")

        draw_point(x, y)

        if len(line1) == 2:
            draw_line_segments(line1,'yellow')

        if len(line1) == 2 and len(line2) == 2:
            draw_line_segments(line2,'green')
            fig.canvas.mpl_disconnect(cid)
            start = t.time()
            if (para_intersection(line1,line2)):
                plt.annotate('Lines are intersecting', xy=(0, 0), xytext=(1, -1.20))
                plt.show()
                # print('Entered lines are intersecting')
            else:
                plt.annotate('Lines are not intersecting', xy=(0, 0), xytext=(1, -1.20))
                plt.show()
                # print('Entered lines are not intersecting')
            end = t.time()
            total = end - start
            plt.annotate(f'Execution Time = {total:.5f}s', xy=(0, 0), xytext=(5, -1.20))
            plt.show()

def draw_line_segments(line,setColor):
    line_segment = Line2D(*zip(line[0], line[1]), color = setColor)
    ax.add_line(line_segment)
    fig.canvas.draw()

cid = fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()