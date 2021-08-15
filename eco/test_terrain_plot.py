from eco.terrain_plot import PlotNameOwnerParser
import unittest


class PlotNameOwnerParserTestCase(unittest.TestCase):
    def test_parse(self):
        parser = PlotNameOwnerParser()
        test_cases = [
            {
                'input': 'tonyduan山, Owner: tonyduan',
                'expected': ('tonyduan山', 'tonyduan'),
            },
        ]
        for c in test_cases:
            with self.subTest(c['input']):
                self.assertEqual(c['expected'], parser.parse(c['input']))
