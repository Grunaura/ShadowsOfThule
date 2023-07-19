#tree_gui.py

import tkinter as tk
from tkinter import ttk
import random, sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from treegen import (generate_recursive_tree, generate_l_system_tree, generate_fractal_tree, generate_space_colonization_tree, generate_biased_random_growth_tree, generate_block_model_tree, generate_agent_based_model_tree, generate_subdivision_tree)

ignore_update = False

# Function to update the view of the 3D plot
def update_view(elevation, azimuth):
    ax.view_init(elev=elevation, azim=azimuth)
    canvas.draw()

# Create a new figure
fig = plt.figure()

# Create a 3D axis
ax = fig.add_subplot(111, projection='3d')

# Function to redraw the 3D plot with a bounding box
def redraw_plot_with_bounding_box(theme, height, width, depth):
    ax.clear()
    ax.grid(color=theme, linestyle='-', linewidth=0.3)

    # Create a bounding box that is 10% larger than the tree dimensions
    max_dim = max([height, width, depth])
    bounding_box_dim = int(max_dim * 1.1)  # 10% larger

    # Create 2D coordinate grids using meshgrid
    x = np.arange(0, bounding_box_dim, 2)
    y = np.arange(0, bounding_box_dim, 2)
    z = np.arange(0, bounding_box_dim, 2)
    xx, yy, zz = np.meshgrid(x, y, z)

    # Create a wireframe for the bounding box
    ax.plot_wireframe(xx, yy, zz, color='gray', linestyle='dashed', linewidth=0.5)

    # Scatter plot representing the tree
    ax.scatter(
        [x for x in range(1, height + 1)],
        [x for x in range(1, width + 1)],
        [x for x in range(1, depth + 1)]
    )
    
# Define the tree generation algorithms
algorithms = ["Generate Recursive Tree", "L-System", "Fractal", "Space Colonization", "Biased Random Growth", "Block Model", "Agent-Based Model", "Subdivision"]

# Define the algorithms and their arguments
algorithm_parameters = {
    "Generate Recursive Tree": {
        "function": generate_recursive_tree,
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
    },
    "L-System": {
        "function": generate_l_system_tree,
        "arguments": {
            "start_string": {"default": "", "range": (0, 10)},  # example range
            "angle": {"default": 30.0, "range": (0, 360)},
            "distance": {"default": 100.0, "range": (0, 200)},
            "depth": {"default": 5, "range": (0, 10)},
        },
    },
    "Fractal": {
        "function": generate_fractal_tree,
        "arguments": {
            "origin": {"default": [0.0, 0.0, 0.0], "range": ([0, 0, 0], [1, 1, 1])},
            "trunk_length": {"default": 100.0, "range": (1, 200)},
            "trunk_vector": {"default": [0.0, 0.0, 1.0], "range": ([-1, -1, -1], [1, 1, 1])},
            "depth": {"default": 6, "range": (1, 10)},
        },
    },
    "Space Colonization": {
        "function": generate_space_colonization_tree,
        "arguments": {
            "attraction_distance": {"default": 10, "range": (1, 20)},
            "branching_angle": {"default": 45.0, "range": (0, 360)},
            "initial_length": {"default": 100.0, "range": (1, 200)},
            "length_reduction": {"default": 0.9, "range": (0.5, 1.0)},
        },
    },
    "Biased Random Growth": {
        "function": generate_biased_random_growth_tree,
        "arguments": {
            "size": {"default": 100, "range": (1, 200)},
            "num_iterations": {"default": 5000, "range": (1000, 10000)},
        },
    },
    "Block Model": {
        "function": generate_block_model_tree,
        "arguments": {
            "origin": {"default": [0.0, 0.0, 0.0], "range": ([0, 0, 0], [1, 1, 1])},
            "trunk_length": {"default": 100.0, "range": (1, 200)},
            "trunk_vector": {"default": [0.0, 0.0, 1.0], "range": ([-1, -1, -1], [1, 1, 1])},
            "num_branches": {"default": 3, "range": (1, 10)},
            "branch_angle": {"default": 45.0, "range": (0, 360)},
            "branch_length": {"default": 50.0, "range": (1, 100)},
        },
    },
    "Agent-Based Model": {
        "function": generate_agent_based_model_tree,
        "arguments": {
            "num_agents": {"default": 100, "range": (10, 1000)},
            "max_iterations": {"default": 100, "range": (10, 1000)},
            "attraction_strength": {"default": 0.1, "range": (0.01, 1)},
            "avoidance_strength": {"default": 0.1, "range": (0.01, 1)},
            "random_strength": {"default": 0.01, "range": (0.001, 0.1)},
        },
    },
    "Subdivision Model": {
        "function": generate_subdivision_tree,
        "arguments": {
            "depth": {"default": 3, "range": (1, 10)},
            "size": {"default": 1.0, "range": (0.1, 10)},
            "min_size": {"default": 0.1, "range": (0.01, 1)},
        },
    }
}


# Your tree preset data
tree_presets = {
    "Deciduous": {
        "Oak": {"trunk_length": 5, "branch_length": 7, "branch_amount": 4, "branch_curve": 5, "fork_amount": 3, "leaf_density": 7, "leaf_color": 5, "trunk_color": 4, "width_taper": 3, "length_taper": 2},
        "Birch": {"trunk_length": 6, "branch_length": 8, "branch_amount": 3, "branch_curve": 6, "fork_amount": 2, "leaf_density": 8, "leaf_color": 6, "trunk_color": 5, "width_taper": 2, "length_taper": 3},
        "Willow": {"trunk_length": 7, "branch_length": 9, "branch_amount": 2, "branch_curve": 7, "fork_amount": 1, "leaf_density": 9, "leaf_color": 7, "trunk_color": 6, "width_taper": 1, "length_taper": 4},
        "Poplar": {"trunk_length": 8, "branch_length": 10, "branch_amount": 1, "branch_curve": 8, "fork_amount": 0, "leaf_density": 10, "leaf_color": 8, "trunk_color": 7, "width_taper": 0, "length_taper": 5},
    },
    "Coniferous": {
        "Pine": {"trunk_length": 7, "branch_length": 6, "branch_amount": 5, "branch_curve": 7, "fork_amount": 4, "leaf_density": 6, "leaf_color": 7, "trunk_color": 3, "width_taper": 4, "length_taper": 5},
        "Spruce": {"trunk_length": 8, "branch_length": 7, "branch_amount": 4, "branch_curve": 8, "fork_amount": 3, "leaf_density": 7, "leaf_color": 8, "trunk_color": 4, "width_taper": 3, "length_taper": 6},
        "Fir": {"trunk_length": 9, "branch_length": 8, "branch_amount": 3, "branch_curve": 9, "fork_amount": 2, "leaf_density": 8, "leaf_color": 9, "trunk_color": 5, "width_taper": 2, "length_taper": 7},
        "Cedar": {"trunk_length": 10, "branch_length": 9, "branch_amount": 2, "branch_curve": 10, "fork_amount": 1, "leaf_density": 9, "leaf_color": 10, "trunk_color": 6, "width_taper": 1, "length_taper": 8},
        "Juniper": {"trunk_length": 11, "branch_length": 10, "branch_amount": 1, "branch_curve": 11, "fork_amount": 0, "leaf_density": 10, "leaf_color": 11, "trunk_color": 7, "width_taper": 0, "length_taper": 9},
        "Yew": {"trunk_length": 12, "branch_length": 11, "branch_amount": 0, "branch_curve": 12, "fork_amount": 0, "leaf_density": 11, "leaf_color": 12, "trunk_color": 8, "width_taper": 0, "length_taper": 10},
        "Hemlock": {"trunk_length": 13, "branch_length": 12, "branch_amount": 0, "branch_curve": 13, "fork_amount": 0, "leaf_density": 12, "leaf_color": 13, "trunk_color": 9, "width_taper": 0, "length_taper": 11},
        "Cypress": {"trunk_length": 14, "branch_length": 13, "branch_amount": 0, "branch_curve": 14, "fork_amount": 0, "leaf_density": 13, "leaf_color": 14, "trunk_color": 10, "width_taper": 0, "length_taper": 12},
        "Redwood": {"trunk_length": 15, "branch_length": 14, "branch_amount": 0, "branch_curve": 15, "fork_amount": 0, "leaf_density": 14, "leaf_color": 15, "trunk_color": 11, "width_taper": 0, "length_taper": 13},
        "Cycad": {"trunk_length": 16, "branch_length": 15, "branch_amount": 0, "branch_curve": 16, "fork_amount": 0, "leaf_density": 15, "leaf_color": 16, "trunk_color": 12, "width_taper": 0, "length_taper": 14},
        "Ginkgo": {"trunk_length": 17, "branch_length": 16, "branch_amount": 0, "branch_curve": 17, "fork_amount": 0, "leaf_density": 16, "leaf_color": 17, "trunk_color": 13, "width_taper": 0, "length_taper": 15},
    },
    "Palm": {"trunk_length": 5, "branch_length": 7, "branch_amount": 4, "branch_curve": 5, "fork_amount": 3, "leaf_density": 7, "leaf_color": 5, "trunk_color": 4, "width_taper": 3, "length_taper": 2},
    "Shrubs": {
        "Shrub type 1": {"trunk_length": 2, "branch_length": 2, "branch_amount": 5, "branch_curve": 3, "fork_amount": 2, "leaf_density": 6, "leaf_color": 2, "trunk_color": 3, "width_taper": 2, "length_taper": 3},
        "Shrub type 2": {"trunk_length": 3, "branch_length": 3, "branch_amount": 6, "branch_curve": 4, "fork_amount": 3, "leaf_density": 7, "leaf_color": 3, "trunk_color": 4, "width_taper": 3, "length_taper": 4},
    },
}


def select_algorithm(selection):
    print("Selected Algorithm: ", selection)
    
    # Get the information for the selected algorithm
    algorithm_info = algorithm_parameters[selection]

    # Get the arguments for the selected algorithm
    arguments = algorithm_info["arguments"]

    # Clear all current sliders
    for widget in left_frame.winfo_children():
        widget.destroy()

    # Create new sliders for each argument
    for argument, info in arguments.items():
        create_slider(left_frame, argument, info["range"], info["default"])


# Initialize root window
root = tk.Tk()
root.geometry("1706x960")
root.configure(bg='black')
root.title("3D Pixel Art Tree Generator")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a variable for holding the dropdown selection
algorithm_var = tk.StringVar(root)

# Set the default value
algorithm_var.set(list(algorithm_parameters.keys())[0])

# Initialize frames
parent_frame = tk.Frame(root, bg='black')
parent_frame.grid(row=1, column=0, sticky='nsew')  # Adjust the row index to 1
parent_frame.grid_rowconfigure(0, weight=1)
parent_frame.grid_rowconfigure(1, weight=1)
parent_frame.grid_columnconfigure(0, weight=1)
parent_frame.grid_columnconfigure(1, weight=1)
parent_frame.grid_columnconfigure(2, weight=1)
parent_frame.grid_columnconfigure(3, weight=1)

far_left_frame = tk.Frame(parent_frame, bg='sky blue')
far_left_frame.grid(row=0, column=0, sticky='nsew')

# Create radio buttons for each algorithm
for idx, algorithm in enumerate(algorithm_parameters):
    rb = tk.Radiobutton(far_left_frame, text=algorithm, variable=algorithm_var, value=algorithm, command=select_algorithm)    
    rb.grid(row=idx+2, column=0, sticky='nsew')  # Adjust the row index to 2
    
left_frame = tk.Frame(parent_frame, bg='black')
left_frame.grid(row=0, column=1, sticky='nsew')

center_frame = tk.Frame(parent_frame, bg='black')
center_frame.grid(row=0, column=2, sticky='nsew')

right_frame = tk.Frame(parent_frame, bg='black')
right_frame.grid(row=0, column=3, sticky='nsew')

bottom_frame = tk.Frame(parent_frame, bg='black')
bottom_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')

title_label = ttk.Label(far_left_frame, text="3D Pixel\nArt Tree\nGenerator", background='sky blue', foreground='black', font=("Helvetica", 14))
title_label.grid(row=0, column=0, pady=10, padx=15, sticky='w')



# Create the Treeview widget
treeview = ttk.Treeview(far_left_frame)

def on_treeview_select(event=None):
    selected_item_id = treeview.focus()  # Get the id of the selected item
    selected_item = treeview.item(selected_item_id)  # Get the item's data
    parent_id = treeview.parent(selected_item_id)  # Get the id of the parent item
    parent_item = treeview.item(parent_id)  # Get the parent item's data

    if parent_item['text'] in tree_presets and selected_item['text'] in tree_presets[parent_item['text']]:
        regen_tree()  # Regenerate the tree with the updated preset parameters

# Populate the Treeview with preset types and tree types
for preset_type in tree_presets:
    parent = treeview.insert('', 'end', text=preset_type)  # Add the preset type as a parent node
    for tree_type in tree_presets[preset_type]:
        treeview.insert(parent, 'end', text=tree_type)  # Add tree types as children of the parent node

treeview.bind('<<TreeviewSelect>>', on_treeview_select)  # Bind a function to selection of an item in the Treeview
treeview.grid(pady=10)

# Pack the treeview to the window
treeview.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

# Set up ttk style
style = ttk.Style()
style.theme_use("clam")
style.configure("TScale", background='black', foreground='white', troughcolor='black')
style.configure("TCheckbutton", background='black', foreground='white')
style.configure("TButton", background='black', foreground='white')
style.configure("TLabel", background='black', foreground='white')

# Define a BooleanVar for the checkbutton
theme_var = tk.BooleanVar()
theme_var.set(True)  # Start in dark mode

# Theme switcher function
def switch_theme(*args):
    theme = 'black' if theme_var.get() else 'SystemButtonFace'
    style.configure("TCheckbutton", background=theme, foreground='white')
    style.configure("TButton", background=theme, foreground='white')
    style.configure("TLabel", background=theme, foreground='white')
    style.configure("TScale", background=theme, foreground='white', troughcolor=theme)
    root.configure(bg=theme)
    #redraw_plot('white' if theme == 'black' else 'black')
"""
# Theme checkbutton
theme_label = ttk.Label(right_frame, text="View mode")
theme_label.pack(anchor='ne', padx=10, pady=(10, 1))
theme_checkbutton = ttk.Checkbutton(right_frame, text="Dark mode", variable=theme_var, style="TCheckbutton")
theme_checkbutton.pack(anchor='ne', padx=10, pady=(1, 10))
theme_var.trace('w', switch_theme)  # Call switch_theme when theme_var changes
"""
# Plot creation
plt.style.use('dark_background')

fig = plt.figure(figsize=(6.4, 4.8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter([1, 2, 3], [1, 2, 3], [1, 2, 3])

ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(color='white', linestyle='-', linewidth=0.3)

canvas = FigureCanvasTkAgg(fig, master=center_frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Rotation controls
rotation_frame = tk.Frame(bottom_frame, bg='black')
rotation_frame.pack(side=tk.LEFT, padx=10, pady=10)

elevation_label = ttk.Label(rotation_frame, text="Elevation")
elevation_label.grid(row=0, column=0, padx=10, pady=10)
elevation_slider = ttk.Scale(rotation_frame, from_=0, to=180, command=lambda _: update_view(elevation_slider.get(), azimuth_slider.get()))
elevation_slider.grid(row=1, column=0, padx=10, pady=10)

azimuth_label = ttk.Label(rotation_frame, text="Azimuth", background='black', foreground='white')
azimuth_label.grid(row=0, column=1, padx=10, pady=10)
azimuth_slider = ttk.Scale(rotation_frame, from_=0, to=360, command=lambda _: update_view(elevation_slider.get(), azimuth_slider.get()))
azimuth_slider.grid(row=1, column=1, padx=10, pady=10)

def get_parameters():
    parameters = {}
    for name, (slider, _, slider_value, _) in slider_locks.items():
        parameters[name] = slider_value.get()
    return parameters

def randomize_tree(event=None):
    for name, (slider, _, slider_value, _) in slider_locks.items():
        min_val, max_val = slider.configure('from')[4], slider.configure('to')[4]
        slider.set(random.uniform(min_val, max_val))
    regen_tree()

def generate_tree():
    # Get the selected algorithm from the algorithm_var
    algorithm = algorithm_var.get()

    # Get the parameters from the sliders
    parameters = {}
    for name, (slider, _, slider_value, _) in slider_locks.items():
        parameters[name] = slider_value.get()

    # Call the appropriate tree generation function with the parameters
    tree = algorithm_parameters[algorithm]['function'](**parameters)

    return tree



def regen_tree(event=None):
    global sliders
    # Extract the current values of the sliders
    slider_values = {name: slider.get() for name, slider in sliders.items()}

    # Call your tree generation function with **slider_values to unpack the dictionary as arguments
    tree = generate_tree(**slider_values)

    # Clear the existing plot
    ax.clear()

    # Create a 3D scatter plot of the tree
    x, y, z = np.where(tree == 1)  # Assume the tree is a 3D numpy array where 1 represents tree and 0 represents empty space
    ax.scatter(x, y, z)

    # Redraw the canvas
    canvas.draw()

def save_tree(event):
    # Implement your PNG saving functionality here
    pass

# Set up a dark theme for ttk widgets
style = ttk.Style()
style.theme_use("clam")
style.configure("TScale", background='black', foreground='white', troughcolor='black')
style.configure("TCheckbutton", background='black', foreground='white')
style.configure("TButton", background='black', foreground='white')

# Create a dictionary to store the slider lock states
slider_locks = {}
# Create the sliders using the argument dictionary and store them in a dictionary
sliders = {}
# Create a checkbox for regen on change
regen_var = tk.BooleanVar()
regen_var.set(True)  # Start with regen on change enabled

def regen_check(*args):
    # If regen on change is enabled, regenerate the tree whenever a slider changes
    if regen_var.get():
        regen_tree()

def update_slider(name, val):
    global ignore_update
    # Check if the slider exists in the slider_locks dictionary
    if name in slider_locks and not ignore_update:  
        slider, lock_var, slider_value, display_value = slider_locks[name]
        if not lock_var.get():  # If the slider is not locked
            display_value.set(f'{val.get():.2f}')  # Update the display value
            regen_check()  # Check if regen is enabled and regenerate tree if it is
        else:  # If the slider is locked
            ignore_update = True  # Set ignore_update to True to avoid an infinite loop
            slider.set(float(display_value.get()))  # Reset the slider value
            ignore_update = False  # Reset ignore_update to False
    
# Function for creating sliders
def create_slider(parent, text, range_, default):
    frame = ttk.Frame(parent, style='Black.TFrame')  # Create a new frame with black background
    frame.pack(fill='x', pady=(5, 10))  # Add padding around the frame

    frame.grid_columnconfigure(1, minsize=120)  # Set minimum width for the second column

    # Create a label
    label = ttk.Label(frame, text=text, background='black', foreground='white')
    label.grid(row=0, column=0, columnspan=3, sticky='w')  # Left-align the label

    # Create a DoubleVar for slider value and a trace
    slider_value = tk.DoubleVar()
    slider_value.trace('w', lambda *args: update_slider(text, slider_value))
    slider_value.trace('w', lambda *args: regen_check())

    # Create a StringVar for the displayed value and a trace
    display_value = tk.StringVar()
    display_value.trace('w', lambda *args: update_entry(text, display_value))

    # Create a slider
    slider = ttk.Scale(frame, from_=range_[0], to=range_[1], orient='horizontal', variable=slider_value)
    slider.set(default)  # Set the default value
    slider.grid(row=1, column=0, columnspan=3, sticky='w', padx=5)

    # Create a lock check button
    lock_var = tk.BooleanVar()
    lock_checkbox = ttk.Checkbutton(frame, text="🔒", variable=lock_var, style="TCheckbutton")
    lock_checkbox.grid(row=2, column=0, sticky='w')

    # Create an Entry that shows the slider value
    slider_value_entry = ttk.Entry(frame, textvariable=display_value, width=5)
    slider_value_entry.grid(row=2, column=1, sticky='w')

    # Store the slider, lock_var, slider_value, and display_value in the dictionary
    slider_locks[text] = (slider, lock_var, slider_value, display_value)

    # Update the slider value display initially
    update_slider(text, slider_value)

    return slider

def update_entry(text, display_value):
    # Check if the slider exists in the slider_locks dictionary
    if text in slider_locks:  
        # Get the slider, lock_var, slider_value, and display_value from the dictionary
        slider, lock_var, slider_value, _ = slider_locks[text]
        if not lock_var.get():  # If the checkbox is not checked
            try:
                new_val = float(display_value.get())
                if 1 <= new_val <= 10:
                    slider_value.set(new_val)
            except ValueError:
                pass


        
# Define a new style
style = ttk.Style()
style.configure('Black.TFrame', background='black')

def update_color_display():
    # Get the RGB values from the sliders
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()

    # Convert the separate RGB values to a single color value
    color = "#{:02x}{:02x}{:02x}".format(int(red), int(green), int(blue))

    # Update the color display
    color_display.config(bg=color)

# Create the RGB sliders
red_slider = create_slider(left_frame, "Red", (0, 255), 0)
green_slider = create_slider(left_frame, "Green", (0, 255), 128)
blue_slider = create_slider(left_frame, "Blue", (0, 255), 0)

# Create a label to display the color
color_display = tk.Label(root, text="Color")
color_display.grid()

# Set the callback function for the RGB sliders
red_slider.config(command=update_color_display)
green_slider.config(command=update_color_display)
blue_slider.config(command=update_color_display)

# Update the color display initially
update_color_display()

        
# Function to get the calling widget
def _get_caller(depth=2):
    """Return the widget that called the function"""
    frm = sys._getframe(depth)
    code = frm.f_code
    if code.co_name != "callit":
        return
    self = frm.f_locals['self']
    try:
        if self.tk.call("info", "commands", self._name):
            return self
    except tk.TclError:
        pass

tk.Widget._get_caller = _get_caller  # Add the function as a method to tk.Widget

# Get the arguments for the Generate Recursive Tree algorithm
arguments = algorithm_parameters["Generate Recursive Tree"]["arguments"]

for argument_name, argument_data in arguments.items():
    sliders[argument_name] = create_slider(left_frame, argument_name, argument_data["range"], argument_data["default"])

# Update function
def update_preset_tree(preset):
    # Check that preset is a dictionary with expected keys
    if not isinstance(preset, dict):
        raise TypeError("Preset must be a dictionary.")
    
    expected_keys = list(arguments.keys())
    
    if not all(key in preset for key in expected_keys):
        raise ValueError("Preset dictionary missing one or more expected keys.")
    
    # Update each slider to match the preset
    for key, value in preset.items():
        sliders[key].set(value)

def regen_tree():
    # Clear the existing tree.
    # This will depend on how your tree is drawn.
    # For example, if you're using a matplotlib plot, you might use plt.clf()

    # Recalculate the tree data.
    # This will depend on how your tree data is represented.
    # If it's a simple data structure like a list or dictionary, you might simply iterate over it and update the values.

    # Redraw the tree.
    # Again, this will depend on how your tree is drawn.
    # If you're using a matplotlib plot, you might use plt.plot()
    pass

regen_on_change = ttk.Checkbutton(left_frame, text="Regen on Change", variable=regen_var)
regen_on_change.pack(anchor='w', pady=10)  # Added pady=10 to add space around the widget, anchor='w' for left justification

# Create buttons in the bottom frame
buttons_frame = tk.Frame(bottom_frame, bg='black')
buttons_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Create buttons in the buttons_frame
regen_button = ttk.Button(buttons_frame, text="Regen")
regen_button.pack(pady=(10, 5))  # grid's pady option adds padding above and below the button
regen_button.bind("<Button-1>", regen_tree)

random_button = ttk.Button(buttons_frame, text="Randomize")
random_button.pack(pady=(10, 5))
random_button.bind("<Button-1>", randomize_tree)

save_button = ttk.Button(buttons_frame, text="Save")
save_button.pack(pady=(10, 5))
save_button.bind("<Button-1>", save_tree)

root.mainloop()