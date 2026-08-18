FROM quay.io/jupyter/base-notebook:latest

# Force Jupyter to use the classic Notebook interface instead of JupyterLab
ENV DOCKER_STACKS_JUPYTER_CMD=notebook

WORKDIR /notebooks

# Install additional libraries
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt


