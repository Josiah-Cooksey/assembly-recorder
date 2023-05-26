# Assembly Step Recorder
Allows the end-user to record step-by step processes for assembling (or disassembling!) things using a webcam.
- *November 2022*

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

### **Image Snapshots:**
The "Capture Image" button just beneath the channel settings can be used to take a picture - all the images that you capture this way will be added to a queue of images that will be included in the same folder with the video recording when saved.

### **Input Preview:**
Below that, there is a preview of the current input of the selected webcam channel, which you can use to adjust your shot before capturing.

### **Video Recording:**
Underneath, there are three buttons, "Start", "Pause", and "Stop" recording, respectively; the function of each of these are fairly self-evident, but I will explain them in detail:
- *Start*:
    - Begins recording video input from the selected webcam; don't start until your shot is ready!
- *Pause*:
    - Temporarily stops recording and changes its text to "Resume"; when clicked again, it regains its original text and continues recording webcam input to the same buffer, allowing for more dynamic cuts in a single video.
- *Stop*:
    - Stops recording and switches to the save GUI.


### **Saving Input:**
You're probably itching to move on to recording the next step, but hold it right there, buckaroo - you need to save it first.
After you stop recording, the app will show a save GUI.

At the top, in the field labeled "Save To:", you can manually type the directory + filename with no extension to save the output, but if you're not a masochist, click the "Save Data" button to do it in the native file browser.

Next, you can optionally add notes to be saved in a text file alongside the video and images, but if you already have explanations in the video, there's no need.

Finally, there are first and final frame previews for a definite confirmation that you captured what you wanted; you can now submit and return to the main window.

However, if you decide that you would like to discard everything and try again, just close and restart the program.