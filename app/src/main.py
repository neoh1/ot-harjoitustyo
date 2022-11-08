import sys
import torch
import pytorch_lightning
import models


def main():
    """ 
    0. Activate PySide GUI 
    1. Test CUDA availability
    2. Load CPU/RAM/GPU stats
    """
    torch.cuda.is_available()
    pass


if __name__ == "__main__":
    sys.exit(main())
