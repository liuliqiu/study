
from datetime import timedelta
from PIL import Image, ImageDraw

def plot_year_list(data_list, get_color):
    data = defaultdict(int)
    for t, d in data_list:
        date = t.date()
        data[date] += d
    return plot_year(data, get_color)

def plot_year(data, get_color):
    print(data)
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
    width = size[0]  * (x + 1) + space * (x - 1) + margin[1] + margin[3]
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
    # img.show()
    # img.save("year.png")
    return img


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
    import json

    def plot_2015():
        data_list = []
        with open("run_2015.json") as run_log:
            for data in json.load(run_log)["datas"]:
                data_list.append((datetime.fromtimestamp(data["lasttime"]), data["meter"]/1000.))
        data_list = filter(lambda x:x[0] < datetime.strptime("2016-01-01", "%Y-%m-%d"), data_list)
        return plot_year_list(data_list, get_color)

    def plot_2016():
        data_list = []
        with open("run.json") as run_log:
            for data in json.load(run_log)["datas"]:
                data_list.append((datetime.fromtimestamp(data["lasttime"]), data["meter"]/1000.))
        data_list.append((datetime.strptime("2016-12-10", "%Y-%m-%d"), 11.10))
        data_list.append((datetime.strptime("2016-12-11", "%Y-%m-%d"), 15.08))
        data_list.append((datetime.strptime("2016-12-13", "%Y-%m-%d"), 4.11))
        data_list.append((datetime.strptime("2016-12-14", "%Y-%m-%d"), 4.12))
        data_list.append((datetime.strptime("2016-12-18", "%Y-%m-%d"), 12.01))
        data_list.append((datetime.strptime("2016-12-28", "%Y-%m-%d"), 2.04))
        data_list.append((datetime.strptime("2016-12-29", "%Y-%m-%d"), 3.07))
        data_list.append((datetime.strptime("2016-12-30", "%Y-%m-%d"), 4.21))

        return plot_year_list(data_list, get_color)

    img_2015 = plot_2015()
    img_2015.save("year_2015.png")
    img_2016 = plot_2016()
    img_2016.save("year_2016.png")

    width = max(img_2015.size[0], img_2016.size[0])
    height = img_2015.size[1] + img_2016.size[1] + 2
    img = Image.new("RGBA", (width, height), (255, 255, 255, 0))

    # h = 0
    # p = img_2015.crop((0, 0, img_2015.size[0], img_2015.size[1]))
    # img.paste(p, (width - img_2015.size[0], h, img_2015.size[0], img_2015.size[1]))
    # h += img_2015.size[1] + 2

    # p = img_2016.crop((0, 0, img_2016.size[0], img_2016.size[1]))
    # img.paste(p, (width - img_2016.size[0], h, img_2016.size[0], img_2016.size[1]))

    img.save("year.png")


