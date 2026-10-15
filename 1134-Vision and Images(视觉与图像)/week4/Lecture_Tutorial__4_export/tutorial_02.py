import cv2
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# PART 2: Image Matching (Lowe's Ratio Test)
# ==========================================
def part2_image_matching(img1, img2):
    print("--- Running Part 2: Image Matching ---")
    
    # 1. Initialize SIFT detector
    sift = cv2.SIFT_create()
    
    # 2. Detect keypoints and compute descriptors
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    
    # 3. Match features using K-Nearest Neighbors (k=2)
    # Using KDTree algorithm for SIFT
    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    
    # 4. Apply Lowe's Ratio Test to filter out bad matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)
            
    print(f"Keypoints in Image 1: {len(kp1)}")
    print(f"Keypoints in Image 2: {len(kp2)}")
    print(f"Good Matches found: {len(good_matches)}")

    
    
    # 5. Visualize the matches
    img_matches = cv2.drawMatches(
        img1, kp1, img2, kp2, good_matches, None, 
        matchColor=(0, 255, 0), singlePointColor=(255, 0, 0), 
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )
    
    plt.figure(figsize=(12, 6))
    plt.title("Part 2: SIFT Feature Matching with Lowe's Ratio Test")
    plt.imshow(img_matches, cmap='gray')
    plt.axis('off')
    plt.show()
    
    return kp1, kp2, good_matches

# ==========================================
# PART 3: Image Warping and Alignment
# ==========================================
def part3_warping_alignment(img1, img2, kp1, kp2, good_matches):
    print("\n--- Running Part 3: Warping and Alignment ---")
    
    MIN_MATCH_COUNT = 4 # We need at least 4 points to compute a homography
    
    if len(good_matches) < MIN_MATCH_COUNT:
        print(f"Not enough matches are found - {len(good_matches)}/{MIN_MATCH_COUNT}")
        return

    # 1. Extract the (x, y) coordinates of the good matches
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    

    # 2. Compute the Homography matrix using RANSAC
    # RANSAC makes the algorithm robust to outlier matches (false positives)
    H_matrix, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    
    inliers = np.sum(mask)
    print(f"Homography computed using {inliers} inlier matches.")
    print("Homography Matrix:\n", H_matrix)

    # 3. Warp Image 1 to align with Image 2's perspective
    h, w = img2.shape
    warped_img1 = cv2.warpPerspective(img1, H_matrix, (w, h))

    # 4. Create an overlay to visually verify the alignment
    # We will put the warped Image 1 in the Red channel and Image 2 in the Green/Blue channels
    alignment_check = np.zeros((h, w, 3), dtype=np.uint8)
    alignment_check[:, :, 0] = warped_img1  # Red channel
    alignment_check[:, :, 1] = img2         # Green channel
    alignment_check[:, :, 2] = img2         # Blue channel

    # Plotting the results
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    axes[0].imshow(img2, cmap='gray')
    axes[0].set_title("Target Perspective (Image 2)")
    axes[0].axis('off')

    axes[1].imshow(warped_img1, cmap='gray')
    axes[1].set_title("Warped Image 1 (Using Homography)")
    axes[1].axis('off')

    axes[2].imshow(alignment_check)
    axes[2].set_title("Alignment Overlay\n(White/Yellow = Perfect Alignment)")
    axes[2].axis('off')

    plt.tight_layout()
    plt.show()

# ==========================================
# MAIN EXECUTION BLOCK
# ==========================================
if __name__ == "__main__":
    # # Step A: Generate our test images
    # image1, image2 = generate_test_images()
    image1 = cv2.imread("D:\Vision_Image\Lec&Teu_04\img_01.jpg", cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread("D:\Vision_Image\Lec&Teu_04\img_02.jpg", cv2.IMREAD_GRAYSCALE)
    # Step B: Run Part 2 (Extract features and match)
    keypoints1, keypoints2, valid_matches = part2_image_matching(image1, image2)
    
    # Step C: Run Part 3 (Compute homography and warp)
    part3_warping_alignment(image1, image2, keypoints1, keypoints2, valid_matches)