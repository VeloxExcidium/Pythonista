#By VeloxExcidium
'''A clipboard manager keyboard extention. Press the green button at the bottom of the keyboard to see your full clipboard if it is more than three lines.'''

import keyboard
import ui
import clipboard

def update_buttons():
	if keyboard.get_selected_text() == "":
		copy.enabled = False
	else:
		copy.enabled = True
	if clipboard.get() == "":
		paste.enabled = False
		clear.enabled = False
	else:
		paste.enabled = True
		clear.enabled = True

def update_label():
	keyboard.move_cursor(1)
	keyboard.move_cursor(-1)

def clear_tapped(sender):
	clipboard.set('')
	update_label()
	
def paste_tapped(sender):
	keyboard.insert_text(clipboard.get())
	
def copy_tapped(sender):
	clipboard.set(keyboard.get_selected_text())
	update_label()

class MyView (ui.View):
	def __init__(self, *args, **kwargs):
		self.label = ui.Label(frame=self.bounds, flex='wh')
		self.background_color = (0.27, 0.27, 0.27)
		self.add_subview(self.label)
		self.label.number_of_lines = 0
		self.label.font = ('Menlo', 11)
		self.label.text = clipboard.get()
		super().__init__(*args, **kwargs)

	def kb_text_changed(self):
		self.label.text = clipboard.get()
		update_buttons()

v = MyView()
keyboard.set_view(v)
clear = ui.Button(frame=(992, 0, 44, 38), flex='hl')
clear.image = ui.Image.named('iow:ios7_trash_32')
clear.action = clear_tapped
clear.tint_color = (1, 1, 1)
v.add_subview(clear)

paste = ui.Button(frame=(954, 0, 44, 40), flex='hl')
paste.image = ui.Image.named('iob:arrow_up_b_256')
paste.action = paste_tapped
paste.tint_color = (1, 1, 1)
v.add_subview(paste)

copy = ui.Button(frame=(916, 0, 44, 40), flex='hl')
copy.image = ui.Image.named('iob:arrow_down_b_256')
copy.action = copy_tapped
copy.tint_color = (1, 1, 1)
v.add_subview(copy)

update_buttons()
