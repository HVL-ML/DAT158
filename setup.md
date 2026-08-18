# Set up your computer for DAT158

To get the most out of the DAT158 machine learning course, you might want to set up the course material on your personal computer. Follow the steps below to install Python and the necessary Python libraries. 

> Note that you can also work with the course material in the cloud using [Google Colab](https://colab.research.google.com/) or [Kaggle Code](https://www.kaggle.com/code) or similar services.

## For Mac users: Installing Xcode

If you are a MacOS user:

1. You might need **Xcode**, which is a free development tool. [Download it here](https://developer.apple.com/xcode/resources/).
2. To install, open `terminal.app`:
   - Press `CMD+SPACE` and search for Terminal.
   - In the terminal, run `xcode-select --install`.

## Step 1: Set up Python

There are a bunch of ways to set up a Python environment, and you can use any AI tool to explain you how to do it on your specific system. From the point of view of the course, we don't care too much on how you do it, as long as you are able to run the notebooks. Below, we suggest to use Anaconda since it works the same way on all platforms/OSes, but if you already know a bit about what you are doing, you can also choose to

- Use the Python installation already present on your computer
- Install Python and the required packages using [`uv`](https://docs.astral.sh/uv/)
- Run Python in a Docker container, to avoid having to install anything. Have a look at the `Dockerfile` in this repo.

If instead of the options above you just want something that works out of the box, the recommended way to install Python for this course is via the [Anaconda Distribution](https://www.anaconda.com/products/distribution#Downloads). It comes with the Conda Package Management System.

> From the [documentation](https://conda.io/docs): _"Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer."_

After you've installed Anaconda:

1. Open a terminal (or "Anaconda Prompt" for Windows users).
2. Run `python --version`.
3. Ensure the output mentions "Anaconda". If so, proceed to the next step.

Now you're ready to get the course environment up and running.

After you have Anaconda set up, follow these steps (Windows users, stick with the "Anaconda Prompt"):

## Step 2: Install Git

1. Open a terminal (or "Anaconda Prompt" for Windows users).
2. Test if you have `git` installed. If not, run `conda install git`.

    
## Step 3: Clone the course repository

1. Run `git clone https://github.com/HVL-ML/DAT158`.
2. Change to the course directory by running `cd DAT158`.



## Step 4: Set up the Python environment

1. Make sure that you're in the course directory. If not, run `cd DAT158`.
2. Run `conda env update --file environment.yml`. The `environment.yml` lists the libraries we need, and you can add libraries to it if you like. 


## Step 5: Activate your environment

1. Run `conda activate dat158`.


## Step 6: Add a Jupyter kernel for the course

1. Make sure the `dat158` environment is activated. If not, run `conda activate dat158`.
2. Run `python -m ipykernel install --user --name dat158 --display-name "DAT158"`

## Step 7: Verify your installation

1. Make sure that you're in the course directory. If not, run `cd DAT158`.
2. Run `jupyter notebook` to open the test notebook located at `notebooks/0.0-test.ipynb`.
3. Alternatively, run `jupyter lab` to open the test notebook in JupyterLab.
Open the test notebook located at `notebooks/0.0-test.ipynb` using:


# Troubleshooting Tips

- **GNU/Linux or MacOS activation issue**: If `conda activate dat158` fails, try executing `source ~/.bash_profile` and repeat the activation.
- **Mac `gcc` error during environment update**: Install [Xcode](https://developer.apple.com/xcode/resources/) from the App Store and then install the **command line tools**.



# Keeping everything updated

The course materials will evolve over time. Ensure you're always up-to-date by regularly executing the following commands:

1. **Update the course materials**:
```bash	
git pull
```

2. **Update the Python environment**:
```bash
conda activate dat158
conda env update
```

