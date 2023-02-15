yolo_gpt

A playground to test integration between GPT3 and Object Recognition using Python.

Introduction
The OpenAI YOLOv8 is a project that demonstrates the integration between GPT-3 and Object Recognition using Python. The project provides a GUI where users can input an image, detect objects in the image using YOLOv8, and generate 5 simple recipes based on the detected objects using GPT-3.

Prerequisites
Before running the project, make sure you have the following installed:

Python 3
tkinter
PIL
openai
ultralytics
Installation
To install the required packages, run the following command in your terminal:

Copy code
pip install tkinter pillow openai yolov5-0.9
Usage
To use the project, simply run the following command in your terminal:

Copy code
python yolo_gpt.py
After running the script, a GUI will be displayed with a drag and drop window where you can input an image, and a results window where the generated recipes will be displayed.

To generate the recipes, simply input an image by clicking on the "Input Image" button and then follow the prompts.

To clear the input and results window, click on the "Clear Input and Results" button.

Note: To use the GPT-3 integration, you will need to have your own OpenAI API key. Update the "Your Own OpenAI API Key" placeholder in the code with your actual API key.

Credits
This project was made possible with the help of the following libraries:

tkinter
PIL
openai
ultralytics
License
This project is licensed under the MIT License. See the LICENSE file for details.
