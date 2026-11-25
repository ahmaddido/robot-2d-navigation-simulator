# 2D Robot Navigation Simulator

### A Python-Based Robot Movement and Obstacle Detection Project

## Project Overview

The 2D Robot Navigation Simulator is a Python project that simulates the movement of a mobile robot in a 2D grid environment. The robot can move forward, rotate, detect obstacles, avoid grid boundaries, and track its movement history.

The main purpose of this project is to strengthen my Python programming fundamentals while refreshing concepts in robotics, including robot localization, orientation, navigation, and obstacle avoidance.

The robot operates inside a imaginary 7 × 7 grid with the following configuration:

| Parameter | Value |
|---|---|
| Starting position | (3, 3) |
| Starting orientation | NORTH |
| Grid boundaries | X: 0–6, Y: 0–6 |
| Obstacle locations | (3, 5), (5, 3), (1, 2) |

The environment is represented logically using Python data structures. No graphical interface or physical robot is required.

## Available Commands

| Command | Description |
|---|---|
| `FORWARD 3` | Attempt to move three cells forward |
| `LEFT` | Rotate 90° counterclockwise |
| `RIGHT` | Rotate 90° clockwise |
| `STATUS` | Display current position and orientation |
| `DONE` | End the simulation and display results |

The robot checks every cell before moving into it. If an obstacle or boundary is detected, the movement is interrupted and the robot remains at the last valid position.

## Project Structure

- `main.py` — Handles user commands, robot movement, orientation, and simulation reporting.
- `data.py` — Contains initial robot configuration, command validation, obstacle checking, and boundary validation.


## Development and Authorship

This project was developed by me as a hands-on Python programming exercise. I personally worked through the implementation, debugging, and integration of the robot simulator. AI-assisted explanations and code review were used as learning resources during development.
