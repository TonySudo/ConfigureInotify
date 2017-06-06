#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from ConfigureInotify import configures

def main():

    print(configures.config["remote"]["IP"])

    ret = input("Enter your input: ")

    configures.parse_config()
    print(configures.config["remote"]["IP"])

if __name__ == "__main__":
    sys.exit(main())
