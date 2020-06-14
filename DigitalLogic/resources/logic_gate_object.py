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
		self.size = (100, 100)
		self.size_hint = (None, None)
		self.text = kwargs['text']
		self.op = kwargs['op']
		self.in_a_obj = None
		self.in_b_obj = None

		self.out_but = Button(size_hint = (None, None), size = (20, 20), pos_hint = (None, None),
			pos = (self.right, self.center_y - 10))
		self.out_but.bind(on_press = self._out_but_press)
		self.add_widget(self.out_but)

		self.in_a_but = Button(size_hint = (None, None), size = (20, 20), pos_hint = (None, None),
			pos = (self.center_x - 70, self.center_y + 10))
		self.in_a_but.bind(on_press = self._in_a_press)
		self.add_widget(self.in_a_but)

		self.in_b_but = Button(size_hint = (None, None), size = (20, 20), pos_hint = (None, None),
			pos = (self.center_x - 70, self.center_y - 30))
		self.in_b_but.bind(on_press = self._in_b_press)
		self.add_widget(self.in_b_but)

		self.bind(pos = self._update_out)
		self.bind(pos = self._update_in_a)
		self.bind(pos = self._update_in_b)	

	def _update_rect(self, *args):
		self.drag_rectangle = (0, 0, Window.width, Window.height)

	def _update_out(self, *args):
		self.out_but.pos = (self.right, self.center_y - 10)

	def _update_in_a(self, *args):
		self.in_a_but.pos = (self.center_x - 70, self.center_y + 10)

	def _update_in_b(self, *args):
		self.in_b_but.pos = (self.center_x - 70, self.center_y - 30)

	def _in_a_press(self, instance):
		self.parent.to_but = instance
		self.in_a_obj = self.parent.from_but.parent
		self.parent.connections.append(Line(width = 4, points = (self.parent.from_but.center_x,
			self.parent.from_but.center_y, self.parent.to_but.center_x,
			self.parent.to_but.center_y)))
		self.parent.canvas.after.add(self.parent.connections[len(self.parent.connections) - 1])
		
	def _in_b_press(self, instance):
		self.parent.to_but = instance
		self.in_b_obj = self.parent.from_but.parent
		self.parent.canvas.after.add(Line(width = 4, points = (self.parent.from_but.center_x,
			self.parent.from_but.center_y, self.parent.to_but.center_x,
			self.parent.to_but.center_y)))
		self.parent.canvas.after.add(self.parent.connections[len(self.parent.connections) - 1])

	def _out_but_press(self, instance):
		self.parent.from_but = instance

	def _eval(self):

		if self.op == 0:

			return (self.in_a_obj._eval() and self.in_b_obj._eval())

		elif self.op == 1:

			return (self.in_a_obj._eval() or self.in_b_obj._eval())

		else:

			return (self.in_a_obj._eval() ^ self.in_b_obj._eval())