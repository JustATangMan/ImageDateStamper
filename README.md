# ImageDateStamper
A Python program to timestamp photos with EXIF tags using the Python `Pillow` Module.
# Technologies Used 
* Python Modules:
  * `Pillow`
  * `os`
  * `glob`
# Usage
* Put photos you want date-stamped into the Photos folder
* Open the ImageDateStamper folder in command line
* Activate a virtual environment with Pillow:
  * Run `pip install virtualenv`
  * Run `virtualenv venv` to create a venv folder in the ImageDateStamper folder
  * Navigate to `ImageDateStamper/venv/Scripts` and run the `activate` command
  * Run `pip install pillow` in the venv
* Run `python ImageDateStamper.py`
* The dates photos will be in the Photos folder
# Functionality
* Loops through a folder of photos with EXIF data
* Extracts the EXIF data to paste the date of the photo in the bottom-right corner
# Before:
  ![moon1](https://github.com/JustATangMan/ImageDateStamper/assets/45743962/46f44aca-8260-4e2e-82fd-70458628627b)
  
# After:
  ![dated_moon1](https://github.com/JustATangMan/ImageDateStamper/assets/45743962/06c5c7d9-7de3-481b-ab42-2c920fdcb36c)
  
