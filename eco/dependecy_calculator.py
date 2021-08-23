from dataclasses import dataclass
from typing import Dict, List


def rule(input, output):
    return (input, output)


@dataclass
class Recipe:
    count: int
    name: str


@dataclass
class Rule:
    name: str
    recipes: List[Recipe]


def index_rules(rules: List[Rule]) -> Dict[str, Rule]:
    dictionary = {}
    for r in rules:
        dictionary[r.name] = r
    return dictionary


class DependencyResolver:
    def __init__(self, rules: List[Rule]) -> None:
        self.rules = index_rules(rules)

    def resolve_all(self, name: str) -> List[Recipe]:
        recipes = []
        work_queue = self.rules[name].recipes
        while len(work_queue) > 0:
            recipe = work_queue.pop()
            crafting_rule = self.rules[recipe.name]
            sub_recipes = crafting_rule.recipes
            if len(sub_recipes) > 0:
                for recipe in sub_recipes.recipes:
                    work_queue.append(recipe)
            else:
                recipes.append(recipe)
