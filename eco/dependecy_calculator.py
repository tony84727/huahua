from dataclasses import dataclass
from typing import Dict, List


def rule(input, output):
    return (input, output)


@dataclass(eq=True, frozen=True)
class Recipe:
    name: str
    count: float

    def add(self, count: float):
        return Recipe(self.name, self.count + count)


@dataclass
class Rule:
    name: str
    recipes: List[Recipe]


def index_rules(rules: List[Rule]) -> Dict[str, Rule]:
    dictionary = {}
    for r in rules:
        dictionary[r.name] = r
    return dictionary


class RecipeAggregator:
    recipes: Dict[str, Recipe]

    def __init__(self) -> None:
        self.recipes = {}

    def add(self, base_recipe: Recipe):
        if base_recipe.name in self.recipes:
            self.recipes[base_recipe.name] = self.recipes[base_recipe.name].add(
                base_recipe.count)
        else:
            self.recipes[base_recipe.name] = base_recipe

    def all_recipes(self) -> List[Recipe]:
        return list(self.recipes.values())


class DependencyResolver:
    def __init__(self, rules: List[Rule]) -> None:
        self.rules = index_rules(rules)

    def resolve_all(self, name: str) -> List[Recipe]:
        recipes = RecipeAggregator()
        work_queue = self.rules[name].recipes
        while len(work_queue) > 0:
            recipe = work_queue.pop()
            crafting_rule = self.rules.get(recipe.name)
            if crafting_rule is None:
                recipes.add(recipe)
            else:
                sub_recipes = crafting_rule.recipes
                if len(sub_recipes) > 0:
                    for recipe in sub_recipes:
                        work_queue.append(recipe)
                else:
                    recipes.add(recipe)
        return recipes.all_recipes()
