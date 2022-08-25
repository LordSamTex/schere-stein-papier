def on_button_pressed_a():
    global _symbol
    _symbol = "schere"
    basic.show_icon(IconNames.SCISSORS)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_down():
    radio.send_string(_symbol)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_button_pressed_ab():
    global _symbol
    _symbol = "papier"
    basic.show_leds("""
        . # # # .
                . # # # .
                . # # # .
                . # # # .
                . # # # .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    global gegner_symbol
    gegner_symbol = receivedString
    if gegner_symbol == _symbol:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        # # # # #
                        . . . . .
        """)
    elif _symbol == "schere" and gegner_symbol == "stein":
        basic.show_icon(IconNames.SAD)
    elif _symbol == "stein" and gegner_symbol == "schere":
        basic.show_icon(IconNames.HAPPY)
    elif _symbol == "stein" and gegner_symbol == "papier":
        basic.show_icon(IconNames.SAD)
    elif _symbol == "papier" and gegner_symbol == "stein":
        basic.show_icon(IconNames.HAPPY)
    elif _symbol == "papier" and gegner_symbol == "schere":
        basic.show_icon(IconNames.SAD)
    elif _symbol == "schere" and gegner_symbol == "papier":
        basic.show_icon(IconNames.HAPPY)
    else:
        pass
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global _symbol
    _symbol = "stein"
    basic.show_leds("""
        . # # # .
                # # # # #
                # # # # #
                # # # # #
                . # # # .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

gegner_symbol = ""
_symbol = ""
_symbol = "schere"
basic.show_icon(IconNames.SCISSORS)
radio.set_group(155)

def on_forever():
    pass
basic.forever(on_forever)
