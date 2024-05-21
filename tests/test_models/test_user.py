#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User
