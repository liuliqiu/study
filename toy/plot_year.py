
from datetime import timedelta
from PIL import Image, ImageDraw


def plot_year(data, get_color):
    first_day = min(data.keys())
    last_day = max(data.keys())

    day = first_day
    x = 0
    y = day.weekday()
    plot_list = []

    while day <= last_day:
        color = get_color(data[day])
        plot_list.append((x, y, color))
        day += timedelta(days=1)
        y = day.weekday()
        if y == 0:
            x += 1
        elif day.day== 1:
            x += 1

    margin = (3, 3, 3, 3)
    size = (10, 10)
    space = 2
    width = size[0]  * x + space * (x - 1) + margin[1] + margin[3]
    height = size[1] * 7 + space * 6 + margin[0] + margin[2]
    img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    for x, y, color in plot_list:
        xy = (
            margin[3] + x * size[0] + x * space,
            margin[0] + y * size[1] + y * space,
            margin[3] + (x + 1) * size[0] + x * space,
            margin[0] + (y + 1) * size[1] + y * space,
        )
        draw.rectangle(xy, color)
    img.show()
    # img.save("year.png")


def get_color(val):
    colors = ((238, 238, 238), (214, 230, 133), (140, 198, 101), (68, 163, 64), (30, 104, 35))
    if val == 0:
        return colors[0]
    elif val < 5:
        return colors[1]
    elif val < 10:
        return colors[2]
    elif val < 20:
        return colors[3]
    else:
        return colors[4]

if __name__ == "__main__":
    from datetime import datetime
    from collections import defaultdict
    data_list = [
        ("2016-12-18 09:44:10", 12.01),
        ("2016-12-14 08:46:10", 4.12),
    ]
    data = defaultdict(int)
    for t, d in data_list:
        date = datetime.strptime(t,  "%Y-%m-%d %H:%M:%S").date()
        data[date] += d
    plot_year(data, get_color)
