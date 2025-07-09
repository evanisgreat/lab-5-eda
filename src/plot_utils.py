import matplotlib.pyplot as plt

def plot_hist(df, col, bins=20):
    df[col].hist(bins=bins, align='left', rwidth=0.8)
    plt.title(col + ' distribution')
    return plt.axes([0.1, 0.1, 0.8, 0.8]) 