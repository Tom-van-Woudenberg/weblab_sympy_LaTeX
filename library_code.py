import matplotlib.pyplot as plt
from sympy import latex
import os

def get_next_counter_value(counter_file):
    # Read the current counter value from the file
    if os.path.exists(counter_file):
        with open(counter_file, 'r') as file:
            counter = int(file.read().strip())
    else:
        counter = 0

    # Increment the counter value
    counter += 1

    # Write the new counter value back to the file
    with open(counter_file, 'w') as file:
        file.write(str(counter))

    return counter

def display(sympy_obj):
    latex_solution = latex(sympy_obj)

    # Create a dummy figure to calculate the bounding box
    plt.figure()
    text = plt.text(0, 0, f"${latex_solution}$", fontsize=12)
    plt.axis('off')

    plt.draw()

    # Get the bounding box of the text
    bbox = text.get_window_extent()

    # Convert bbox to figure coordinates
    bbox = bbox.transformed(plt.gcf().dpi_scale_trans.inverted())

    # Close the dummy figure
    plt.close()

    # Create the final figure with the calculated size
    width, height = bbox.width, bbox.height
    plt.figure(figsize=(width, height))
    plt.text(0.5, 0.5, f"${latex_solution}$", fontsize=12, ha='center', va='center')
    plt.axis('off')

    # Get the next counter value for the unique filename
    output_dir = 'output'
    counter_file = os.path.join(output_dir, 'counter.txt')
    counter = get_next_counter_value(counter_file)
    output_path = os.path.join(output_dir, f'output_{counter}.png')

    # Save the image to the specified output path
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
