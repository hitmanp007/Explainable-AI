import sys
from pathlib import Path


train_loader, val_loader, test_loader = create_data_loaders()

print("Training batches:", len(train_loader))
print("Validation batches:", len(val_loader))
print("Testing batches:", len(test_loader))