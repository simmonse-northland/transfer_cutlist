import tkinter as tk
import os
import subprocess
import time
import shutil

new_orders=r'H:\test_data\unprocessed'
processed_orders=r'H:\test_data\processed'

def get_cutlist(source_dir):
    cutlist = []
    for filename in os.listdir(source_dir):
        if filename.endswith('.csv'):
            basename = os.path.basename(filename)
            cutlist.append(basename)
            cutlist = sorted(cutlist, reverse=True)
    return cutlist[:10]


def draw_buttons(cutlist, column):
    for row, item in enumerate(cutlist):
        filename = os.path.join(new_orders if item in new_orders_cutlist else processed_orders, item)
        if os.path.isfile(filename):
            button = tk.Button(root, text=item, command=lambda item=item: button_click(item))
            button.grid(row=row+1, column=column, sticky="w", padx=10, pady=5)


def draw_headers():
    new_orders_label = tk.Label(root, text="New Orders")
    new_orders_label.grid(row=0, column=0, padx=10, pady=5)

    processed_orders_label = tk.Label(root, text="Processed Orders")
    processed_orders_label.grid(row=0, column=1, padx=10, pady=5)

def button_click(item):
    global new_orders_cutlist, processed_orders_cutlist
    # Delete the file from the source directory
    source_filename = os.path.join(new_orders, item)
    destination_filename = os.path.join(processed_orders, item)
    shutil.move(source_filename, destination_filename)
    os.utime(destination_filename, (time.time(), time.time()))
    os.startfile(destination_filename)

    # Redraw the buttons
    for button in root.grid_slaves():
        button.destroy()
    new_orders_cutlist = get_cutlist(new_orders)
    processed_orders_cutlist = get_cutlist(processed_orders)
    draw_headers()
    draw_buttons(new_orders_cutlist, 0)
    draw_buttons(processed_orders_cutlist, 1)

root = tk.Tk()

new_orders_cutlist = get_cutlist(new_orders)
processed_orders_cutlist = get_cutlist(processed_orders)
draw_headers()
draw_buttons(new_orders_cutlist, 0)
draw_buttons(processed_orders_cutlist, 1)

root.mainloop()
