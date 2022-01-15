# AlteMatrix
================================================

This tool lets you convert strings and numbers between number bases (2, 8, 10 and 16) as well as ASCII text.
You can use the IP address analyzer to find out details on IPv4 and perform abbreviation as well as expansion on IPv6 addresses. It can also perform a two's complement calculation as well.

You can visit [CodingPeps](https://codingpeps.com) to learn more about how to use it.

## Installation
================

```python
$ pip install AlteMatrix
```

## Usage

```python
$ python
$ import AlteMatrix as AM
```
>Note that all the functions can perform a silent operation by adding the " **_s** " to the end of the function, unless stated otherwise!

### "converter" module

```python
$ import AlteMatrix.converter as con
```

Call | Function
---- | --------
**converter.binary.**
to_octal()        | Convert binary to octal.
to_decimal()      | Convert binary to decimal.
to_hexadecimal()  | Convert binary to hexadecimal.
to_text()         | Convert binary to ASCII text.
**converter.decimal.**
to_binary()       | Convert decimal to binary.
to_octal()        | Convert decimal to octal.
to_hexadecimal()  | Convert decimal to hexadecimal.
to_text()         | Convert decimal to ASCII text.
**converter.octal.**
to_binary()       | Convert octal to binary.
to_decimal()      | Convert octal to decimal.
to_hexadecimal()  | Convert octal to hexadecimal.
to_text()         | Convert octal to ASCII text.
**converter.hexadecimal.**
to_binary()       | Convert hexadecimal to binary.
to_octal()        | Convert hexadecimal to octal.
to_decimal()      | Convert hexadecimal to decimal.
to_text()         | Convert hexadecimal to ASCII text.
**converter.user_defined.**
udf()       | Convert from any number base to another.
udt()       | Convert from text to any number base or vice-versa.



### "ipanalyzer" module

```python
$ import AlteMatrix.ipanalyzer as ipan
```

- ipv4() - Perform analysis on IPv4 addresses.

- ipv6() - Perform analysis on IPv6 addresses.



### "2comp" module
```python
$ import AlteMatrix.twos_complement as comp2
```

+ com2() - Perform two's complement test on a number with a multiplier.

================================================
```python
Try help(fucntion_name) to learn more about a function.
```

## Support Teams
* CodingPeps - [https://www.codingpeps.com](https://www.codingpeps.com/) 
* BrownBear(https://github.com/Brown-Bear-2021)
* BearSec

Follow [@codingpeps](https://www.instagram.com/codingpeps/) 

:octocat: