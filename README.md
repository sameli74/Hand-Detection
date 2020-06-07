# Hand Detection Using Transfer Learning 
![alt text](https://raw.githubusercontent.com/sameli74/Hand-Detection/master/examples/example2-detected.png)
<!-- ![alt text](https://raw.githubusercontent.com/sameli74/Hand-Detection/master/examples/example4-detected.png) -->

A Hand Detection system based on ResNet50 and SSD. 


# Training Procedure
I collected a dataset of hands and labeled them using LabelImg. Afterwards,the transfer learning method is used to save time in training phase.

# Dependencies
* Opencv
* Tensorflow (You can use tensorflow to run this project. However, main.py does not include the code for that)

# Testing the Model

To test the hand detector, you need to run main.py file. Some examples and output of my classifier are available in examples folder.
```
python main.py
```
