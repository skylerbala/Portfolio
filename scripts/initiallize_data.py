from apps.home.models import *
from datetime import date

#SKILLS
general_skills = ['Microsoft']
programming_skills = ["C++", "HTML", "CSS", "JavaScript", "Python", "Swift", "Java", "x86 Assembly"]
libraries_skills = ["ReactJS", "React Native", "Django", "Node.js", "jQuery", "SQL"]
languages_skills = ["English", "Tagalog", "Spanish"]

for e in libraries_skills:
  Skill.create(skill_type=Skill.FRAMEWORKS_LIBRARIES, name=e, icon='/static/images/skills/' + e + '-icon', proficiency=Skill.PROFICIENT)

for e in libraries_skills:
  Skill.create(skill_type=Skill.PROGRAMMING_LANGUAGES, name=e, icon='/static/images/skills/' + e + '-icon', proficiency=Skill.PROFICIENT)

for e in libraries_skills:
  Skill.create(skill_type=Skill.LANGUAGES, name=e, icon="", proficiency=Skill.PROFICIENT)

#PROJECTS
{
  AllerFree: {
    description: "•	Mobile-app leveraging cloud vision and machine translation to provide users multilingual food allergen content\n•	Received Best Google Cloud Platform Hack Award by Google\n•	Languages/ APIs: Swift, Python, Google Cloud Platform, Django"  
  },

}

#JOBS

class Job(models.Model):
  company = models.TextField()
  position = models.TextField()
  location = models.TextField()
  description = models.TextField()
  start_date = models.DateField()
  end_date = models.DateField()
  company_image = models.CharField(default='/static/images/company/', max_length=500, null=True, blank=True)

[
  {
    company: "Unitrans",
    position: "Web Developer",
    location: "Davis, CA",
    description: "•  Design and implement novel web solutions on Unitrans’ administrative website to streamline Unitrans’ administrative tasks•  Work closely with Unitrans managers to better understand Unitrans’ Web Suite needs•  Languages/ APIs: Django, JavaScript, HTML, CSS, PostgreSQL, jQuery, Python",
    start_date: date(2018, 6, 1),
    end_date: "",
    company_image = '/static/images/company/' + unitrans.png
  },
  {
    company: "The Little Green Coupon Machine",
    position: "iOS Engineer",
    location: "Davis, CA",
    description: "•	Revamped existing coupon aggregator iOS app, The Little Green App – enables users to discover and access deals from local Davis businesses•	Resolved issues with deprecated software by re-writing app with modern frameworks/ libraries•	Identified and Troubleshot UX issues; Enhanced graphic UI elements•	Languages/ APIs: Swift",
    start_date: date(2017, 8, 1),
    end_date: date(2017, 10, 1),
    company_image = '/static/images/company/' + lgcm.png
  },
  {
    company: "Mathnasium",
    position: "Mathematics Instructor",
    location: "Mountain View, CA",
    description: "•	Tutored students grades 8th – 12th one-on-one in math subjects from Algebra to Calculus•	Developed customized learning plans to suit needs of each student",
    start_date: date(2015, 8, 1),
    end_date: date(2016, 4, 1),
    company_image = '/static/images/company/' + mathnasium.png
  },
]