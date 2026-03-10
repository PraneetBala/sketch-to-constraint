import cv2
import numpy as np
import math

def detect_lines(image_path):
    """
    Detects lines in a sketch image using Hough Transform.
    """
    # Load image in grayscale
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Invert if the sketch is dark on a white background (common for sketches)
    if np.mean(gray) > 127:
        gray = 255 - gray
        
    # Apply thresholding
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    
    # Edge detection
    edges = cv2.Canny(thresh, 50, 150, apertureSize=3)
    
    # Detect lines using Probabilistic Hough Transform
    # Adjust parameters based on typical sketch stroke thickness
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=20)
    
    raw_lines = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            # Calculate angle in degrees
            angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
            # Normalize angle to be between 0 and 180
            if angle < 0:
                angle += 180
                
            # Calculate the midpoint
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
                
            raw_lines.append({
                'pts': (x1, y1, x2, y2),
                'angle': angle,
                'mid': (mid_x, mid_y),
                'length': math.hypot(x2 - x1, y2 - y1)
            })

    # Merge overlapping lines
    merged_lines = []
    angle_tolerance = 10.0
    dist_tolerance = 30.0
    
    for r_line in raw_lines:
        merged = False
        for m_line in merged_lines:
            # Check if angles are similar
            angle_diff = abs(r_line['angle'] - m_line['angle'])
            angle_diff = min(angle_diff, 180 - angle_diff)
            
            if angle_diff < angle_tolerance:
                # Check if midpoints are close
                dist = math.hypot(r_line['mid'][0] - m_line['mid'][0], r_line['mid'][1] - m_line['mid'][1])
                if dist < dist_tolerance:
                    # Merge: keep the longest one or average them. Here we just take the longest.
                    if r_line['length'] > m_line['length']:
                        m_line['pts'] = r_line['pts']
                        m_line['angle'] = r_line['angle']
                        m_line['mid'] = r_line['mid']
                        m_line['length'] = r_line['length']
                    merged = True
                    break
                    
        if not merged:
            merged_lines.append(r_line)
            
    detected_lines = [{'pts': l['pts'], 'angle': l['angle']} for l in merged_lines]
            
    return img, detected_lines

if __name__ == "__main__":
    # Simple test
    print("detect_primitives module loaded.")
