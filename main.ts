let x = 0
let arrows = [images.arrowImage(ArrowNames.North), images.arrowImage(ArrowNames.NorthEast), images.arrowImage(ArrowNames.East), images.arrowImage(ArrowNames.SouthEast), images.arrowImage(ArrowNames.South), images.arrowImage(ArrowNames.SouthWest), images.arrowImage(ArrowNames.West), images.arrowImage(ArrowNames.NorthWest), images.arrowImage(ArrowNames.North)]
basic.forever(function on_forever() {
    
    let list2 : Image[] = []
    x = 8 - Math.round(input.compassHeading() / 45)
    basic.pause(100)
    list2[x].showImage(0)
})
