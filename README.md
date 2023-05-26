# Assembly Step Recorder
Allows the end-user to record step-by step processes for assembling (or disassembling!) things using a webcam.
- *November 2022*

![webcam main window overview](https://github.com/Josiah-Cooksey/portfolio/assets/108890925/c2d6c033-afa2-4dd9-ba91-22e3715ebfde)

## Features:
- Video recording functionality
- Simple GUI
- Recording preview
- Image snapshots
- First and final frame previews
- Optional ability to add notes for each step
- Customisable output locations and file names using the native file explorer
- Webcam channels switching

## See it in action! Full demo run ---> 
TODO

## Setup
- pip install -r requirements.txt


## Usage
### **Webcam Channels:**
At the top of the GUI, the left and right buttons can be used to switch between webcam channels; although this is almost never necessary, it is useful for those with more than a single webcam connected to their PCs.

![webcam channel switching buttons](https://github.com/Josiah-Cooksey/portfolio/assets/108890925/a3c1da0d-bf61-4738-9bca-83309fd23dc3)

### **Image Snapshots:**
The "Capture Image" button just beneath the channel settings can be used to take a picture - all the images that you capture this way will be added to a queue of images that will be included in the same folder with the video recording when saved.

![capture image button](https://github.com/Josiah-Cooksey/portfolio/assets/108890925/d02618af-d7ac-472f-abeb-611bb882895d)

### **Input Preview:**
Below that, there is a preview of the current input of the selected webcam channel, which you can use to adjust your shot before capturing.

![webcam preview](https://github.com/Josiah-Cooksey/portfolio/assets/108890925/183fd0c8-e1c9-4b36-ba33-a55790bec290)

### **Video Recording:**
Underneath, there are three buttons, "Start", "Pause", and "Stop" recording, respectively; the function of each of these are fairly self-evident, but I will explain them in detail:
- *Start*:
    - Begins recording video input from the selected webcam; don't start until your shot is ready!
- *Pause*:
    - Temporarily stops recording and changes its text to "Resume"; when clicked again, it regains its original text and continues recording webcam input to the same buffer, allowing for more dynamic cuts in a single video.
- *Stop*:
    - Stops recording and switches to the save GUI.

![recording control buttons](https://github.com/Josiah-Cooksey/portfolio/assets/108890925/2c8101d0-776a-4a79-81be-5c7902363996)

### **Saving Input:**
You're probably itching to move on to recording the next step, but hold it right there, buckaroo - you need to save it first.
After you stop recording, the app will show a save GUI.

![save window overview](https://github.com/Josiah-Cooksey/portfolio/assets/108890925/fc6a8f31-4776-45d4-bf06-d5b6581ac9e0)

At the top, in the field labeled "Save To:", you can manually type the directory + filename with no extension to save the output, but if you're not a masochist, click the "Save Data" button to do it in the native file browser.

![save location fields](https://github.com/Josiah-Cooksey/portfolio/assets/108890925/8a62b313-d136-4907-8b0d-c8e898a5eeba)

Next, you can optionally add notes to be saved in a text file alongside the video and images, but if you already have explanations in the video, there's no need.

![note input field](https://github.com/Josiah-Cooksey/portfolio/assets/108890925/986b4e82-4d4c-4681-a99d-3c50789a1d09)

Finally, there are first and final frame previews for a definite confirmation that you captured what you wanted:

![first and last frame previews](https://github.com/Josiah-Cooksey/portfolio/assets/108890925/ed34e29f-7f5e-46f3-90d2-bb50d1260b53)

You can now save the output.

![submit save button](https://github.com/Josiah-Cooksey/portfolio/assets/108890925/22f04b9e-8cb5-42f8-86ac-7d190841d2b1)

However, if you decide that you would like to discard everything and try again, just close and restart the program.
