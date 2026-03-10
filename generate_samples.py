import cv2
import numpy as np
import os

def generate_mock_sketches():
    os.makedirs('data', exist_ok=True)
    
    # 1. Parallel Lines (cleaner separation)
    img_parallel = np.ones((400, 400), dtype=np.uint8) * 255
    cv2.line(img_parallel, (50, 100), (350, 100), 0, 4)
    cv2.line(img_parallel, (50, 200), (350, 200), 0, 4)
    cv2.imwrite('data/parallel_lines.png', img_parallel)
    
    # 2. Perpendicular Lines
    img_perp = np.ones((400, 400), dtype=np.uint8) * 255
    cv2.line(img_perp, (200, 50), (200, 350), 0, 4)
    cv2.line(img_perp, (50, 200), (350, 200), 0, 4)
    cv2.imwrite('data/perpendicular_lines.png', img_perp)
    
    # 3. Random/No Constraint Lines
    img_random = np.ones((400, 400), dtype=np.uint8) * 255
    cv2.line(img_random, (50, 50), (300, 300), 0, 4)
    cv2.line(img_random, (100, 350), (350, 100), 0, 4)
    cv2.imwrite('data/random_lines.png', img_random)
    
    print("Mock sketches generated in the 'data' folder.")

if __name__ == "__main__":
    generate_mock_sketches()
