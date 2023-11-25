import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import time as t

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
line1 = []
line2 = []
plt.title('Slope Intercept Form')

def slope_intersection(line1,line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    slope1 = ((y2 - y1) / (x2 - x1)) if (x2 - x1) != 0  else float('inf')
    slope2 = ((y4 - y3) / (x4 - x3)) if (x4 - x3) != 0  else float('inf')

    if (slope1 != slope2):
        if (slope1 == float('inf')):
            crossings = 0

            cond1 = (x3 <= x1) and (x1 < x4)
            cond2 = (x4 <= x1) and (x1 < x3)
            cond3 = (x3 <= x2) and (x2 < x4)
            cond4 = (x4 <= x2) and (x2 < x3)
            
            above1 = (y1 < slope2 * (x1 - x3) + y3)
            above2 = (y2 < slope2 * (x2 - x3) + y3)

            if (cond1 or cond2) and above1:
                crossings += 1
            if (cond3 or cond4) and above2:
                crossings += 1
            return (crossings % 2 != 0)
        elif (slope2 == float('inf')):
            crossings = 0

            cond1 = (x1 <= x3) and (x3 < x2)
            cond2 = (x2 <= x3) and (x3 < x1)
            cond3 = (x1 <= x4) and (x4 < x2)
            cond4 = (x2 <= x4) and (x4 < x1)
            
            above1 = (y3 < slope1 * (x3 - x1) + y1)
            above2 = (y4 < slope1 * (x4 - x1) + y1)

            if (cond1 or cond2) and above1:
                crossings += 1
            if (cond3 or cond4) and above2:
                crossings += 1
            return (crossings % 2 != 0)
        else:
            x = (y3 - (slope2 * x3) - y1 +(slope1 * x1))/(slope1 - slope2)
            y = slope1 * (x - x1) + y1
            if ((min(x1,x2) <= x and x <= max(x1,x2)) and (min(x3,x4) <= x and x <= max(x3,x4)) and (min(y1,y2) <= y and y <= max(y1,y2)) and (min(y3,y4) <= y and y <= max(y3,y4))):
                return 1
    elif (slope1 == float('inf') and slope2 == float('inf') and x1==x2==x3==x4 and y1==y2==y3==y4):
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
            if (slope_intersection(line1,line2)):
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