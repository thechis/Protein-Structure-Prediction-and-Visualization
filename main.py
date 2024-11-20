import os
import subprocess
import logging


# Set up logging
log_file_path = os.path.join(os.path.dirname(__file__),"logs", "workflow.log")
if os.path.exists(log_file_path):
    os.remove(log_file_path)
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Also log to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

logging.info("Starting main.py")

# Optional: Install dependencies
install_requirements = True
install_pymol = True

if install_requirements:
    try:
        logging.info("Installing dependencies from requirements.txt")
        subprocess.run("pip install -r requirements.txt", shell=True, check=True)
        logging.info("Successfully installed dependencies from requirements.txt")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error installing dependencies: {e}")

if install_pymol:
    try:
        logging.info("Running install_pymol.sh to install PyMOL")
        subprocess.run("bash src/install_pymol.sh", shell=True, check=True)
        logging.info("Successfully installed PyMOL")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error installing PyMOL: {e}")

# Define the order of script execution
scripts = [
    ("data_download.py", "python src/data_download.py"),
    ("preprocess_data.py", "python src/preprocess_data.py --input data/proteins.fasta --output data/processed/"),
    ("train_model.py", "python src/train_model.py --config configs/train_config.yaml"),
    ("evaluate_model.py", "python src/evaluate_model.py --model checkpoints/model_checkpoint.h5 --test_data data/processed/test/"),
    ("visualize_structures.py", "python src/visualize_structures.py --input predictions/ --output visualizations/")
]


# Execute each script in sequence
for script_name, command in scripts:
    try:
        logging.info(f"Running {script_name}")
        subprocess.run(command, shell=True, check=True)
        logging.info(f"Successfully ran {script_name}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error while running {script_name}: {e}")
        break

logging.info("Workflow completed.")
