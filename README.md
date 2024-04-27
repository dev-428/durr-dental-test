# durr-dental-test

**Note: The following guide is for MacOS with ARM chips only**

## Introduction

This repo contains automated test to test the frontend application for Durr Dental VistaSoft Monitor IoT Solution.

# Installations

### 1. Get VS Code

Free and open source IDE.

[VS Code Download Link](https://code.visualstudio.com/download)

### 2. Get Python

High-level, general-purpose programming language.

[Python Download Link](https://www.python.org/downloads/)

## VS Code Extensions

Install the extensions listed below in VS Code

### 1. [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

Rich support for Python language

### 2. [IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)

Provides AI-assisted development features.

# Setup

### 1. ChromeDriver Download & Add To PATH
reference: https://stackoverflow.com/a/38087347

Check what is your current Chrome version in settings and download the correct version [here](https://googlechromelabs.github.io/chrome-for-testing/).

Run following commands in terminal:
```
$ cd $HOME/Downloads
$ unzip chromedriver-mac-arm64.zip
$ mkdir -p $HOME/bin
$ mv chromedriver-mac-arm64/chromedriver $HOME/bin
$ echo "export PATH=$PATH:$HOME/bin" >> $HOME/.zshrc
```

### 2. Install, Create & Activate Virtual Environment

Run following commands in terminal: 

`pip install virtualenv`

`virtualenv .venv`

`source .venv/bin/activate`

### 3. Install pip Requirements

Run following command in terminal:

`pip install -r requirements.txt`

### 4. Install Behave

Run following command in terminal:

`pip install behave`

### 5. Install Selenium

Run following command in terminal:

`pip install selenium`

### 6. Fill Email & Password

Navigate to `behave.ini` and copy paste your email & password in their respective fields.

# Common Errors Faced & Solutions

**Error:** `Selenium : ValueError`
**Solution:** `Downgrade urllib3 version from 2 to 1.26.18` `pip install --force-reinstall urllib3==1.26.18`

