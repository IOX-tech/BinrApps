# utf - 8
# program to find platform

from sys import platform

def env():
    if platform == 'linux':
        return "LCA" # linux cmpactable

    elif platform == 'Darwin':
        return "MCA" # MacOS compactible

    elif platform.startswith('win'):
        return "WCA" # Windows compactible

def config(ram):
    if ram < 4:
        return "L1"
    if ram == 4:
        return "L1A"
    if ram >= 4 and ram <= 8:
        return "L2AA"
    if ram >= 8 and ram <16:
        return "A1"
    if ram > 16:
        return "A"

# It is been exported to JS