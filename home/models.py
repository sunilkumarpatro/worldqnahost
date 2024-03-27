from django.db import models
# Create your models here.
DEFAULT_FACEBOOK_IMAGE_URL = "facebook/facebook.png"
DEFAULT_TWITTER_IMAGE_URL = "twitter/twiter.png"  
class Qna(models.Model):
    Hide = 'hide'
    Show = 'show'
 
    HideShow_CHOICES = [
        (Hide, 'hide'),
        (Show, 'show'),
    ]
    id = models.AutoField(primary_key=True)
    showhide = models.CharField(max_length=20, choices=HideShow_CHOICES, default=Hide)
    question_image = models.FileField(upload_to="question/", max_length=250, null=True, blank=True)
    youtube_link = models.TextField()
    facebook_image = models.FileField(upload_to="facebook/", max_length=250, null=True, blank=True)
    twitter_image = models.FileField(upload_to="twitter/", max_length=250, null=True, blank=True)

    def save(self, *args, **kwargs):
        # If no facebook_image is provided, set the default
        if not self.facebook_image:
            self.facebook_image = DEFAULT_FACEBOOK_IMAGE_URL

        # If no twitter_image is provided, set the default
        if not self.twitter_image:
            self.twitter_image = DEFAULT_TWITTER_IMAGE_URL

        super(Qna, self).save(*args, **kwargs)
# Default image URLs  
    # slug
    slug = models.TextField()
  
    # 21 title question
    english_title_question = models.TextField()
    hindi_title_question = models.TextField()
    spanish_title_question = models.TextField()
    chinese_title_question = models.TextField()
    arabic_title_question = models.TextField()
    portuguese_title_question = models.TextField()
    russian_title_question = models.TextField()
    french_title_question = models.TextField()
    japanese_title_question = models.TextField()
    german_title_question = models.TextField()

  
    # descripton
    english_descripton = models.TextField()
    hindi_descripton = models.TextField()
    spanish_descripton = models.TextField()
    chinese_descripton = models.TextField()
    arabic_descripton = models.TextField()
    portuguese_descripton = models.TextField()
    russian_descripton = models.TextField()
    french_descripton = models.TextField()
    japanese_descripton = models.TextField()
    german_descripton = models.TextField()
   
    # keyword
    english_keyword = models.TextField()

    # answer
    english_answer = models.TextField()
    hindi_answer = models.TextField()
    spanish_answer = models.TextField()
    chinese_answer = models.TextField()
    arabic_answer = models.TextField()
    portuguese_answer = models.TextField()
    russian_answer = models.TextField()
    french_answer = models.TextField()
    japanese_answer = models.TextField()
    german_answer = models.TextField()
    
    # 21 end
    def __str__(self):
        return self.english_title_question or f"Qna #{self.id}"
 
class Comment(models.Model):
 
      id = models.AutoField(primary_key=True)
    
      qna_catagary = models.ForeignKey(Qna, on_delete=models.CASCADE)
      english_comment = models.TextField()
      hindi_comment = models.TextField()
      spanish_comment = models.TextField()
      chinese_comment = models.TextField()
      arabic_comment = models.TextField()
      portuguese_comment = models.TextField()
      russian_comment = models.TextField()
      french_comment = models.TextField()
      japanese_comment = models.TextField()
      german_comment = models.TextField()
     
      def __str__(self):
       return f"{self.id}"
class Related(models.Model):
      id = models.AutoField(primary_key=True)
      qna_catagary = models.ForeignKey(Qna, on_delete=models.CASCADE)
    #   question
      english_question = models.TextField()
      hindi_question = models.TextField()
      spanish_question = models.TextField()
      chinese_question = models.TextField()
      arabic_question = models.TextField()
      portuguese_question = models.TextField()
      russian_question = models.TextField()
      french_question = models.TextField()
      japanese_question = models.TextField()
      german_question = models.TextField()
    #   answer
      english_answer = models.TextField()
      hindi_answer = models.TextField()
      spanish_answer = models.TextField()
      chinese_answer = models.TextField()
      arabic_answer = models.TextField()
      portuguese_answer = models.TextField()
      russian_answer = models.TextField()
      french_answer = models.TextField()
      japanese_answer = models.TextField()
      german_answer = models.TextField()
    #   url
      url = models.TextField()
   
      def __str__(self):
       return f"{self.english_question}  | related - {self.qna_catagary}"



class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    msg = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.time}"





