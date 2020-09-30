# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:38:49 2020

@author: harinder
"""
from convertXLSX import convertXLSX

from convertYAML import convertYAML


def main():
    convertXLSX("BaseProfile-Template.xlsx")
    convertYAML()

if __name__ == "__main__":
    main()