# Vegetation Management

This project contains the code for the solution to prevent forest fire by detecting the potential locations at which the trees are dangerously close to the high tension wires by analysing the video captured by the drone.

## Problem Statement
- Maintaining appropriate distance of tree-tops from high voltage wires.
- To ensure safe, reliable and economical electric service.

## Devised Solution
- **Segementation of Video frame** - Achieved via OpenCV python library for Image Processing.
- **Calculation of relative depth** - Storing the depth values and subtracting the corresponding values to provide relative depth values.
- **Relative Graph Depth** - Plotting the graph with the values provided and analysing the information to provide alert of dangerous situations. Achieved via CanvasJS.
