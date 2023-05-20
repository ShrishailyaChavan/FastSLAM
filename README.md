
# FastSLAM - Python Simulation

Welcome to the FastSLAM Python simulation! This project provides a comprehensive implementation of both FastSLAM 1.0 and 2.0. FastSLAM is a popular approach for solving the Simultaneous Localization and Mapping (SLAM) problem, which is essential in mobile robotics.

## Install Dependencies

It's recommended to create a new Python virtual environment for this project. You can install all the necessary packages by running:
Using a new virtual env to install the packages:

`pip install -r requirements.txt`

## Run Simulation
To execute the simulation, use the following commands:
1. For FastSLAM 1.0:
`python Fast_Slam.py`

2. For FastSLAM 2.0:
`python Fast_Slam2.py`

## Interacting with the Simulation

### Control
You can navigate the robot within the simulation using the arrow keys. You can adjust the number of steps the robot moves per key press in the **'Fast_Slam.py'** script.

### Sensor Configuration
Our virtual world is currently set up with 4 landmarks, which the robot uses to estimate its location and the map of the environment. You can add or modify these landmarks in the **'world.py'** file in the **'setup_world'** method.

The **'sense'** method in the **'particle.py'** file enables the robot to observe landmarks. At each step, it randomly chooses 2 landmarks and measures the distance and direction to them, with Gaussian noise added to simulate real-world measurement noise.

## Noise Settings

This simulation includes various types of noise to mimic real-world uncertainties:

1. **Bearing Noise:** Represents angular measurement errors.
2. **Distance Noise:** Represents distance measurement errors.
3. **Control Noise:** Models the uncertainty in the robot's movement.

The noise levels can be adjusted in the **'set_noise'** method in the **'particle.py'** file. The **'obs_noise'** attribute, an important part of the prediction step of the EKF, can also be tuned to adjust the model's tolerance for data association.

## Output

![Output of FastSLAM 1.0](https://github.com/ShrishailyaChavan/FastSLAM/blob/main/Output/FastSLAM.png)

## Souce of the Implementation
[fastSLAM paper](https://www.ri.cmu.edu/pub_files/pub4/montemerlo_michael_2003_1/montemerlo_michael_2003_1.pdf)
