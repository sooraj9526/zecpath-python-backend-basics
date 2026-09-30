# CRUD Simulation - Zecpath AI Job Portal


candidates = []


# CREATE
def create_candidate(name, email, role):
    candidate = {
        "name": name,
        "email": email,
        "role": role
    }

    candidates.append(candidate)
    print("Candidate created successfully.")


# READ
def read_candidates():
    if not candidates:
        print("No candidates found.")
        return

    print("\nCandidate List")
    print("--------------")

    for index, candidate in enumerate(candidates, start=1):
        print(f"{index}. {candidate}")


# UPDATE
def update_candidate(index, name, email, role):
    if 0 <= index < len(candidates):
        candidates[index]["name"] = name
        candidates[index]["email"] = email
        candidates[index]["role"] = role

        print("Candidate updated successfully.")
    else:
        print("Candidate not found.")


# DELETE
def delete_candidate(index):
    if 0 <= index < len(candidates):
        deleted_candidate = candidates.pop(index)
        print("Candidate deleted:", deleted_candidate["name"])
    else:
        print("Candidate not found.")


# Test CRUD operations

create_candidate(
    "Sooraj",
    "sooraj@example.com",
    "Python Developer"
)

create_candidate(
    "Rahul",
    "rahul@example.com",
    "Web Developer"
)

read_candidates()

update_candidate(
    0,
    "Sooraj A",
    "sooraja@example.com",
    "Django Developer"
)

read_candidates()

delete_candidate(1)

read_candidates()