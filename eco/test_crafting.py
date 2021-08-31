import unittest

from eco.crafting import RecipeResolver, Recipe, Rule, StaticRuleLookup, parse_craft_rule


class TestRecipeResolver(unittest.TestCase):
    def test_resolve_simple(self):
        rule_lookup = StaticRuleLookup([
            Rule('furnace', [Recipe('cobblestone', 8)]),
        ])
        resolver = RecipeResolver(rule_lookup)
        recipes = resolver.resolve_all('furnace')
        self.assertEqual([Recipe('cobblestone', 8)], recipes)

    def test_resolve_powered_cart(self):
        rule_lookup = StaticRuleLookup([
            Rule('furnace', [Recipe('cobblestone', 8)]),
            Rule('powered cart', [Recipe('cart', 1), Recipe('furnace', 1)]),
            Rule('cart', [Recipe('iron ingot', 5)])
        ])
        resolver = RecipeResolver(rule_lookup)
        recipes = resolver.resolve_all('powered cart')
        self.assertEqual(
            [Recipe('cobblestone', 8), Recipe('iron ingot', 5)], recipes)

    def test_resolve_furnace(self):
        rule_lookup = StaticRuleLookup([
            Rule('glass', [Recipe('sand', 4), Recipe(
                'crushed limestone', 1), Recipe('glassworking labor', 0.5)]),
            Rule('crushed limestone', [
                 Recipe('mining labor', 1000), Recipe('limestone', 4)])
        ])
        resolver = RecipeResolver(rule_lookup)
        recipes = resolver.resolve_all('glass')
        self.assertEqual(
            {Recipe('mining labor', 1000), Recipe('glassworking labor', 0.5), Recipe('sand', 4),
             Recipe('limestone', 4)},
            set(recipes))


class TestParseCraftRule(unittest.TestCase):
    def test_parse(self):
        with open('craft_rule_sample', 'r') as sample_file:
            rules = parse_craft_rule(sample_file.read())
            self.assertEqual(
                [
                    Rule('Blast Furnace', [Recipe('Engineering Labor', 100), Recipe('Iron Bar', 60)]),
                    Rule('Empty Pot', [Recipe('Glass', 1), Recipe('Glassworking Labor', 100)]),
                    Rule('高爐', [Recipe('基礎工程勞動力', 10.4), Recipe('鐵條', 60)])
                ],
                rules,
            )
