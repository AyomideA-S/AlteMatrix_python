"""Altematrix

http://www.codingpeps.com/software//

This tool lets you convert strings and numbers between number bases (2, 8, 10 and 16) as well as ASCII text.
You can use the IP address analyzer to find out details on IPv4 and perform abbreviation as well as expansion on IPv6 addresses.
It can also perform a two's complement calculation as well.

Altematrix works best with Python 3.10.0 and up.

To know more, see the documentation: https://github.com/Ir0n-c0d3X/AlteMatrix/README.md
"""

__author__ = "Ayomide Ayodele-Soyebo (midesuperbest@gmail.com) (inquiry@codingpeps.com)"
__version__ = "1.0.0"
__copyright__ = "Copyright (c) 2022 Ayomide Ayodele-Soyebo"
# Use of this source code is governed by the MIT license.
__license__ = "MIT"

from AlteMatrix.converter import binary
from AlteMatrix.converter import decimal
from AlteMatrix.converter import hexadecimal
from AlteMatrix.converter import octal
from AlteMatrix.converter import user_defined

from AlteMatrix.ipanalyzer import ipv4_address_analyzer
from AlteMatrix.ipanalyzer import ipv6_address_analyzer

from AlteMatrix.twos_complement import twos_comp