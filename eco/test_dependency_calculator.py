from eco.dependecy_calculator import DependencyResolver, Recipe, Rule
import unittest


class TestDependencyCalculator(unittest.TestCase):
    def test_resolve_simple(self):
        resolver = DependencyResolver([
            Rule('furnace', [Recipe('cobblestone', 8)])
        ])
        recipes = resolver.resolve_all('furnace')
        self.assertEqual([Recipe('cobblestone', 8)], recipes)

    def test_resolve_powered_cart(self):
        resolver = DependencyResolver([
            Rule('furnace', [Recipe('cobblestone', 8)]),
            Rule('powered cart', [Recipe('cart', 1), Recipe('furnace', 1)]),
            Rule('cart', [Recipe('iron ingot', 5)])
        ])
        recipes = resolver.resolve_all('powered cart')
        self.assertEqual(
            [Recipe('cobblestone', 8), Recipe('iron ingot', 5)], recipes)

    def test_resolve_furnace(self):
        resolver = DependencyResolver([
            Rule('glass', [Recipe('sand', 4), Recipe(
                'crushed limestone', 1), Recipe('glassworking labor', 0.5)]),
            Rule('crushed limestone', [
                 Recipe('mining labor', 1000), Recipe('limestone', 4)])
        ])
        recipes = resolver.resolve_all('glass')
        self.assertEqual(
            set([
                Recipe('mining labor', 1000),
                Recipe('glassworking labor', 0.5),
                Recipe('sand', 4),
                Recipe('limestone', 4)
            ]),
            set(recipes))
