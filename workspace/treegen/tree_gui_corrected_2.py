#tree_gui.py

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
import random, sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from trees import *

ignore_update = False

# Function to update the view of the 3D plot
def update_view(elevation, azimuth):
    ax.view_init(elev=elevation, azim=azimuth)
    canvas.draw()

# Function to redraw the 3D plot with a new theme
def redraw_plot(theme, height, width, depth):
    ax.clear()
    ax.grid(color=theme, linestyle='-', linewidth=0.3)
    ax.scatter([x for x in range(1, height + 1)], [x for x in range(1, width + 1)], [x for x in range(1, depth + 1)])

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

# Define the algorithms and their arguments
algorithms = {
    "L-System": {
        "function": generate_l_system_tree,
        "arguments": {
            "start_string": "",
            "angle": 30.0,
            "distance": 100.0,
            "depth": 5,
        },
    },
    "Fractal": {
        "function": generate_fractal_tree,
        "arguments": {
            "origin": [0.0, 0.0, 0.0],
            "trunk_length": 100.0,
            "trunk_vector": [0.0, 0.0, 1.0],
            "depth": 6,
        },
    },
    "Space Colonization": {
        "function": generate_space_colonization_tree,
        "arguments": {
            # The generate_space_colonization_tree function is not implemented in the script, 
            # so it's not possible to provide the parameters at this moment. 
        },
    },
    "Biased Random Growth": {
        "function": generate_biased_random_growth_tree,
        "arguments": {
            "size": 100,
            "num_iterations": 5000,
        },
    },
    "Block Model": {
        "function": generate_block_model_tree,
        "arguments": {
            "origin": [0.0, 0.0, 0.0],
            "trunk_length": 100.0,
            "trunk_vector": [0.0, 0.0, 1.0],
            "num_branches": 3,
            "branch_angle": 45.0,
            "branch_length": 50.0,
        },
    },
    "Agent-Based Model": {
        "function": generate_agent_based_model_tree,
        "arguments": {
            "num_agents": 100,
            "max_iterations": 100,
            "attraction_strength": 0.1,
            "avoidance_strength": 0.1,
            "random_strength": 0.01,
        },
    },
    "Subdivision Model": {
        "function": generate_subdivision_tree,
        "arguments": {
            "depth": 3,
            "size": 1.0,
            "min_size": 0.1,
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
    },
    "Palm": {"trunk_length": 5, "branch_length": 7, "branch_amount": 4, "branch_curve": 5, "fork_amount": 3, "leaf_density": 7, "leaf_color": 5, "trunk_color": 4, "width_taper": 3, "length_taper": 2},
    "Shrubs": {
        "Shrub type 1": {"trunk_length": 2, "branch_length": 2, "branch_amount": 5, "branch_curve": 3, "fork_amount": 2, "leaf_density": 6, "leaf_color": 2, "trunk_color": 3, "width_taper": 2, "length_taper": 3},
        "Shrub type 2": {"trunk_length": 3, "branch_length": 3, "branch_amount": 6, "branch_curve": 4, "fork_amount": 3, "leaf_density": 7, "leaf_color": 3, "trunk_color": 4, "width_taper": 3, "length_taper": 4},
    },
}

# Define the tree generation algorithms
algorithms = ["L-System", "Fractal", "Space Colonization", "Biased Random Growth", "Block Model", "Agent-Based Model", "Subdivision"]

def select_algorithm(selection):
    print("Selected Algorithm: ", selection)

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
algorithm_var.set(algorithms[0])

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

# Create the dropdown menu
dropdown = tk.OptionMenu(far_left_frame, algorithm_var, *algorithms, command=select_algorithm)
dropdown.grid(row=1, column=0, sticky='nsew')  # Placed on `far_left_frame`, not on `root`

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
        update_preset_tree(tree_presets[parent_item['text']][selected_item['text']])
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
    redraw_plot('white' if theme == 'black' else 'black')

# Theme checkbutton
theme_label = ttk.Label(right_frame, text="View mode")
theme_label.pack(anchor='ne', padx=10, pady=(10, 1))
theme_checkbutton = ttk.Checkbutton(right_frame, text="Dark mode", variable=theme_var, style="TCheckbutton")
theme_checkbutton.pack(anchor='ne', padx=10, pady=(1, 10))
theme_var.trace('w', switch_theme)  # Call switch_theme when theme_var changes

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

def update_preset_tree(preset_parameters):
    trunk_length_slider.set(preset_parameters['trunk_length'])
    branch_length_slider.set(preset_parameters['branch_length'])
    branch_amount_slider.set(preset_parameters['branch_amount'])
    branch_curve_slider.set(preset_parameters['branch_curve'])
    fork_amount_slider.set(preset_parameters['fork_amount'])
    leaf_density_slider.set(preset_parameters['leaf_density'])
    leaf_color_slider.set(preset_parameters['leaf_color'])
    trunk_color_slider.set(preset_parameters['trunk_color'])
    width_taper_slider.set(preset_parameters['width_taper'])
    length_taper_slider.set(preset_parameters['length_taper'])

def get_parameters():
    # Implement this function to retrieve the parameters from the GUI inputs
    return {
        "trunk_length": trunk_length_slider.get(),
        "branch_length": branch_length_slider.get(),
        "branch_amount": branch_amount_slider.get(),
        "branch_curve": branch_curve_slider.get(),
        "fork_amount": fork_amount_slider.get(),
        "leaf_density": leaf_density_slider.get(),
        "leaf_color": leaf_color_slider.get(),
        "trunk_color": trunk_color_slider.get(),
        "width_taper": width_taper_slider.get(),
        "length_taper": length_taper_slider.get(),
    }

def randomize_tree(event=None):
    # Set each slider to a random value
    trunk_length_slider.set(random.randint(1, 10))
    branch_length_slider.set(random.randint(1, 10))
    branch_amount_slider.set(random.randint(1, 10))
    branch_curve_slider.set(random.randint(1, 10))
    fork_amount_slider.set(random.randint(1, 10))
    leaf_density_slider.set(random.randint(1, 10))
    leaf_color_slider.set(random.randint(1, 10))
    trunk_color_slider.set(random.randint(1, 10))
    width_taper_slider.set(random.randint(1, 10))
    length_taper_slider.set(random.randint(1, 10))

    # Regenerate the tree
    regen_tree()

def generate_tree():
    algorithm = dropdown.get()  # get selected algorithm
    parameters = get_parameters()  # get parameters from the GUI

    if algorithm in algorithms:
        algorithm_info = algorithms[algorithm]
        function = algorithm_info["function"]
        default_arguments = algorithm_info["default_arguments"]

        # Update the default arguments with the user-selected parameters
        arguments = {**default_arguments, **parameters}

        # Call the tree generation function
        tree = function(**arguments)
        # Handle the generated tree


def regen_tree(event=None):
    generate_tree()
    # Extract the current values of the sliders
    trunk_length = trunk_length_slider.get()
    branch_length = branch_length_slider.get()
    branch_amount = branch_amount_slider.get()
    branch_curve = branch_curve_slider.get()
    fork_amount = fork_amount_slider.get()
    leaf_density = leaf_density_slider.get()
    leaf_color = leaf_color_slider.get()
    trunk_color = trunk_color_slider.get()
    width_taper = width_taper_slider.get()
    length_taper = length_taper_slider.get()

    # Call your tree generation function
    tree = generate_tree(trunk_length, branch_length, branch_amount, branch_curve, fork_amount, leaf_density, leaf_color, trunk_color, width_taper, length_taper)

    # Handle the tree (e.g., display it, save it to a file, etc.)

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

def update_slider(name, val):
    global ignore_update
    if not ignore_update:  # Only run this code if ignore_update is False
        if name not in slider_locks:
            return

        if not lock_var.get():  # If the slider is not locked
            display_value.set(f'{val.get():.2f}')  # Update the display value
        else:  # If the slider is locked
            ignore_update = True  # Set ignore_update to True to avoid an infinite loop
            slider.set(float(display_value.get()))  # Reset the slider value
            ignore_update = False  # Reset ignore_update to False


def update_entry(text, display_value):
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

# Function for creating sliders
def create_slider(parent, text):
    frame = ttk.Frame(parent, style='Black.TFrame')  # Create a new frame with black background
    frame.pack(fill='x', pady=(5, 10))  # Add padding around the frame

    frame.grid_columnconfigure(1, minsize=120)  # Set minimum width for the second column

    # Create a label
    label = ttk.Label(frame, text=text, background='black', foreground='white')
    label.grid(row=0, column=0, columnspan=3, sticky='w')  # Left-align the label

    # Create a DoubleVar for slider value and a trace
    slider_value = tk.DoubleVar()
    slider_value.trace('w', lambda *args: update_slider(text, slider_value))

    # Create a StringVar for the displayed value and a trace
    display_value = tk.StringVar()
    display_value.trace('w', lambda *args: update_entry(text, display_value))

    # Create a slider
    slider = ttk.Scale(frame, from_=1, to=10, orient='horizontal', variable=slider_value)
    slider.set(random.randint(1, 10))  # Set a random initial value
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

trunk_length_slider = create_slider(left_frame, "Trunk Length")
branch_length_slider = create_slider(left_frame, "Branch Length")
branch_amount_slider = create_slider(left_frame, "Branch Amount")
branch_curve_slider = create_slider(left_frame, "Branch Curve")
fork_amount_slider = create_slider(left_frame, "Fork Amount")
leaf_density_slider = create_slider(left_frame, "Leaf Density")
leaf_color_slider = create_slider(left_frame, "Leaf Color")
trunk_color_slider = create_slider(left_frame, "Trunk Color")
width_taper_slider = create_slider(left_frame, "Width Taper")
length_taper_slider = create_slider(left_frame, "Length Taper")

# Create a checkbox for regen on change
regen_var = tk.BooleanVar()
regen_var.set(True)  # Start with regen on change enabled

def regen_check(*args):
    # If regen on change is enabled, regenerate the tree whenever a slider changes
    if regen_var.get():
        regen_tree()

regen_on_change = ttk.Checkbutton(left_frame, text="Regen on Change", variable=regen_var)
regen_on_change.pack(pady=10)  # Added pady=10 to add space around the widget

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
