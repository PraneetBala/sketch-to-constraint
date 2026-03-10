# Intelligent Sketch-to-Constraint Prototype

![Python](https://img.shields.io/badge/python-3.8+-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)

> **A lightweight Computer Vision pipeline to automatically detect and classify geometric constraints (Parallelism, Perpendicularity) from freehand sketches.**

## 📋 Overview
This prototype simulates the core logic required for intelligent parametric CAD augmentation. Instead of relying purely on heavy deep learning models for parsing constraint topography, this pipeline uses classical computer vision techniques as a rapid, interpretable baseline.

- **Goal:** Extract primitive geometry (lines) from noisy sketches and infer spatial constraints.
- **Method:** 
  1. Image binarization and Canny Edge detection.
  2. Probabilistic Hough Transforms to extract line segments.
  3. Rule-based geometric inference engine operating on polar coordinates to classify constraints.
- **Results:** Instantly overlay color-coded constraints (e.g., Green for Parallel, Blue for Perpendicular) back onto the original sketch.

## 💻 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/PraneetBala/sketch-to-constraint.git
cd sketch-to-constraint

# Install dependencies
pip install -r requirements.txt
```

## 🏃‍♂️ Usage

1. **Generate sample mock sketches:**
```bash
python generate_samples.py
```

2. **Run inference on a sketch:**
```bash
python main.py --input data/parallel_lines.png --output results/output_parallel.png
```

## 📂 Project Structure
- `src/detect_primitives.py`: Edge detection and Hough Transform line extraction.
- `src/infer_constraints.py`: Geometric rule engine for angle difference calculation.
- `src/visualize.py`: Overlays detected lines (Red) and inferred constraint connections.
- `main.py`: The pipeline orchestrator.
- `generate_samples.py`: Helper script to create mock data.

## 🔮 Future Work
While this classical approach acts as a lightweight heuristic baseline, the next iterative phase of this project involves **integrating Vision-Language Models (VLMs)**. 
By utilizing advanced multimodal architectures, the pipeline will be able to ingest highly complex, robust, and noisy engineering sketches and output deep contextual information (e.g., parsing part dimensions, recognizing mechanical hierarchies, and outputting JSON schema) far beyond simple parametric line constraints.
