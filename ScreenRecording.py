import cv2 as c
import pyautogui as p
import numpy as np
import pyaudio
import wave
import time
import threading
import moviepy.editor as mpe

def record_audio(audio_filename, audio_frames, sample_format, channels, rate, stop_event):
    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    frames_per_buffer=1024,
                    input=True)

    print("Recording audio...")

    try:
        while not stop_event.is_set():
            data = stream.read(1024)
            audio_frames.append(data)
    except Exception as e:
        print(f"Audio recording error: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        print("Audio recording stopped.")

def save_audio(audio_filename, audio_frames, sample_format, channels, rate):
    wf = wave.open(audio_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(audio_frames))
    wf.close()

def combine_audio_video(video_filename, audio_filename):
    video = mpe.VideoFileClip(video_filename)
    audio = mpe.AudioFileClip(audio_filename)
    final_video = video.set_audio(audio)
    final_video.write_videofile(f"final_{video_filename}", codec='libx264')

def record_video(video_filename, audio_filename, fps, rs, sample_format, channels, rate):
    fourcc = c.VideoWriter_fourcc(*get_codec(video_filename))
    video_output = c.VideoWriter(video_filename, fourcc, fps, rs)
    audio_frames = []
    stop_event = threading.Event()

    c.namedWindow("Live_Recording", c.WINDOW_NORMAL)
    c.resizeWindow("Live_Recording", 600, 400)

    audio_thread = threading.Thread(target=record_audio, args=(audio_filename, audio_frames, sample_format, channels, rate, stop_event))
    audio_thread.start()

    try:
        while True:
            img = p.screenshot()
            frame = np.array(img)
            frame = c.cvtColor(frame, c.COLOR_RGB2BGR)
            video_output.write(frame)
            c.imshow("Live_Recording", frame)

            if c.waitKey(1) == ord("q"):
                stop_event.set()
                break

            time.sleep(0.1)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        stop_event.set()
        audio_thread.join()
        video_output.release()
        c.destroyAllWindows()
        save_audio(audio_filename, audio_frames, sample_format, channels, rate)
        combine_audio_video(video_filename, audio_filename)

def get_codec(filename):
    if filename.endswith('.avi'):
        return 'XVID'
    elif filename.endswith('.mp4') or filename.endswith('.mkv'):
        return 'libx264'
    elif filename.endswith('.mov'):
        return 'libx264'
    else:
        raise ValueError("Unsupported file format. Please use .avi, .mp4, .mov, or .mkv.")

def main():
    rs = p.size()
    video_filename = input("Please enter a video file name with path (e.g., 'output.avi'): ")
    audio_filename = "temp_audio.wav"
    fps = 10.0
    sample_format = pyaudio.paInt16
    channels = 2
    rate = 44100

    record_video(video_filename, audio_filename, fps, rs, sample_format, channels, rate)

if __name__ == "__main__":
    main()