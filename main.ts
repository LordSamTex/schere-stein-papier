input.onButtonPressed(Button.A, function () {
    _symbol = "schere"
    basic.showIcon(IconNames.Scissors)
})
input.onGesture(Gesture.Shake, function () {
    radio.sendString(_symbol)
    gesendet = true
})
input.onButtonPressed(Button.AB, function () {
    _symbol = "papier"
    basic.showLeds(`
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        `)
})
radio.onReceivedString(function (receivedString) {
    while (gesendet == false) {
        basic.pause(100)
    }
    gesendet = false
    gegner_symbol = receivedString
    if (gegner_symbol == _symbol) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # # # # #
            . . . . .
            `)
    } else if (_symbol == "schere" && gegner_symbol == "stein") {
        basic.showIcon(IconNames.Sad)
    } else if (_symbol == "stein" && gegner_symbol == "schere") {
        basic.showIcon(IconNames.Happy)
    } else if (_symbol == "stein" && gegner_symbol == "papier") {
        basic.showIcon(IconNames.Sad)
    } else if (_symbol == "papier" && gegner_symbol == "stein") {
        basic.showIcon(IconNames.Happy)
    } else if (_symbol == "papier" && gegner_symbol == "schere") {
        basic.showIcon(IconNames.Sad)
    } else if (_symbol == "schere" && gegner_symbol == "papier") {
        basic.showIcon(IconNames.Happy)
    }
})
input.onButtonPressed(Button.B, function () {
    _symbol = "stein"
    basic.showLeds(`
        . # # # .
        # # # # #
        # # # # #
        # # # # #
        . # # # .
        `)
})
let gegner_symbol = ""
let _symbol = ""
let gesendet = false
gesendet = false
_symbol = "schere"
basic.showIcon(IconNames.Scissors)
radio.setGroup(20)
