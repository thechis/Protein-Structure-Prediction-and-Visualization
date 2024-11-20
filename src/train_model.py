import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, Flatten, Dense, Dropout
import yaml
import os
import logging

# Set up logging
log_file_path = os.path.join(os.path.dirname(__file__), "..", "logs", "workflow.log")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting train_model.py")

# Also log to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

def build_model(input_shape):
    model = Sequential([
        Conv1D(64, kernel_size=3, activation='relu', input_shape=input_shape),
        Dropout(0.3),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(3, activation='softmax')
    ])
    return model


def train(config_file):
    config_file = os.path.join(os.path.dirname(__file__), "..", config_file)
    with open(config_file) as f:
        config = yaml.safe_load(f)

    try:
        model = build_model(config["input_shape"])
        model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

        # Sample data loaded in
        train_data = tf.random.normal(config['train_size'])
        val_data = tf.random.normal(config['val_size'])

        early_stopping = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=5)
        model.fit(
            train_data,
            validation_data=val_data,
            epochs=config['epochs'],
            callbacks=[early_stopping]
        )
        checkpoint_path = os.path.join(os.path.dirname(__file__), "..", config['checkpoint_path'])
        if not os.path.exists(checkpoint_path):
            os.makedirs(checkpoint_path)
        model.save(os.path.join(checkpoint_path, "model_checkpoint.h5"))
        logging.info(f"Model training completed successfully and saved to {checkpoint_path}")
    except Exception as e:
        logging.error(f"Error during model training: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path to training config")
    args = parser.parse_args()
    train(args.config)
