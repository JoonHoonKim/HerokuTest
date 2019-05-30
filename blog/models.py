from django.db import models

# Create your models here.
class Blog(models.Model):#난 제목과 날짜와 본문이 있는 클래스야
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("data published")
    body = models.TextField()

    def __str__(self):#admin에서 볼 때 나는 내 이름으로 보여줘
        return self.title

    def summary(self):#난 본문을 짤라줘
        return self.body[:100]

    def pretty_pub_date(self):#날짜를 이쁘게 보여줄꺼야
        return self.pub_date.strftime("%y.%m.%d")

class Image(models.Model):
    image = models.ImageField(upload_to = 'image/')#image파일을 올려줘