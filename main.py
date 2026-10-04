def on_button_pressed_a():
    global light_on
    if light_on == 0:
        light_on = 1
        basic.show_icon(IconNames.HEART)
        basic.clear_screen()
        basic.show_string("LO")
        basic.clear_screen()
        basic.pause(300)
    else:
        light_on = 0
        basic.show_icon(IconNames.ASLEEP)
        basic.clear_screen()
        basic.show_string("LC")
    basic.pause(300)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    if armed == 1:
        music.play(music.builtin_playable_sound_effect(soundExpression.soaring),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Armed! Armed!")
        basic.show_icon(IconNames.CONFUSED)
        basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    global armed
    if armed == 0:
        armed = 1
        basic.show_icon(IconNames.SQUARE)
        music.play(music.builtin_playable_sound_effect(soundExpression.slide),
            music.PlaybackMode.UNTIL_DONE)
    else:
        armed = 0
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_sound_loud():
    global light_on
    if light_on == 0:
        light_on = 1
        basic.show_icon(IconNames.HEART)
    else:
        light_on = 0
        basic.show_icon(IconNames.ASLEEP)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

armed = 0
light_on = 0
light_on = 0
armed = 0
basic.show_icon(IconNames.ASLEEP)
basic.pause(500)
basic.clear_screen()

def on_forever():
    if light_on == 1:
        basic.show_icon(IconNames.HEART)
        basic.pause(500)
    else:
        basic.show_number(input.temperature())
        basic.pause(1500)
basic.forever(on_forever)
