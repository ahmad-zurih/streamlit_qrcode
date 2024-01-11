import streamlit as st
import qrcode
from PIL import Image
import io
import random

# Streamlit application
def main():
    st.title("QR Code Generator")

    # Input from user
    link = st.text_area("Insert a link, phone number, email or a value to make it into a QR Code. Use newline for a new line:")

    if st.button("Generate QR Code"):
        out = link.replace(r'\n', '\n')

        qr = qrcode.QRCode(
            version=1,
            box_size=30,
            border=10)

        qr.add_data(out)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

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
        The app was created by Ahmad Alhineidi. It mainly utilites the following python modules (streamlit, qrcode, PIL). 
        Contact <a href='mailto:ahmadhineidi@hotmail.com' style='text-decoration: none; color: gray;'>ahmadhineidi@hotmail.com</a> for issues or bugs.
     </p>
    """, 
    unsafe_allow_html=True
   )


if __name__ == "__main__":
    main()
