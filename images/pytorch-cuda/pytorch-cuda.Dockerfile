# Use an official Python runtime as a parent image
FROM pytorch/pytorch:1.7.1-cuda11.0-cudnn8-devel

# Set the working directory in the container
WORKDIR /app

# Install Prefect 2
RUN pip install prefect prefect-kubernetes

# Copy the current directory contents into the container at /app
ADD . /app

# Run when the container launches
CMD ["prefect", "version"]

