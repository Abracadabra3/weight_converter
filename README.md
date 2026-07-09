# Volume to Weight Converter
**This is a Python script to make cooking easier by quickly determining any amount of an ingredient to its weight. For example, it could take the '2 tbs (32g)' on an Nutrition Facts label and tell you how much 2 cups weighs.**

<img src="images/terminal.png" alt="Program output in the terminal." style="width:75%; height:Auto;">

## Quick start
Run [weight_converter.exe](code/weight_converter.exe) in the Code folder or by clicking this link.

## Features
- Takes input in all common US measuring sizes
- Accepts grams, ounces, and pounds as weight units
- Outputs weight in whatever weight and volume unit you want
- Uses Python 3.13 and [PyInputPlus](pyinputplus.readthedocs.io/en/latest/)
- Formatted as both a .py and .exe file

## Design decisions
When I was trying to figure out if I had enough of a few ingredients to make a recipe, I needed to know how much large amounts of ingredients weighed. I could not find anything that would tell me that, and I figured that a Python script to do this was something I could make.
So I did.
The use of PyInputPlus does mean that there is another library that needs to be installed before running this script, but it provides an easy input method. Colored text printed to the terminal makes it easy to see what you are supossed to input and prevents the terminal becoming a wall of text.

## Credits
The book [Automate the Boring Stuff with Python, by Al Sweigart](https://automatetheboringstuff.com/3e/chapter0.html) had information about PyInputPlus and formatting strings.
