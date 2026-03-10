import os
import argparse
from src.detect_primitives import detect_lines
from src.infer_constraints import infer_constraints
from src.visualize import visualize_results

def main():
    parser = argparse.ArgumentParser(description="Sketch-to-Constraint Prototype")
    parser.add_argument('--input', type=str, default='data/parallel_lines.png', help='Path to input sketch image')
    parser.add_argument('--output', type=str, default='results/output.png', help='Path to output visualized image')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} does not exist.")
        return
        
    print(f"Processing sketch: {args.input}")
    
    # Step 1: Detect lines
    img, lines = detect_lines(args.input)
    print(f"Detected {len(lines)} distinct lines.")
    
    # Step 2: Infer constraints
    constraints = infer_constraints(lines, angle_threshold=5.0)
    print(f"Inferred {len(constraints)} constraints:")
    for c in constraints:
        print(f"  - {c['type']} between Line {c['line1_idx']} and Line {c['line2_idx']}")
        
    # Step 3: Visualize
    visualize_results(img, lines, constraints, args.output)
    
if __name__ == "__main__":
    main()
