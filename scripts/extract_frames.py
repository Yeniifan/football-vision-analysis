
import cv2
import os
import argparse

def extract_frames(video_path, output_dir, rate=2):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"無法開啟影片: {video_path}")
        return

    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"影片資訊: 共 {total} 幀, FPS: {fps}, 每秒擷取 {rate} 幀")

    count = 0
    saved = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if int(count % round(fps / rate)) == 0:
            filename = os.path.join(output_dir, f"frame_{saved:04d}.jpg")
            cv2.imwrite(filename, frame)
            saved += 1
        count += 1

    cap.release()
    print(f"完成擷取，共儲存 {saved} 張圖片至 {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", type=str, required=True, help="影片檔案路徑")
    parser.add_argument("--output", type=str, default="data/frames", help="輸出圖片資料夾")
    parser.add_argument("--rate", type=int, default=2, help="每秒擷取幾張圖片")
    args = parser.parse_args()

    extract_frames(args.video, args.output, args.rate)
