from selenium import webdriver
from selenium.webdriver.support.ui import Select
from os import path
import time
import csv
import subprocess
from cx_Freeze import setup, Executable

exe = Executable(
    script=r"autofill_pravnicka_osoba.py",
    base="Console",
)

setup(
    name="Autofill",
    version="0.3",
    description="Autofill PGRLF formuláře",
    executables=[exe],
)