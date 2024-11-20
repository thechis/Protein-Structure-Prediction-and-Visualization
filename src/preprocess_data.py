import pandas as pd
import numpy as np
import os
from Bio import SeqIO
import logging
from Bio.Seq import Seq

# Set up logging
log_file_path = os.path.join(os.path.dirname(__file__), "..", "logs", "workflow.log")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting preprocess_data.py")

def pad_sequences(sequences, max_length, padding_char='-'):
    """Pads all sequences to the same length with the given padding character."""
    padded_sequences = []
    for seq in sequences:
        if len(seq) < max_length:
            seq += padding_char * (max_length - len(seq))
        else:
            seq = seq[:max_length]  # Truncate if sequence is longer than max_length
        padded_sequences.append(seq)
    return padded_sequences

def preprocess(input_file, output_folder, max_length=None):
    input_file = os.path.join(os.path.dirname(__file__), "..", input_file)
    output_folder = os.path.join(os.path.dirname(__file__), "..", output_folder)

    sequences = []

    try:
        # Extract sequences from the input FASTA file
        for record in SeqIO.parse(input_file, "fasta"):
            sequences.append(str(record.seq))

        # Determine the maximum length if not specified
        if max_length is None:
            max_length = max(len(seq) for seq in sequences)

        # Pad all sequences to the same length
        padded_sequences = pad_sequences(sequences, max_length)

        # Convert sequences to a numpy array and save them
        processed_sequences = np.array(padded_sequences, dtype=str)
        os.makedirs(output_folder, exist_ok=True)
        np.save(os.path.join(output_folder, "processed_sequences.npy"), processed_sequences)

        logging.info(f"Successfully processed data from {input_file} and saved to {output_folder}")
    except Exception as e:
        logging.error(f"Error during preprocessing: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Input file")
    parser.add_argument("--output", help="Output folder")
    parser.add_argument("--max_length", type=int, default=None, help="Maximum length to pad/truncate sequences")
    args = parser.parse_args()

    preprocess(args.input, args.output, args.max_length)
