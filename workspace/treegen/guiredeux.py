import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import turtle
import random
import noise
import math
import sys
import inspect
from itertools import combinations, product
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk,
)

print("Script started.")

ignore_update = False


def update_view(elevation, azimuth):
    print("update_view called.")
    ax.view_init(elev=elevation, azim=azimuth)
    canvas.draw()
    print("update_view finished.")


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

print("Figure and Axes created.")


def redraw_plot_with_bounding_box(theme, height, width, depth):
    print("redraw_plot_with_bounding_box called.")
    ax.clear()
    ax.grid(color=theme, linestyle='-', linewidth=0.3)

    max_dim = max([height, width, depth])
    bounding_box_dim = int(max_dim * 1.1)  # 10% larger

    x = np.arange(0, bounding_box_dim, 2)
    y = np.arange(0, bounding_box_dim, 2)
    z = np.arange(0, bounding_box_dim, 2)
    xx, yy, zz = np.meshgrid(x, y, z)

    ax.plot_wireframe(xx, yy, zz, color='gray', linestyle='dashed', linewidth=0.5)

    ax.scatter(
        [x for x in range(1, height + 1)],
        [x for x in range(1, width + 1)],
        [x for x in range(1, depth + 1)]
    )
    print("redraw_plot_with_bounding_box finished.")


def generate_recursive_tree(
    trunk_length=1.0,
    branch_length=0.5,
    branch_amount=3,
    branch_curve=45.0,
    fork_amount=2,
    leaf_density=0.5,
    width_taper=0.8,
    length_taper=0.8,
    leaf_color_red=0,
    leaf_color_green=128,
    leaf_color_blue=0,
    trunk_color_red=165,
    trunk_color_green=42,
    trunk_color_blue=42,
    max_branches=100,  # new parameter
    max_volume=1e6,  # new parameter
    max_time=60,  # new parameter
):
    import time  # needed for the time check

    print("generate_recursive_tree started.")
    tree = np.zeros((100, 100, 100))
    MAX_RECURSION_DEPTH = 50

    start_time = time.time()  # record the start time
    num_branches = 0  # counter for the number of branches

    def generate_branch(start_point, length, direction, depth=0):
        nonlocal num_branches  # declare num_branches as nonlocal

        print(f"generate_branch called with start_point={start_point}, length={length}, direction={direction}, depth={depth}")
        
        if time.time() - start_time > max_time:
            print("generate_branch exited early due to exceeding max_time.")
            return
        if length <= 0 or depth > MAX_RECURSION_DEPTH:
            print("generate_branch exited early due to length or depth.")
            return
        if num_branches >= max_branches:
            print("generate_branch exited early due to exceeding max_branches.")
            return
        if np.sum(tree) > max_volume:
            print("generate_branch exited early due to exceeding max_volume.")
            return

        start_point = start_point.astype(int)
        end_point = (start_point + direction * length).astype(int)

        tree[start_point[0]:end_point[0], start_point[1]:end_point[1], start_point[2]:end_point[2]] = 1
        num_branches += 1  # increment the number of branches

        for _ in range(branch_amount):
            new_direction = np.array(
                [
                    direction[0] + np.random.uniform(-branch_curve, branch_curve),
                    direction[1] + np.random.uniform(-branch_curve, branch_curve),
                    direction[2] + np.random.uniform(-branch_curve, branch_curve),
                ]
            )
            print(f"Calling generate_branch recursively with end_point={end_point}, length={length * length_taper}, new_direction={new_direction}, depth={depth+1}")
            generate_branch(end_point, length * length_taper, new_direction, depth+1)

    print("Calling generate_branch for the first time.")
    generate_branch(np.array([50, 50, 0]), trunk_length, np.array([0, 0, 1]))
    print("generate_recursive_tree finished.")
    return tree


print("Function definitions finished.")


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
}

print("Algorithm parameters defined.")

root = tk.Tk()
root.title("Grid Example")

algorithm_var = tk.StringVar(root)
algorithm_var.set(list(algorithm_parameters.keys())[0])

for row in range(2):
    for col in range(4):
        label_text = f"Row {row + 1}, Column {col + 1}"
        label = tk.Label(root, text=label_text, padx=10, pady=5, relief=tk.RAISED)
        label.grid(row=row, column=col, padx=5, pady=5)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.geometry("1706x960")
root.configure(bg='black')
root.title("3D Pixel Art Tree Generator")

parent_frame = tk.Frame(root, bg='black')
parent_frame.grid(row=1, column=0, sticky='nsew')  # Adjust the row index to 1
parent_frame.grid_rowconfigure(0, weight=1)
parent_frame.grid_rowconfigure(1, weight=1)
parent_frame.grid_columnconfigure(0, weight=1)
parent_frame.grid_columnconfigure(1, weight=1)
parent_frame.grid_columnconfigure(2, weight=1)
parent_frame.grid_columnconfigure(3, weight=1)

left_frame = tk.Frame(parent_frame, bg='black')
left_frame.grid(row=0, column=1, sticky='nsew', pady=10)

center_frame = tk.Frame(parent_frame, bg='black')
center_frame.grid(row=0, column=2, sticky='nsew')

right_frame = tk.Frame(parent_frame, bg='black')
right_frame.grid(row=0, column=3, sticky='nsew')

bottom_frame = tk.Frame(parent_frame, bg='black')
bottom_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')

title_label = ttk.Label(
    left_frame,
    text="3D Pixel\nArt Tree\nGenerator",
    background='sky blue',
    foreground='black',
    font=("Helvetica", 14)
)
title_label.grid(row=0, column=0, pady=10, padx=15, sticky='w')

style = ttk.Style()
style.theme_use("clam")
style.configure("TScale", background='black', foreground='white', troughcolor='black')
style.configure("TCheckbutton", background='black', foreground='white')
style.configure("TButton", background='black', foreground='white')
style.configure("TLabel", background='black', foreground='white')

theme_var = tk.BooleanVar()
theme_var.set(True)  # Start in dark mode

plt.style.use('dark_background')

rotation_frame = tk.Frame(bottom_frame, bg='black')
rotation_frame.pack(side=tk.LEFT, padx=10, pady=10)

elevation_label = ttk.Label(rotation_frame, text="Elevation")
elevation_label.grid(row=0, column=0, padx=10, pady=10)
elevation_slider = ttk.Scale(
    rotation_frame,
    from_=0,
    to=180,
    command=lambda _: update_view(elevation_slider.get(), azimuth_slider.get())
)
elevation_slider.grid(row=1, column=0, padx=10, pady=10)

azimuth_label = ttk.Label(rotation_frame, text="Azimuth", background='black', foreground='white')
azimuth_label.grid(row=0, column=1, padx=10, pady=10)
azimuth_slider = ttk.Scale(
    rotation_frame,
    from_=0,
    to=360,
    command=lambda _: update_view(elevation_slider.get(), azimuth_slider.get())
)
azimuth_slider.grid(row=1, column=1, padx=10, pady=10)

print("Sliders created.")


def get_parameters():
    print("get_parameters called.")
    parameters = {}
    for name, (slider, _, slider_value, _) in slider_locks.items():
        parameters[name] = slider_value.get()
    print("get_parameters finished.")
    return parameters


def randomize_tree(event=None):
    print("randomize_tree called.")
    for name, (slider, _, slider_value, _) in slider_locks.items():
        min_val, max_val = slider.configure('from')[4], slider.configure('to')[4]
        slider.set(random.uniform(min_val, max_val))
    regen_tree()
    print("randomize_tree finished.")


fig = plt.figure(figsize=(6.4, 4.8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter([1, 2, 3], [1, 2, 3])

ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(color='white', linestyle='-', linewidth=0.3)

canvas = FigureCanvasTkAgg(fig, master=center_frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def generate_tree():
    print("generate_tree called.")
    algorithm = algorithm_var.get()
    parameters = {}
    for name in algorithm_parameters[algorithm]['arguments'].keys():
        if name in slider_locks:
            slider, _, slider_value, _ = slider_locks[name]
            parameters[name] = slider_value.get()

    tree = algorithm_parameters[algorithm]['function'](**parameters)

    print("generate_tree finished.")
    return tree


def plot_tree(tree):
    print("plot_tree called.")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = np.where(tree == 1)  # get the coordinates of all '1's in the tree array
    ax.scatter(x, y, z)  # plot the points at these coordinates
    plt.show()
    print("plot_tree finished.")


def regen_tree(event=None):
    print("regen_tree called.")
    slider_values = {name: slider.get() for name, slider in sliders.items()}

    tree = generate_tree(**slider_values)

    plot_tree(tree)  # plot the tree using matplotlib

    canvas.draw()
    print("regen_tree finished.")


def save_tree(event):
    """Save the tree to a PNG file."""
    pass


style = ttk.Style()
style.theme_use("clam")
style.configure("TScale", background='black', foreground='white', troughcolor='black')
style.configure("TCheckbutton", background='black', foreground='white')
style.configure("TButton", background='black', foreground='white')

slider_locks = {}
sliders = {}
regen_var = tk.BooleanVar()
regen_var.set(True)


def regen_check(*args):
    print("regen_check called.")
    if regen_var.get():
        regen_tree()
    print("regen_check finished.")


def update_slider(name, val):
    print("update_slider called.")
    global ignore_update
    if name in slider_locks and not ignore_update:
        slider, lock_var, slider_value, display_value = slider_locks[name]
        if not lock_var.get():
            display_value.set(f'{val.get():.2f}')
            regen_check()
        else:
            ignore_update = True
            slider.set(float(display_value.get()))
            ignore_update = False
    print("update_slider finished.")


def create_slider(parent, text, range_, default, index):
    print("create_slider called.")
    frame = ttk.Frame(parent, style='Black.TFrame')
    frame.grid(sticky='ew')
    parent.grid_rowconfigure(index, pad=10)
    frame.grid_columnconfigure(1, minsize=120)

    label = ttk.Label(frame, text=text, background='black', foreground='white')
    label.grid(row=0, column=0, columnspan=3, sticky='w')

    slider_value = tk.DoubleVar()
    slider_value.trace('w', lambda *args: update_slider(text, slider_value))
    slider_value.trace('w', lambda *args: regen_check())

    display_value = tk.StringVar()
    display_value.trace('w', lambda *args: update_entry(text, display_value))

    slider = ttk.Scale(frame, from_=range_[0], to=range_[1], orient='horizontal', variable=slider_value)
    slider.set(default)
    slider.grid(row=1, column=0, columnspan=3, sticky='w', padx=5)

    lock_var = tk.BooleanVar()
    lock_checkbox = ttk.Checkbutton(frame, text="🔒", variable=lock_var, style="TCheckbutton")
    lock_checkbox.grid(row=2, column=0, sticky='w')

    slider_value_entry = ttk.Entry(frame, textvariable=display_value, width=5)
    slider_value_entry.grid(row=2, column=2, sticky='e')

    slider_locks[text] = slider, lock_var, slider_value, display_value
    sliders[text] = slider
    print("create_slider finished.")


def update_entry(name, val):
    print("update_entry called.")
    global ignore_update
    if name in slider_locks and not ignore_update:
        slider, lock_var, slider_value, display_value = slider_locks[name]
        if not lock_var.get():
            try:
                slider.set(float(val.get()))
            except ValueError:
                ignore_update = True
                display_value.set(f'{slider.get():.2f}')
                ignore_update = False
            regen_check()
    print("update_entry finished.")


def update_algorithm(*args):
    print("update_algorithm called.")
    regen_tree()
    print("update_algorithm finished.")


algorithms = algorithm_parameters.keys()

algorithm_optionmenu = ttk.OptionMenu(
    left_frame,
    algorithm_var,
    algorithm_var.get(),
    *algorithms,
    command=lambda _: update_algorithm()
)
algorithm_optionmenu.grid(row=1, column=0, padx=15, pady=10)

for i, (name, param) in enumerate(algorithm_parameters[algorithm_var.get()]['arguments'].items()):
    create_slider(left_frame, name, param['range'], param['default'], i + 2)

regen_on_change_checkbutton = ttk.Checkbutton(
    left_frame,
    text="Regen on change",
    variable=regen_var,
    style="TCheckbutton"
)
regen_on_change_checkbutton.grid(row=14, column=0, sticky='w', padx=15, pady=10)

randomize_button = ttk.Button(
    left_frame,
    text="Randomize",
    command=randomize_tree,
    style="TButton"
)
randomize_button.grid(row=15, column=0, sticky='w', padx=15, pady=10)

generate_button = ttk.Button(
    left_frame,
    text="Generate",
    command=regen_tree,
    style="TButton"
)
generate_button.grid(row=16, column=0, sticky='w', padx=15, pady=10)

save_button = ttk.Button(
    left_frame,
    text="Save as PNG",
    command=save_tree,
    style="TButton"
)
save_button.grid(row=17, column=0, sticky='w', padx=15, pady=10)

root.mainloop()

print("Script finished.")
