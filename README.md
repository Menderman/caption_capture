# caption_capture：根據台詞搜尋節目截圖
影片經過預處理轉成圖片檔存放在media資料夾中。
使用easyocr辨識字幕文字，`ocr_results.txt`儲存圖片與台詞的對應關係

匯入圖片台詞的對應關係到資料庫`python screenshots/scripts/import_subtitles.py`

網頁使用Django框架：

執行指令：`python manage.py runserver`

主頁面url：`localhost:8000/search`

資料庫後台url：`localhost:8000/admin`

API url：`http://localhost:8000/load-searchItems/?query="台詞"&episode="集數"`

# Demo
![image](https://github.com/Menderman/caption_capture/blob/main/demo1.png)
![image](https://github.com/Menderman/caption_capture/blob/main/demo2.png)
