# Image Resizer

This is a simple image resizer web application built with Python and Streamlit. With this app, you can easily upload an image and resize it to your desired dimensions.

## Usage

1. Go to https://deepankarvarma-image-resizer-using-python-app-9d3lg8.streamlit.app/
2. Click on the "Choose an image..." button to upload an image
3. The app will display the original image size
4. Use the sliders to set the new width and height for the resized image
5. If you want to preserve the aspect ratio, check the "Preserve Aspect Ratio" checkbox
6. Click on the "Download Resized Image" button to download the resized image

## Installation

To run this app locally, you need to follow these steps:

1. Clone the repository: `git clone https://github.com/<username>/<repository>.git`
2. Install the requirements: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## Code Explanation

The code is an implementation of a simple image resizer web application built using Python and Streamlit.

The first section of the code imports the required libraries - Streamlit for building the web app and PIL (Python Imaging Library) for image manipulation.

The st.title and st.markdown functions are used to set the title and background image of the web app.

The next section of the code allows the user to upload an image. The user can choose an image in JPG, JPEG, or PNG format.

If an image is uploaded, the code opens the image and gets its size using the Image.open() function from the PIL library. The original size of the image is displayed using the st.write() function.

Next, the user can use the sliders to set the new width and height for the resized image. If the user wants to preserve the aspect ratio of the original image, they can check the "Preserve Aspect Ratio" checkbox.

If the aspect ratio is preserved, the code calculates the new height of the image based on the new width using a simple formula. The image is then resized using the image.resize() function from the PIL library.

Finally, the resized image is displayed using the st.image() function. The user can also download the resized image using the "Download Resized Image" button. When the button is clicked, the resized image is saved to the local disk using the resized_image.save() function from the PIL library, and then downloaded using the st.download_button() function from the Streamlit library.
