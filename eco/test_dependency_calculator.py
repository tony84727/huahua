from eco.dependecy_calculator import DependencyResolver, MakefileRuleParser, Recipe, Rule, StaticRuleLookup
import unittest


class TestDependencyCalculator(unittest.TestCase):
    def test_resolve_simple(self):
        rule_lookup = StaticRuleLookup([
            Rule('furnace', [Recipe('cobblestone', 8)]),
        ])
        resolver = DependencyResolver(rule_lookup)
        recipes = resolver.resolve_all('furnace')
        self.assertEqual([Recipe('cobblestone', 8)], recipes)

    def test_resolve_powered_cart(self):
        rule_lookup = StaticRuleLookup([
            Rule('furnace', [Recipe('cobblestone', 8)]),
            Rule('powered cart', [Recipe('cart', 1), Recipe('furnace', 1)]),
            Rule('cart', [Recipe('iron ingot', 5)])
        ])
        resolver = DependencyResolver(rule_lookup)
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
        resolver = DependencyResolver(rule_lookup)
        recipes = resolver.resolve_all('glass')
        self.assertEqual(
            set([
                Recipe('mining labor', 1000),
                Recipe('glassworking labor', 0.5),
                Recipe('sand', 4),
                Recipe('limestone', 4)
            ]),
            set(recipes))


class TestMakefileRuleParser(unittest.TestCase):
    def test_parse(self):
        parser = MakefileRuleParser()
        rules = parser.parse('''
        Furnace: Cobblestone@8
        HwenLog: WoodTag
        ''')
        self.assertEqual(
            [
                Rule('Furnace', [Recipe('Cobblestone', 8)]),
                Rule('HwenLog', [Recipe('WoodTag', 1)]),
            ],
            rules,
        )
