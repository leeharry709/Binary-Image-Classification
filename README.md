# ripe-mango-detector
Determines if submitted mango image is ripe or not based on database of mangos at different ripeness

This program is only calibrated for kent mangos. Other varieties of mangos will not classify correctly!

This program utilizes machine learning through tensorflow and a database of 427 ripe mangos and 1003 unripe (or green) mangos. By first training a model to differentiate between what is a "green mango" versus what is a "ripe mango", the user can input a filepath (ex: ripe mango.jpg) and it will predict whether or not it is a ripe mango based on its color.

Primarily, the program detects how much of either green, yellow, or red is found on the mango. Based on how much green is missing and red is showing, the program can tell if a mango is ripe or not. The major limiting factor is how much yellow is showing. For mangos, yellow tends to be both ripe and unripe depending on how much green or red is showing. If too much yellow is showing, the program will classify it as unripe. Therefore, it is important to submit a picture that best shows all of the colors on the mango.
