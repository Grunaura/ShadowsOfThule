#trees.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import turtle
import random
import noise
import math
from itertools import combinations, product

# L-system rules (now with probabilities)
rules_prob = {
    "1": [
        (0.5, "11"),  # Apply "11" with 0.5 probability
        (0.5, "1[0]1")  # Apply "1[0]1" with 0.5 probability
    ],
    "0": [
        (0.5, "1[0]0"),  # Apply "1[0]0" with 0.5 probability
        (0.5, "11")  # Apply "11" with 0.5 probability
    ],
}

# Starting string
start_string = "0"

def apply_rules(input_str):
    output = ""
    for character in input_str:
        if character in rules_prob:
            prob, replacement = random.choices(
                rules_prob[character], weights=[p for p, _ in rules_prob[character]]
            )[0]
            output += replacement
        else:
            output += character
    return output

def process_string(input_str, angle, distance, depth):
    stack = []
    for character in input_str:
        if character == "0" or character == "1":
            turtle.forward(distance)
        elif character == "[":
            stack.append((turtle.position(), turtle.heading()))
            turtle.left(angle * (1.0 + random.uniform(-0.1, 0.1)))
        elif character == "]":
            position, heading = stack.pop()
            turtle.penup()
            turtle.goto(position)
            turtle.setheading(heading)
            turtle.pendown()
            turtle.right(angle * (1.0 + random.uniform(-0.1, 0.1)))

        distance *= 0.99 - depth * 0.01

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
):
    """
    This function generates a tree using a recursive algorithm.

    Args:
    trunk_length: The length of the tree's trunk.
    branch_length: The length of the tree's branches.
    branch_amount: The amount of branches the tree has.
    branch_curve: The curvature of the tree's branches.
    fork_amount: The amount of forks the tree has.
    leaf_density: The density of the tree's leaves.
    width_taper: The tapering of the tree's width.
    length_taper: The tapering of the tree's length.
    leaf_color_red: The red component of the tree's leaf color.
    leaf_color_green: The green component of the tree's leaf color.
    leaf_color_blue: The blue component of the tree's leaf color.
    trunk_color_red: The red component of the tree's trunk color.
    trunk_color_green: The green component of the tree's trunk color.
    trunk_color_blue: The blue component of the tree's trunk color.

    Returns:
    A tree represented by a 3D numpy array.
    """
    # Initialize the tree as an empty 3D numpy array
    tree = np.zeros((100, 100, 100))

    # Use a recursive function to generate the tree
    # This function generates a branch of the tree
    def generate_branch(start_point, length, direction):
        if length <= 0:
            return

        end_point = start_point + length * direction
        tree[start_point[1]:end_point[1], start_point[1]:end_point[1], start_point[2]:end_point[2]] = 1

        for _ in range(branch_amount):
            new_direction = np.array(
                [
                    direction[0] + np.random.uniform(-branch_curve, branch_curve),
                    direction[1] + np.random.uniform(-branch_curve, branch_curve),
                    direction[2] + np.random.uniform(-branch_curve, branch_curve),
                ]
            )
            generate_branch(end_point, length * length_taper, new_direction)

    # Generate the trunk of the tree
    generate_branch(np.array([50, 50, 0]), trunk_length, np.array([0, 0, 1]))

    return tree


def generate_l_system_tree(parameters):
    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()

    start_string = parameters.get("start_string")
    angle = parameters.get("angle")
    distance = parameters.get("distance")
    depth = parameters.get("depth")

    for _ in range(depth):
        start_string = apply_rules(start_string)

    process_string(start_string, angle, distance, depth)

    turtle.done()

def generate_fractal_tree(parameters):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    origin = parameters.get("origin")
    trunk_length = parameters.get("trunk_length")
    trunk_vector = parameters.get("trunk_vector")
    depth = parameters.get("depth")

    if depth == 0:
        ax.plot(
            [origin[0], origin[0] + trunk_length * trunk_vector[0]],
            [origin[1], origin[1] + trunk_length * trunk_vector[1]],
            [origin[2], origin[2] + trunk_length * trunk_vector[2]],
            color="brown",
        )
    else:
        ax.plot(
            [origin[0], origin[0] + trunk_length * trunk_vector[0]],
            [origin[1], origin[1] + trunk_length * trunk_vector[1]],
            [origin[2], origin[2] + trunk_length * trunk_vector[2]],
            color="brown",
        )
        trunk_vector = [
            trunk_vector[0] * random.uniform(0.8, 1.2),
            trunk_vector[1] * random.uniform(0.8, 1.2),
            trunk_vector[2],
        ]
        generate_fractal_tree(
            {
                "origin": [
                    origin[0] + trunk_length * trunk_vector[0],
                    origin[1] + trunk_length * trunk_vector[1],
                    origin[2] + trunk_length * trunk_vector[2],
                ],
                "trunk_length": trunk_length / 2.0,
                "trunk_vector": [
                    trunk_vector[0] / 1.5,
                    trunk_vector[1] / 1.5,
                    trunk_vector[2] + 0.5,
                ],
                "depth": depth - 1,
            }
        )
        generate_fractal_tree(
            {
                "origin": [
                    origin[0] + trunk_length * trunk_vector[0],
                    origin[1] + trunk_length * trunk_vector[1],
                    origin[2] + trunk_length * trunk_vector[2],
                ],
                "trunk_length": trunk_length / 2.0,
                "trunk_vector": [
                    trunk_vector[0] / 1.5,
                    trunk_vector[1] / 1.5,
                    trunk_vector[2] - 0.5,
                ],
                "depth": depth - 1,
            }
        )

    plt.show()

def generate_space_colonization_tree(parameters):
    pass

def generate_biased_random_growth_tree(parameters):
    size = parameters.get("size")
    num_iterations = parameters.get("num_iterations")

    grid = np.zeros((size, size, size), dtype=bool)
    root = (size // 2, size // 2, 0)
    grid[root] = True
    frontier = [root]
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    scale = 0.1
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0

    for _ in range(num_iterations):
        voxel = random.choice(frontier)
        weights = [
            1
            + noise.pnoise3(
                voxel[0] * scale + dir[0],
                voxel[1] * scale + dir[1],
                voxel[2] * scale + dir[2],
                octaves=octaves,
                persistence=persistence,
                lacunarity=lacunarity,
                repeatx=size,
                repeaty=size,
                repeatz=size,
            )
            + (dir[2] > 0)
            for dir in directions
        ]
        weights /= np.sum(weights)
        direction = np.random.choice(directions, p=weights)
        new_voxel = (
            voxel[0] + direction[0],
            voxel[1] + direction[1],
            voxel[2] + direction[2],
        )

        if (
            0 <= new_voxel[0] < size
            and 0 <= new_voxel[1] < size
            and 0 <= new_voxel[2] < size
        ):
            if not grid[new_voxel]:
                grid[new_voxel] = True
                frontier.append(new_voxel)

    return grid

def rotate_vector(vector, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                [np.sin(theta), np.cos(theta), 0],
                                [0, 0, 1]])
    return rotation_matrix.dot(vector)

def generate_block_model_tree(parameters):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    origin = parameters.get("origin")
    trunk_length = parameters.get("trunk_length")
    trunk_vector = parameters.get("trunk_vector")
    num_branches = parameters.get("num_branches")
    branch_angle = parameters.get("branch_angle")
    branch_length = parameters.get("branch_length")

    ax.plot(
        [origin[0], origin[0] + trunk_length * trunk_vector[0]],
        [origin[1], origin[1] + trunk_length * trunk_vector[1]],
        [origin[2], origin[2] + trunk_length * trunk_vector[2]],
        color="brown",
    )

    for _ in range(num_branches):
        branch_vector = rotate_vector(trunk_vector, branch_angle)
        branch_origin = [
            origin[0] + trunk_length * trunk_vector[0],
            origin[1] + trunk_length * trunk_vector[1],
            origin[2] + trunk_length * trunk_vector[2],
        ]
        branch_end = [
            branch_origin[0] + branch_length * branch_vector[0],
            branch_origin[1] + branch_length * branch_vector[1],
            branch_origin[2] + branch_length * branch_vector[2],
        ]
        ax.plot(
            [branch_origin[0], branch_end[0]],
            [branch_origin[1], branch_end[1]],
            [branch_origin[2], branch_end[2]],
            color="green",
        )

    plt.show()

def generate_agent_based_model_tree(parameters):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    num_agents = parameters.get("num_agents")
    max_iterations = parameters.get("max_iterations")
    attraction_strength = parameters.get("attraction_strength")
    avoidance_strength = parameters.get("avoidance_strength")
    random_strength = parameters.get("random_strength")

    agents = np.random.rand(num_agents, 3)

    for _ in range(max_iterations):
        for agent in agents:
            distances = np.linalg.norm(agents - agent, axis=1)
            nearest_neighbors = np.argsort(distances)[1:]
            attraction_vector = np.mean(agents[nearest_neighbors] - agent, axis=0) * attraction_strength
            avoidance_vector = np.mean((agents[nearest_neighbors] - agent) / distances[nearest_neighbors][:, np.newaxis], axis=0) * avoidance_strength
            random_vector = np.random.rand(3) * random_strength
            agent += attraction_vector + avoidance_vector + random_vector
        ax.scatter(agents[:, 0], agents[:, 1], agents[:, 2], color="green")

    plt.show()

class Box:
    def __init__(self, center, size):
        self.center = center
        self.size = size

def subdivide_box(box, min_size):
    new_size = box.size / 2.0
    if new_size < min_size:
        return []

    x, y, z = box.center

    boxes = []
    for dx, dy, dz in product([-1, 1], repeat=3):
        center = [x + dx * new_size, y + dy * new_size, z + dz * new_size]
        boxes.append(Box(center, new_size))

    return boxes

def draw_box(ax, box):
    x, y, z = box.center
    size = box.size
    vertices = np.array(
        [
            [x - size / 2, y - size / 2, z - size / 2],
            [x - size / 2, y - size / 2, z + size / 2],
            [x - size / 2, y + size / 2, z - size / 2],
            [x - size / 2, y + size / 2, z + size / 2],
            [x + size / 2, y - size / 2, z - size / 2],
            [x + size / 2, y - size / 2, z + size / 2],
            [x + size / 2, y + size / 2, z - size / 2],
            [x + size / 2, y + size / 2, z + size / 2],
        ]
    )
    edges = [
        (0, 1),
        (0, 2),
        (0, 4),
        (1, 3),
        (1, 5),
        (2, 3),
        (2, 6),
        (3, 7),
        (4, 5),
        (4, 6),
        (5, 7),
        (6, 7),
    ]
    for edge in edges:
        ax.plot(
            [vertices[edge[0]][0], vertices[edge[1]][0]],
            [vertices[edge[0]][1], vertices[edge[1]][1]],
            [vertices[edge[0]][2], vertices[edge[1]][2]],
            color="blue",
        )

def generate_subdivision_tree(parameters):
    depth = parameters.get("depth")
    size = parameters.get("size")
    min_size = parameters.get("min_size")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    boxes = [Box([0, 0, 0], size)]
    for _ in range(depth):
        new_boxes = []
        for box in boxes:
            new_boxes.extend(subdivide_box(box, min_size))
        boxes = new_boxes
    for box in boxes:
        draw_box(ax, box)

    plt.show()

if __name__ == "__main__":
    l_system_parameters = {
        "start_string": start_string,
        "angle": 30.0,
        "distance": 100.0,
        "depth": 5,
    }
    generate_l_system_tree(l_system_parameters)

    fractal_parameters = {
        "origin": [0, 0, 0],
        "trunk_length": 1.0,
        "trunk_vector": [0, 0, 1],
        "depth": 5,
    }
    generate_fractal_tree(fractal_parameters)

    space_colonization_parameters = {}
    generate_space_colonization_tree(space_colonization_parameters)

    biased_random_growth_parameters = {
        "size": 100,
        "num_iterations": 10000,
    }
    grid = generate_biased_random_growth_tree(biased_random_growth_parameters)

    block_model_parameters = {
        "origin": [0, 0, 0],
        "trunk_length": 1.0,
        "trunk_vector": [0, 0, 1],
        "num_branches": 3,
        "branch_angle": 45.0,
        "branch_length": 0.5,
    }
    generate_block_model_tree(block_model_parameters)

    agent_based_model_parameters = {
        "num_agents": 100,
        "max_iterations": 1000,
        "attraction_strength": 0.01,
        "avoidance_strength": 0.01,
        "random_strength": 0.01,
    }
    generate_agent_based_model_tree(agent_based_model_parameters)

    subdivision_parameters = {
        "depth": 3,
        "size": 1.0,
        "min_size": 0.1,
    }
    generate_subdivision_tree(subdivision_parameters)
    
    
algorithms = {
    "Generate Recursive Tree": generate_recursive_tree,
    "L-System": generate_l_system_tree,
    "Fractal": generate_fractal_tree,
    "Space Colonization": generate_space_colonization_tree,
    "Biased Random Growth": generate_biased_random_growth_tree,
    "Block Model": generate_block_model_tree,
    "Agent-Based Model": generate_agent_based_model_tree,
    "Subdivision": generate_subdivision_tree,
}

