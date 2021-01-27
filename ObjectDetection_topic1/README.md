# ObjectDetection_topic1
This subdirectory includes examples for the topics cover in Object Detection for Dummies Part 1: Gradient Vector, Histogram of Gradients, Image Segmentation, and Selective Search.
## Prerequisites
Python 3.7 +

Install all the required packages with `pip install -r requirements.txt`

## Image Gradient Vectors
## Histogram of Gradients

## Image Segmentation
We provide examples for visualizing the image segmentation process with the Felzenszwalb’s Algorithm. 

Navigation to ../ImageSegmentation, the directory or scripts that you may need are:
* ../main.py: the visualization script that does the image segmentation and save intermediate results to ../ImageSegmentation/output.
  You may want to change line 108-112 to use your own image or change the hyperparameters. Note that the script will a while to run, depending on the size of the input image.
* ../ImageSegmentation/data: contains three example images that can be the input of the algorithm, you are welcome to use your own images
* ../ImageSegmentation/gif: contains animated results for running the visualization script on the example images in ../ImageSegmentation/data
* ../ImageSegmentation/output: this is where the results of the running the visualization script are saved. 
## Selective search
In ../SelectiveSearch/, you will find ../SelectiveSearch/SelectiveSearch.py. This script gives simple visualization of the 
region proposal algorhtm using selective search.

To run the script, you need to provide argument to the input image, and to aim for fast (f) execution or quality (q) of the results.

For example, if the input image is ObjectDetection/selective_search/data/dog.png, and we want fast execution, you can run the following command:

`python3 ObjectDetection/selective_search/SelectiveSearch.py ObjectDetection/selective_search/data/dog.png f`

The script will create a window showing the region proposal results. While having the window selected. you may press:
* **M** for showing more proposed regions
* **L** for showing fewer proposed regions
* **Q** for quit the script

## Questions?
For any questions or concerns, 
please email to Ziheng (Leo) Li <zl2990@columbia.edu>, Lechen Li <ll3097@columbia.edu>, Adithya Narayana <an3017@columbia.edu>

## References
[1] https://lilianweng.github.io/lil-log/2017/10/29/object-recognition-for-dummies-part-1.html

[2] Felzenszwalb, Pedro F., and Daniel P. Huttenlocher. "Efficient graph-based image segmentation." International journal of computer vision 59.2 (2004): 167-181.

[3] https://github.com/salaee/pegbis

[4] https://sandipanweb.wordpress.com/2018/02/25/graph-based-image-segmentation-in-python/

[5] https://learnopencv.com/selective-search-for-object-detection-cpp-python/

[6] https://www.koen.me/research/selectivesearch/

[7] https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/#:~:text=In%20the%20end%2C%20we%20end,2%20%2B%203%20%2B%205).&text=Time%20Complexity%3A,Time%20Complexity%20of%20the%20algorithm.

[8] https://www.geeksforgeeks.org/selective-search-for-object-detection-r-cnn/

