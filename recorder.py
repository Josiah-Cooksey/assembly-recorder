import datetime
import os
import shutil
import cv2
import keycodes
import PySimpleGUI as sg


tooltipCharacter = "i"
helpCharacter = "?"

windowWidth = 600
windowHeight = 350

captureWidth = 640
captureHeight = 480

imageDisplayWidth = (windowWidth / 2)
imageDisplayHeight = (imageDisplayWidth / captureWidth) * captureHeight
# known valid formats: avi, mp4
videoFormat = "mp4"
tempVideoFilename = "output"

imageFormat = "png"
tempImageFilename = "output"

fps = 30

timeout = 1000//fps

webcamChannel = 0

bigFont = "Helvetica 20"

# recording times
"""hours = 0
minutes = 0
seconds = 0
framesRecorded = 0"""

def main():
    shouldContinue = True
    while shouldContinue:
        shouldContinue = startProcess()

def startProcess():
    global webcamChannel
    """global hours
    global minutes
    global seconds"""
    # initialise webcam
    cam = cv2.VideoCapture(webcamChannel)

    # video capture output stream
    out = ""
    recording = False
    pausedRecording = False
    firstFrame = ""
    lastFrame = ""
    screenshotsCaptured = 0

    # show the recording window first
    window = constructWindow("webcam")
    # reference the elements we'll need to update at some point
    webcamImage = window["webcamImage"]
    pauseButton = window["togglePause"]
    webcamInfo = window["webcamInfo"]
    # recordTimer = window["timer"]
    recordingIndicator = window["recordingIndicator"]
    

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break

        event, values = window.read(timeout=timeout)
        # print(event)

        if event == sg.WIN_CLOSED or event == "Exit":
            return False

        elif event == "captureImage":
            screenshotsCaptured += 1
            # imageName = f"{datetime.datetime.now().strftime('%a %d-%m-%Y %H-%M-%S')}.{imageFormat}" 
            imageName = f"{tempImageFilename}-{str(screenshotsCaptured).zfill(2)}.{imageFormat}" 
            cv2.imwrite(imageName, frame)

        elif event == "startRecording":
            recordingIndicator.update("Recording")
            # you can press S repeatedly to change the start of the video to the current time of your keypress
            # define the codec and create VideoWriter object
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(tempVideoFilename + "." + videoFormat, fourcc, 20.0, (captureWidth, captureHeight))
            recording = True
            pausedRecording = False
            # update the first frame image variable
            firstFrame = frame
            # framesRecorded = 0

        elif event == "stopRecording":
            if recording:
                recordingIndicator.update(" ")
                try:
                    lastFrame = frame
                    # save and close the output stream
                    out.release()
                    # save the first and last frames as images
                    cv2.imwrite(tempImageFilename + "_first." + imageFormat, firstFrame)
                    cv2.imwrite(tempImageFilename + "_last." + imageFormat, lastFrame)
                    recording = False
                    """hours = 0
                    minutes = 0
                    seconds = 0
                    framesRecorded = 0"""
                except:
                    continue
                if recording == False:
                    window.close()
                    window = constructWindow("saveOptionsWindow")

                    while True:
                        event, values = window.read()
                        print(values)
                        if event == sg.WIN_CLOSED or event == "Exit":
                            return False
                        
                        elif event == "helpMenu1":
                            sg.popup("help menu1 text here blah blah blah lorem ipsem")
                        match(event):
                            case "recordNew":
                                if values["savePath"] != "":
                                    try:
                                        # notes
                                        with open(values["savePath"] + "_notes.txt", "w") as file:
                                            file.write(values["notes"])
                                        # save video
                                        shutil.move(tempVideoFilename + "." + videoFormat, values["savePath"] + "." + videoFormat)
                                        # no need to move the first and last frames due to the below transferring loop for screenshots
                                        """# first frame
                                        shutil.move(tempImageFilename + "_first." + imageFormat, values["savePath"] + "_frame_first." + imageFormat)
                                        # last frame
                                        shutil.move(tempImageFilename + "_last." + imageFormat, values["savePath"] + "_frame_last." + imageFormat)"""
                                        
                                        # transfer and rename all screenshots
                                        filesInCurrentFolder = os.listdir(os.getcwd())
                                        if not len(filesInCurrentFolder) == 0:
                                            # for each of those files
                                            for filename in filesInCurrentFolder:
                                                # splits the filename and the extension
                                                splitFilename = filename.rsplit(".", 1)
                                                if len(splitFilename) == 2:
                                                    if splitFilename[1] == imageFormat:
                                                        # last frame
                                                        shutil.move(filename, values["savePath"] + filename)
                                    except:
                                        continue
                                window.close()
                                cam.release()
                                return True

        elif event == "togglePause":
            pausedRecording = not pausedRecording
            if pausedRecording:
                pauseButton.update("Resume Recording")
                recordingIndicator.update("Paused")
            else:
                pauseButton.update("Pause Recording")
                recordingIndicator.update("Recording")

        elif event == "decreaseWebcamIndex":
            try:
                webcamChannel -= 1
                webcamInfo.update(f"Webcam Channel: ({webcamChannel})")
                cam.release()
                cam = updateCam()
            except:
                continue

        elif event == "increaseWebcamIndex":
            try:
                webcamChannel += 1
                webcamInfo.update(f"Webcam Channel: ({webcamChannel})")
                cam.release()
                cam = updateCam()
            except:
                continue
        


        # update the "image" in the GUI with a new frame from the webcam
        imgbytes = cv2.imencode('.ppm', frame)[1].tobytes()  # can also use png.  ppm found to be more efficient
        webcamImage.update(data=imgbytes)
        
            
        # if we're recording
        if recording:
            if not pausedRecording:
                # read from the webcam
                success, buf = cam.read()
                # and write a frame
                out.write(buf)
                # increment frames recorded
                """framesRecorded += 1
                if framesRecorded >= fps:
                    framesRecorded -= fps
                    seconds += 1
                if seconds >= 60:
                    seconds -= 60
                    minutes += 1
                if minutes >= 60:
                    minutes = 0
                    hours += 1
                recordTimer.update(f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")"""
                
        else:
            try:
                # save and close the output stream
                out.release()
                framesRecorded = 0
            except:
                continue
    return False

def updateCam():
    return cv2.VideoCapture(webcamChannel)

def yscroll(self, event):   # tkinter code
    if self.canvas.yview() == (0.0, 1.0):
        return
    if event.num == 5 or event.delta < 0:
        self.canvas.yview_scroll(1, "unit")
    elif event.num == 4 or event.delta > 0:
        self.canvas.yview_scroll(-1, "unit")

# returns a different window based on the passed "index", which is really just a string for readability
def constructWindow(index):
    match(index):
        case "saveOptionsWindow":
            sg.theme("DarkTeal9")
            textAndHelp = [sg.Text("Text"), sg.Push(), sg.Text("?")]
            sg.TkScrollableFrame.yscroll = yscroll   
            homeLayout = [
                [sg.Text("Save To: "), sg.InputText(""), sg.FileSaveAs("Save Data", enable_events=True, key="savePath"), sg.Push()],
                # [sg.Push(), sg.InputText(""), sg.FileSaveAs("Save First Frame", enable_events=True, key="saveFirstFrame", file_types=[("PNG", ".png")]), sg.Push()],
                # [sg.Push(), sg.InputText(""), sg.FileSaveAs("Save Last Frame", enable_events=True, key="saveLastFrame", file_types=[("PNG", ".png")]), sg.Push()],
                # [sg.Push(), sg.Submit(), sg.Exit(), sg.Push()],
                [sg.Text("Notes:    "), sg.Multiline(size=(30, 5), key="notes"), sg.Push()],
                [sg.VPush()],
                [sg.Push(), sg.Text("first frame"), sg.Push(), sg.Text("last frame"), sg.Push()],
                [sg.Push(), sg.Image(tempImageFilename + "_first." + imageFormat, size=(imageDisplayWidth, imageDisplayHeight)), sg.Push(), sg.Push(), sg.Image(tempImageFilename + "_last." + imageFormat, size=(imageDisplayWidth, imageDisplayHeight)), sg.Push()],
                [sg.VPush()],
                [sg.Push(), sg.Button("Submit and back to recording window", enable_events=True, key="recordNew"), sg.Push()],
                [sg.VPush()],
                [sg.Text("Text"), sg.Push(), sg.Button(helpCharacter, enable_events=True, key="helpMenu1")]
            ]
            
            return sg.Window("Save Options", homeLayout)

        case "webcam":
            sg.theme("Black")
            layout = [
                [sg.Push(), sg.Text(f"Webcam Channel: ({webcamChannel})", font=bigFont, key="webcamInfo"), sg.Push(), sg.Button("   -   ", font=bigFont, key="decreaseWebcamIndex"), sg.Button("   +   ", font=bigFont, key="increaseWebcamIndex"), sg.Push()],
                [sg.Push(), sg.Button("Capture Image", font=bigFont, key="captureImage"), sg.Push()],
                # [sg.Push(), sg.Text(f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}", font=bigFont, key="timer"), sg.Push()],
                [sg.Push(), sg.Text(f"", font=bigFont, key="recordingIndicator", text_color="red"), sg.Push()],
                [sg.Push(), sg.Image(key="webcamImage"), sg.Push()],
                [sg.Push(), sg.Button("Start Recording", font=bigFont, key="startRecording"), sg.Push(), sg.Button("Pause Recording", font=bigFont, key="togglePause"), sg.Push(), sg.Button("Stop Recording", font=bigFont, key="stopRecording"), sg.Push()]
            ]

            return sg.Window("Webcam", layout, no_titlebar=False, location=(0, 0))


if __name__ == "__main__":
    main()