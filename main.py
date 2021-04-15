def on_button_pressed_a():
    if player_a.get(LedSpriteProperty.Y) >= 4:
        player_a.set(LedSpriteProperty.Y, 0)
    else:
        player_a.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if player_b.get(LedSpriteProperty.Y) >= 4:
        player_b.set(LedSpriteProperty.Y, 0)
    else:
        player_b.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

player_b: game.LedSprite = None
player_a: game.LedSprite = None
# let ball = game.createSprite(4, 2)
player_a = game.create_sprite(0, 2)
player_b = game.create_sprite(4, 2)
# .set(LedSpriteProperty.X, 5)

def on_forever():
    pass
basic.forever(on_forever)
