Zhu Zhiyu

Tutorial 01: Python environment set up and basic image processing

# (1) Python environment setup

Anaconda Distribution for Windows

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2Fc0e89ffd5b8841b685c4a241e5e54b93.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253882&Signature=TD7F5TO8pyi42vUdG7%2Bhz0r7tiU%3D)

Anaconda Distribution for macOS/Linux

https://www.anaconda.com/docs/getting-started/main

# (1) Python environment setup

1. Download the installer from the Anaconda website or by using your preferred command line interface:

Anaconda website Command Prompt PowerShell

Open a Command Prompt window and run the following command:

curl https://repo.anaconda.com/archive/Anaconda3-2025.12-1-Win© 🔒 🔄 🔊 .e

curl https://repo.anaconda.com/archive/Anaconda3-2025.12-1-Windows-x86_64.exe --output.\Downloads\Anaconda3-2025.12-1-Windows-x86_64.exe

# (1) Python environment setup

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2Fc38bc0cda2d849a18bd4c4c1471dd35d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253882&Signature=SNL0pwQ02EK9zB8oObsIqIbdOHo%3D)

# (1) Python environment setup

3. Go to your Downloads folder (or Home folder if downloaded via CLI) and double-click the installer to launch.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2F8759d89fb74046958617ada48e2e1313.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253883&Signature=sPR882hmCDIB2Zoipn%2FxA1v5ue0%3D)

To prevent permission errors, do not launch the installer from the  $ \underline{\text{Favorites folder.}} $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2F6f1428d2ced84f44b1edaed21ff5daa9.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253883&Signature=7ZhBywR3%2F0kkkM2BpXbPi556OIY%3D)

If you encounter issues during installation, temporarily disable your anti-virus software during install, then re-enable it after the installation concludes. If you installed for All Users, uninstall Anaconda and re-install it for Just Me only.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2Fe34dcecafab048d5b1e3cd8d8e27f7fb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253883&Signature=iHwo94h9rriosNADfvOMzZVE9tc%3D)

# (1) Python environment setup

4. Click Next and then I Agree to agree to Anaconda's Terms of Service (TOS). You can read the full TOS at  $ \underline{\text{https://anaconda.com/legal.}} $

5. Select an installation option:

• Just Me (Recommended): Install Anaconda Distribution for the current user account.

- All Users: Install Anaconda Distribution for all user accounts on the computer (requires Windows Administrator privileges).

# (1) Python environment setup

6. Click Next.

7. Select a destination folder to install Anaconda, then click Next.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2F7c8b51eb9e004db08ad083ea7a72a029.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253883&Signature=rBaBiPmvMJPsdJyEiArEJkM%2BbT8%3D)

Anaconda recommends installing Anaconda Distribution in a directory with no spaces or special characters to avoid potential compatibility issues with open-source tools. For more information, see the FAQ.

- Do not install as Administrator unless admin privileges are required.

# (1) Python environment setup

8. Customize your installation options:

• Create shortcuts - Selected by default. Creates Start Menu shortcuts for the Anaconda Navigator, Spyder, Jupyter Notebook, and Anaconda Prompt packages. Deselecting this option skips creating these shortcuts.

- Add Anaconda3 to my PATH environment variable - Adds the path that contains the conda binaries to your PATH environment variable. Anaconda does not recommend selecting this option. The conda binaries path contains other package binaries, which are permanently added to your PATH environment variable, even if no conda environment is currently active. This makes it possible for other software to use these package files, which might lead to errors.

① Unless you plan on installing and running multiple versions of Anaconda Distribution or Python, open Anaconda Navigator or the Anaconda Prompt from the Start Menu to begin your environment management work.

As of Anaconda Distribution 2022.05, the option to add Anaconda to the PATH environment variable during an All Users installation has been disabled. This was done to address a security exploit. You can still add Anaconda to the PATH environment variable during a Just Me installation.

- Register Anaconda3 as my default Python 3.12 - Selected by default. Registers the Python package in this install as the default Python for programs like VSCode, PyCharm, and so on.

• Clear the package cache upon completion - Runs  $ \underline{\text{conda clean --all --force-pkgs-dirs}} $ after the install finishes. For more information on these commands, see the  $ \underline{\text{conda command documentation.}} $

9. Click Install. The installation might take a few minutes to complete. Click Show details to view the packages being installed.

10. Click Next twice, then click Finish to close the installer.

11. Open  $ \underline{\text{Anaconda Prompt}} $ to use Anaconda Distribution.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2Fc5cfb2dbf5ea4751b2d8546fd6ad8c95.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253883&Signature=v%2FOHR9woRX89hR8kxhVl9vhjW4o%3D)

If you are behind a company proxy, you might need to do some additional setup. For more information, see  $ \underline{\text{Using Anaconda behind a company proxy.}} $

# (1) Python environment setup

Add anaconda to system variable.

<table><tr><td>%SystemRoot%\system32</td><td>新建(N)</td></tr><tr><td>%SystemRoot%</td><td>编辑(E)</td></tr><tr><td>%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\</td><td>浏览(B)...</td></tr><tr><td>%SYSTEMROOT%\System32\OpenSSH\</td><td>删除(D)</td></tr><tr><td>D:\ProgramData\anaconda3\condabin</td><td>上移(U)</td></tr><tr><td>下移(O)</td><td>编辑文本①...</td></tr><tr><td>确定</td><td>取消</td></tr></table>

# (1) Python environment setup

Activate base environment or set up your own environment

Token

tos

Set repository access token and configure default_channels

A subcommand for viewing, accepting, rejecting, and otherwise interacting with a channel's Terms of Service (ToS). This plugin periodically checks for updated Terms of Service for the active/selected channels. Channels with a Terms of Service will need to be accepted or rejected prior to use. Conda will only allow package installation from channels without a Terms of Service or with an accepted Terms of Service. Attempting to use a channel with a rejected Terms of Service will result in an error.

Update (upgrade)

Update conda packages to the latest compatible version.

# (1) Python environment setup

(base) C:\Users\zhiyu.zhu>conda create -n my_py python=3.12

3 channel Terms of Service accepted

Retrieving notices: \

The following packages will be downloaded:

<table><tr><td>package</td><td>build</td></tr><tr><td>expat-2.7.3</td><td>h885b0b7_4</td></tr><tr><td>libexpat-2.7.3</td><td>h885b0b7_4</td></tr><tr><td>python-3.12.12</td><td>h716150d_1</td></tr><tr><td>setuptools-80.9.0</td><td>py312haa95532_0</td></tr><tr><td>sqlite-3.51.1</td><td>hda9a48d_0</td></tr><tr><td>vc-14.3</td><td>h2df5915_10</td></tr><tr><td>wheel-0.45.1</td><td>py312haa95532_0</td></tr><tr><td></td><td>Total: 18.2 MB</td></tr></table>

**The following NEW packages will be INSTALLED:**

# (1) Python environment setup

Installing necessary package. numpy and opencv-python

(my_py) C:\Users\zhiyu.zhu>pip install numpy opencv-python

Collecting numpy

Downloading numpy-2.4.1-cp312-cp312-win_amd64.whl.metadata (6.6 kB)

Collecting opencv-python

Downloading opencv_python-4.13.0.90-cp37-abi3-win_amd64.whl.metadata (20 kB)

Downloading numpy-2.4.1-cp312-cp312-win_amd64.whl (12.3 MB)

12.3/12.3 MB 19.3 MB/s 0:00:00

Downloading opencv_python-4.13.0.90-cp37-abi3-win_amd64.whl (40.2 MB)

40.2/40.2 MB 18.7 MB/s 0:00:02

Installing collected packages: numpy, opencv-python

Successfully installed numpy-2.4.1 opencv-python-4.13.0.90

(2) Experiment 1 (average blurring the example image)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2Fe73fa984ddc74e4f975351574089e1db.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253883&Signature=8TaJjj1LlSwAvtWLoK5XRKFbzGY%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2F2c58aef89cb4453ea03c1a658413a7dd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253883&Signature=xYc9NpisowfMPJeGFYM1Zmv8DYU%3D)

import cv2

import numpy as np

# Load the image

image = cv2.imread('input_image.png')

if image is None:

print("Error: Image not found.")

# 1. Averaging (Box Filter) Kernel

kernel_averaging = np.ones((5, 5), np.float32) / 25

res_averaging = cv2.filter2D(image, -1, kernel_averaging)

# Save results

cv2.imwrite('manual_averaging.png', res_averaging)

print("Manual filtering complete. Images saved.")

(3) Experiment 2 (gaussian blurring the example image)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2F168758542c4d4c398ce12e5eba3a09aa.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253883&Signature=ndIKe6PT%2BBX3SZhLlBH6vET1jgs%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2F68e491b6265b451da3626af5ea86cee5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253883&Signature=%2FFSWfyDVxydPqaykmaAojp1%2FCYk%3D)

res_gaussian = cv2.filter2D(image, -1, kernel_gaussian)

cv2.imwrite('manual_gaussian.png', res_gaussian)

(4) Experiment 3 (Sharpening for example image)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2F4b82a3aa5dde484d875348f3bfefe423.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253884&Signature=KMG5DPLgsAJcAZrIpwPnXInX6MM%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2Fac464162ddd74f539abc0b1b94021c38.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253884&Signature=bQu96lmXG9I4XhE1seoDD1ZbRO0%3D)

res_sharpening = cv2.filter2D(image, -1, kernel_sharpening)

cv2.imwrite('manual_sharpened.png', res_sharpening)

(4) Experiment 3 (edge filtering for example image

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2Fcc515603ef2849c78c8780cbf69142e5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253884&Signature=8Gqt2nLUNHfK4dIXZ7c8QsbTjW8%3D)

# 4. Edge Detection (Sobel Filter - Horizontal)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel_sobel_x = np.array([[ -1, 0, 1],

[-2, 0, 2],

[-1, 0, 1]])

res_edges = cv2.filter2D(gray_image, -1, kernel_sobel_x)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8f39450dea9049b6b97521fd6c887efc%2Fmedia%2F4360884edd4a45cb99a6b259c9335172.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253884&Signature=IG59dHL73VzG9Hazci%2FFONoFhZA%3D)

cv2.imwrite('manual_edges.png', res_edges)

# (4)

Experiment 4 (Calculating PSNR)

import cv2

import numpy as np

import math

def calculate_psnr(img1, img2):

if img1.shape != img2.shape:

raise ValueError("Input images must have the same dimensions.")

mse = np.mean((img1.astype(np.float64) - img2.astype(np.float64)) ** 2)

if mse == 0:

return float('inf')

max_pixel = 255.0

psnr = 20 * math.log10(max_pixel / math.sqrt(mse))

return psnr

original = cv2.imread('input_image.png')

processed = cv2.imread('manual_gaussian.png')

if original is not None and processed is not None:

score = calculate_psnr(original, processed)

print(f"PSNR value: {score:.2f} dB")

**Questions?**
