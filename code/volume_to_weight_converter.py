# Weight converter for cooking
# By Abracadabra3
try:
    import pyinputplus
except ImportError:
    print("This script needs pyinputplus. Please run pip install pyinputplus.")
    exit()


def convert_unit(quantity, unit):
    if unit == "tbs" or unit == "tbsp":
        return int(quantity)
    elif unit == "tsp":
        return int(quantity) / 3
    elif unit == "c":
        return int(quantity) * 16
    elif unit == "pt":
        return int(quantity) * 32
    elif unit == "qt":
        return int(quantity) * 64
    elif unit == "gal" or unit == "g":
        return int(quantity) * 256


def convert_weight_unit(quantity, unit):
    if unit == "g":
        return int(quantity)
    elif unit == "oz":
        return int(quantity) * 28.3
    elif unit == "lbs" or unit == "lb":
        return int(quantity) * 453.6


def unconvert_weight_unit(quantity, desired_unit):
    if desired_unit == "g":
        return quantity
    elif desired_unit == "oz":
        return quantity / 28.3
    elif desired_unit == "lb" or desired_unit == "lbs":
        return quantity / 453.6


reset = "\033[0m"
bold = "\033[1m"
beginning = "\x1b[38;2;91;132;140m"
halfway = "\x1b[38;2;14;203;48m"
red = "\x1b[38;2;206;10;6m"
finish = "\x1b[38;2;95;217;251m"
example = "\x1b[38;2;123;125;127m"
num = "\x1b[38;2;200;100;0m"
weight = "\x1b[38;2;0;200;100m"
volume = "\x1b[38;2;100;0;200m"

print(f"{beginning}This is a volume-to-weight converter for cooking.")
print(f"Begin by entering the given volume-to-weight in the nutrition facts on your ingredient label.{volume}")
label_x = pyinputplus.inputMenu(['tbs', 'tsp', 'c', 'qt', 'pt', 'gal'], lettered= True, prompt=" What is the unit given? \n")
print(f'{num}', end="")
x = pyinputplus.inputNum(prompt="How many units? ")
print(f'{weight}', end="")
label_y = pyinputplus.inputMenu(['g', 'oz', 'lbs'], lettered= True, prompt=" What is the weight unit given? \n")
print(f'{num}', end="")
y = pyinputplus.inputNum(prompt="How many weight units given? ")

print(f"{bold}{halfway}Now enter the amount you want{volume}")
label_z = pyinputplus.inputMenu(['tbs', 'tsp', 'c', 'pt', 'qt', 'gal'], lettered= True, prompt="What unit? \n")
print(f'{num}', end="")
z = pyinputplus.inputNum(prompt="How many units? ")
print(f'{weight}', end="")
u = pyinputplus.inputMenu(['g', 'oz', 'lbs'], lettered= True, prompt="What weight unit do you want the answer in? \n")
print(f'{num}', end="")

x = convert_unit(x, label_x)
label_x = "tbs"
z_2 = convert_unit(z, label_z)
label_z_2 = "tbs"
y = convert_weight_unit(y, label_y)
label_y = "g"

# Weight per tablespoon
if not x == 1:
    b = y / x

# Figure out how much the desired quantity (y) weighs in grams
alpha = b * z_2

alpha = unconvert_weight_unit(alpha, u)
alpha = round(alpha, 2)
print(f"{finish}{str(z)} {str(label_z)} weighs {str(alpha)} {str(u)}{reset}")
