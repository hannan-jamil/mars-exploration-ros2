FROM osrf/ros:humble-desktop

ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]

# Install required tools
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    git \
    nano \
    vim \
    x11-apps \
    mesa-utils \
    && rm -rf /var/lib/apt/lists/*

# Initialize rosdep (ignore if already initialized)
RUN rosdep init || true
RUN rosdep update

WORKDIR /mars_ws

CMD ["bash"]
