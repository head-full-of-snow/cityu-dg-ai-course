import cv2
import torch
import urllib.request
import matplotlib.pyplot as plt

# 1. Setup Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Running depth estimation on: {device}")

# 2. Load the MiDaS Model from PyTorch Hub
# Options: 
# "DPT_Large" (highest accuracy, slowest)
# "DPT_Hybrid" (mid-tier)
# "MiDaS_small" (lowest accuracy, fastest/mobile-friendly)
model_type = "DPT_Large" 
print(f"Loading {model_type} model...")
midas = torch.hub.load("intel-isl/MiDaS", model_type)
midas.to(device)
midas.eval() # Set model to evaluation mode

# 3. Load the corresponding transforms to preprocess the image
midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    transform = midas_transforms.dpt_transform
else:
    transform = midas_transforms.small_transform

# 4. Download a sample image (if you don't have one locally)
url, filename = ("https://github.com/pytorch/hub/raw/master/images/dog.jpg", "dog.jpg")
urllib.request.urlretrieve(url, filename)
img_path = filename

# 5. Load and preprocess the image
print(f"Processing image: {img_path}")
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply transforms and move to device
input_batch = transform(img).to(device)

# 6. Perform Depth Estimation
print("Estimating depth...")
with torch.no_grad():
    prediction = midas(input_batch)

    # Resize the predicted depth map back to the original image resolution
    prediction = torch.nn.functional.interpolate(
        prediction.unsqueeze(1),
        size=img.shape[:2],
        mode="bicubic",
        align_corners=False,
    ).squeeze()

# Move the prediction back to CPU and convert to a numpy array
depth_map = prediction.cpu().numpy()

# 7. Visualize the Results
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img)
plt.axis('off')

# Depth Map
plt.subplot(1, 2, 2)
plt.title("Predicted Depth Map")
# 'inferno' or 'plasma' colormaps work well for visualizing depth
plt.imshow(depth_map, cmap='inferno') 
plt.axis('off')

plt.tight_layout()
plt.show()

print("Process complete!")