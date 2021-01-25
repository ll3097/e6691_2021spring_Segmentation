from scipy import ndimage
import matplotlib.pyplot as plt
from filter import *
from segment_graph import *
import time
import cv2
import os

# --------------------------------------------------------------------------------
# Segment an image:
# Returns a color image representing the segmentation.
#
# Inputs:
#           in_image: image to segment.
#           sigma: to smooth the image.
#           k: constant for threshold function.
#           min_size: minimum component size (enforced by post-processing stage).
#
# Returns:
#           num_ccs: number of connected components in the segmentation.
# --------------------------------------------------------------------------------
def segment(in_image, sigma, k, min_size, output_dir, break_every_percentage=None):
    start_time = time.time()
    height, width, band = in_image.shape
    print("Height:  " + str(height))
    print("Width:   " + str(width))
    smooth_red_band = smooth(in_image[:, :, 0], sigma)
    smooth_green_band = smooth(in_image[:, :, 1], sigma)
    smooth_blue_band = smooth(in_image[:, :, 2], sigma)

    # build graph
    edges_size = width * height * 4
    edges = np.zeros(shape=(edges_size, 3), dtype=object)
    num = 0
    for y in range(height):
        for x in range(width):
            if x < width - 1:
                edges[num, 0] = int(y * width + x)
                edges[num, 1] = int(y * width + (x + 1))
                edges[num, 2] = diff(smooth_red_band, smooth_green_band, smooth_blue_band, x, y, x + 1, y)
                num += 1
            if y < height - 1:
                edges[num, 0] = int(y * width + x)
                edges[num, 1] = int((y + 1) * width + x)
                edges[num, 2] = diff(smooth_red_band, smooth_green_band, smooth_blue_band, x, y, x, y + 1)
                num += 1

            if (x < width - 1) and (y < height - 2):
                edges[num, 0] = int(y * width + x)
                edges[num, 1] = int((y + 1) * width + (x + 1))
                edges[num, 2] = diff(smooth_red_band, smooth_green_band, smooth_blue_band, x, y, x + 1, y + 1)
                num += 1

            if (x < width - 1) and (y > 0):
                edges[num, 0] = int(y * width + x)
                edges[num, 1] = int((y - 1) * width + (x + 1))
                edges[num, 2] = diff(smooth_red_band, smooth_green_band, smooth_blue_band, x, y, x + 1, y - 1)
                num += 1
    # Segment
    step = int(num * break_every_percentage) if break_every_percentage else num
    for break_at_edge_index in range(step, num + step, step):
        u = segment_graph(width * height, num, edges, k, break_at_egde_i = break_at_edge_index)

        # post process small components
        # for i in range(num):
        #     a = u.find(edges[i, 0])
        #     b = u.find(edges[i, 1])
        #     if (a != b) and ((u.size(a) < min_size) or (u.size(b) < min_size)):
        #         u.join(a, b)

        num_cc = u.num_sets()
        output = np.zeros(shape=(height, width, 3))

        # pick random colors for each component
        colors = np.zeros(shape=(height * width, 3))
        random.seed(3)
        for i in range(height * width):
            colors[i, :] = random_rgb()

        for y in range(height):
            for x in range(width):
                comp = u.find(y * width + x)
                output[y, x, :] = colors[comp, :]

        elapsed_time = time.time() - start_time
        print(
            "Execution time: " + str(int(elapsed_time / 60)) + " minute(s) and " + str(
                int(elapsed_time % 60)) + " seconds")

        # displaying the result
        output_int = np.array(output, dtype=np.uint8)
        fig = plt.figure()
        a = fig.add_subplot(1, 2, 1)
        plt.imshow(in_image)
        a.set_title('Original Image')
        a = fig.add_subplot(1, 2, 2)
        plt.imshow(output_int)
        a.set_title('Segmented Image')
        plt.suptitle('k = ' + str(k))

        out_path = os.path.join(output_dir, str(break_at_edge_index))
        plt.savefig(out_path)
        print('image save to ' + out_path)
    return fig


if __name__ == "__main__":
    image_name = 'bridge'
    sigma = 0.5
    k = 1000
    min = 50
    input_path = "data/" + image_name + ".jpg"

    # Loading the image
    input_image = cv2.imread(input_path)
    # input_image = cv2.normalize(input_image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)  # normalize the image
    output_dir = 'output/' + image_name + '_k' + str(k) + '/'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    print("Loading is done.")
    print("processing...")
    output = segment(input_image, sigma, k, min, output_dir, break_every_percentage=0.01)

# save to gifs
import imageio
import os

images = ['paris', 'BigTree', 'bridge']
ks = [100, 500, 1000]
output_root = 'ObjectDetection/ImageSegmentation/output'

paths = [[os.path.join(output_root, img + '_k' + str(k)) for k in ks] for img in images]
paths = [item for sublist in paths for item in sublist]

for pth in paths:
    image_list = []
    files = os.listdir(pth)
    files = [f for f in files if not f.startswith('.')]
    files.sort(key = lambda x: int(x.replace('.png', '')))
    for filename in files:
        image_list.append(imageio.imread(os.path.join(pth, filename)))
    imageio.mimsave(pth.replace('output', 'gif') +'.gif', image_list, fps=5)