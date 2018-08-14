from apps.home.models.jobs import Job
from datetime import date

jobs = [
  {
    "company": "Unitrans",
    "position": "Web Developer",
    "location": "Davis, CA",
    "description": "•  Design and implement novel web solutions on Unitrans’ administrative website to streamline Unitrans’ administrative tasks•  Work closely with Unitrans managers to better understand Unitrans’ Web Suite needs•  Languages/ APIs: Django, JavaScript, HTML, CSS, PostgreSQL, jQuery, Python",
    "start_date": date(2018, 6, 1),
    "end_date": "",
    "company_image": '/static/images/company/' + "unitrans.png"
  },
  {
    "company": "The Little Green Coupon Machine",
    "position": "iOS Engineer",
    "location": "Davis, CA",
    "description": "•	Revamped existing coupon aggregator iOS app, The Little Green App – enables users to discover and access deals from local Davis businesses•	Resolved issues with deprecated software by re-writing app with modern frameworks/ libraries•	Identified and Troubleshot UX issues; Enhanced graphic UI elements•	Languages/ APIs: Swift",
    "start_date": date(2017, 8, 1),
    "end_date": date(2017, 10, 1),
    "company_image":'/static/images/company/' + "lgcm.png"
  },
  {
    "company": "Mathnasium",
    "position": "Mathematics Instructor",
    "location": "Mountain View, CA",
    "description": "•	Tutored students grades 8th – 12th one-on-one in math subjects from Algebra to Calculus•	Developed customized learning plans to suit needs of each student",
    "start_date": date(2015, 8, 1),
    "end_date": date(2016, 4, 1),
    "company_image": '/static/images/company/' + "mathnasium.png"
  },
]

def create_jobs():
  for j in jobs:
    if j["end_date"] == "":
      job_new = Job(company=j["company"], position=j["position"], location=j["location"], description=j["description"], start_date=j["start_date"], company_image=j["company_image"])
    else:
      job_new = Job(company=j["company"], position=j["position"], location=j["location"], description=j["description"], start_date=j["start_date"], end_date=j["end_date"], company_image=j["company_image"])
    job_new.save()
