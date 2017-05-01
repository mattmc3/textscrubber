#!/usr/bin/env python3

from unittest import TestCase, main as unittest_main
from collections import namedtuple
from textscrubber import prose


class TestDbConnection(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_prosescrubber(self):
        txt = "Four score and seven years ago..."
        ps = prose.ProseScrubber(txt)
        self.assertEqual(ps.text, txt)
        self.assertEqual(str(ps), txt)

    # def test_hyphens_to_emdash(self):
    #     TestData = namedtuple('TestData', 'input num_hyphens expected')
    #     emdash = '—'
    #     tests = (
    #         TestData('help -- I need somebody',
    #                  2,
    #                  f'help {emdash} I need somebody'),
    #         TestData('help --- I need somebody',
    #                  2,
    #                  f'help --- I need somebody'),
    #         TestData('lots -- of --- dashes ---- but -- only -- some - match',
    #                  2,
    #                  f'lots {emdash} of --- dashes ---- but {emdash} only {emdash} some - match'),
    #         TestData('---',
    #                  3,
    #                  f'{emdash}'),
    #         TestData('- - -',
    #                  1,
    #                  f'{emdash} {emdash} {emdash}'),
    #     )
    #     for td in tests:
    #         ps = prose.ProseScrubber(td.input)
    #         actual = ps.hyphens_to_emdash(td.num_hyphens).text
    #         self.assertEqual(td.expected, actual)

    def test_emdash_to_hyphens(self):
        TestData = namedtuple('TestData', 'input num_hyphens expected')
        emdash = '—'
        tests = (
            TestData(f'help {emdash} I need somebody',
                     2,
                     'help -- I need somebody'),
            TestData(f'help {emdash}{emdash} I need somebody',
                     3,
                     'help ------ I need somebody'),
            TestData(f'{emdash} {emdash} {emdash}',
                     1,
                     '- - -'),
        )
        for td in tests:
            ps = prose.ProseScrubber(td.input)
            actual = ps.replace_emdash_and_endash_with_hyphens(td.num_hyphens).text
            self.assertEqual(td.expected, actual)

if __name__ == '__main__':
    unittest_main()
