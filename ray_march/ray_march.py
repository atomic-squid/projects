"""
# The goal of this project is to generate a raymarching engine that can render 3D primatives and their
# CSG operations. I will implemnent any features that I cannot find in the standard libraries.
"""

from tkinter import *
from tkinter import ttk

# Hardcoded camera transformation matrix
camera_matrix = [
    [1.071111, 0.0, 0.0, 0.0],
    [0.0, 1.428148, 0.0, 0.0],
    [0.0, 0.0, -1.002002, 4.004004],
    [0.0, 0.0, -1.0, 2.0]
]

print("Camera Transformation Matrix:")
for row in camera_matrix:
    print(row)

root = Tk()
root.title("Ray March")

# canvas
cnv = Canvas(root, width=800, height=600, bg="black")
cnv.pack()


root.mainloop()
