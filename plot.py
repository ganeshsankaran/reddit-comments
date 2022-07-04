import matplotlib.pyplot as plt
import numpy as np

def save_histogram_as_png(xdata, id, xlabel):
    plt.figure()
    plt.hist(xdata)
    plt.yscale('log')
    plt.xlabel(xlabel)
    plt.ylabel('Count')
    plt.title(f'{id}: {xlabel}s of Comments')
    plt.savefig(f'{id}_{xlabel}.png')

def save_scatter_as_png(xdata, ydata, xlabel, ylabel):
    k = len(xdata)

    plt.figure()
    plt.scatter(xdata, ydata)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f'{ylabel} vs {xlabel} (size {k})')
    plt.savefig(f'{k}_{ylabel}_{xlabel}.png')