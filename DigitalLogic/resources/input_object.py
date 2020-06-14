from kivy.core.window import Window
from kivy.uix.behaviors import DragBehavior
from kivy.uix.button import Button


class DragButton(DragBehavior, Button):

	def __init__(self, **kwargs):
		super().__init__()
		self.drag_distance = 0
		self.drag_rectangle = (0, 0, Window.width, Window.height)
		self.drag_timeout = 1000000
		self.pos = (200, 200)
		self.size = (80, 80)
		self.size_hint = (None, None)
		self.text = kwargs['text']
		self.out = kwargs['out']

		self.out_but = Button(size_hint = (None, None), size = (20, 20), pos_hint = (None, None),
			pos = (self.right, self.center_y - 10))
		self.out_but.bind(on_press = self._out_but_press)
		self.add_widget(self.out_but)

	def _update_rect(self, *args):
		self.drag_rectangle = (0, 0, Window.width, Window.height)

	def _update_out_but(self, *args):
		self.out_but.pos = (self.right, self.center_y - 10)

	def _out_but_press(self, instance):
		self.parent.from_but = instance

	def _eval(self):
		return self.out