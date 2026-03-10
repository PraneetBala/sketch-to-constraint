import math

def calculate_angle_difference(angle1, angle2):
    """
    Calculates the absolute difference between two angles (0-180),
    accounting for circular wraparound.
    """
    diff = abs(angle1 - angle2)
    return min(diff, 180 - diff)

def infer_constraints(lines, angle_threshold=10.0):
    """
    Infers geometric constraints (Parallel, Perpendicular) between detected lines.
    
    Returns a list of constraints:
    [
        {'type': 'Parallel', 'line1_idx': 0, 'line2_idx': 1},
        ...
    ]
    """
    constraints = []
    n_lines = len(lines)
    
    if n_lines < 2:
        return constraints
        
    for i in range(n_lines):
        for j in range(i + 1, n_lines):
            angle1 = lines[i]['angle']
            angle2 = lines[j]['angle']
            
            diff = calculate_angle_difference(angle1, angle2)
            
            # Check for Parallelism (angles are almost the same)
            if diff <= angle_threshold:
                constraints.append({
                    'type': 'Parallel',
                    'line1_idx': i,
                    'line2_idx': j,
                    'color': (0, 255, 0) # Green for parallel
                })
            # Check for Perpendicularity (angles differ by ~90 degrees)
            elif abs(diff - 90) <= angle_threshold:
                constraints.append({
                    'type': 'Perpendicular',
                    'line1_idx': i,
                    'line2_idx': j,
                    'color': (255, 0, 0) # Blue for perpendicular
                })
                
    return constraints

if __name__ == "__main__":
    print("infer_constraints module loaded.")
