from apps.home.models.project import Project
from datetime import date

projects = [
	{
		"Name": "WakePoint",
		"Description": "• Geo-notification alarm mobile app alerting public transit commuters once they reach their destination",
		"Project_Image_1": "/static/images/projects/wakepoint1.png",
		"Project_image_2": "/static/images/projects/wakepoint2.png",
		"Link": "https://github.com/skylerbala/WakePoint"
	},
	{
		"Name": "PitchShifter",
		"Description": "• Music player app equipped with pitch and rate-playback shifting capabilities",
		"Project_Image_1": "/static/images/projects/pitchshifter1.png",
		"Project_image_2": "/static/images/projects/pitchshifter2.png",
		"Link": "https://github.com/skylerbala/PitchShifter"
	},
	{
		"Name": "Poshmark Bot",
		"Description": "• Mobile app bot increasing social media/ e-commerce presence by automating various social media marketing functions (following",
		"Project_Image_1": " commenting",
		"Project_image_2": " etc.)",
		"Link": "/static/images/projects/poshmarkbot1.png"
	},
	{
		"Name": "SmartSpray",
		"Description": "• Design a mobile app (SmartSpray) that provides farmers spray coverage data as well as analytical instruments to reduce pesticide resistance development and optimize pesticide application costs •\tDesigned image color quantization algorithm to measure pesticide coverage",
		"Project_Image_1": "/static/images/projects/smartspray1.png",
		"Project_image_2": "/static/images/projects/smartspray2.png",
		"Link": "https://github.com/skylerbala/SmartSpray"
	},
	{
		"Name": "Unitrans Mobile App",
		"Description": "•\tMobile app that allows UC Davis students with real-time bus stop/location information",
		"Project_Image_1": "/static/images/projects/unitrans1.png",
		"Project_image_2": "/static/images/projects/unitrans2.png",
		"Link": "https://github.com/skylerbala/Unitrans-Mobile-App"
	},
	{
		"Name": "AllerFree",
		"Description": "•\tMobile-app leveraging cloud vision and machine translation to provide users multilingual food allergen content",
		"Project_Image_1": "/static/images/projects/allerfree1.png",
		"Project_image_2": "/static/images/projects/allerfree2.png",
		"Link": "https://github.com/skylerbala/AllerFree"
	},
	{
		"Name": "Bus Shifts Manager",
		"Description": "• Django-built administrative web suite prototype for Unitrans",
		"Project_Image_1": "/static/images/projects/busshiftsmanager1.png",
		"Project_image_2": "/static/images/projects/busshiftsmanager2.png",
		"Link": "https://github.com/skylerbala/Bus-Shifts-Manager"
	},
	{
		"Name": "LlamaDuck App",
		"Description": "• Mobile-app mini-game",
		"Project_Image_1": "/static/images/projects/llamaduck1.png",
		"Project_image_2": "/static/images/projects/llamaduck2.png",
		"Link": "https://github.com/skylerbala/LlamaDuckApp"
	},
]

def create_projects():
  for project in projects:
    new_project = Project(name=project["Name"], description=project["Description"], project_image_1=project["Project_Image_1"], project_image_2=project["Project_image_2"], link=project["Link"])
    new_project.save()