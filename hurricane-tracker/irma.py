import turtle
import tkinter as tk
import csv
import os

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle, the Screen, and the root window
    """
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Tracker")

    # Get the canvas and root window from the Screen
    canvas = wn.getcanvas()
    root = canvas.master  # The root window

    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    # Use tk.PhotoImage to load the background image
    map_bg_img = tk.PhotoImage(file="images/atlantic-basin.png")

    # Display the background image on the canvas
    canvas.create_image(-1175, -580, anchor=tk.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    # Keep a reference to the image to prevent garbage collection
    wn.map_bg_img = map_bg_img

    return (t, wn, root)

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
    """Animates the path of the selected hurricane."""

    (t, wn, root) = irma_setup()
    t.pendown()

    # Create a Frame for the buttons
    control_frame = tk.Frame(root)
    control_frame.pack(side=tk.BOTTOM, fill=tk.X)

    # Variable to store the selected hurricane
    selected_hurricane = tk.StringVar()

    # Get list of hurricane data files
    file_list = os.listdir('./data')
    file_list = [
        file for file in file_list
        if os.path.isfile(os.path.join('./data', file)) and file.endswith('.csv')
    ]
    hurricane_names = [os.path.splitext(file)[0] for file in file_list]

    if not hurricane_names:
        raise FileNotFoundError("No hurricane data files found in the './data' directory.")

    # Set default value
    selected_hurricane.set(hurricane_names[0])

    # Create a dropdown menu (OptionMenu) for hurricane selection
    hurricane_menu = tk.OptionMenu(control_frame, selected_hurricane, *hurricane_names)
    hurricane_menu.pack(side=tk.LEFT, padx=5, pady=5)

    # Function to start the animation
    def start_animation():
        hurricane = selected_hurricane.get() + '.csv'
        t.clear()
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.speed(10)

        with open(f"data/{hurricane}", 'r') as file:
            reader = list(csv.reader(file))
            for i in range(1, len(reader)):
                # Lat is column 2, Lon is column 3, Wind Speed is column 4
                (lat, lon, wind) = float(reader[i][2]), float(reader[i][3]), int(reader[i][4])

                # Draw the hurricane path
                category = get_category_storm(wind)
                t.color(get_storm_color(category))
                t.pensize(category ** 1.2)
                t.setpos(lon, lat)

        # Update the screen
        wn.update()

    # Create a "Start Animation" button
    start_button = tk.Button(control_frame, text="Start Animation", command=start_animation)
    start_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Create a "Replay Animation" button
    replay_button = tk.Button(control_frame, text="Replay Animation", command=start_animation)
    replay_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Mainloop
    wn.mainloop()

if __name__ == "__main__":
    irma()
