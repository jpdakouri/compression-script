#### IN PROGRESS ####

import os
import sys
import subprocess
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import ffmpeg

# ask user about directory
# input_folder = askdirectory(title="Source Location")
# messagebox.showinfo("Information", "Select output folder")
# output_folder = askdirectory(title="Destination Location")

# ask user aboutnumber of threads to use 
num_threads = input("Indicate the number of threads to use : ")
print(num_threads + " threads will be used")


# ask user about directory in CL
input_folder = output_folder = os.getcwd()
print("Using " + input_folder + " as the current directory ")

# remove processed files
# delete_input_file = True


# remove substring 
# substring = "_h265"

# containers type list
container_extensions = [".m4v", ".mp4", ".mov", ".webm"]

# ffmpeg
# def ffmpeg_fonction(input_file,num_threads):
#     input = ffmpeg.input(input_file)
#     audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
#     video = input.video.hflip()
#     out = ffmpeg.output(audio, video, 'out.mp4')


if os.listdir(input_folder).count == 0:
    sys.exit("Error: No file to be found")
else:
# loop through all video files in the input folder
    for filename in os.listdir(input_folder):
        if any((filename.endswith(extension) for extension in container_extensions)):

            # build the ffmpeg command
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(
                output_folder, os.path.splitext(filename)[0] + "_h265.mp4"
            )

            command_ffmpeg_bar = [
                "ffmpeg-bar",
                "-i",
                input_file,
                "-c:v",
                "libx265",
                "-crf",
                "24",
                "-preset",
                "medium",
                "-c:a",
                "aac",
                "-b:a",
                "128k",
                "-threads",
                str(num_threads),
                output_file,
            ]

            subprocess.run(command_ffmpeg_bar, shell=True)
            if delete_input_file:
                os.remove(input_file)
            
            for filename in os.listdir(input_folder):
                if substring in filename:
                    new_filename = filename.replace(substring, "")
                    os.rename(os.path.join(input_folder, filename), os.path.join(input_folder, new_filename)) 

                    print(f"Renamed {filename} to {new_filename}")
                    print(f"File {new_filename} is finished. Saved")


