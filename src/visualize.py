import cv2
import numpy as np
import os

def visualize_results(img, lines, constraints, output_path):
    """
    Draws the detected lines and constraints on the image and saves it.
    """
    # Create a copy to draw on
    if len(img.shape) == 2:
        img_drawn = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    else:
        img_drawn = img.copy()
        
    # Draw all detected lines in red
    for line in lines:
        x1, y1, x2, y2 = line['pts']
        cv2.line(img_drawn, (x1, y1), (x2, y2), (0, 0, 255), 2)
        
    # Highlight constrained lines
    for count, constraint in enumerate(constraints):
        c_type = constraint['type']
        l1_idx = constraint['line1_idx']
        l2_idx = constraint['line2_idx']
        color = constraint.get('color', (255, 0, 255))
        
        # Draw the lines involved in the constraint with the specific color
        for idx in [l1_idx, l2_idx]:
            x1, y1, x2, y2 = lines[idx]['pts']
            cv2.line(img_drawn, (x1, y1), (x2, y2), color, 4) # Thicker line
            
        # Optional: Add text label near the midpoint of line 1
        x1, y1, x2, y2 = lines[l1_idx]['pts']
        mid_x = int((x1 + x2) / 2)
        mid_y = int((y1 + y2) / 2)
        
        text = f"{c_type}"
        cv2.putText(img_drawn, text, (mid_x, mid_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imwrite(output_path, img_drawn)
    print(f"Result saved to: {output_path}")
    
if __name__ == "__main__":
    print("visualize module loaded.")
