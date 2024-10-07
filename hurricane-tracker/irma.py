import turtle
# import csv

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

def get_category_storm(wind_speed: int) -> int:
    '''Returns the storm category 0-5
    '''
    if wind_speed > 0 and wind_speed < 74:
        return 0
    elif wind_speed < 96:
        return 1
    elif wind_speed < 111:
        return 2
    elif wind_speed < 130:
        return 3
    elif wind_speed < 157:
        return 4
    elif wind_speed >= 158:
        return 5
    else:
        return 0

def get_storm_color(category: int) -> str:
    '''
    Red for Category 5
    Orange for Category 4
    Yellow for Category 3
    Green for Category 2
    Blue for Category 1
    White if not hurricane strength
    '''
    color_dict = {
        5: 'red',
        4: 'orange',
        3: 'yellow',
        2: 'green',
        1: 'blue',
        0: 'white'
    }
    return color_dict[category]


def irma():
    """Animates the path of hurricane Irma
    """
    import csv
    import os

    (t, wn, map_bg_img) = irma_setup()
    t.pendown()

    hurricane = ''
    while not hurricane:
        file_list = os.listdir('./data')
        file_list = [file for file in file_list if os.path.isfile(os.path.join('./data', file))]
        user = input("which hurricane would you like to select? (type list for list)")
        if user == "list":
            for file in file_list:
                name = file.split('.')[0]
                print(name)
        elif (user + '.csv') in file_list:
            hurricane = user + '.csv'

    with open(f"data/{hurricane}", 'r') as file:
        reader = list(csv.reader(file))
        for i in range(1,len(reader)):
            # Lat is 2, Lon is 3, Wind Speed is 4
            (lat, lon, wind) = float(reader[i][2]), float(reader[i][3]), int(reader[i][4])

            # draw frame
            category = get_category_storm(wind)
            t.color(get_storm_color(category))
            t.pensize(category**1.2)
            t.setpos(lon, lat)

    wn.mainloop()

if __name__ == "__main__":
    irma()
