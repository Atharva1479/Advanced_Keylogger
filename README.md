# Advanced_Keylogger

Advanced Keylogger: It is a simple demonstration project showcasing a Python keylogger script with added functionalities. This keylogger is strictly intended for educational purposes to demonstrate Python programming skills and the use of various Python libraries responsibly. It captures and logs keyboard activity, gathers system information, records audio, takes screenshots, and securely sends the captured data to a designated email address.

Please note that this keylogger is intended for educational purposes only, and any use for unauthorized access or malicious activities is strictly prohibited. Always respect individuals' privacy and abide by all relevant laws and regulations before deploying any monitoring or logging software.

## Key Features

- **Keylogging:** Capture and log key presses, providing insights into keyboard activity.

- **System Information:** Gather essential information about the computer system, such as hostname, IP addresses, processor details, and operating system.

- **Clipboard Capture:** Log clipboard contents, tracking copied text or data.

- **Microphone Audio Capture:** Record audio from the microphone for a specified duration, allowing users to analyze audio patterns.

- **Screenshot Capture:** Take screenshots of the user's screen, aiding in visual monitoring and analysis.

- **Email Sending:** Send captured keylog data, system information, clipboard data, and screenshots to a designated email address using secure SMTP communication.

- **Encryption:** Before sending data via email, sensitive files (e.g., systeminfo.txt, clipboard.txt, and key_log.txt) are encrypted using Fernet symmetric encryption to ensure security during transmission.

## Disclaimer

The creator of this project assumes no responsibility for any misuse or damage caused by the keylogger. Users are solely responsible for their actions and must use this project in compliance with all applicable laws and regulations. Be responsible and ethical in your use of this keylogger.

## Requirements

- Python 3.6 or higher

## Usage

1. Clone the repository to your local machine.

2. Install the required Python libraries using the following command:
   pip install -r requirements.txt
   
3. Run the keylogger script using the following command:
   python keylogger.py

4. The keylogger will start capturing key presses, system information, clipboard data, and audio. It will take screenshots at regular intervals and send the captured data to the specified email address.

**Note:** Modify the `email_address`, `password`, and `toaddr` variables in the script with your email credentials and the email address where you want to receive the captured data.

## Important Note

This keylogger script is intended for educational purposes only. Do not use it for any unauthorized access, surveillance, or any malicious activities. Respect individuals' privacy, and always use it responsibly and in compliance with the law.
