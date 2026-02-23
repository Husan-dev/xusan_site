from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    tags = models.CharField(max_length=200, help_text="Vergul bilan ajratib yozing (masalan: Django, Redis)")
    description_uz = models.TextField()
    description_en = models.TextField()
    live_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return self.tags.split(',')


class CreateBlog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Sites/')
    tags = models.CharField(max_length=200, help_text="Vergul bilan ajratib yozing (masalan: Django, Redis)")
    description_uz = models.TextField()
    description_en = models.TextField()
    live_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return self.tags.split(',')

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    title2 = models.CharField(max_length=200)
    description2 = models.TextField()
    title3 = models.TextField()
    description3 = models.TextField()
    def __str__(self):
        return self.title

class Experience(models.Model):
    experience = models.IntegerField(default=0)
    project_complated = models.IntegerField(default=0)
    Technologies = models.IntegerField(default=0)
    Happy_clients = models.IntegerField(default=0)


class Skills(models.Model):
    python = models.IntegerField(default=0)
    Rest_API = models.IntegerField(default=0)
    PostgreSQL = models.IntegerField(default=0)
    Docker = models.IntegerField(default=0)

class About(models.Model):
    body = models.TextField()
    image = models.ImageField(upload_to='about/')
    def __str__(self):
        return self.body

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    message = models.TextField()

    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


    def __str__(self):
        return self.first_name + " " + self.last_name



