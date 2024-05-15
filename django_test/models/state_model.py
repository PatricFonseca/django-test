from django.db import models


class State(models.Model):
    id = models.UUIDField(primary_key=True)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.state
