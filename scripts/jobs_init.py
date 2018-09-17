from apps.home.models.job import Job
from datetime import date

jobs = [
 {
   "A": "Unitrans",
   "B": "Web Developer",
   "C": "Davis, CA",
   "D": "• Design and implement novel solutions on Unitrans’ administrative/ human capital management software<br />• Work closely with Unitrans managers to better understand Unitrans’ web suite needs<br />• Languages/ APIs: Django, JavaScript, HTML, CSS, PostgreSQL, jQuery, Python",
   "E": "2018-06-01",
   "F": "None",
   "G": "/static/images/jobs/unitrans.png"
 },
 {
   "A": "UC Davis Department of Entomology",
   "B": "Mobile App/ Web Developer ",
   "C": "Davis, CA",
   "D": "•\tDesign a mobile app (SmartSpray) that provides farmers spray coverage data as well as analytical instruments to reduce pesticide resistance development and optimize pesticide application costs<br />•\tDesigned image color quantization algorithm to measure pesticide coverage<br />•\tLanguages/ APIs: Swift, Core Graphics",
   "E": "2018-06-01",
   "F": "None",
   "G": "/static/images/jobs/ucdavis.png"
 },
 {
   "A": "The Little Green Coupon Machine",
   "B": "iOS Engineer",
   "C": "Davis, CA",
   "D": "•\tRevamped existing coupon aggregator iOS app, The Little Green App – enables users to discover and access deals from local Davis businesses <br />•\tResolved issues with deprecated software by re-writing app with modern frameworks/ libraries<br />•\tIdentified and Troubleshot UX issues; Enhanced graphic UI elements<br />•\tLanguages/ APIs: Swift, ",
   "E": "2017-08-01",
   "F": "2017-10-01",
   "G": "/static/images/jobs/lgcm.png"
 },
 {
   "A": "Empoder",
   "B": "Volunteer CS Curriculum Designer/Instructor",
   "C": "Mountain View, CA",
   "D": "•\tDesigned and taught 10-week computer science curriculum to underprivileged groups <br />•\t400+ Volunteer Hours<br />•\tAssisted organization in procuring $25,000 in grant money via Google Rise Award",
   "E": "2016-06-01",
   "F": "2016-07-01",
   "G": "/static/images/jobs/empoder.png"
 },
 {
   "A": "Mathnasium",
   "B": "Mathematics Instructor",
   "C": "Mountain View, CA",
   "D": "•\tTutored students grades 8th – 12th one-on-one in math subjects from Algebra to Calculus<br />•\tDeveloped customized learning plans to suit needs of each student",
   "E": "2015-08-01",
   "F": "2016-04-01",
   "G": "/static/images/jobs/mathnasium.png"
 }
]

def create_jobs():
  for j in jobs:
    if j["F"] is "None":
      new_job = Job(company=j["A"], position=j["B"], location=j["C"], description=j["D"], start_date=j["E"], end_date=None, company_image=j["G"])
      new_job.save()
    else:
      new_job = Job(company=j["A"], position=j["B"], location=j["C"], description=j["D"], start_date=j["E"], end_date=j["F"], company_image=j["G"])
      new_job.save()