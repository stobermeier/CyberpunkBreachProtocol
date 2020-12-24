# Cyberpunk Breach Protocol Solver
Solve the breach protocol in Cyberpunk 2077 automatically

## Problem Description
In CD Project REDs Cyberpunk 2077 "hacking" plays a big role. There are many access points all over the map with the possibility to earn in-game money. 
This is basically about selecting double hex values in a matrix in the right order. Depending on your equipment, you can select different numbers of values (RAM).
Especially if you want to solve several sequences in such a data breach, you are faced with a quite complex problem, which you cannot solve so quickly in your head.

## Solution
The problem can be solved quite easily with backtracking. 
The "Code Matrix" is also available in a readable format, which is why it is useful to use OCR to extract the values from a screenshot.
However, due to time constraints, I did not work further on a text recognition function.

## Requirements
* Python 3
* Numpy
* Flask

## Usage
Simply run user_interface.py. The console output will tell you how to open the web interface (should be http://127.0.0.1:5000/).
Enter the Code Matrix, your RAM, and the three Datamine sequences (e.g. 1CE955). 

## Contributing and License
Feel free to contribute or further develop this idea in general. Make sure to use the MIT License adopting using my Code.