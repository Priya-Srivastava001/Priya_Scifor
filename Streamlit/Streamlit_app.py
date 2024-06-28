import streamlit as st

# Set the title of the app
st.title("Streamlit App")

# Add a button widget
if st.button('Click Here'):
    st.write("Hello, My Name is Priya Srivastava, and currently associated with Meta Scifor Technologies Pvt. Ltd.")

# Add a slider widget
slider_value = st.slider('Select a number', 0, 100, 50)
st.write(f'Selected number: {slider_value}')

# Display an image with a caption using a raw string for the file path
# Ensure the file path is correct
image_path = r"C:\Users\Priya\IMG20230515165806.jpg"
st.image(image_path, caption="Picture of mine working in previous company.", use_column_width=True)

