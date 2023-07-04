# ImageDateStamper
A Python program to timestamp photos with EXIF tags using the Python `Pillow` Module.
# Technologies Used 
* Python Modules:
  * `Pillow`
  * `os`
  * `glob`
  * `time`
# Usage
* Put photos you want date-stamped into the Photos folder
* Open the ImageDateStamper folder in command line
* Activate a virtual environment with Pillow:
  * Run `pip install virtualenv`
  * Run `virtualenv venv` to create a venv folder in the ImageDateStamper folder
  * Navigate to `ImageDateStamper/venv/Scripts` and run the `activate` command
  * Run `pip install pillow` in the venv
* Run `python ImageDateStamper.py`
* The dated photos will be in the ImageDateStamper/Photos/Dated folder
# Functionality
* Loops through a folder of photos with EXIF data
* Extracts the EXIF data to paste the date of the photo in the bottom-right corner; if no EXIF data available, it will instead pull from the file's size and created date
# Before (photo with EXIF data):
  <picture>
    <img alt="moon1" src="https://github.com/JustATangMan/ImageDateStamper/blob/main/docs/moon1.jpg">
  </picture>
  
# After (photo with EXIF data):
  <picture>
    <img alt="dated_moon1" src="https://github.com/JustATangMan/ImageDateStamper/blob/main/docs/dated_moon1.jpg">
  </picture>
  
# Before (photo without EXIF data):
  <picture>
    <img alt="TangMan" src="https://github.com/JustATangMan/ImageDateStamper/blob/main/docs/TangMan.jpg">
  </picture>
  
# After (photo without EXIF data):
  <picture>
    <img alt="dated_TangMan" src="https://github.com/JustATangMan/ImageDateStamper/blob/main/docs/dated_TangMan.jpg">
  </picture>
