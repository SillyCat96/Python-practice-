from pynput import mouse, keyboard

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

holding_mouse = False
holding_shift = False

# Определяем виртуальные коды клавиш (по физическому расположению)
VK_H = 72  # физическая клавиша H
VK_S = 83  # физическая клавиша S

def on_press(key):
    global holding_mouse, holding_shift

    try:
        if key == keyboard.Key.esc:
            print("Выход из программы.")
            return False  # завершить слушатель

        if isinstance(key, keyboard.KeyCode):
            if key.vk == VK_H and ctrl_pressed():
                toggle_mouse()

            elif key.vk == VK_S and ctrl_pressed():
                toggle_shift()

    except AttributeError:
        pass

def ctrl_pressed():
    # Проверка, нажата ли клавиша Ctrl
    return any(k in currently_pressed for k in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r])

def on_release(key):
    if key in currently_pressed:
        currently_pressed.remove(key)

def on_key_press(key):
    currently_pressed.add(key)

def toggle_mouse():
    global holding_mouse
    holding_mouse = not holding_mouse
    if holding_mouse:
        mouse_controller.press(mouse.Button.left)
        print("Нажали кнопку мыши")
    else:
        mouse_controller.release(mouse.Button.left)
        print("Отпустили кнопку мыши")

def toggle_shift():
    global holding_shift
    holding_shift = not holding_shift
    if holding_shift:
        keyboard_controller.press(keyboard.Key.shift)
        print("Нажали кнопку Shift")
    else:
        keyboard_controller.release(keyboard.Key.shift)
        print("Отпустили кнопку Shift")

currently_pressed = set()

# Слушатель
with keyboard.Listener(
    on_press=lambda key: [on_key_press(key), on_press(key)],
    on_release=on_release
) as listener:
    listener.join()
