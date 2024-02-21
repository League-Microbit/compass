x = 0
arrows = [images.arrow_image(ArrowNames.NORTH),
    images.arrow_image(ArrowNames.NORTH_EAST),
    images.arrow_image(ArrowNames.EAST),
    images.arrow_image(ArrowNames.SOUTH_EAST),
    images.arrow_image(ArrowNames.SOUTH),
    images.arrow_image(ArrowNames.SOUTH_WEST),
    images.arrow_image(ArrowNames.WEST),
    images.arrow_image(ArrowNames.NORTH_WEST),
    images.arrow_image(ArrowNames.NORTH)]

def on_forever():
    global x
    list2: List[Image] = []
    x = 8 - Math.round(input.compass_heading() / 45)
    basic.pause(100)
    list2[x].show_image(0)
basic.forever(on_forever)
