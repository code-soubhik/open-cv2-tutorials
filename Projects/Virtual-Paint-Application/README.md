# Virtual Paint Application

This project is a virtual paint application that allows you to draw on the screen using hand gestures detected via a webcam. It uses MediaPipe Holistic for hand tracking and OpenCV for image processing and drawing.

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/code-soubhik/open-cv2-practice.git
   ```

2. Navigate to the Virtual Paint Application directory:
   ```bash
   cd open-cv2-practice/Projects/Virtual-Paint-Application
   ```

3. Set up the environment:\
   For Windows
   ```bash
   python -m venv myenv
   source myenv/Scripts/activate
   ```

   For macOS/Linux:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the project:
   ```bash
   python main.py
   ```

## Features

- **Color Selection**: Choose a color by placing the tip of your left-hand index finger over the color panels located at the top of the screen.
- **Drawing**: To draw, touch the tip of your right-hand index finger to your right thumb tip, then move your hand to begin sketching.
- **Clear Screen**: Clear the canvas by moving your left-hand index finger over the "Clear Screen" area.

## Prerequisites

- Python 3.x
- Webcam


## Usage

Once the run script will start executing.
The webcam will open, and you can start painting using your hands. 
Follow the instructions displayed on the screen.

Press `ESC` to exit the application.

## Dependencies

- OpenCV (opencv-python >= 4.11.0)
- MediaPipe (>= 0.10.0)
- NumPy (>= 1.26.0)

## Troubleshooting

### Common Issues:

1. **Webcam not detected:**
   - Ensure your webcam is properly connected
   - Check if other applications are using the webcam
   - Try running the script with administrator/sudo privileges

2. **Virtual Environment Issues:**
   - On Windows, if `source` command is not recognized, try using:
     ```bash
     .\myenv\Scripts\activate
     ```
   - On macOS/Linux, if you get permission errors:
     ```bash
     chmod +x myenv/bin/activate
     ```

3. **Import Errors:**
   - Make sure you've activated the virtual environment
   - Try reinstalling the requirements:
     ```bash
     pip install --upgrade -r requirements.txt
     ```

For additional issues, please open an issue on the GitHub repository.
