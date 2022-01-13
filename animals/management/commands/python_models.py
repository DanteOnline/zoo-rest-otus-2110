class Family:

    def __init__(self, name, max_age):
        self.name = name
        self.max_age = max_age


class FamilyCard:

    def __init__(self, text, family):
        self.text = text
        self.family = family


class Kind:

    def __init__(self, name, family):
        self.name = name
        self.family = family


class Food:

    def __init__(self, name, families):
        self.name = name
        self.families = families
