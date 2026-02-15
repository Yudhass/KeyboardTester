import pygame
import sys

pygame.init()
pygame.font.init()

# Warna
BG_COLOR      = (28, 28, 35)
KEY_DEFAULT   = (60, 60, 70)
KEY_EVER      = (80, 200, 120)
KEY_CURRENT   = (220, 60, 60)
BORDER_COLOR  = (100, 100, 120)
TEXT_COLOR    = (240, 240, 255)
RESET_COLOR   = (50, 120, 255)

# Font
TITLE_FONT    = pygame.font.SysFont('consolas', 22, bold=True)
PRESSED_FONT  = pygame.font.SysFont('consolas', 15)
KEY_FONT      = pygame.font.SysFont('consolas', 18, bold=True)
KEY_FONT_SMALL = pygame.font.SysFont('consolas', 14)

# Layout keyboard (dengan ukuran tombol fungsi/navigation lebih kecil & numpad digeser ke kiri)
KEY_LAYOUT = [
    ('Esc', 0, 0, 1, 1),
    ('F1', 1.5, 0, 1, 1), ('F2', 2.5, 0, 1, 1), ('F3', 3.5, 0, 1, 1), ('F4', 4.5, 0, 1, 1),
    ('F5', 6, 0, 1, 1), ('F6', 7, 0, 1, 1), ('F7', 8, 0, 1, 1), ('F8', 9, 0, 1, 1),
    ('F9', 10.5, 0, 1, 1), ('F10', 11.5, 0, 1, 1), ('F11', 12.5, 0, 1, 1), ('F12', 13.5, 0, 1, 1),
    ('PrtSc', 15.2,   0, 1.2, 1),
    ('ScrLk', 16.4,   0, 1.2, 1),
    ('Pause', 17.6,   0, 1.2, 1),

    ('`', 0, 1, 1, 1), ('1', 1, 1, 1, 1), ('2', 2, 1, 1, 1), ('3', 3, 1, 1, 1),
    ('4', 4, 1, 1, 1), ('5', 5, 1, 1, 1), ('6', 6, 1, 1, 1), ('7', 7, 1, 1, 1),
    ('8', 8, 1, 1, 1), ('9', 9, 1, 1, 1), ('0', 10, 1, 1, 1), ('-', 11, 1, 1, 1),
    ('=', 12, 1, 1, 1), ('Backspace', 13, 1, 2, 1),
    ('Ins',   15.2, 1, 1.2, 1),
    ('Home',  16.4, 1, 1.2, 1),
    ('PgUp',  17.6, 1, 1.2, 1),

    ('Tab', 0, 2, 1.5, 1), ('Q', 1.5, 2, 1, 1), ('W', 2.5, 2, 1, 1), ('E', 3.5, 2, 1, 1),
    ('R', 4.5, 2, 1, 1), ('T', 5.5, 2, 1, 1), ('Y', 6.5, 2, 1, 1), ('U', 7.5, 2, 1, 1),
    ('I', 8.5, 2, 1, 1), ('O', 9.5, 2, 1, 1), ('P', 10.5, 2, 1, 1), ('[', 11.5, 2, 1, 1),
    (']', 12.5, 2, 1, 1), ('\\', 13.5, 2, 1.5, 1),
    ('Del',   15.2, 2, 1.2, 1),
    ('End',   16.4, 2, 1.2, 1),
    ('PgDn',  17.6, 2, 1.2, 1),

    ('Caps', 0, 3, 1.75, 1), ('A', 1.75, 3, 1, 1), ('S', 2.75, 3, 1, 1), ('D', 3.75, 3, 1, 1),
    ('F', 4.75, 3, 1, 1), ('G', 5.75, 3, 1, 1), ('H', 6.75, 3, 1, 1), ('J', 7.75, 3, 1, 1),
    ('K', 8.75, 3, 1, 1), ('L', 9.75, 3, 1, 1), (';', 10.75, 3, 1, 1), ("'", 11.75, 3, 1, 1),
    ('Enter', 12.75, 3, 2.25, 1),

    ('Shift', 0, 4, 2.25, 1), ('Z', 2.25, 4, 1, 1), ('X', 3.25, 4, 1, 1), ('C', 4.25, 4, 1, 1),
    ('V', 5.25, 4, 1, 1), ('B', 6.25, 4, 1, 1), ('N', 7.25, 4, 1, 1), ('M', 8.25, 4, 1, 1),
    (',', 9.25, 4, 1, 1), ('.', 10.25, 4, 1, 1), ('/', 11.25, 4, 1, 1),
    ('Shift', 12.25, 4, 2.75, 1),
    ('↑',     16.4,  4, 1.2,  1),

    ('Ctrl', 0, 5, 1.25, 1), ('Win', 1.25, 5, 1.25, 1), ('Alt', 2.5, 5, 1.25, 1),
    ('Space', 3.75, 5, 6.25, 1),
    ('Alt', 10, 5, 1.25, 1), ('Win', 11.25, 5, 1.25, 1), ('Menu', 12.5, 5, 1.25, 1),
    ('Ctrl', 13.75, 5, 1.25, 1),
    ('←',    15.2,  5, 1.2,  1),
    ('↓',    16.4,  5, 1.2,  1),
    ('→',    17.6,  5, 1.2,  1),

    # Numpad – digeser ke kiri sekitar 1.3 unit
    ('Num',  18.9, 0, 1, 1),
    ('/',    19.9, 0, 1, 1),
    ('*',    20.9, 0, 1, 1),
    ('-',    21.9, 0, 1, 1),

    ('7',    18.9, 1, 1, 1),
    ('8',    19.9, 1, 1, 1),
    ('9',    20.9, 1, 1, 1),
    ('+',    21.9, 1, 1, 2),

    ('4',    18.9, 2, 1, 1),
    ('5',    19.9, 2, 1, 1),
    ('6',    20.9, 2, 1, 1),

    ('1',    18.9, 3, 1, 1),
    ('2',    19.9, 3, 1, 1),
    ('3',    20.9, 3, 1, 1),
    ('↵',    21.9, 3, 1, 2),

    ('0',    18.9, 4, 2, 1),
    ('.',    20.9, 4, 1, 1),
]

# Mapping tombol (tidak berubah)
KEY_NAME_MAP = {
    pygame.K_ESCAPE: 'Esc',
    pygame.K_F1: 'F1', pygame.K_F2: 'F2', pygame.K_F3: 'F3', pygame.K_F4: 'F4',
    pygame.K_F5: 'F5', pygame.K_F6: 'F6', pygame.K_F7: 'F7', pygame.K_F8: 'F8',
    pygame.K_F9: 'F9', pygame.K_F10: 'F10', pygame.K_F11: 'F11', pygame.K_F12: 'F12',
    pygame.K_PRINT: 'PrtSc',
    pygame.K_SCROLLLOCK: 'ScrLk',
    pygame.K_PAUSE: 'Pause',
    pygame.K_BACKQUOTE: '`', pygame.K_1: '1', pygame.K_2: '2', pygame.K_3: '3', pygame.K_4: '4',
    pygame.K_5: '5', pygame.K_6: '6', pygame.K_7: '7', pygame.K_8: '8', pygame.K_9: '9', pygame.K_0: '0',
    pygame.K_MINUS: '-', pygame.K_EQUALS: '=', pygame.K_BACKSPACE: 'Backspace',
    pygame.K_INSERT: 'Ins', pygame.K_HOME: 'Home', pygame.K_PAGEUP: 'PgUp',
    pygame.K_TAB: 'Tab',
    pygame.K_q: 'Q', pygame.K_w: 'W', pygame.K_e: 'E', pygame.K_r: 'R', pygame.K_t: 'T',
    pygame.K_y: 'Y', pygame.K_u: 'U', pygame.K_i: 'I', pygame.K_o: 'O', pygame.K_p: 'P',
    pygame.K_LEFTBRACKET: '[', pygame.K_RIGHTBRACKET: ']', pygame.K_BACKSLASH: '\\',
    pygame.K_DELETE: 'Del', pygame.K_END: 'End', pygame.K_PAGEDOWN: 'PgDn',
    pygame.K_CAPSLOCK: 'Caps',
    pygame.K_a: 'A', pygame.K_s: 'S', pygame.K_d: 'D', pygame.K_f: 'F', pygame.K_g: 'G',
    pygame.K_h: 'H', pygame.K_j: 'J', pygame.K_k: 'K', pygame.K_l: 'L',
    pygame.K_SEMICOLON: ';', pygame.K_QUOTE: "'", pygame.K_RETURN: 'Enter',
    pygame.K_LSHIFT: 'Shift', pygame.K_RSHIFT: 'Shift',
    pygame.K_z: 'Z', pygame.K_x: 'X', pygame.K_c: 'C', pygame.K_v: 'V', pygame.K_b: 'B',
    pygame.K_n: 'N', pygame.K_m: 'M', pygame.K_COMMA: ',', pygame.K_PERIOD: '.', pygame.K_SLASH: '/',
    pygame.K_LCTRL: 'Ctrl', pygame.K_RCTRL: 'Ctrl',
    pygame.K_LSUPER: 'Win', pygame.K_RSUPER: 'Win',
    pygame.K_LALT: 'Alt', pygame.K_RALT: 'Alt',
    pygame.K_SPACE: 'Space',
    pygame.K_MENU: 'Menu',
    1073741925: 'Menu',
    pygame.K_UP: '↑', pygame.K_DOWN: '↓', pygame.K_LEFT: '←', pygame.K_RIGHT: '→',
    pygame.K_NUMLOCK: 'Num',
    pygame.K_KP_DIVIDE: '/', pygame.K_KP_MULTIPLY: '*', pygame.K_KP_MINUS: '-',
    pygame.K_KP_PLUS: '+', pygame.K_KP_ENTER: '↵',
    pygame.K_KP7: '7', pygame.K_KP8: '8', pygame.K_KP9: '9',
    pygame.K_KP4: '4', pygame.K_KP5: '5', pygame.K_KP6: '6',
    pygame.K_KP1: '1', pygame.K_KP2: '2', pygame.K_KP3: '3',
    pygame.K_KP0: '0', pygame.K_KP_PERIOD: '.',
}

def get_key_name(key):
    return KEY_NAME_MAP.get(key)

def main():
    info = pygame.display.Info()
    init_w = min(1440, info.current_w - 100)
    init_h = min(920, info.current_h - 100)
    screen = pygame.display.set_mode((init_w, init_h), pygame.RESIZABLE)
    pygame.display.set_caption("Keyboard Tester V1.0.0")
    clock = pygame.time.Clock()

    ever_pressed = set()
    current_pressed = set()
    pressed_order = []
    reset_rect = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                name = get_key_name(event.key)
                if name:
                    current_pressed.add(name)
                    if name not in ever_pressed:
                        ever_pressed.add(name)
                        pressed_order.append(name)
            elif event.type == pygame.KEYUP:
                name = get_key_name(event.key)
                if name:
                    current_pressed.discard(name)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if reset_rect and reset_rect.collidepoint(event.pos):
                    ever_pressed.clear()
                    current_pressed.clear()
                    pressed_order.clear()

        w, h = screen.get_size()
        base_unit = min(w / 24.5, (h - 220) / 7.2)
        unit = max(22, min(base_unit, 48))
        gap = unit * 0.14

        # Geser seluruh keyboard agak ke kiri (bisa diubah nilainya)
        left_offset = 50          # ← naikkan jika ingin lebih ke kiri lagi
        margin_x = (w - 23 * unit - 10 * gap) // 2 - left_offset
        margin_y = 140

        screen.fill(BG_COLOR)

        # Judul
        title = TITLE_FONT.render("Keyboard Tester", True, TEXT_COLOR)
        screen.blit(title, (25, 25))

        # Pressed keys (10 terakhir)
        pressed_str = "Pressed: " + " ".join(pressed_order[-10:])
        pressed_surf = PRESSED_FONT.render(pressed_str, True, TEXT_COLOR)
        screen.blit(pressed_surf, (25, 65))

        # Reset button
        reset_rect = pygame.Rect(w - 180, 25, 160, 50)
        pygame.draw.rect(screen, RESET_COLOR, reset_rect, border_radius=12)
        reset_txt = KEY_FONT.render("Reset", True, TEXT_COLOR)
        screen.blit(reset_txt, (reset_rect.x + 45, reset_rect.y + 12))

        # Gambar semua tombol
        for name, col, row, w_u, h_u in KEY_LAYOUT:
            x = margin_x + col * (unit + gap)
            y = margin_y + row * (unit + gap)
            width  = w_u * (unit + gap) - gap
            height = h_u * (unit + gap) - gap

            color = KEY_CURRENT if name in current_pressed else \
                    KEY_EVER    if name in ever_pressed else KEY_DEFAULT

            rect = pygame.Rect(x, y, width, height)
            pygame.draw.rect(screen, color, rect, border_radius=9)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 2, border_radius=9)

            font = KEY_FONT if unit > 32 or len(name) <= 4 else KEY_FONT_SMALL
            text = font.render(name, True, TEXT_COLOR)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()