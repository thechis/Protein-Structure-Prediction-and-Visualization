import pymol
import os
import logging

# Set up logging
log_file_path = os.path.join(os.path.dirname(__file__), "..", "logs", "workflow.log")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting visualize_structures.py")

# Also log to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

def visualize(structure_path, output_path):
    structure_path = os.path.join(os.path.dirname(__file__), "..", structure_path)
    output_path = os.path.join(os.path.dirname(__file__), "..", output_path)
    try:
        pymol.finish_launching()
        pymol.cmd.load(structure_path)
        pymol.cmd.save(output_path)
        pymol.cmd.quit()
        logging.info(f"Visualization completed successfully for {structure_path}")
    except Exception as e:
        logging.error(f"Error during visualization: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Path to the structure file")
    parser.add_argument("--output", help="Path to save the visualization")
    args = parser.parse_args()
    visualize(args.input, args.output)
