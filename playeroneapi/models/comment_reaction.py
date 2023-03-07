from django.db import models

class CommentReaction(models.Model):
  user = models.ForeignKey("User", on_delete=models.CASCADE)
  comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
  reaction = models.ForeignKey("Reaction", on_delete=models.CASCADE)
 

@property
def reaction_image(self):
    return self.reaction.image_url
