#!/usr/bin/env python3
"""
Train ML models using Kaggle datasets or synthetic fallback.
If Kaggle is not configured, it will generate and train on synthetic data.
"""

import os
import sys
# Add the student backend directory to the path
_script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_script_dir, 'students', 'Train'))

from ml_training_kaggle import MLModelTrainer

def train_models():
    """Train all ML models."""
    trainer = MLModelTrainer()
    
    print("=" * 70)
    print("YSMAI ML Model Training")
    print("=" * 70)
    print("\nAttempting to use Kaggle datasets...")
    print("Note: If Kaggle credentials are not configured,")
    print("      synthetic data will be used as fallback.\n")
    
    # Train all models
    results = trainer.train_all_models()
    
    # Display results
    print("\n" + "=" * 70)
    print("Training Complete - Model Information")
    print("=" * 70)
    
    if results:
        for model_name, metrics in results.items():
            print(f"\n{model_name}:")
            for key, value in metrics.items():
                if isinstance(value, float):
                    print(f"  {key}: {value:.4f}")
                else:
                    print(f"  {key}: {value}")
    
    print("\n" + "=" * 70)
    print(f"Trained models saved to: {os.path.join(_script_dir, 'models')}/")
    print("=" * 70)
    
    return trainer

if __name__ == "__main__":
    trainer = train_models()
