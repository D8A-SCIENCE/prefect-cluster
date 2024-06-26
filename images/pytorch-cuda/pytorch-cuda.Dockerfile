# Use an official Python runtime as a parent image
FROM pytorch/pytorch:1.7.1-cuda11.0-cudnn8-devel

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y apt-transport-https

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    curl \
    git \
    git-lfs 

# Install and configure kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    kubectl version --client

# Install Prefect 2
RUN pip install prefect-kubernetes

# Copy the current directory contents into the container at /app
ADD . /app

# Run when the container launches
CMD ["prefect", "version"]

