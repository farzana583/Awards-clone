from django.db import models
from django.contrib.auth.models import User
from PIL import Image as Img
from django.db.models.signals import post_save
from django.dispatch import receiver 
# import PIL

class Image(models.Model):
    title=models.CharField(default='', max_length=50)
    user_name = models.CharField(default='',max_length=200)
    image = models.ImageField(upload_to ='profile_pics')
    project = models.TextField(default='',max_length=200)
    link =models.URLField(default='', max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    @classmethod
    def all_images(cls):
        all_posts = cls.objects.all()
        # print(all_posts)
        return all_posts

    def save_images(self):
        self.save()

    def delete_all_image(self):
        self.delete()

    
    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(default='', max_length=50)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Img                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  .open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()


class Ratings(models.Model):
    design = models.IntegerField(default=1)
    usability = models.IntegerField(default=1)
    content = models.IntegerField(default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Image,on_delete=models.CASCADE)
    