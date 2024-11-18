import os
import sys
import django

# 加入專案根目錄到 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # 加入專案根目錄

# 設定 Django 環境變數
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytestsite.settings')
django.setup()

# 匯入模型
from screenshots.models import Subtitle, Show
#Subtitle.objects.all().delete()#刪除所有資料
# 配置參數
show_title = "BanG Dream! It's MyGO!!!!!"  # 要匯入的 Show 標題
season_number = 1  # 要匯入的季
episode_number = 13  # 要匯入的集
relative_screenshot_path = f'screenshots/{episode_number:02d}/'
screenshot_folder = f'media/{relative_screenshot_path}'
subtitles_file = f'data/ocr_results_{episode_number:02d}.txt'

def import_subtitles():
    try:
        # 確認指定的 Show 存在
        show = Show.objects.get(
            title=show_title, 
            season_number=season_number, 
            episode_number=episode_number
        )
    except Show.DoesNotExist:
        print(f"Show with title '{show_title}' does not exist.")
        return

    # 讀取 ocr_results.txt 檔案，解析字幕資料
    with open(subtitles_file, 'r', encoding='utf-8') as f:
        for line in f:
            # 清理並分割每一行的內容
            line = line.strip()
            if not line:
                continue
            try:
                # 分割 frame number 和 text
                frame_number, text = line.split(',', 1)
                frame_number = frame_number.strip().zfill(5)  # 補足 5 位數
                text = text.strip()
            except ValueError:
                print(f"Error parsing line: {line}")
                continue

            # 如果 text 為空，不新增資料
            if not text:
                print(f"Skipping empty text for frame {frame_number}")
                continue

            # 找到對應的圖片
            screenshot_filename = f"MyGO_{episode_number:02d}_{frame_number}.jpg"
            screenshot_path = os.path.join(screenshot_folder, screenshot_filename)
            
            # 檢查圖片是否存在，若不存在則跳過
            if not os.path.exists(screenshot_path):
                print(f"Screenshot not found: {screenshot_path}")
                continue

            # 儲存 Subtitle 到資料庫
            subtitle = Subtitle(
                show=show,
                start_frame=int(frame_number),
                end_frame=int(frame_number),  # start_frame 和 end_frame 相同
                text=text,
                screenshot_path=os.path.join(relative_screenshot_path, screenshot_filename)
            )
            subtitle.save()
            print(f"Subtitle imported: Frame {frame_number} - {text}")

    print("字幕匯入完成")

if __name__ == "__main__":
    import_subtitles()
