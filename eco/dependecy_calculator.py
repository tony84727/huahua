import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


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


class RuleLookup:
    """Lookup dependency """

    def lookup(self, name: str) -> Optional[Rule]:
        pass


class StaticRuleLookup(RuleLookup):
    def __init__(self, rules: List[Rule]) -> None:
        self.rules = index_rules(rules)

    def lookup(self, name: str) -> Optional[Rule]:
        return self.rules.get(name)


class MakefileRuleSyntaxError(RuntimeError):
    def __init__(self, line_number: int, line: str) -> None:
        super().__init__(
            f"Make file syntax error at line {line_number}: {line}")


class MakefileRuleParser:
    def __init__(self) -> None:
        self.dependency_pattern = re.compile(r"([^\s@]+)(@([0-9]+))?")

    def parse(self, input: str) -> List[Rule]:
        rules = list()
        for line_number, line in enumerate(input.split("\n")):
            rule = self.parse_line(line)
            if rule is not None:
                rules.append(rule)
        return rules

    def parse_line(self, line: str) -> Optional[Rule]:
        target_dependencies = self.split_target_dependencies(line)
        if target_dependencies is None:
            return None
        (target, dependencies) = target_dependencies
        return Rule(target, self.parse_dependencies(dependencies))

    def split_target_dependencies(self, line: str) -> Optional[Tuple[str, str]]:
        segments = line.split(":")
        if len(segments) != 2:
            return None
        return (segments[0].strip(), segments[1].strip())

    def parse_dependencies(self, dependencies: str):
        recipes = list()
        dependencies = dependencies.split(' ')
        for deps in dependencies:
            matches = self.dependency_pattern.search(deps)
            count = 1
            if matches[3] is not None:
                count = float(matches[3])
            recipes.append(Recipe(matches[1], count))
        return recipes


class MakeFileStyleRuleLookup(StaticRuleLookup):
    def __init__(self, rules: str) -> None:
        parser = MakefileRuleParser()
        super(parser.parse(rules))


class DependencyResolver:
    def __init__(self, rule_lookup: RuleLookup) -> None:
        self.rule_lookup = rule_lookup

    def resolve_all(self, name: str) -> List[Recipe]:
        recipes = RecipeAggregator()
        work_queue = self.rule_lookup.lookup(name).recipes
        while len(work_queue) > 0:
            recipe = work_queue.pop()
            crafting_rule = self.rule_lookup.lookup(recipe.name)
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
