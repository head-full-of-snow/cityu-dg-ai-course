import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torchvision.models import vit_b_16

# 1. Setup Device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Training Vision Transformer on device: {device}")

# 2. Data Loading and Transformations
# ViTs usually expect 224x224 inputs for standard 16x16 patching
transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
# Batch size reduced to 32 to prevent Out-Of-Memory (OOM) errors on GPUs
trainloader = torch.utils.data.DataLoader(trainset, batch_size=32,
                                          shuffle=True, num_workers=2)

# 3. Model Definition
def get_vit_model():
    # Load un-trained ViT architecture
    model = vit_b_16(weights=None) 
    # Modify the classification head for 10 CIFAR-10 classes instead of 1000
    model.heads.head = nn.Linear(model.heads.head.in_features, 10)
    return model

# 4. Training Loop
def train_transformer():
    model = get_vit_model().to(device)
    criterion = nn.CrossEntropyLoss()
    # ViTs trained from scratch often require a smaller learning rate
    optimizer = optim.Adam(model.parameters(), lr=0.0001)
    epochs = 5

    print("Starting Vision Transformer Training...")
    for epoch in range(epochs):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data[0].to(device), data[1].to(device)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            if i % 100 == 99:
                print(f'[Epoch {epoch + 1}, Batch {i + 1}] loss: {running_loss / 100:.3f}')
                running_loss = 0.0

    print("Finished Training Vision Transformer")

if __name__ == '__main__':
    train_transformer()