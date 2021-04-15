input.onButtonPressed(Button.A, function on_button_pressed_a() {
    if (player_a.get(LedSpriteProperty.Y) >= 4) {
        player_a.set(LedSpriteProperty.Y, 0)
    } else {
        player_a.change(LedSpriteProperty.Y, 1)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    if (player_b.get(LedSpriteProperty.Y) >= 4) {
        player_b.set(LedSpriteProperty.Y, 0)
    } else {
        player_b.change(LedSpriteProperty.Y, 1)
    }
    
})
let player_b : game.LedSprite = null
let player_a : game.LedSprite = null
//  let ball = game.createSprite(4, 2)
player_a = game.createSprite(0, 2)
player_b = game.createSprite(4, 2)
//  .set(LedSpriteProperty.X, 5)
basic.forever(function on_forever() {
    
})
