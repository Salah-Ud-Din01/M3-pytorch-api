import torch
from torch.utils.data import DataLoader
import torchvision
import torchvision.transforms as transforms


def get_cifar10_loaders(batch_size=32, data_dir='./data'):
    """
    Load CIFAR-10 dataset and return train and test dataloaders.
    """
    # Define transforms (same as teacher's code)
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    
    # Download and load training data
    trainset = torchvision.datasets.CIFAR10(
        root=data_dir,
        train=True,
        download=True,
        transform=transform
    )
    
    trainloader = DataLoader(
        trainset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=2
    )
    
    # Download and load test data
    testset = torchvision.datasets.CIFAR10(
        root=data_dir,
        train=False,
        download=True,
        transform=transform
    )
    
    testloader = DataLoader(
        testset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=2
    )
    
    # CIFAR-10 classes
    classes = ('plane', 'car', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck')
    
    return trainloader, testloader, classes