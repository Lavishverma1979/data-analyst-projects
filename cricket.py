import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample cricket player dataset
data = {
    'Player': ['Virat Kohli', 'Rohit Sharma', 'Sachin Tendulkar', 'MS Dhoni', 'Jacques Kallis'],
    'Matches Played': [254, 227, 200, 350, 319],
    'Runs Scored': [12169, 9200, 18426, 10773, 11579],
    'Average': [59.07, 48.96, 44.83, 50.23, 55.37],
    'Strike Rate': [93.17, 98.24, 86.52, 87.56, 76.31]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Function to show the DataFrame
def show_dataframe():
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, df.to_string())

# Function to show basic statistics
def show_statistics():
    stats = df.describe()
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, stats.to_string())

# Function to plot a bar chart of Runs Scored vs Matches Played
def plot_runs_vs_matches():
    plt.figure(figsize=(8, 4))
    sns.barplot(x='Player', y='Runs Scored', data=df)
    plt.title('Runs Scored by Players')
    plt.xlabel('Player')
    plt.ylabel('Runs Scored')
    
    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.get_tk_widget().pack()
    canvas.draw()

# Function to plot a box plot for player averages
def plot_averages():
    plt.figure(figsize=(8,4))
    sns.barplot(x='Player',y='Average', data=df)
    plt.title('Player Batting Averages')
    
    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.get_tk_widget().pack()
    canvas.draw()

# Function to clear the plot from the screen
def clear_plot():
    for widget in window.winfo_children():
        widget.pack_forget()
    # Re-pack the buttons and text box
    button_show_df.pack(pady=5)
    button_show_stats.pack(pady=5)
    button_plot_runs.pack(pady=5)
    button_plot_avg.pack(pady=5)
    button_clear_plot.pack(pady=5)
    text_box.pack(padx=10, pady=10)

# GUI Setup
window = tk.Tk()
window.title("Cricket Player Data Analysis")
window.geometry("800x600")

# Text box for displaying data or stats
text_box = tk.Text(window, wrap=tk.WORD, height=15, width=80)
text_box.pack(padx=10, pady=10)

# Buttons for different actions
button_show_df = tk.Button(window, text="Show DataFrame", command=show_dataframe)
button_show_df.pack(pady=5)

button_show_stats = tk.Button(window, text="Show Statistics", command=show_statistics)
button_show_stats.pack(pady=5)

button_plot_runs = tk.Button(window, text="Plot Runs Scored by Players", command=plot_runs_vs_matches)
button_plot_runs.pack(pady=5)

button_plot_avg = tk.Button(window, text="Plot Batting Averages", command=plot_averages)
button_plot_avg.pack(pady=5)

button_clear_plot = tk.Button(window, text="Clear Plot", command=clear_plot)
button_clear_plot.pack(pady=5)

# Start the Tkinter event loop
window.mainloop()
