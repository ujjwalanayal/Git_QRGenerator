**GitHub QR Code Generator**
This project is a simple Python script that generates a personalized QR code for a GitHub profile. The QR code is a square image with an embedded GitHub logo in the center and the GitHub username displayed below it.

**Features**
Generates a QR code for a given GitHub profile URL.

Embeds the official GitHub logo in the center of the QR code.

Adds the username as text below the QR code.

Saves the final image as 

github_profile_qr.png.


Uses a .gitignore file to ensure the generated QR code image is not committed to the repository.

**Requirements**
The script requires the following Python libraries:


**Pillow**: A Python Imaging Library fork used for image processing, such as creating the final image, resizing the logo, and adding text.


**qrcode**: A library used to generate the QR code from the URL.

You can install these dependencies using pip and the requirements.txt file provided in the repository:

**Bash**

pip install -r requirements.txt

**How to Use**
Clone the repository to your local machine.

Install the required libraries using the command above.

**Run the main.py script:**

Bash

python main.py

Enter the GitHub URL and username when prompted by the script.

The script will then generate a new image file named 

github_profile_qr.png in the same directory.
