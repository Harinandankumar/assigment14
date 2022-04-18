#!/usr/bin/env python
# coding: utf-8

# 1. What does RGBA stand for?
# 
# 
# 
# Ans:-
#       RGBA is a four-channel format containing data for Red, Green, Blue, and an Alpha value. Where Alpha Represents the Opacity

# 2. From the Pillow module, how do you get the RGBA value of any images?
# 
# 
# 
# Ans:-
#     ImageColor.getcolor() gives rgba value of any image

# 3. What is a box tuple, and how does it work?
# 
# 
# Ans:-
#     A box tuple is a tuple value of four integers: the left-edge x-coordinate, the top-edge y-coordinate,the width, and the height, respectively.

# 4. Use your image and load in notebook then, How can you find out the width and height of an Image object?
# 
# 
# 
# Ans:-

# In[19]:


#Example Program
from PIL import Image
pic = Image.open('Pic.jpg')
print(f'Width, Height -> {pic.size}') # Approach 1
print(f'Width, Height -> {pic.width},{pic.height}') # Approach 2
width,height = pic.size
print(f'Width, Height -> {width},{height}') # Approach 3


# 5. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?
# 
# 
# 
# Ans:-

# In[20]:


from PIL import Image
img = Image.open('Pic.jpg')
new_img = img.crop((0,50,50,50))


# 6. After making changes to an Image object, how could you save it as an image file?
# 
# 
# Ans:-

# In[ ]:


#Example Program
from PIL import Image
pic = Image.open('pic.jpg')
pic.save('pic2.jpg')


# 7. What module contains Pillow’s shape-drawing code?
# 
# 
# Ans:-
#      Pillows ImageDraw module contains Shape drawing methods

# 8. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?
# 
# 
# 
# Ans:-
#       ImageDraw objects have shape-drawing methods such as point(), line(), or rectangle().They are returned by passing the Image object to the ImageDraw.Draw() function.
