from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=200)  # 節目名稱，如電影名稱或影集名稱
    season_number = models.PositiveIntegerField(default=1)  # 季數
    episode_number = models.PositiveIntegerField(default=1)  # 集數

    def __str__(self):
        return f"{self.title} - S{self.season_number:02d}E{self.episode_number:02d}"

class Subtitle(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='subtitles')
    start_frame = models.PositiveIntegerField()  # 字幕的開始幀數
    end_frame = models.PositiveIntegerField()  # 字幕的結束幀數
    text = models.TextField()  # 字幕內容
    screenshot_path = models.ImageField(upload_to='screenshots/', null=True, blank=True)  # 截圖路徑

    def __str__(self):
        return f"{self.show.title} - Frame {self.start_frame} to {self.end_frame}: {self.text[:30]}"

    def duration_in_frames(self):
        """計算字幕的持續幀數"""
        return self.end_frame - self.start_frame
