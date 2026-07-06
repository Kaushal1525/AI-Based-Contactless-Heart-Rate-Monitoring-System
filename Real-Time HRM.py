import cv2
import numpy as np
from scipy.fftpack import fft
from scipy.signal import butter, lfilter
from cvzone.FaceDetectionModule import FaceDetector
import matplotlib.pyplot as plt
from collections import deque
import time


buffer_size = 300
fps = 30
min_hz = 1.0
max_hz = 2.0


def bandpass_filter(signal, fps, lowcut, highcut):
    nyq = 0.5 * fps
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(1, [low, high], btype='band')
    return lfilter(b, a, signal)


cap = cv2.VideoCapture(0)
detector = FaceDetector()
green_intensity = deque(maxlen=buffer_size)
timestamps = deque(maxlen=buffer_size)

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_ylim(40, 120)
ax.set_title("Estimated Heart Rate (BPM)")
ax.set_ylabel("BPM")
ax.set_xlabel("Time")

start_time = time.time()

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    img, faces = detector.findFaces(frame, draw=True)

    if faces:
        face = faces[0]
        x, y, w, h = face["bbox"]

        roi = frame[y:y + int(h / 4), x:x + w]
        if roi.size == 0:
            continue


        green_channel = roi[:, :, 1]
        avg_green = np.mean(green_channel)
        green_intensity.append(avg_green)
        timestamps.append(time.time() - start_time)

        if len(green_intensity) == buffer_size:

            signal = np.array(green_intensity)
            signal = signal - np.mean(signal)
            filtered = bandpass_filter(signal, fps, min_hz, max_hz)


            freqs = np.fft.rfftfreq(buffer_size, d=1.0 / fps)
            fft_values = np.abs(fft(filtered))
            peak_freq = freqs[np.argmax(fft_values)]
            bpm = peak_freq * 60.0


            line.set_ydata(np.append(line.get_ydata(), bpm)[-buffer_size:])
            line.set_xdata(np.linspace(0, len(line.get_ydata()), len(line.get_ydata())))
            ax.set_xlim(0, len(line.get_ydata()))
            fig.canvas.draw()
            fig.canvas.flush_events()


            cv2.putText(frame, f"Heart Rate: {int(bpm)} BPM", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Heart Rate Monitor", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
