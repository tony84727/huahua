from eco.dependecy_calculator import DependencyResolver, Recipe, Rule
import unittest


class TestDependencyCalculator(unittest.TestCase):
    def test_resolve_simple(self):
        resolver = DependencyResolver([
            Rule('furnace', [Recipe('cobblestone', 1)])
        ])
        recipes = resolver.resolve_all('furnace')
        self.assertEqual(Recipe('cobblestone', 8), recipes)
