#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 18:14:18 2018

@author: team6; andrew caide
@project: CS109 Final Project; Twitter Bot Detector
 
"""
if platform.system() == 'Darwin':
    import getpass
    import os
    usr = getpass.getuser()
    os.chdir('../BotReader')
    import twitter_interfacing as ti
    import twitter_credentials
else:
    import twitter_interfacing
    import twitter_credentials