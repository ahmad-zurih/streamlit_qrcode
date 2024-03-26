import streamlit as st
import qrcode
from PIL import Image, ImageOps
import io
import random

# Streamlit application
def main():
    st.title("QR Code Generator")

    # Input from user
    link = st.text_area("Insert a link, phone number, email, or a value to make it into a QR Code:")

    # Color selection
    fg_color = st.color_picker('Choose the foreground color for your QR Code', '#000000')  # Default to black
    bg_color = st.color_picker('Choose the background color for your QR Code', '#FFFFFF')  # Default to white

    # Option for inverted QR code
    inverted = st.checkbox("Generate Inverted QR Code")

    # Allow the user to choose the size of the QR code
    size = st.slider('Choose the size of your QR Code', min_value=1, max_value=30, value=10)  # Default to 10, adjust min/max as needed

    if st.button("Generate QR Code"):
        out = link.replace(r'\n', '\n')

        qr = qrcode.QRCode(
            version=None,  # Automatic version selection
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=size,  # User-selected size
            border=5)
        qr.add_data(out)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fg_color, back_color=bg_color).convert('RGB')

        # Invert colors if selected
        if inverted:
            img = ImageOps.invert(img)

        # Convert to a format that can be displayed by Streamlit
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        img = Image.open(buf)

        # Display the image
        st.image(img, caption='Generated QR Code')

        # Provide a download button
        buf.seek(0)
        st.download_button(
            label="Download QR Code",
            data=buf,
            file_name=f"qrcode{random.randint(10000,100000)}.png",
            mime="image/png"
        )
    
    # Creator and contact information
    st.markdown("---")
    st.markdown(
        """
        <p style='text-align: center; color: gray; font-size: small;'>
            The app was created by Ahmad Alhineidi. It mainly utilises the following python modules (streamlit, qrcode, PIL). 
            Contact <a href='mailto:ahmadhineidi@hotmail.com' style='text-decoration: none; color: gray;'>ahmadhineidi@hotmail.com</a> for issues or bugs.
        </p>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
