import tkinter as tk
from tkinter import messagebox
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the Penguins dataset
df = sns.load_dataset("penguins")

# Function to show the DataFrame
def show_dataframe():
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, df.to_string())

# Function to show basic statistics
def show_statistics():
    stats = df.describe()
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, stats.to_string())

# Function to show a simple plot of the dataset (e.g., Species vs Bill Length)
def plot_data():
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='species', y='bill_length_mm', data=df)
    plt.title('Bill Length by Species')
    
    # Convert plot to Tkinter Canvas
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
    button_plot_data.pack(pady=5)
    button_clear_plot.pack(pady=5)
    text_box.pack(padx=10, pady=10)

# GUI Setup
window = tk.Tk()
window.title("Penguins Data Analysis")
window.geometry("800x600")

# Text box for displaying data or stats
text_box = tk.Text(window, wrap=tk.WORD, height=15, width=80)
text_box.pack(padx=10, pady=10)

# Buttons for different actions
button_show_df = tk.Button(window, text="Show DataFrame", command=show_dataframe)
button_show_df.pack(pady=5)

button_show_stats = tk.Button(window, text="Show Statistics", command=show_statistics)
button_show_stats.pack(pady=5)

button_plot_data = tk.Button(window, text="Plot Bill Length by Species", command=plot_data)
button_plot_data.pack(pady=5)

button_clear_plot = tk.Button(window, text="Clear Plot", command=clear_plot)
button_clear_plot.pack(pady=5)

# Start the Tkinter event loop
window.mainloop()
