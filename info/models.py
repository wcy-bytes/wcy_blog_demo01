from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.

class Info(models.Model):

    # 信息标题 例如 Home, Groups等等...
    title = models.CharField(max_length=100)

    # 详细信息
    detail = RichTextField()

    def __str__(self):
        return f"{self.title}"  # 这会显示文件的路径名
