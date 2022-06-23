class Administrative_type():
    def __init__(self):
        self.idea_groups = ["Innovative", "Religious"]
        self.unlocked_idea_groups = []

    def unlock_idea_group(self, idea_group: str):
        if (idea_group == "Innovative" and ("Innovative") not in self.unlocked_idea_groups):
            self.unlocked_idea_groups.append(idea_group)
        elif(idea_group == "Religious" and ("Religious") not in self.unlocked_idea_groups):
            self.unlocked_idea_groups.append(idea_group)


class Innovative_ideas(Administrative_type):
    def __init__(self):
        self.ideas = ["Prestige", "Mercenary_maintenance"]
        self.unlocked_ideas = []

    def unlock_idea(self, idea_group: str):
        """Avaliable choices: Prestige, Mercenary_maintenance"""
        print(idea_group)
        print(self.unlocked_ideas)
        if idea_group == "Prestige" and ("Prestige") not in self.unlocked_ideas:
            self.unlocked_ideas.append(idea_group)
        elif self.unlocked_ideas[-1] == "Prestige" and idea_group == "Mercenary_maintenance":
            self.unlocked_ideas.append(idea_group)
        elif (idea_group) in self.unlocked_ideas:
            return print("you have already chosen this idea")


admin = Administrative_type()
admin.unlock_idea_group("Innovative")
print(admin.unlocked_idea_groups)
innovative = Innovative_ideas()
innovative.unlock_idea("Prestige")
innovative.unlock_idea("Mercenary_maintenance")
print(innovative.unlocked_ideas)
