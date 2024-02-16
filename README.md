# Image Color Frequency Analyzer

## Overview

This web application allows users to upload an image and analyzes the frequency of colors in the image. It then displays the top 10 most frequent colors along with their respective frequencies.

## Prerequisites

- Python 3.x
- Flask
- OpenCV (cv2)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Anandoptimus/Day92.git
    ```

2. **Install the required dependencies:**

    ```bash
    pip install flask opencv-python
    ```

## Usage

1. **Navigate to the project directory:**

    ```bash
    cd Day92
    ```

2. **Run the Flask application:**

    ```bash
    python main.py
    ```

3. **Open your web browser and go to [http://localhost:5000](http://localhost:5000).**

4. **Upload an image using the provided form and click on the "Upload" button.**

5. **View the top 10 most frequent colors and their frequencies.**

## Project Structure

- `main.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates.
  - `index.html`: The main page with the image upload form.
  - `msg.html`: Displaying the top 10 most frequent colors.
- `static/`: Directory containing static files such as CSS.
  - `css/styles.css`: CSS styling for the HTML templates.

## Screenshot

![image](https://github.com/Anandoptimus/Day92/assets/101982906/668c03e6-a858-40f6-b14b-a9dbabcd9be7)

![image](https://github.com/Anandoptimus/Day92/assets/101982906/29d08a72-0d5d-4af0-89fd-92668c10f0d7)


## Contributing

If you'd like to contribute to the project, please follow the standard GitHub flow: fork the repository, create a branch, make changes, and create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
