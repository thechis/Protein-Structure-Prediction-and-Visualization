
# Protein Structure Prediction and Visualization

## Overview
This project focuses on predicting and visualizing the 3D structures of proteins from their amino acid sequences. Using deep learning techniques, the project aims to enhance understanding of protein folding and its functional properties.

## Features
- **Deep Learning Model**: Built a Convolutional Neural Network (CNN) using TensorFlow and Keras for protein structure prediction.
- **High Accuracy**: Achieved 85% validation accuracy in predicting 3D protein structures.
- **Protein Visualization**: Leveraged PyMOL to visualize and interpret predicted protein structures.
- **Comprehensive Pipeline**: Includes data collection, preprocessing, model training, and visualization.

## Technologies
- **Programming Languages**: Python
- **Libraries and Frameworks**: TensorFlow, Keras, PyMOL, Biopython
- **Tools**: PyMOL for visualization, Jupyter Notebook for code execution and analysis

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/protein-structure-prediction.git
   cd protein-structure-prediction
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure PyMOL is installed for structure visualization:
   - Download PyMOL and follow the installation instructions.

## Usage
- **Download Data**:
  - Use ncbi-acc-download and RCSB PDB to download protein sequences and structures.
  - Example command:
    ```bash
    ncbi-acc-download --molecule protein --format fasta --out proteins.fasta <protein_ids>
    ```
  - Example script usage:
    ```python
    from script import download_protein_sequences, download_protein_structures
    download_protein_sequences(protein_ids=["<ids>"])
    download_protein_structures(pdb_ids=["<ids>"])
    ```

- **Preprocess Data**:
  - Load and encode sequences, parse structures using BioPython.

- **Train Model**:
  - Run the training script:
    ```bash
    python train_model.py
    ```

- **Visualize Results**:
  - Use PyMOL to visualize predicted structures:
    ```bash
    pymol predicted_structure.pdb
    ```

## Results
- **Prediction Accuracy**: 85% validation accuracy in protein structure prediction.
- **Visualization**: Below are sample visualizations of the predicted protein structures.

## Project Workflow
- **Data Collection**: Protein sequences and structures were sourced from NCBI and RCSB PDB.
- **Data Preprocessing**: Encoded sequences into numeric format; extracted atomic coordinates.
- **Model Training**: CNN-based architecture trained on processed data.
- **Evaluation**: Assessed model performance using Mean Absolute Error (MAE) and Root Mean Square Deviation (RMSD).
- **Visualization**: Utilized PyMOL for rendering 3D structures.

## Challenges
- Ensuring consistent sequence-structure mapping.
- Optimizing hyperparameters for better model performance.

## Future Work
- Explore advanced neural network architectures like Transformer models for improved accuracy.
- Automate structure visualization and interpretation using PyMOL plugins.

## Contact
- For further information or inquiries:
