from django.db import models


class Comment(models.Model):
  user= models.ForeignKey("User", on_delete=models.CASCADE)
  game= models.ForeignKey("VideoGame", on_delete=models.CASCADE)
  comment_title = models.CharField(max_length=50)
  comment = models.CharField(max_length=50)
  date_created = models.CharField(max_length=50)
  reactions= models.ManyToManyField("Reaction", through="CommentReaction", related_name="comment")
