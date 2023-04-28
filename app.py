import tkinter as tk
import os

# Define the source directories for new and processed orders
NEW_ORDERS_DIR = r'H:\test_data\unprocessed'
PROCESSED_ORDERS_DIR = r'H:\test_data\processed'

# Define the maximum number of cutlists to display
MAX_CUTLISTS = 10

# Define the padding for the grid layout
GRID_PADDING = {'padx': 10, 'pady': 5}

def get_cutlists(source_dir):
    """
    Get the cutlists in the given source directory, sorted by modification time.
    """
    cutlists = [os.path.join(source_dir, filename) for filename in os.listdir(source_dir) if filename.endswith('.csv')]
    cutlists.sort(key=os.path.getmtime, reverse=True)
    return cutlists[:MAX_CUTLISTS]

def delete_cutlist(filename):
    """
    Delete the cutlist file with the given filename.
    """
    os.remove(filename)

def redraw_buttons():
    """
    Redraw the buttons for the new and processed cutlists.
    """
    for button in root.grid_slaves():
        button.destroy()

    new_cutlists = get_cutlists(NEW_ORDERS_DIR)
    processed_cutlists = get_cutlists(PROCESSED_ORDERS_DIR)

    for column, (cutlists, label_text) in enumerate(zip([new_cutlists, processed_cutlists], ['New Orders', 'Processed Orders'])):
        label = tk.Label(root, text=label_text)
        label.grid(row=0, column=column, **GRID_PADDING)

        for row, cutlist_filename in enumerate(cutlists, 1):
            cutlist_name = os.path.basename(cutlist_filename)
            button = tk.Button(root, text=cutlist_name, command=lambda filename=cutlist_filename: delete_cutlist(filename))
            button.grid(row=row, column=column, sticky="w", **GRID_PADDING)

# Create the root window
root = tk.Tk()

# Draw the initial buttons
redraw_buttons()

# Start the event loop
root.mainloop()
