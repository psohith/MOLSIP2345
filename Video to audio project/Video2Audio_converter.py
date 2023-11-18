import moviepy.editor
from tkinter.filedialog import askopenfilename
from tkinter import *

def video_to_audio():
    try:
        label.config(text="Select file...",bg="white" ,fg="black")
        
        video_path = askopenfilename()
        label.config(text="Conversion begins...")
        
        video_name = video_path.split('/')[-1].split('.')[0]
        audio_file = video_name + '.mp3'

        video_clip = moviepy.editor.VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_file)

        text = f"{video_name}.mp4 is converted into {audio_file}"
        label.config(text=text ,bg="#00ff1a", fg="black")
        print("Conversion successful!")
    
    except Exception as e:
        label.config(text="Invalid file selected" , bg = "#e60000" , fg="#000000")
    
    finally:
        btn.config(text="Click here for a new one")

# Create the main window
window = Tk()
window.title("File selection window")

# Create and configure widgets
label = Label(window, text="", padx=10, pady=10)
btn = Button(window, text="Click here to select the video file", command=video_to_audio, padx=60, pady=70, bg="#001840" ,fg="#ffffff")

# Grid layout
label.grid(row=1, column=0)
btn.grid(row=0, column=0)

# Start the Tkinter event loop
window.mainloop()

print("Program finished")
