from kb import KMKKeyboard
from kb import data_pin

from kmk.keys import KC

from kmk.extensions.rgb import RGB
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData

from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide
from kmk.modules.tapdance import TapDance
from kmk.modules.combos import Combos, Chord, Sequence

from kmk.handlers.sequences import simple_key_sequence

keyboard = KMKKeyboard()

# OLED
oled_ext = Oled(OledData(image={0:OledReactionType.LAYER,1:["ma.bmp","co.bmp","mc.bmp","md.bmp","np.bmp"]}),toDisplay=OledDisplayMode.IMG,flip=False)
keyboard.extensions.append(oled_ext) 

# TapDance
tapdance = TapDance()
tapdance.tap_time = 300
keyboard.modules.append(tapdance)

# RGB
rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=27, val_limit=100, hue_default=190, sat_default=100, val_default=5)
keyboard.extensions.append(rgb)

# TODO Split Rename drives https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/split_keyboards.md
split = Split()
keyboard.modules.append(split)

# Layers
keyboard.modules.append(Layers())

# Media Keys
keyboard.extensions.append(MediaKeys())

# Combo
combos = Combos()
keyboard.modules.append(combos)
combos.combos = [
    # match matrix so it doesn't matter layer
    # [] keys
    Chord((3, 4), KC.LBRACKET, match_coord=True),
    Chord((28, 27), KC.RBRACKET, match_coord=True),

    # Toggle Colemak
    Chord((12, 13, 14, 15, 23), KC.RBRACKET, match_coord=True),
    # Toggle Numpad
    Chord((12, 13, 14, 23), KC.RBRACKET, match_coord=True)
]

# Key names
_______ = KC.TRNS
XXXXXXX = KC.NO

MISC = KC.LT(2, KC.ENTER, prefer_hold=True, tap_interrupted=False, tap_time=250)
MEDIA = KC.TD(KC.LGUI, KC.MO(3))

RGB_TOG = KC.RGB_TOG
RGB_HUI = KC.RGB_HUI
RGB_HUD = KC.RGB_HUI
RGB_SAI = KC.RGB_SAI
RGB_SAD = KC.RGB_SAD
RGB_VAI = KC.RGB_VAI
RGB_VAD = KC.RGB_VAD

# Macro/Sequence
MNT = simple_key_sequence((KC.MEDIA_NEXT_TRACK, KC.MEDIA_FAST_FORWARD))
MPT = simple_key_sequence((KC.MEDIA_PREV_TRACK, KC.MEDIA_REWIND))

keyboard.keymap = [
    [  # QWERTY
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSLS,\
        KC.LCTL,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,\
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,\
                                            KC.LALT,  MEDIA,  KC.BSPC,      KC.SPC,  MISC, KC.RALT,
    ],
    [  # Colemak
        KC.TAB,  _______, _______,    KC.F,    KC.P,    KC.G,                        KC.J,    KC.L,    KC.U,    KC.Y, KC.SCLN, KC.BSLS,\
        KC.LCTL, _______,    KC.R,    KC.S,    KC.T,    KC.D,                     _______,    KC.N,    KC.E,    KC.I,    KC.O, KC.QUOT,\
        KC.LSFT, _______, _______, _______, _______, _______,                        KC.K, _______, _______, _______, _______, KC.RSFT,\
                                            _______, _______, _______,     _______, _______, _______,
    ],
    [  # Misc
        KC.ESC,    KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                        KC.N6,   KC.N7,  KC.N8,    KC.N9,   KC.N0, _______,\
        KC.CAPS, _______, _______, KC.MINS,  KC.EQL,  KC.GRV,                      KC.LEFT, KC.DOWN,  KC.UP, KC.RIGHT, _______, _______,\
        KC.LSFT, _______, _______, _______, _______, _______,                      _______, _______, _______, _______, _______, _______,\
                                            _______, KC.LGUI, _______,     _______, _______, _______,
    ],
    [  # Media
        RGB_TOG,   KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,                         KC.F6,  KC.F7,   KC.F8,   KC.F9,  KC.F10, XXXXXXX,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.F11, KC.F12, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                       KC.MUTE,    MPT, KC.MPLY,     MNT, XXXXXXX, XXXXXXX,\
                                            _______, _______, _______,     _______, KC.VOLD, KC.VOLU,
    ],
    [  # Numpad
        RGB_TOG, XXXXXXX,   KC.N7,   KC.N8,   KC.N9, XXXXXXX,                        XXXXXXX, XXXXXXX,   KC.UP, XXXXXXX, XXXXXXX, XXXXXXX,\
        XXXXXXX, XXXXXXX,   KC.N4,   KC.N5,   KC.N6, XXXXXXX,                        XXXXXXX, KC.LEFT, KC.DOWN, KC.RIGHT, XXXXXXX, XXXXXXX,\
        XXXXXXX, XXXXXXX,   KC.N1,   KC.N2,   KC.N3,  KC.ENT,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                                            KC.DOT,    KC.N0, _______,     _______,  _______, _______,
    ]
]

if __name__ == '__main__':
    keyboard.go()
