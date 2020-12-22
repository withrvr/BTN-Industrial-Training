from django.shortcuts import render
from .models import AboutModels, ExperienceModels, SkillModels, EducationModels, ContactModels
from .forms import ContactForm
# Create your views here.


def contact_view(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)		
		
		if form.is_valid():
			name = form.cleaned_data.get('name')
			form.save()
			contact_save_msg = True
			form = ContactForm()
	else:
		form = ContactForm()
		contact_save_msg = False
		name = ''


	context = {
		'form': form,
		'contact_save_msg': contact_save_msg,
		'name': name,
	}	
	return render(request, "contact_html.html", context)


def home_view(request, *args, **kargs):

	about = AboutModels.objects.get(pk=1)
	experience = ExperienceModels.objects.get(pk=1)
	skill = SkillModels.objects.get(pk=1)
	education = EducationModels.objects.get(pk=1)

	context = {
		# "about": about,
		"about_values": about.values.split(","),
		"about_goals": about.goals.split(","),
		"about_hobbies": about.hobbies.split(","),
		"about_discription": about.discription,
		"about_projects": about.projects.split(","),
		"about_logo": about.logo,

		# "experience": experience,
		"experience_company_name": experience.company_name,
		"experience_duration": (experience.duration_ending - experience.duration_starting),
		"experience_designation": experience.designation.split(","),
		"experience_description": experience.description,

		# "skill": skill,
		"skill_description": skill.description,
		"skill_skills": skill.skills.split(","),
		"skill_percentage": skill.percentage,

		# "education": education,
		"education_degree": education.degree,
		"education_college_name": education.college_name,
		"education_course_duration": (education.course_ending - education.course_starting),
		"education_percentage": education.percentage,
		"education_description": education.description,
	}
	return render(request, "home_html.html", context)


