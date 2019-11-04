# Hand-Detection
![alt text](https://raw.githubusercontent.com/sameli74/Hand-Detection/master/examples/example2-detected.png)
<!-- ![alt text](https://raw.githubusercontent.com/sameli74/Hand-Detection/master/examples/example4-detected.png) -->

I have trained a classifier using resnet 50 that is able to detect hands from first person viewpoint. To do so, I collected a dataset of hands and labeled them using LabelImg. In addition, I used transfer learning to save time in training phase. To test the hand detector, you need to run main.py file. Some examples and output of my classifier are available in examples folder.

# Dependencies
* Opencv
* Tensorflow (You can use tensorflow to run this project. However, main.py does not include the code for that)

# Running
```
python main.py
```
