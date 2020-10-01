# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:38:49 2020

@author: harinder
"""
from convertXLSX import convert_to_yaml

from convertYAML import convert_to_jmx


def main():
    convert_to_yaml("template/BaseProfile-Template.xlsx")
    convert_to_jmx()

if __name__ == "__main__":
    main()