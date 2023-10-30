import json
import re

# Sample JSON data for members and jobs
members_data = [
    {
        "name": "Joe",
        "bio": "I'm a designer from London, UK"
    },
    {
        "name": "Marta",
        "bio": "I'm looking for an internship in London"
    },
    {
        "name": "Hassan",
        "bio": "I'm looking for a design job"
    },
    {
        "name": "Grace",
        "bio": "I'm looking for a job in marketing outside of London"
    },
    {
        "name": "Daisy",
        "bio": "I'm a software developer currently in Edinburgh but looking to relocate to London"
    }
]

jobs_data = [
    {
        "title": "Software Developer",
        "location": "London"
    },
    {
        "title": "Marketing Internship",
        "location": "York"
    },
    {
        "title": "Data Scientist",
        "location": "London"
    },
    {
        "title": "Legal Internship",
        "location": "London"
    },
    {
        "title": "Project Manager",
        "location": "Manchester"
    },
    {
        "title": "Sales Internship",
        "location": "London"
    },
    {
        "title": "UX Designer",
        "location": "London"
    },
    {
        "title": "Software Developer",
        "location": "Edinburgh"
    }
]

# List of major cities in the UK
uk_cities = ["London", "Edinburgh", "Manchester", "York"]

# Convert JSON data to Python dictionaries
members = json.loads(json.dumps(members_data))
jobs = json.loads(json.dumps(jobs_data))

# Simple recommendation algorithm
recommended_jobs = {}

for member in members:
    member_name = member["name"]
    member_bio = member["bio"]

    # Extract the member's location from the list of major UK cities
    member_location = next((city for city in uk_cities if city in member_bio), None)

    # Extract the job title preferences by looking for any words of the job title in the member's bio
    job_title_preferences = []

    for job in jobs:
        job_title = job["title"]
        job_title_words = re.findall(r'\w+', job_title)
        for word in job_title_words:
            if re.search(rf'\b{word}\b', member_bio, re.IGNORECASE):
                job_title_preferences.append(job_title)
                break

    member_preferences = {
        "location": member_location,
        "job_title": job_title_preferences
    }

    for job in jobs:
        job_title = job["title"]
        job_location = job["location"]

        # Check if the job location and title match the member's preferences
        if job_location == member_preferences["location"] and \
                job_title in member_preferences["job_title"]:
            if member_name not in recommended_jobs:
                recommended_jobs[member_name] = []
            recommended_jobs[member_name].append((job_title, job_location))

# Print the recommendations
for member_name, recommended_jobs_info in recommended_jobs.items():
    print(f"{member_name} may be interested in the following jobs:")
    for job_info in recommended_jobs_info:
        job_title, job_location = job_info
        print(f"- {job_title} in {job_location}")
    print()

