from ._anvil_designer import EditableLinkTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class EditableLink(EditableLinkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.link_1.visible = False
    self.text_box_1.visible = True
    self.text_box_1.focus()
    self.text_box_1.text = self.link_1.text

  def save_text(self, **event_args):
    if self.text_box_1.text != self.link_1.text:
      self.raise_event('x-change-text', text=self.text_box_1.text)
      self.text = self.text_box_1.text
      self.link_1.text = self.text
    self.link_1.visible = True
    self.text_box_1.visible = False
    print("vykonaná funkce save_text")

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.save_text()
    

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.save_text()
    
