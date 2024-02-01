from django.db import models


class HW(models.Model):
    school_subject = models.CharField(max_length=50)
    task_text = models.TextField()
    fact_answer = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
