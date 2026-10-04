input.onButtonPressed(Button.A, function () {
    if (light_on == 0) {
        light_on = 1
        basic.showIcon(IconNames.Heart)
        basic.clearScreen()
        basic.showString("LO")
        basic.clearScreen()
        basic.pause(300)
    } else {
        light_on = 0
        basic.showIcon(IconNames.Asleep)
        basic.clearScreen()
        basic.showString("LC")
    }
    basic.pause(300)
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
    if (armed == 1) {
        music.play(music.builtinPlayableSoundEffect(soundExpression.soaring), music.PlaybackMode.UntilDone)
        basic.showString("Armed! Armed!")
        basic.showIcon(IconNames.Confused)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.B, function () {
    if (armed == 0) {
        armed = 1
        basic.showIcon(IconNames.Square)
        music.play(music.builtinPlayableSoundEffect(soundExpression.slide), music.PlaybackMode.UntilDone)
    } else {
        armed = 0
        basic.showIcon(IconNames.No)
    }
})
input.onSound(DetectedSound.Loud, function () {
    if (light_on == 0) {
        light_on = 1
        basic.showIcon(IconNames.Heart)
    } else {
        light_on = 0
        basic.showIcon(IconNames.Asleep)
    }
})
let armed = 0
let light_on = 0
light_on = 0
armed = 0
basic.showIcon(IconNames.Asleep)
basic.pause(500)
basic.clearScreen()
basic.forever(function () {
    if (light_on == 1) {
        basic.showIcon(IconNames.Heart)
        basic.pause(500)
    } else {
        basic.showNumber(input.temperature())
        basic.pause(1500)
    }
})
