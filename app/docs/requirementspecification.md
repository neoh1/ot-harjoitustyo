# Software Requirements Specification

## deepLearning GUI
The program was designed to ease the use and training of deep learning networks.
The template network can be optimized and trained. System utilization and state of training can be tracked.
 

## Users
The program only requires normal users, but the user must have rights to operate Docker, and internet access.
(If GUI via docker turns out to be too timeconsuming to implement, the program will simply run without docker in conda environment)

## GUI draft
- Options: Selection of models to be trained. 
- Input for data open-folder-button. 
- Progressbars for training. 
- Options for training. 
- Refreshing statistics for system utilization.
- Refreshing statistics for training.
- Stylish looking using some premade-theme. 
  - Close-resize-minimize-buttons. 
  - Make left-navigator smaller via animation. 
- Help-section for program usage. 
- Multiple model training possibilities, if system allows (free GPU, and non-throttling CPU etc.).
- Continuing training of pretrained models. 
- Minor adjustment possibilities like switching optimizers. 
  - Or possibility to quickly adjust settings in a 'training_settings.yaml' file.

## Software Requirements
Docker. Ubuntu 20.04 LTS or Windows 10+. The Docker container will run:
```sh
> python 3.10, and its modules
> Nvidia drivers and CUDA, most likely Ubuntu based.
> x11 for GUI implementation via Docker
```

## Hardware requirements 
Minimum requirements:
```
A modern CPU able to run aforementioned Operating Systems.
At least 5 GB of harddisk space and 12 GB of RAM
```
Recommended requirements:
```
Modern multicore processors, with a lot of RAM and multiple modern NVIDIA GPUs.
```
## Future development ideas

- Multiple user accounts.
- More optimized data handling.
- Website backend and frontend
- Tracking training adjustments effect on training visually
- Cloud support

