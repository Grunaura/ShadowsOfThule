#generateTreeTwo.py

from PIL import Image, ImageDraw

# Image size
width = 200
height = 200

# Define the trunk of the tree
trunk_height = 50
trunk_width = 10

# Define the tree color
tree_color = (34, 139, 34) # Green
trunk_color = (139,69,19) # Brown

# Create a new image with white background
img = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Draw the trunk
draw.rectangle(
    [(width // 2 - trunk_width // 2, height - trunk_height), 
     (width // 2 + trunk_width // 2, height)], 
    fill=trunk_color
)

# Draw the tree
for i in range(height - trunk_height, 0, -1):
    color = tree_color
    start = width // 2 - i
    end = width // 2 + i
    draw.line([(start, i), (end, i)], fill=color)

# Save the image
img.save('pixel_tree.png')
