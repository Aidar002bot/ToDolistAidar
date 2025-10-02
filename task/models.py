from django.db import models
class Task(models.Model):
    class Status(models.TextChoices):
        CREATED = 'created',"sozdanie"
        IN_PROGRESS = "in_progress","V rabote"
        CAMPLETED = "completed", "zaversheno"
    title = models.CharField(
        max_length=255,
        verbose_name="название задачи",
        help_text="короткое название задачи(до255 символлв)"

    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CREATED,
        verbose_name="status zadachi",
        help_text="tekushi status zadachi"

    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="data zadanie",
        help_text="vremia, kogda zadacha bylo sozdana"
    )
    def __str__(self):
        return f"{self.title} ---> {self.status}"



