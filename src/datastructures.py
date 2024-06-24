

from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

        
        john = {
            "id": self._generateId(),
            "first_name": "John",
            "last_name": self.last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        }
        self._members.append(john)

        jane = {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": self.last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        }
        self._members.append(jane)

        jimmy = {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers": [1]
        }
        self._members.append(jimmy)

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId()
        member["last_name"] = self.last_name 
        self._members.append(member)
        return {"message": "Member added successfully", "member": member}

    def delete_member(self, id):
        for idx, member in enumerate(self._members):
            if member["id"] == id:
                del self._members[idx]
                return {"done": True}  
        return {"error": f"Member with ID {id} not found"}

    def update_member(self, id, new_data):
        for member in self._members:
            if member["id"] == id:
                member.update(new_data)
                return {"message": f"Member with ID {id} updated successfully", "member": member}
        return {"error": f"Member with ID {id} not found"}

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                member_dict = {
                    "name": f"{member['first_name']} {self.last_name}",
                    "id": member["id"],
                    "age": member["age"],
                    "lucky_numbers": member["lucky_numbers"]
                }
                return member_dict
        return {"error": f"Member with ID {id} not found"}

    def get_all_members(self):
        return self._members
