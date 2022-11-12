#colors thats will be used throughout the playing of the game
Green = "#538d4e"
Yellow = "#b59f3b"
Grey1 = "#3a3a3c"
Grey2 = "#565758"
Grey3 = "#3a3a3d"
Black = "#121213"
White = "#ffffff"
Red = "#cc0000"

#make an array of colors
colors_arr = [White, Black, Green, Yellow, Red, Grey1, Grey2, Grey3]

#this array wil be used for Animations.outcome_animation()
colorTemp = [colors_arr[7] for i in range(10)]

#this grid will tell what each tile color should be throughout the Worlde game
colorTile = [[colors_arr[7] for i in range(10)] for i in range(10)]
