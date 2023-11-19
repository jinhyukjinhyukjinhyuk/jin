#!/usr/bin/env python
# coding: utf-8

# In[10]:


from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Load the trained model
model = load_model("keras_Model.h5", compile=False)

# Load the class labels
class_names = open("labels.txt", "r").readlines()

# Create an array to feed the model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Load and preprocess the image you want to classify
image = Image.open("C:/Users/98wkd/reverset/11.jpg").convert("RGB")
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
data[0] = normalized_image_array

# Make a prediction using the model
prediction = model.predict(data)

# Get the predicted class index
predicted_class_index = np.argmax(prediction)

# Get the class name from the labels file
class_name = class_names[predicted_class_index]

# Get the confidence score
confidence_score = prediction[0][predicted_class_index]

# Print the prediction and confidence score
print("Predicted Class:", class_name.strip())
print("Confidence Score:", confidence_score)


# In[ ]:




