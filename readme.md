# Streamlit QR Code Generator

This repository contains the source code for a Streamlit app that generates downloadable QR codes from text inputs like URLs or emails or any text that you wish to convert into a qr-code. The app is very straightforward and easy to use.

## Live App
The app is deployed and can be accessed here: [Streamlit QR Code App](https://stramlit-qrcode.streamlit.app/)

## Features
- Generate QR codes from any text (URL, email, etc.)
- Download the generated QR code as an image

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Docker (optional, for running with Docker)

### Running Locally

1. **Clone the Repository**

    ```bash
    git clone https://github.com/ahmad-zurih/streamlit_qrcode.git
    cd streamlit_qrcode
    ```

2. **Install Requirements**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the App**

    ```bash
    streamlit run home.py
    ```

    The app will start running on `http://localhost:8501`.

### Running with Docker

1. **Using Docker Compose**

    This is the easiest way to get started with Docker:

    ```bash
    docker-compose up
    ```

    The app will be available at `http://localhost:8510`. you can edit the port number in the Dockerfile

2. **Using Dockerfile**

    Alternatively, you can build and run the container manually:

    ```bash
    docker build -t streamlit_qrcode .
    docker run -p 8510:8510 streamlit_qrcode
    ```

    The app will be running on `http://localhost:8510`.


