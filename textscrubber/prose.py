#!/usr/bin/env python3

"""
Text scrubbers for prose.
"""

import re
from .ascii import AsciiMixin


class ProseScrubber(AsciiMixin):
    def __init__(self, s):
        self._orig = s
        self._s = s
        self._flags = re.IGNORECASE
        self.__special_chars = {
            'emdash': '—',
        }

    @property
    def text(self):
        return self._s

    def __str__(self):
        return self._s


if __name__ == '__main__':
    main()
