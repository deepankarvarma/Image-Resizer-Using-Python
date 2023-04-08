import streamlit as st
from PIL import Image

# Define the Streamlit app
st.title("Image Resizer")
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.teahub.io/photos/full/24-245583_black-diamond-background-hd.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
# Allow the user to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If an image is uploaded, display its size and allow the user to resize it
if uploaded_file is not None:
    # Open the image and get its size
    image = Image.open(uploaded_file)
    width, height = image.size
    st.write(f"Original Image Size: {width} x {height}")

    # Allow the user to resize the image
    new_width = st.slider("New Width", 1, 1000, width)
    new_height = st.slider("New Height", 1, 1000, height)
    preserve_aspect_ratio = st.checkbox("Preserve Aspect Ratio", value=True)

    # Resize the image
    if preserve_aspect_ratio:
        new_height = int(new_width / width * height)
    resized_image = image.resize((new_width, new_height))

    # Display the resized image
    st.image(resized_image, caption=f"Resized to {new_width} x {new_height}")

    # Add a button to download the resized image
    download_button = st.button("Download Resized Image")
    if download_button:
        st.download_button(
            label="Download",
            data=resized_image.save("resized_image.jpg"),
            file_name="resized_image.jpg",
            mime="image/jpeg"
        )
