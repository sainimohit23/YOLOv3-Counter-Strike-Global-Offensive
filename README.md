# YOLOv3-Counter-Strike-Global-Offensive
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

This program is trained to detect and classify `terrorists` and `counter-terrorists` from a CS:GO gameplay clip. I made a dataset containing 434 images from CS:GO gameplay. Then I labelled the bounding box manually for each image and trained YOLOv3 model on the dataset. 

### Dependencies
* Tensorflow
* Keras
* Pillow
* Numpy
* Matplotlib
* Time
* colorsys
* OpenCV
* os

### Quick Start
1. Run `convert.py` to convert darknet weights to keras weights. Download darknet model from [YOLO website](http://pjreddie.com/darknet/yolo/).
2. Use `create_annotationsV2.py` to manually create annotations for images and save them to `train.txt` file. I have already done that boring part for you.

   
   * Press 1 to set class to '0' (CT).
   * Press 2 to set class to '1' (Terrorists).
   * '0' is the default class for every image.
   
   
   Example1:
   ![screenshot_23](https://user-images.githubusercontent.com/26195811/47453100-78de8180-d7e9-11e8-90e6-9c3deadbf276.png)
   Example2:
   ![screenshot_24](https://user-images.githubusercontent.com/26195811/47455710-2d7ba180-d7f0-11e8-968c-7303ed3d66d1.png)

3. Modify `train.py` and start training. I have already included a trained `tiny_yolo` model.
4. `yolo_video.py` uses trained model to detect objects in video/images.
   


To know more about issues and the YOLOv3 implementation that I used, refer to [qqwweee/keras-yolo3](https://github.com/qqwweee/keras-yolo3).
To learn the implementation of annotations tool watch this tutorial  [mark-jay-yolo](https://www.youtube.com/watch?v=PyjBd7IDYZs&list=PLX-LrBk6h3wSGvuTnxB2Kj358XfctL4BM).


---

### Result obtained using tiny_yolo model

![sample](sample.gif)



Above sample struggles to classify terrorists properly. Since it is obtained using tiny_yolo model, something like this was expected. I don't have a gpu to train full model.
