#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="activar verbosidad", action="store_true")
parser.add_argument("-f", "--file", help="Nombre de archivo a procesar")
args = parser.parse_args()

if args.verbose:
    print("Depuracion activada")
elif args.file:
    print("el nombre del archivo es: ", args.file)



