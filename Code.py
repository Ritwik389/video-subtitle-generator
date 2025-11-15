import cv2
import os
input_path = input("Enter the input path for the video to edit")
output_path = "output_video.mp4"
sav_dir = "saved_frames"

cap = cv2.VideoCapture(input_path)
if not cap.isOpened():
    print("Error: Could not open the video file")
    exit()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"the width of video is {width} and height is {height}")
x = int(input("Enter the x cordinate of the subtitles"))
y = int(input("Enter the y cordinate of the subtitles"))

os.makedirs(sav_dir, exist_ok=True)

fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"total no. of frames in the video {frame_count}")

font = cv2.FONT_HERSHEY_PLAIN
font_scale = 1
font_color = (0,0,0)
bg_color = (255,255,255)
thickness = 2

num_subs = int(input("Enter number of subtitles: "))
subtitles = []

for i in range(num_subs):
    print(f"\nSubtitle {i + 1}:")
    text = input("Enter subtitle text: ")
    start = int(input("Start frame number: "))
    end = int(input("End frame number: "))
    subtitles.append((start, end, text))


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
print("Press 's' to save current frame.")
print("Press 'q' to quit.")

frame_number = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_number+=1
    current_subtitle = ""
    for start, end, text in subtitles:
        if start <= frame_number <= end:
            current_subtitle = text
            break
    if current_subtitle:
        text_size, _ = cv2.getTextSize(current_subtitle, font, font_scale, thickness)
        text_w, text_h = text_size
        cv2.rectangle(frame, (x - 10, y - text_h - 10), (x + text_w + 10, y + 10), bg_color, -1)
        cv2.putText(frame, current_subtitle, (x,y), font, font_scale, font_color, thickness)
    out.write(frame)
    cv2.imshow("Video", frame)
    key = cv2.waitKey(30) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        file = os.path.join(sav_dir, f"frame number_{frame_number}.jpg")
        cv2.imwrite(file, frame)
        print(f"saved frame {frame_number} as frame_number_{frame_number}.jpg")

cap.release()
out.release()
cv2.destroyAllWindows()
print(f"Video saved as {output_path}")

