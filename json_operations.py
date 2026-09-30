# JSON Read and Write Practice

import json


# Candidate data
candidate = {
    "name": "Sooraj",
    "email": "sooraja@example.com",
    "role": "Django Developer",
    "skills": ["Python", "Django", "HTML", "CSS"]
}


# WRITE JSON
with open("candidate.json", "w") as file:
    json.dump(candidate, file, indent=4)

print("Candidate data written to candidate.json")


# READ JSON
with open("candidate.json", "r") as file:
    data = json.load(file)

print("\nCandidate Details")
print("-----------------")
print("Name:", data["name"])
print("Email:", data["email"])
print("Role:", data["role"])
print("Skills:", ", ".join(data["skills"]))