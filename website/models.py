from django.db import models

class AboutModels(models.Model):
	values 		= models.TextField(null=True, blank=True)
	goals 		= models.TextField(null=True, blank=True)
	hobbies 	= models.TextField(null=True, blank=True)
	discription = models.TextField(null=True, blank=True)
	projects 	= models.TextField(null=True, blank=True)
	logo 		= models.ImageField(upload_to="logo/", null=True, blank=True)
	

class ExperienceModels(models.Model):
	company_name 		= models.CharField(max_length=100, null=True, blank=True)
	duration_starting 	= models.DateField(null=True, blank=True)
	duration_ending		= models.DateField(null=True, blank=True)
	designation 		= models.TextField(null=True, blank=True)
	description 		= models.TextField(null=True, blank=True)


class SkillModels(models.Model):
	description		= models.TextField(null=True, blank=True)
	skills			= models.TextField(null=True, blank=True)
	percentage		= models.PositiveSmallIntegerField(null=True, blank=True)

class EducationModels(models.Model):
	degree			= models.CharField(max_length=100, null=True, blank=True)
	college_name	= models.CharField(max_length=100, null=True, blank=True)
	course_starting	= models.DateField(null=True, blank=True)
	course_ending	= models.DateField(null=True, blank=True)
	percentage		= models.PositiveSmallIntegerField(null=True, blank=True)
	description		= models.TextField(null=True, blank=True)

class ContactModels(models.Model):
	name	= models.CharField(max_length=100, null=True, blank=True)
	email 	= models.EmailField(max_length=100, null=True, blank=True)
	message	= models.TextField(null=True, blank=True)

# class ____(models.Model):
# 	pass

