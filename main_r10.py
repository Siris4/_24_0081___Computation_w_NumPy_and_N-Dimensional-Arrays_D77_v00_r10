from PIL import Image  # Import the Image class from the PIL library
import numpy as np

# Full path to the image file
file_name = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0081__Day77_Computation_w_NumPy_and_N-Dimensional Arrays__240822\NewProject\r00-r09 START\r00_env_START\yummy_macarons.jpg'

# Open the image file
my_img = Image.open(file_name)

# Convert the image to a NumPy array
img_array = np.array(my_img)

# Invert the colors by subtracting each value from 255
inverted_img_array = 255 - img_array

# Print out the original and inverted values for a specific pixel range for comparison
# (For large images, printing all values isn't practical, so let's just do a section, e.g., first 5 rows and columns)
print("Original pixel values (first 5 rows and columns):")
print(img_array[:5, :5])

print("\nInverted pixel values (first 5 rows and columns):")
print(inverted_img_array[:5, :5])

# Convert the inverted array back to an image
inverted_img = Image.fromarray(inverted_img_array)

# Save the inverted image if you want to save it
inverted_img.save(r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0081__Day77_Computation_w_NumPy_and_N-Dimensional Arrays__240822\NewProject\r00-r09 START\r00_env_START\inverted_yummy_macarons.jpg')

# Display the inverted image
inverted_img.show()

# To confirm it's a NumPy array, you can print its type and shape
print("\nType of inverted_img_array:", type(inverted_img_array))
print("Shape of inverted_img_array:", inverted_img_array.shape)

###
Original pixel values (first 5 rows and columns):
[[[66 47 30]
  [67 48 31]
  [68 49 32]
  [69 50 33]
  [68 49 32]]

 [[66 48 28]
  [66 48 28]
  [68 50 30]
  [70 52 32]
  [70 52 32]]

 [[66 48 28]
  [65 47 27]
  [67 49 29]
  [70 52 32]
  [72 54 34]]

 [[66 48 28]
  [64 46 26]
  [65 47 27]
  [68 50 30]
  [70 52 32]]

 [[66 48 28]
  [64 46 26]
  [63 45 25]
  [65 47 27]
  [67 49 29]]]

Inverted pixel values (first 5 rows and columns):
[[[189 208 225]
  [188 207 224]
  [187 206 223]
  [186 205 222]
  [187 206 223]]

 [[189 207 227]
  [189 207 227]
  [187 205 225]
  [185 203 223]
  [185 203 223]]

 [[189 207 227]
  [190 208 228]
  [188 206 226]
  [185 203 223]
  [183 201 221]]

 [[189 207 227]
  [191 209 229]
  [190 208 228]
  [187 205 225]
  [185 203 223]]

 [[189 207 227]
  [191 209 229]
  [192 210 230]
  [190 208 228]
  [188 206 226]]]

Type of inverted_img_array: <class 'numpy.ndarray'>
Shape of inverted_img_array: (533, 799, 3)
