from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Line
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
		self.in_obj = None
		
		self.in_but = Button(size_hint = (None, None), size = (20, 20), pos_hint = (None, None),
			pos = (self.center_x - 60, self.center_y - 10))
		self.in_but.bind(on_press = self._in_but_press)
		self.add_widget(self.in_but)


	def _update_rect(self, *args):
		self.drag_rectangle = (0, 0, Window.width, Window.height)

	def _update_in_but(self, *args):
		self.in_but.pos = (self.center_x - 60, self.center_y - 10)

	def _in_but_press(self, instance):
		self.parent.to_but = instance
		self.in_obj = self.parent.from_but.parent
		self.parent.canvas.after.add(Line(width = 4, points = (self.parent.from_but.center_x,
			self.parent.from_but.center_y, self.parent.to_but.center_x,
			self.parent.to_but.center_y)))
		self.parent.canvas.after.add(self.parent.connections[len(self.parent.connections) - 1])

	def _eval(self):
		return self.in_obj._eval()