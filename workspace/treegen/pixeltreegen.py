#pixeltreegen.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import json
from PIL import Image, ImageTk
import os
import sys
import subprocess


# Lock values for sliders
slider_locks = {}

# Variable to store the tree image
tree_image = None
tree_image_label = None

# Function to update the slider values
def update_slider(name, value):
    if name not in slider_locks:
        slider, lock_var, slider_value, display_value = None, None, None, None
        slider_locks[name] = slider, lock_var, slider_value, display_value

    slider, lock_var, slider_value, display_value = slider_locks[name]
    display_value.set(f"{value:.2f}")

# Function to generate the tree
def generate_tree():
    global tree_image
    global tree_image_label
    # Collect the parameters from the sliders
    parameters = {name: var.get() for name, var in slider_values.items()}

    # Generate the tree using the generate_tree_image function
    tree_image_path = os.path.join(os.path.dirname(__file__), "tree.png")
    image = generate_tree_image(parameters)
    image.save(tree_image_path)

    # Load the generated image
    image.thumbnail((400, 400), Image.ANTIALIAS)
    tree_image = ImageTk.PhotoImage(image)
    tree_image_label.config(image=tree_image)  # We can now use tree_image_label here

# The generate_tree_image function would look something like this:
def generate_tree_image(parameters):
    # This is where you would put the code to generate the tree image based on the parameters
    # For now, I'll just return a new blank image
    return Image.new('RGB', (400, 400))

# Default tree parameters
default_tree_parameters = {
        "function": generate_tree,
        "arguments": {
            "trunk_length": {"default": 1.0, "range": (0.1, 5.0)},
            "branch_length": {"default": 0.5, "range": (0.1, 2.5)},
            "branch_amount": {"default": 3, "range": (1, 10)},
            "branch_curve": {"default": 45.0, "range": (0.0, 90.0)},
            "fork_amount": {"default": 2, "range": (1, 5)},
            "leaf_density": {"default": 0.5, "range": (0.1, 1.0)},
            "width_taper": {"default": 0.8, "range": (0.5, 1.0)},
            "length_taper": {"default": 0.8, "range": (0.5, 1.0)},
            "leaf_color_red": {"default": 0, "range": (0, 255)},
            "leaf_color_green": {"default": 128, "range": (0, 255)},
            "leaf_color_blue": {"default": 0, "range": (0, 255)},
            "trunk_color_red": {"default": 165, "range": (0, 255)},
            "trunk_color_green": {"default": 42, "range": (0, 255)},
            "trunk_color_blue": {"default": 42, "range": (0, 255)},
        },
    }

def save_image():
    # Generate the image
    parameters = {name: var.get() for name, var in slider_values.items()}
    image = generate_tree_image(parameters)

    # Ask the user for a file to save to
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if not file_path:
        return

    # Save the image to the file
    image.save(file_path)

def save_parameters():
    # Collect the parameters from the sliders
    parameters = {name: var.get() for name, var in slider_values.items()}

    # Ask the user for a file to save to
    file_path = filedialog.asksaveasfilename(defaultextension=".json")
    if not file_path:
        return

    # Save the parameters to the file
    with open(file_path, "w") as f:
        json.dump(parameters, f)

def load_parameters():
    # Ask the user for a file to load from
    file_path = filedialog.askopenfilename(defaultextension=".json")
    if not file_path:
        return

    # Load the parameters from the file
    with open(file_path, "r") as f:
        parameters = json.load(f)

    # Set the sliders to the loaded parameters
    for name, value in parameters.items():
        if name in slider_values:
            slider_values[name].set(value)

    # Update the tree image
    generate_tree()

def reset_parameters():
    # Set the sliders to the default parameters
    for name, value in default_tree_parameters.items():
        if name in slider_values:
            slider_values[name].set(value)

    # Update the tree image
    generate_tree()
'''
def create_parameter_frame(parent, name, row, column, value=0.5, from_=0.0, to=1.0, resolution=0.01):
    # Create a new frame for the parameter
    parent_frame = tk.Frame(root)
    parent_frame.grid(row=1, column=0, sticky='nsew')  # Adjust the row index to 1
    parent_frame.grid_rowconfigure(0, weight=1)
    parent_frame.grid_rowconfigure(1, weight=1)
    parent_frame.grid_columnconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(1, weight=1)
            
    frame = ttk.Frame(parent)
    frame.grid(row=row, column=column)
    
    top_frame = tk.Frame(parent_frame,)
    top_frame.grid(row=0, column=0, sticky='nsew')
    
    left_frame = tk.Frame(parent_frame)
    left_frame.grid(row=1, column=1, sticky='nsew')

    center_frame = tk.Frame(parent_frame)
    center_frame.grid(row=1, column=2, sticky='nsew')

    right_frame = tk.Frame(parent_frame)
    right_frame.grid(row=1, column=3, sticky='nsew')

    bottom_right_frame = tk.Frame(parent_frame)
    bottom_right_frame.grid(row=2, column=0, columnspan=3, sticky='nsew')

    bottom_middle_frame = tk.Frame(parent_frame)
    bottom_middle_frame.grid(row=2, column=1, columnspan=3, sticky='nsew')

    bottom_left_frame = tk.Frame(parent_frame)
    bottom_left_frame.grid(row=2, column=2, columnspan=3, sticky='nsew')



    return slider_value
'''
def create_parameter_frame(parent, name, value=0.5, from_=0.0, to=1.0, resolution=0.01):
    # Create a new frame for the parameter
    frame = tk.Frame(parent)
    frame.grid(row=0, column=1, sticky='nsew')  # Place the frame in row 0, column 1
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    # Create sub-frames within the parameter frame for the different elements
    top_frame = tk.Frame(frame)
    top_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

    middle_frame = tk.Frame(frame)
    middle_frame.grid(row=1, column=0, columnspan=2, sticky='nsew')

    bottom_frame = tk.Frame(frame)
    bottom_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')

    # Create the slider and associated elements within the parameter frame
    slider_value = create_slider(frame, name, value, from_, to)

    return slider_value

def create_slider(parent, name, row, column, value=0.5, from_=0.0, to=1.0, resolution=0.01):
    slider_value = tk.DoubleVar(value=value)
    slider_value.trace("w", lambda *args: update_slider(name, slider_value.get()))

    # Replace underscores with spaces and capitalize the first letter of each word
    formatted_name = name.replace("_", " ").title()
    name_label = ttk.Label(parent, text=formatted_name)
    name_label.grid(row=int(row)*2, column=int(column), sticky="nsew")

    min_label = ttk.Label(parent, text=f"{from_:.2f}")
    min_label.grid(row=int(row)*2+1, column=int(column), sticky="w", padx=5)

    slider = ttk.Scale(parent, from_=from_, to=to, variable=slider_value, command=lambda v: update_slider(name, float(v)), length=200)
    slider.grid(row=int(row)*2+1, column=int(column)+1, sticky="ew")  # Change the column number here

    max_label = ttk.Label(parent, text=f"{to:.2f}")
    max_label.grid(row=int(row)*2+1, column=int(column)+1, sticky="e", padx=5)

    lock_var = tk.BooleanVar(value=False)
    lock_checkbutton = ttk.Checkbutton(parent, text="🔒", variable=lock_var, command=lambda: lock_slider(name))
    lock_checkbutton.grid(row=int(row)*2+2, column=int(column), sticky="w", padx=5)

    display_value = tk.StringVar()
    validate_command = parent.register(lambda s: len(s) <= 4)
    display_entry = ttk.Entry(parent, textvariable=display_value, validate="key", validatecommand=(validate_command, '%P'), width=4)
    display_entry.grid(row=int(row)*2+2, column=int(column)+1, sticky="e")  # Change the column number here

    slider_locks[name] = slider, lock_var, slider_value, display_value

    # When the entry value is manually changed, update the slider and the display_value
    def update_entry(*args):
        try:
            value = float(display_value.get())
            if lock_var.get():
                # If the slider is locked, reset the entry value to the slider value
                display_value.set(f"{slider_value.get():.2f}")
            else:
                # If the value exceeds the maximum, warn the user and reset the entry value to the slider value
                if value > to:
                    print("Value exceeds the maximum value.")
                    display_value.set(f"{slider_value.get():.2f}")
                else:
                    slider_value.set(value)
                    display_value.set(f"{value:.2f}")
        except ValueError:
            pass

    display_value.trace("w", update_entry)

    return slider_value

root = tk.Tk()

# Create a master frame for all sliders in the main window
sliders_frame = tk.Frame(root)
sliders_frame.grid(row=0, column=1, sticky='nsew')

slider_values = {}
for i, (name, details) in enumerate(default_tree_parameters["arguments"].items()):
    default_value = details["default"]
    slider_range = details["range"]
    slider_values[name] = create_parameter_frame(sliders_frame, name, value=default_value, from_=slider_range[0], to=slider_range[1])


def lock_slider(name):
    slider, lock_var, slider_value, display_value = slider_locks[name]
    if lock_var.get():
        slider.config(state="disabled")
    else:
        slider.config(state="normal")


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

# Create the main frame
main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.grid(row=0, column=0, sticky="nsew")

# Create the sliders
slider_values = {}
for i, (name, details) in enumerate(default_tree_parameters["arguments"].items()):
    default_value = details["default"]
    slider_range = details["range"]
    slider_values[name] = create_slider(main_frame, name, i, 0, value=default_value, from_=slider_range[0], to=slider_range[1])
for name in slider_values:
    update_slider(name, slider_values[name].get())
    ttk.Separator(main_frame, orient='horizontal').grid(row=i*2+3, column=0, columnspan=3, sticky='ew', pady=10)

# Configure the grid
for i in range(len(default_tree_parameters["arguments"])):
    main_frame.columnconfigure(i, weight=1)
    main_frame.rowconfigure(i, weight=1, minsize=50)  # Minimum size of 50 pixels

# Create the sliders
slider_values = {}
for i, (name, details) in enumerate(default_tree_parameters["arguments"].items()):
    default_value = details["default"]
    slider_range = details["range"]
    slider_values[name] = create_slider(main_frame, name, i*2, 0, value=default_value, from_=slider_range[0], to=slider_range[1])
for name in slider_values:
    update_slider(name, slider_values[name].get())


def create_color_display(parent, row, column, color_vars):
    canvas = tk.Canvas(parent, width=50, height=50)
    canvas.grid(row=int(row)*3, column=column)
    
    def update_color(*args):
        color = '#%02x%02x%02x' % (int(color_vars[0].get()), int(color_vars[1].get()), int(color_vars[2].get()))
        canvas.configure(bg=color)

    for var in color_vars:
        var.trace('w', update_color)
    
    update_color()

    separator = ttk.Separator(main_frame, orient='horizontal')
    separator.grid(row=len(default_tree_parameters["arguments"]), columnspan=4, sticky='ew')

    create_color_display(main_frame, len(default_tree_parameters["arguments"]), 3, [
        slider_values["leaf_color_red"], 
        slider_values["leaf_color_green"], 
        slider_values["leaf_color_blue"]
    ])

    separator = ttk.Separator(main_frame, orient='horizontal')
    separator.grid(row=len(default_tree_parameters["arguments"]), columnspan=4, sticky='ew')

    create_color_display(main_frame, len(default_tree_parameters["arguments"])+1, 3, [
        slider_values["trunk_color_red"], 
        slider_values["trunk_color_green"], 
        slider_values["trunk_color_blue"]
    ])

    # Create the generate button
    generate_button = ttk.Button(main_frame, text="Generate", command=generate_tree)
    generate_button.grid(row=len(default_tree_parameters), column=0, columnspan=3, sticky="nsew")

    # Create the save parameters button
    save_parameters_button = ttk.Button(main_frame, text="Save Parameters", command=save_parameters)
    save_parameters_button.grid(row=len(default_tree_parameters)+1, column=0, sticky="nsew")
    
    # Create the load parameters button
    load_parameters_button = ttk.Button(main_frame, text="Load Parameters", command=load_parameters)
    load_parameters_button.grid(row=len(default_tree_parameters)+1, column=1, sticky="nsew")

    # Create the reset parameters button
    reset_parameters_button = ttk.Button(main_frame, text="Reset Parameters", command=reset_parameters)
    reset_parameters_button.grid(row=len(default_tree_parameters)+1, column=2, sticky="nsew")

    # Create the save image button
    save_image_button = ttk.Button(main_frame, text="Save Image", command=save_image)
    save_image_button.grid(row=len(default_tree_parameters)+2, column=0, sticky="nsew")
    
    # Create the tree image label
    tree_image_label = ttk.Label(main_frame)
    tree_image_label.grid(row=0, column=3, rowspan=len(default_tree_parameters)+2, sticky="nsew")

# Start the main loop
root.mainloop()
