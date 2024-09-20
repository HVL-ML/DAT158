import itertools
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

    
# Modified from A. Geron
def plot_decision_boundary(clf, X, y, legend=False, plot_training=True, ax=None, figsize=(10,6)):
        
    if not ax: f, ax = plt.subplots(figsize=figsize)
    
    # Convert to numpy arrays in case X and y are data frames
    X, y = np.array(X), np.array(y)

    x1 = X[:,0] # First feature
    x2 = X[:, 1] # Second feature
    
    
    x1s = np.linspace(np.min(x1)-0.1*np.mean(x1), 1.1*np.max(x1), 100)
    x2s = np.linspace(np.min(x2)-0.1*np.mean(x2), 1.1*np.max(x2), 100)
    x1, x2 = np.meshgrid(x1s, x2s)
    X_new = np.c_[x1.ravel(), x2.ravel()]
    
    y_pred = clf.predict(X_new).reshape(x1.shape)
    
    custom_cmap = ListedColormap(['#fafab0','#9898ff','#a0faa0'])
    ax.contourf(x1, x2, y_pred, alpha=0.3, cmap=custom_cmap)

    custom_cmap2 = ListedColormap(['#7d7d58','#4c4c7f','#507d50'])
    ax.contour(x1, x2, y_pred, cmap=custom_cmap2, alpha=0.8)
    
    dots = ["yo", "bs", "g^"]
    
    if plot_training:
        for i in np.unique(y):
            
            ax.plot(X[:, 0][y==i], X[:, 1][y==i], dots[i], label=str(i))
    
    else:
        ax.set_xlabel(r"$x_1$", fontsize=18)
        ax.set_ylabel(r"$x_2$", fontsize=18, rotation=0)
    ax.legend(loc="lower right", fontsize=14)
    ax.set_title("Decision boundary")
    
    return ax