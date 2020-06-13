from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Line
from kivy.input.motionevent import MotionEvent
from kivy.metrics import Metrics
from kivy.uix.behaviors import DragBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from resources import input_object, logic_gate_object, output_object


class MainApp(App):

	def build(self):

		self.root = root =  FloatLayout()
		self.box = box = BoxLayout(orientation = 'horizontal', spacing = 10,
			padding = [10, 0, 0, 10])
		root.add_widget(box)

		self.root.inputs = []
		self.root.gates = []
		self.root.outputs = []
		self.root.connections = []
		self.root.from_but = None
		self.root.to_but = None


		self.add_in_but = Button(text = 'Add Input', size_hint = (None, None),
			size = (100, 80))
		self.add_in_but.bind(on_press = self._add_in_but)
		box.add_widget(self.add_in_but)

		self.add_gate_but = Button(text = 'Add Gate', size_hint = (None, None),
			size = (100, 80))
		self.add_gate_but.bind(on_press = self._add_gate_but)
		box.add_widget(self.add_gate_but)

		self.add_out_but = Button(text = 'Add Output', size_hint = (None, None),
			size = (100, 80))
		self.add_out_but.bind(on_press = self._add_out_but)
		box.add_widget(self.add_out_but)

		self.eval_but = Button(text = 'Evaluate', size_hint = (None, None),
			size = (100, 80))
		self.eval_but.bind(on_press = self._eval_but)
		box.add_widget(self.eval_but)

		self.reset_but = Button(text = 'Reset', size_hint = (None, None),
			size = (100, 80))
		self.reset_but.bind(on_press = self._reset_but)
		box.add_widget(self.reset_but)

		self.rect = Rectangle(size = root.size)
		root.canvas.before.add(Color(1, 1, 1))
		root.canvas.before.add(self.rect)
		root.canvas.after.add(Color(0, 0, 0))
		root.bind(size = self._update_back)

		return root

	def _update_back(self, *args):

		self.rect.size = self.root.size

	def _add_in_but(self, instance):
		
		self.btn = input_object.DragButton(text = 'Input: ' + str(len(self.root.inputs)))
		self.btn.bind(pos = self.btn._update_out_but)
		self.root.add_widget(self.btn)
		instance.parent.bind(size = self.btn._update_rect)
		self.root.inputs.append(self.btn)

	def _add_gate_but(self, instance):

		self.btn = logic_gate_object.DragButton(text = 'Gate: ' + str(len(self.root.gates)))
		self.btn.bind(pos = self.btn._update_out)
		self.btn.bind(pos = self.btn._update_in_a)
		self.btn.bind(pos = self.btn._update_in_b)		
		self.root.add_widget(self.btn)
		instance.parent.bind(size = self.btn._update_rect)
		self.root.gates.append(self.btn)

	def _add_out_but(self, instance):

		self.btn = output_object.DragButton(text = 'Output: ' + str(len(self.root.outputs)))
		self.btn.bind(pos = self.btn._update_in_but)
		self.root.add_widget(self.btn)
		instance.parent.bind(size = self.btn._update_rect)
		self.root.outputs.append(self.btn)

	def _eval_but(self, instance):

		try:

			print(self.root.outputs[0]._eval())
		except:

			print('Digital Circuit Not Complete')

	def _reset_but(self, instance):
		
		if self.root.inputs:
			self.root.clear_widgets(children = self.root.inputs)
			self.root.inputs = []

		if self.root.gates:
			self.root.clear_widgets(children = self.root.gates)
			self.root.gates = []

		if self.root.outputs:
			self.root.clear_widgets(children = self.root.outputs)
			self.root.outputs = []

		self.root.canvas.after.clear()
		self.root.canvas.after.add(Color(0, 0, 0))
		self.root.from_but = None
		self.root.to_but = None

if __name__ == '__main__':
    MainApp().run()